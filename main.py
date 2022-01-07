import argparse
from SlideExtractor.extractSlides import extractSlides
import cv2

parser = argparse.ArgumentParser(description="Extract slides or smth")
parser.add_argument('-v','--video',help="Specifies the name of the video file")
parser.add_argument('-s','--skips',help="Specifies the number of seconds to be skipped while searching",default=60)

args = parser.parse_args()


# Read in file


video_filename=args.video
seconds_skipped=int(args.skips)



pdf_name=f"{video_filename.split('/')[-1].split('.')[0]}.pdf"

video = cv2.VideoCapture(video_filename)
fps = video.get(cv2.CAP_PROP_FPS)
frames_skipped=fps*seconds_skipped

extractSlides(video,frames_skipped=frames_skipped)