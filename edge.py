import numpy as np
import matplotlib.pylab as plt
from skimage import io
from utils import gaussian_kernel, filter2d, partial_x, partial_y

def main():
    # Load image
    img = io.imread('iguana.png', as_gray=True)

    ### YOUR CODE HERE

    # Smooth image with Gaussian kernel
    smooth = filter2d(img, gaussian_kernel())

    # Compute x and y derivate on smoothed image
    dx = partial_x(smooth)
    dy = partial_y(smooth)

    # Compute gradient magnitude
    grad_mag = np.sqrt(np.square(dx) + np.square(dy))

    # Visualize results
    plt.imshow(dx)
    plt.title("Gradient along x")
    plt.show()
    plt.imshow(dy)
    plt.title("Gradient along y")
    plt.show()
    plt.imshow(grad_mag)
    plt.title("Gradient magnitude")
    plt.show()
    ### END YOUR CODE
    
if __name__ == "__main__":
    main()

