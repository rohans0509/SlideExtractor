import cv2
from SlideExtractor.detection.detectSlide import detectSlide
from SlideExtractor.utils.convertToPDF import convertToPDF
from SlideExtractor.utils.imageProcessing import *

from tqdm import tqdm




def extractSlides(video,frames_skipped=3000):
    print("Extracting...")
    deleteImages()
    index = 0
    ret, frame = video.read()


    prevSlide=frame
    slide_num=1
    saveSlide(frame,slide_num)

    total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))-1
    pbar=tqdm(total=total)
    while(True):
        ret, frame = video.read()
        if not ret: 
            break

        if index%frames_skipped==0:
            if detectSlide(frame,prevSlide):
                slide_num+=1
                saveSlide(frame,slide_num)
                prevSlide=frame
                
        index += 1
        pbar.update(1)
    
    convertToPDF()
    deleteImages()
