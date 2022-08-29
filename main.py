from moviepy.editor import *

import numpy as np

import os, random, re

from effects import Effects
from genSettings import GenerationSettings
from outSettings import OutputSettings


def getVideoName(video):
    regex_pattern = "\w+\.\w+$"
    return re.findall(regex_pattern, video.filename)[0]


class VideoRandomizer:
    gathered_videos: list[VideoFileClip] = []
    edited_clips = []

    check_paths_to_gather_from: list[str] = [os.path.curdir + r"\vidsToTestWith"]
    paths_to_gather_from: list[str] = []
    compatible_formats: list[str] = ["mp4", "avi", "mov", "webm", "3gp"]
    amount_of_videos_to_get: int = 10

    output_settings = OutputSettings()
    generation_params = GenerationSettings()

    vfx = Effects(generation_params)

    def __init__(self):
        self.checksStuff()

        for path in self.paths_to_gather_from:
            self.getVideos(path)

        for video in self.gathered_videos:
            print(getVideoName(video))

        self.processVideos()

        self.glueVideos()


    def checksStuff(self):
        for path in self.check_paths_to_gather_from:
            if os.path.exists(path):
                self.paths_to_gather_from.append(path)

        assert len(self.paths_to_gather_from) != 0, "No valid paths to get videos from were specified!"

        try:
            os.mkdir(self.output_settings.path_output)
        except OSError as e:
            print("Output path already exists!")



    def getVideos(self, path: str):
        video_count = 0
        print("\n[[ ~~~~~ Loading Videos! ~~~~~ ]]")

        for video in os.listdir(path):
            match = re.match(".+\.(\w+)$", video)
            if match.group(1) in self.compatible_formats:
                video_path = path + f"\\{video}"
                print(f"{video_count} Video loaded: {video}")
                self.gathered_videos.append(VideoFileClip(video_path))

                video_count+=1
                if video_count != 0 and video_count == self.amount_of_videos_to_get: return

        random.shuffle(self.gathered_videos)

        print("[[ ~~~~~ DONE Loading Videos! ~~~~~ ]]\n")


    def glueVideos(self):
        print(f"\n[[ ========= COMPILING EVERYTHING ========= ]]")
        final_clip = concatenate_videoclips(self.edited_clips, method ="compose") # this doesn't break vids

        final_clip.write_videofile(self.output_settings.path_output+"\\"+self.output_settings.output_name+self.output_settings.output_format)


    def processVideos(self):
        for video in self.gathered_videos:
            video_name = getVideoName(video)
            print(f"\n[[ ========= Processing: {video_name} ========= ]]")

            edited_vid = video

            edited_vid = self.vfx.lagVideo(edited_vid)
            # edited_vid = self.vfx.reverseWholeVideo(edited_vid)

            self.edited_clips.append(edited_vid)

            break





def main():
    vr = VideoRandomizer()


main()