import cv2
import numpy as np
import time

class orta:
    def __init__(self):
        
        
        cap = cv2.VideoCapture(0)
 
        while (True):
            time.sleep(0.1)
            ret, frame = cap.read()
            
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


            lower_blue = np.array([102, 141, 59]) # min hsv color code
            upper_blue = np.array([131, 236, 190]) # max hsv color code
            
            blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

            # windows size 
            frame = cv2.resize(frame, (600,600))
            blue_mask = cv2.resize(blue_mask, (600,600))
            
            # Apply binary thresholding to blue_mask: pixel values below 127 become 0, and pixel values 127 and above become 255.
            ret,thres = cv2.threshold(blue_mask,127,255,cv2.THRESH_BINARY)
            
            cv2.line(frame,(200,0),(200,600),(0,0,255),2)
            cv2.line(frame,(400,0),(400,600),(0,0,255),2)

            cv2.line(frame,(0,200),(600,200),(0,0,255),2)
            cv2.line(frame,(0,400),(600,400),(0,0,255),2)
            
            M = cv2.moments(thres)
            # m00: The zeroth-order moment, which gives the total number of white (or bright) pixels in the image. This can be considered as the area of the object.
            # m10 and m01 values determine the position of the object along the horizontal (x) and vertical (y) axes respectively.
            if int(M["m10"]) != 0 and int(M["m00"]) !=0 and int(M["m01"]) !=0  :

                x=int(M["m10"]/M["m00"])
                y=int(M["m01"]/M["m00"])
            # print(x,y)
                
                cv2.circle(frame, (x, y),10,[0,0,0],3)
                if x < 200 and y < 200:
                    print("The object is in the 1st region")

                if 200<x<400 and y < 200:
                    print("The object is in the 2st region")

                if 400<x<600 and y < 200:
                    print("The object is in the 3st region")

                if x<200 and 200<y<400:
                    print("The object is in the 4st region")

                if 200<x<400 and 200<y<400:
                    print("The object is in the middle")

                if 400<x<600 and 200<y<400:
                    print("The object is in the 6st region")

                if x<200 and 400<y<600:
                    print("The object is in the 7st region")  

                if 200<x<400 and 400<y<600:
                    print("The object is in the 8st region") 

                if 400<x<600 and 400<y<600:
                    print("The object is in the 9st region")  
            else:
                print("Object not detected")         

            cv2.imshow("Camera", frame)
            cv2.imshow("Blue Filter", blue_mask)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        
        cap.release()
        cv2.destroyAllWindows()

orta()   