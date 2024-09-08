import numpy as np
from utils import filter2d, partial_x, partial_y, gaussian_kernel
from skimage.feature import peak_local_max
from skimage.io import imread
import matplotlib.pyplot as plt

def harris_corners(img, window_size=3, k=0.04):
    """
    Compute Harris corner response map. Follow the math equation
    R=Det(M)-k(Trace(M)^2).
        
    Args:
        img: Grayscale image of shape (H, W)
        window_size: size of the window function
        k: sensitivity parameter

    Returns:
        response: Harris response image of shape (H, W)
    """

    response = None
    
    ### YOUR CODE HERE
    dx = partial_x(img)
    dy = partial_y(img)

    dx2 = np.square(dx)
    dy2 = np.square(dy)
    dxdy = dx*dy

    g_dx2 = filter2d(dx2, gaussian_kernel(l=window_size))
    g_dy2 = filter2d(dy2, gaussian_kernel(l=window_size))
    g_dxdy = filter2d(dxdy, gaussian_kernel(l=window_size))

    detM = g_dx2*g_dy2 - np.square(g_dxdy)
    traceM = g_dx2 + g_dy2

    response = detM - k*np.square(traceM)
    ### END YOUR CODE

    return response

def main():
    img = imread('building.jpg', as_gray=True)

    ### YOUR CODE HERE
    
    # Compute Harris corner response
    harris = harris_corners(img)

    # Threshold on response
    thresh_harris = np.where(harris > (2.5e-04), harris, 0)

    # Perform non-max suppression by finding peak local maximum
    coordinates = peak_local_max(thresh_harris)
    loc = np.zeros_like(thresh_harris)
    loc[coordinates[:, 0], coordinates[:, 1]] = thresh_harris[coordinates[:, 0], coordinates[:, 1]]

    # Visualize results
    plt.imshow(harris)
    plt.title("Harris corners")
    plt.show()

    plt.imshow(thresh_harris)
    plt.title("Harris corners + thresholding")
    plt.show()

    plt.imshow(loc)
    plt.scatter(coordinates[:, 1], coordinates[:, 0], marker='x', color='green')
    plt.title("Local maximums")
    plt.show()
    
    ### END YOUR CODE
    
if __name__ == "__main__":
    main()
