import argparse
from utils.video import VideoMaker

image_folder="./images"

def create_movie(image_folder="images",output="output.mp4"):
    video = VideoMaker()
    video.create_video(image_folder)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image_folder", required=False,help="Images folder")
    ap.add_argument("-o", "--output", required=False,help="Output filename")
    args = vars(ap.parse_args())
    create_movie()#image_folder=args['image_folder'], output=args['output'])