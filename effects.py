from moviepy.editor import *
from moviepy.editor import vfx

import random, time, warnings

class Effects:
    generation_params = None

    def __init__(self, gen_params):
        self.generation_params = gen_params


    def lagVideo(self, video):
        if random.uniform(0, 1) > self.generation_params.chances["lag"]: return

        lags_range = self.generation_params.amount_of_random_parts_per_video["lags"]
        lags = random.randrange(lags_range[0], lags_range[1])

        last_clip = video
        new_clips = []
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

            new_clips.append(first_clip)
            for i in range(lag_segments):
                new_clips.append(lag_clip)

        # put it here to prevent dublications and end with the rest of the video
        new_clips.append(last_clip)

        # We make a whole clip out of it to process again later if desired
        return concatenate_videoclips(new_clips)


    def reverseWholeVideo(self, video):
        if random.uniform(0, 1) > self.generation_params.chances["reverse_whole_video"]: return
        print("[FX] Reversing Whole Video...")

        edited_video = video
        try:
            edited_video = vfx.time_mirror(video)
            print("DONE!")
        except IOError as e:
            print("Error: could not process video!")
            # print(e)

            # edited_video = edited_video.set_start((1.0/edited_video.fps))
            # edited_video = edited_video.fl_time(lambda t: edited_video.duration - t, keep_duration=True)

            # warnings.warn("[reverseWholeVideo] Error: could not process video:")
            # warnings.warn(e)
            edited_video = video

        return edited_video


    def reversePartOfTheVideo(self, video):
        pass

    def souosPartOfTheVideo(self, video):
        pass

    def replaceAudio(self, video):
        pass

    def overlayAudio(self, video):
        pass