import argparse
from utils.video import VideoMaker

image_folder="./images"

def create_movie(image_folder="images",output_file_name="output.mp4"):
    video = VideoMaker(image_folder,output_file_name)
    video.create_video()

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image_folder", required=True,help="Images folder")
    ap.add_argument("-o", "--output", required=True,help="Output filename")
    args = vars(ap.parse_args())
    create_movie(image_folder=args['image_folder'], output_file_name=args['output'])