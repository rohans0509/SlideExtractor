from PIL import Image,ImageChops
import cv2
import numpy as np

# Calculate Difference Coefficient
def difference(frame,prevSlide,threshold=20):
    frame=toImgPIL(frame)
    prevSlide=toImgPIL(prevSlide)

    diff = ImageChops.difference(frame, prevSlide)

    diff_grayscale=diff.convert("L")



    diff_arr=np.array(diff_grayscale)
    total_change=np.count_nonzero(diff_arr)
    max_change=np.prod(np.shape(diff_arr))
    
    percent_change=100*total_change/max_change
    changed=percent_change>threshold
        
    return(changed)



def toImgPIL(imgOpenCV): 
    return Image.fromarray(cv2.cvtColor(imgOpenCV, cv2.COLOR_BGR2RGB))