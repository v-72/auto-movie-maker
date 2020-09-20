import os
from moviepy.editor import *
import cv2

def create_video(
    image_folder="images",
    output="output.mp4",
    output_fps=24
    ):
    img  = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    [preprocess_image(i) for i in img]
    clips = [ImageClip(m).set_duration(5).crossfadein( 0.5).crossfadeout(0.5)
      for m in img]
    [preprocess_image(i) for i in clips]
    clips = [c.resize( (1920, 1080) ) for c in clips]
    clipStart = VideoFileClip(image_folder+"/tip10intro.mov")
    clipEnd = VideoFileClip(image_folder+"/tip10end.mov")
    clips.append(clipEnd)
    clips = [clipStart] + clips
    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile(output, fps=output_fps)

def preprocess_image(image):
    # im = cv2.imread(image)
    print(dir(image))
    pass

def intro_video():
    pass

def end_video():
    pass

def add_text_to_image():
    pass

def add_transition():
    pass