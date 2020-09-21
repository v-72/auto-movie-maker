from utils.video import VideoMaker

image_folder="./images"

def create_movie(image_folder="images"):
    video = VideoMaker()
    video.create_video(image_folder)

if __name__ == '__main__':
    create_movie(image_folder)