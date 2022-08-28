from moviepy.editor import *
import numpy as np

import os
import sys
import random
import re


class GenerationParams:
    chances = {
        "reverse_whole_video": 1,
        "reverse_part_of_the_video": 1,
        "lag": 1,
    }

    amount_of_random_parts_per_video = {
        "reverses": [1, 3],

        "lags": [3, 4],
        "lag_segments": [10, 30],
    }

    lengths = {
        "lag_lengths_in_frames": [4, 10]
    }

    pick_unique = False


class OutputSettings:
    out_resolution = [640, 360]

    path_output:    str = os.path.curdir + "\TestOutput"
    output_name:    str = "test"
    output_format:  str = ".mp4"


class VideoRandomizer:
    gathered_videos: list[VideoFileClip] = []
    edited_clips = []

    paths_to_gather_from: list[str] = [os.path.curdir + r"\vidsToTestWith"]
    compatible_formats: list[str] = ["mp4", "avi", "mov", "webm", "3gp"]
    amount_of_videos_to_get: int = 10

    output_settings = OutputSettings()
    generation_params = GenerationParams()

    def __init__(self):
        for path in self.paths_to_gather_from:
            self.getVideos(path)

        print(self.gathered_videos)

        self.glueVideos()


    def getVideos(self, path: str):
        video_count = 0

        for video in os.listdir(path):
            match = re.match(".+\.(\w+)$", video)
            if match.group(1) in self.compatible_formats:
                video_path = path + f"\\{video}"
                print(f"{video_count} Video loaded: {video}")
                self.gathered_videos.append(VideoFileClip(video_path))

                video_count+=1
                if video_count != 0 and video_count == self.amount_of_videos_to_get: return

        self.processVideo()


    def glueVideos(self):
        final_clip = None

        # final_clip = clips_array(
        #     [[self.videos[0], self.videos[1]],[self.videos[2], self.videos[0]]]
        # )

        final_clip = concatenate_videoclips(self.edited_clips, method ="compose") # this doesn't break vids

        final_clip.write_videofile(self.output_settings.path_output+"\\"+self.output_settings.output_name+self.output_settings.output_format)


    def processVideo(self):
        vid = self.gathered_videos[random.randrange(0, len(self.gathered_videos)-1)]

        self.lagVideo(vid)

        self.glueVideos()


    def lagVideo(self, video: VideoFileClip):
        lag_chance = self.generation_params.chances["lag"]
        if random.uniform(0, 1) > lag_chance: return

        lags_range = self.generation_params.amount_of_random_parts_per_video["lags"]
        lags = random.randrange(lags_range[0], lags_range[1])

        last_clip = video
        for lag in range(lags):
            lag_segments_range = self.generation_params.amount_of_random_parts_per_video["lag_segments"]
            lag_segments = random.randrange(lag_segments_range[0], lag_segments_range[1])

            lag_len_range = self.generation_params.lengths["lag_lengths_in_frames"]
            lag_len = random.randrange(lag_len_range[0], lag_len_range[1])
            frame_time = 1.0/last_clip.fps
            lag_part_len = frame_time*lag_len

            lag_pos_start = random.uniform(0, last_clip.duration * 0.9)

            if lag_pos_start+lag_part_len > last_clip.duration:
                lag_part_len = abs(last_clip.duration-lag_pos_start)

            first_clip  = last_clip.subclip(0, lag_pos_start)
            lag_clip    = last_clip.subclip(lag_pos_start, lag_pos_start + lag_part_len)
            last_clip   = last_clip.subclip(lag_pos_start + lag_part_len, last_clip.duration)

            self.edited_clips.append(first_clip)
            for i in range(lag_segments):
                self.edited_clips.append(lag_clip)

        self.edited_clips.append(last_clip)




def main():
    vr = VideoRandomizer()


main()