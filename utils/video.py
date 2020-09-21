import os
from moviepy.editor import *

"""
Default parameters
"""
INDEX = 0
FONT_SIZE = 58
FONT_COLOR = "yellow"
IMAGE_DURATION = 5
TRANSITION_DURATION = 0.5
INTRO_NAME = "tip10intro.mov"
END_SCREEN_NAME = "tip10end.mov"
SUBTITLE_POSITION = "bottom"
OUTPUT_FPS = 30
IMAGE_FOLDER = "images"
OUTPUT_FILE_NAME = "output.mp4"
SUBTITLE_FILE = "subtitle.txt"

def create_video(
    image_folder=IMAGE_FOLDER,
    output=OUTPUT_FILE_NAME,
    output_fps=OUTPUT_FPS
    ):
    images  = get_image_files(image_folder)
    subtitles = get_subtitles(image_folder)
    clips = [generate_image_clip(m,subtitles) for m in images]
    # clips = [c.resize( (1920, 1080) ) for c in clips]
    clipStart = intro_video(image_folder)
    clipEnd = end_video(image_folder)
    clips.append(clipEnd)
    clips = [clipStart] + clips
    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile(output, fps=output_fps)

"""
Generate movie clip
"""
def generate_image_clip(image,subtitles):
    image_clip = ImageClip(image).set_duration(IMAGE_DURATION).crossfadein(TRANSITION_DURATION).crossfadeout(TRANSITION_DURATION)
    txt_clip = TextClip(subtitles[0],fontsize=FONT_SIZE,color=FONT_COLOR)
    txt_clip = txt_clip.set_pos(SUBTITLE_POSITION).set_duration(IMAGE_DURATION)
    video_clip = CompositeVideoClip([image_clip, txt_clip])
    # INDEX += 1
    return video_clip
"""
    Preprocess image
"""
def preprocess_image(image):
    pass

def intro_video(image_folder):
    return VideoFileClip(image_folder+"/"+INTRO_NAME)

def end_video(image_folder):
    return VideoFileClip(image_folder+"/"+END_SCREEN_NAME)

def add_text_to_image(subtitles,index):
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

def get_subtitles(image_folder):
    subtitle_file = open(image_folder+'/'+SUBTITLE_FILE, 'r') 
    count = 0
    subtitles = []
    for line in subtitle_file: 
        count += 1
        subtitles.append(line)

    subtitle_file.close() 
    return subtitles