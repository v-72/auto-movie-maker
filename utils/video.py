import os
from moviepy.editor import *

def create_video(
    image_folder="images",
    output="output.mp4",
    output_fps=24
    ):
    images  = get_image_files(image_folder)
    clips = [generate_image_clip(m) for m in images]
    # clips = [c.resize( (1920, 1080) ) for c in clips]
    clipStart = VideoFileClip(image_folder+"/tip10intro.mov")
    clipEnd = VideoFileClip(image_folder+"/tip10end.mov")
    clips.append(clipEnd)
    clips = [clipStart] + clips
    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile(output, fps=output_fps)

"""
Generate movie clip
"""
def generate_image_clip(image):
    image_clip = ImageClip(image).set_duration(5).crossfadein( 0.5).crossfadeout(0.5)
    return image_clip
"""
    Preprocess image
"""
def preprocess_image(image):
    pass

def intro_video():
    pass

def end_video():
    pass

def add_text_to_image():
    pass

def add_transition():
    pass

"""
Get image files from image folder
"""
def get_image_files(image_folder):
    return [
        image_folder+'/'+image 
        for image 
        in os.listdir(image_folder) if (
                image.endswith(".jpg") or
                image.endswith(".jpeg")
            )
        ]