from utils.video import create_video

image_folder="./images"

def create_movie(image_folder="images"):
    create_video(image_folder)

if __name__ == '__main__':
    create_movie(image_folder)