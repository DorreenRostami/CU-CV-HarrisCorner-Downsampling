Gradiant and Edge Detection)
Gradient along the x axis calculates the vertical edges and uses the following matrix: <br/>
0	0	0 <br/>
-1	0	1 <br/>
0	0	0 <br/>

![image](https://github.com/user-attachments/assets/2b6c7347-2290-48c9-b553-3dc5f4e07689) <br/>

Gradient along the y axis calculates the horizontal edges and uses the following matrix: <br/>
0	-1	0 <br/>
0	0	0 <br/>
0	1	0 <br/>

![image](https://github.com/user-attachments/assets/1b50671d-4726-4b95-bceb-d519f163db7c) <br/>

Gradient magnitude = √(〖grad_x〗^2+ 〖grad_y〗^2 ) <br/>

![image](https://github.com/user-attachments/assets/bba8334b-8ef8-4310-bdf7-8579f11ebc86) <br/>

Corner Detection)  <br/>
![image](https://github.com/user-attachments/assets/8b572c3b-83ac-4746-b9ba-2e4555484343) <br/>

I tried different thresholds like 1.0e-02 to 1.0e-06 first, realized 1.0e-04 is the best since it shows the corner of the windows on the buildings in the image. 4.0e-04 is too high and removes these points (this fact is more easily visible in the plot where it marks the points with an x) so I just used 2.5e-04 which is in the middle of this range (1.0e-04 to 4.0e-04). <br/>
 
 ![image](https://github.com/user-attachments/assets/9462d503-cfbc-4c18-90dc-eb27f747e585) <br/>

Plot which shows the points of local maximums with an x: <br/>
 ![image](https://github.com/user-attachments/assets/1dddb6a8-b78e-4883-a928-ffe3fa0693b7) <br/>


Subsampling) <br/>
The results of the naïve downsampling are in the 1st row and the results from the anti-aliasing downsampling are in the 2nd row. <br/>
 ![image](https://github.com/user-attachments/assets/14cc85f5-bfce-43f3-8d78-726ea4efa7b4)

