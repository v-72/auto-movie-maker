import os
from moviepy.editor import *
from utils.scale_image import Image
"""
Default parameters
"""
INDEX = 0
FONT_SIZE = 58
FONT_COLOR = "yellow4"
FONT_STROKE_COLOR = "yellow1"
STROKE_WIDTH = 0.5
IMAGE_DURATION = 5
TRANSITION_DURATION = 0.5
INTRO_NAME = "tip10intro.mov"
END_SCREEN_NAME = "tip10end.mov"
SUBTITLE_POSITION = "bottom"
OUTPUT_FPS = 30
IMAGE_FOLDER = "images"
OUTPUT_FILE_NAME = "output.mp4"
SUBTITLE_FILE = "subtitle.txt"

class VideoMaker():
    def __init__(self,
        image_folder = IMAGE_FOLDER,
        output_file_name = OUTPUT_FILE_NAME,
        add_subtitle = False,
        subtitle_file = SUBTITLE_FILE,
        intro_name = INTRO_NAME,
        end_screen_name = END_SCREEN_NAME,
        subtitle_position = END_SCREEN_NAME,
        font_size = FONT_SIZE,
        font_color = FONT_COLOR,
    ):
        self.image_folder = image_folder
        self.output_file_name = output_file_name
        self.add_subtitle = False
        self.subtitle_file = SUBTITLE_FILE
        self.intro_name = INTRO_NAME
        self.end_screen_name = END_SCREEN_NAME
        self.subtitle_position = END_SCREEN_NAME
        self.font_size = FONT_SIZE
        self.font_color = FONT_COLOR
        self.output_fps = OUTPUT_FPS
        self.index = 0

    def create_video(self):
        images  = self.get_image_files(self.image_folder)
        images.sort()
        subtitles = self.get_subtitles()
        clips = [self.generate_image_clip(m,subtitles) for m in images]
        # clips = [c.resize( (1920, 1080) ) for c in clips]
        clipStart = self.intro_video(self.image_folder)
        clipEnd = self.end_video(self.image_folder)
        clips.append(clipEnd)
        clips = [clipStart] + clips
        concat_clip = concatenate_videoclips(clips, method="compose")
        concat_clip.write_videofile(filename=self.output_file_name, fps=self.output_fps)


    def generate_image_clip(self,image,subtitles):
            _image = self.preprocess_image(image)
            image_clip = ImageClip(_image).set_duration(IMAGE_DURATION).crossfadein(TRANSITION_DURATION).crossfadeout(TRANSITION_DURATION)
            txt_clip = TextClip(subtitles[self.index],size=(1280,720),fontsize=FONT_SIZE,color=FONT_COLOR, stroke_color=FONT_STROKE_COLOR,stroke_width=STROKE_WIDTH,method="caption",align="South")
            self.index += 1
            txt_clip = txt_clip.set_pos(SUBTITLE_POSITION).set_duration(IMAGE_DURATION - 0.20)
            video_clip = CompositeVideoClip([image_clip, txt_clip])
            return video_clip

    """
        CHECK IMAGE RESULATION AND ADJEST IT ACCORDING TO OUTPUT
    """
    def preprocess_image(self,image):
           img = Image(image)
           _image = img.resize()
           return _image

    def intro_video(self,image_folder):
            return VideoFileClip(image_folder+"/"+self.intro_name)

    def end_video(self,image_folder):
            return VideoFileClip(image_folder+"/"+self.end_screen_name)

    def add_text_to_image(self,subtitles,index):
            pass
    
    def get_image_files(self,image_folder):
            return [
                image_folder+'/'+image 
                for image 
                in os.listdir(image_folder) if (
                    image.endswith(".jpg") or
                    image.endswith(".jpeg")
                )
            ]

    """
        Read subtitle file and return arrray
        'new line \n' is the delimiter
    """
    def get_subtitles(self):
            subtitle_file = open(self.image_folder+'/'+self.subtitle_file, 'r') 
            count = 0
            subtitles = []
            for line in subtitle_file: 
                count += 1
                subtitles.append(line)

            subtitle_file.close() 
            return subtitles