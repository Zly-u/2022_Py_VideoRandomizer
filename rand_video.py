from moviepy.editor import *
from moviepy.video.fx.all import *
import random
from datetime import datetime
from os import path, listdir
import os
import numpy as np
import sys

from config import config

media_path = ['output', 'song', 'song_short', 'videos']

def to_bool(bool_str):
    low_str = bool_str.lower()
    if low_str == 'true':
        return True
    elif low_str == 'false':
        return False
    elif low_str == '1':
        return True
    else:
        return False

exit_after = False
for p in media_path:
    if not path.exists(p):
        os.mkdir(p)
        if p == media_path[3]:
            exit_after = True

if exit_after:
    print("Folders were created, exiting...")
    os.exit()

print("Parsing cmd args")
print('Args: ', sys.argv)
if(len(sys.argv) > 1):
    try:
        for i in range(1, len(sys.argv)):
            if(sys.argv[i] in config):                
                config[sys.argv[i]] = sys.argv[i+1]                
    except e as Exception:
        print(f'Wrong command line arguments\n{e}')

# reading config into variables
# variables
vids = []
index = 0
min_duration = float(config['min_duration'])
max_duration = float(config['max_duration'])
clips_amount = int(config['clips_amount'])
filename = config['filename']

max_reverses = int(config['max_reverses'])
max_lags = int(config['max_lags'])
threads_amount = int(config['threads_amount'])
min_volume_mult = int(config['min_volume_mult'])
max_volume_mult = int(config['max_volume_mult'])
earrape_multiplier = int(config['earrape_multiplier'])
min_short_sounds = int(config['min_short_sounds'])
max_short_sounds = int(config['max_short_sounds'])
min_randomized_frames = int(config['min_randomized_frames'])
max_randomized_frames = int(config['max_randomized_frames'])
min_frame_duration = float(config['min_frame_duration'])
max_frame_duration = float(config['max_frame_duration'])

#     probabilities
reverse_prob = int(config['reverse_prob'])
lag_prob = int(config['lag_prob'])
random_audio_prob = int(config['random_audio_prob'])
speed_prob = int(config['speed_prob'])
volume_increase_prob = int(config['volume_increase_prob'])
mirror_prob = int(config['mirror_prob'])
image_distortion_prob = int(config['image_distortion_prob'])
random_earrape_prob = int(config['random_earrape_prob'])
randomize_frames_prob = int(config['randomize_frames_prob'])
add_random_sound_prob = int(config['add_random_sound_prob'])
add_short_sound_prob = int(config['add_short_sound_prob'])

#     attributes
random_audio = to_bool(config['random_audio'])
random_mirror = to_bool(config['random_mirror'])
speed_up = to_bool(config['speed_up'])
audio_split = to_bool(config['audio_split'])
reverse_video = to_bool(config['reverse_video'])
video_lag = to_bool(config['video_lag'])
increase_volume = to_bool(config['increase_volume'])
distort_image = to_bool(config['distort_image'])
random_earrape = to_bool(config['random_earrape'])
randomize_frames = to_bool(config['randomize_frames'])
add_random_sound = to_bool(config['add_random_sound'])
add_short_sound = to_bool(config['add_short_sound'])
enable_all = to_bool(config['enable_all'])

hell_mode = to_bool(config['hell_mode'])

print("Loading videos...")
video_path = f'{path.curdir}\\{media_path[3]}'
videos = [[VideoFileClip(f'{video_path}\\{f}'), f, 0] for f in listdir(video_path) if f.endswith('.mp4') or f.endswith('.mov') or f.endswith('.avi')]

print("Loading songs...")
song_path = f'{path.curdir}\\{media_path[1]}'
songs = [AudioFileClip(f'{song_path}\\{f}') for f in listdir(song_path) if f.endswith('.mp3')]

print("Loading sounds...")
short_sound_path = f'{path.curdir}\\{media_path[2]}'
short_sound = [AudioFileClip(f'{short_sound_path}\\{f}') for f in listdir(short_sound_path) if f.endswith('.mp3')]

print("Resizing videos...")
if(len(videos) == 0):
    os.exit(0)
size = (1280,720)
for i in range(0, len(videos)):
    videos[i][0] = videos[i][0].resize(size)

def enable_all_options():
    global random_audio
    global speed_up 
    global reverse_video 
    global video_lag
    global increase_volume
    global random_earrape
    global randomize_frames
    global add_random_sound
    global add_short_sound 

    random_audio = True
    speed_up = True
    reverse_video = True
    video_lag = True
    increase_volume = True
    random_earrape = True
    randomize_frames = True
    add_random_sound = True
    add_short_sound = True

def switch_all_probabilities(value = 100):
    global reverse_prob
    global lag_prob 
    global random_audio_prob 
    global speed_prob 
    global volume_increase_prob
    global mirror_prob 
    global image_distortion_prob
    global random_earrape_prob
    global randomize_frames_prob 
    global add_random_sound_prob
    global add_short_sound_prob

    reverse_prob = value
    lag_prob = value
    random_audio_prob = value
    speed_prob = value
    volume_increase_prob = value
    mirror_prob = value
    image_distortion_prob = value
    random_earrape_prob = value
    randomize_frames_prob = value
    add_random_sound_prob = value
    add_short_sound_prob = value
    
def randomize_values():
    global random_earrape
    global add_random_sound
    global max_reverses
    global max_lags
    global earrape_multiplier
    global min_short_sounds
    global max_short_sounds
    global min_randomized_frames
    global max_randomized_frames
    global min_frame_duration
    global max_frame_duration
    global randomize_frames

    max_reverses = random.randint(7, 15)
    max_lags = random.randint(6, 40)
    earrape_multiplier = random.randint(4, 8)
    min_short_sounds = random.randint(3, 15)
    max_short_sounds = random.randint(min_short_sounds + 1, 50)
    min_randomized_frames = random.randint(25, 67)
    max_randomized_frames = random.randint(min_randomized_frames + 1, 200)
    min_frame_duration = random.uniform(0.09, 0.1)
    max_frame_duration = random.uniform(min_frame_duration + 0.04, 0.25)

def get_next_index(index, do_random = False):
    global videos
    if do_random:
        return random.randint(0, len(videos) - 1)
    index += 1
    if(index == len(videos)):
        return 0
    else:
        return index

def get_begin_end(vid_duration, clip_duration = 1):
    beg = random.uniform(0, vid_duration - clip_duration)
    end = beg + clip_duration
    return beg, end

def change_img(img):
    A = img.shape[0] / random.uniform(1,4)
    w = random.uniform(2,4) / img.shape[0]
    shift = lambda x: A * np.sin(random.uniform(2,3)*np.pi*x * w)
    for i in range(img.shape[1]):
        img[:,i] = np.roll(img[:,i], int(shift(i)))
    return img

def insert_random_sound(clip):
    if(len(short_sound) == 0):
        return clip
    sounds_amount = random.randint(min_short_sounds, max_short_sounds)
    for _ in range(0, sounds_amount):
        sound = short_sound[random.randint(0, len(short_sound)-1)]
        sound = sound.volumex(2)
        
        if(clip.duration < sound.duration):
            sound = sound.subclip(0, clip.duration)
        
        clip_audio = clip.audio
        b, _ = get_begin_end(clip.duration, sound.duration)        
        final_audio = CompositeAudioClip([sound.set_start(b), clip_audio])
        clip.audio = final_audio
    return clip

def randomize_clip(clip):
    duration_ = clip.duration
    do_speed = random.randint(0, 100)
    do_random_audio = random.randint(0, 100)    
    do_mirror_x = random.randint(0, 100)
    do_split_audio_clip = random.randint(0, 100)
    do_reverse_video = random.randint(0, 100)
    do_video_lag = random.randint(0, 100)    
    do_increase_volume = random.randint(0, 100)
    do_image_distortion = random.randint(0, 100)
    do_random_earrape = random.randint(0, 100)
    do_randomize_frames = random.randint(0, 100)
    do_add_random_sound = random.randint(0, 100)
    do_add_short_sound = random.randint(0, 100)
    do_insert_random_short_after_edit = random.randint(0, 100)

    print(f" - do_speed: {do_speed < speed_prob and speed_up}")
    print(f" - do_random_audio: {do_random_audio < random_audio_prob and random_audio}")
    print(f" - do_mirror_x: {do_mirror_x < mirror_prob and random_mirror}")
    print(f" - do_reverse_video: {do_reverse_video < reverse_prob and reverse_video}")
    print(f" - do_video_lag: {do_video_lag < lag_prob and video_lag}")
    print(f" - do_increase_volume: {do_increase_volume < volume_increase_prob and increase_volume}")
    print(f" - do_image_distortion: {do_image_distortion < image_distortion_prob and distort_image}")
    print(f" - do_random_earrape: {do_random_earrape < random_earrape_prob and random_earrape}")
    print(f" - do_randomize_frames: {do_randomize_frames < randomize_frames_prob and randomize_frames}")
    print(f" - do_add_random_sound: {do_add_random_sound < add_random_sound_prob and add_random_sound}")
    print(f" - do_add_short_sound: {do_add_short_sound < add_short_sound_prob and add_short_sound}")
    print(f" - do_insert_random_short_after_edit: {do_insert_random_short_after_edit <= 67 and add_short_sound}")
    
    if(do_random_audio < random_audio_prob and random_audio):
        indx = get_next_index(0, do_random=True)        
        counter = 0
        while(videos[indx][0].duration < duration_):
            indx = get_next_index(indx)
            counter += 1
            if(counter == len(videos)):
                break                
        b, e = get_begin_end(videos[indx][0].duration, duration_)
        audio = videos[indx][0].audio
        if audio == None:
            print(f"Audio of {videos[indx][1]} is none")
        else:
            audio = audio.subclip(b, e)
            clip = clip.set_audio(audio)
    
    # random short sound
    if(do_insert_random_short_after_edit > 67):
        if(add_short_sound and do_add_short_sound > add_short_sound_prob):
            clip = insert_random_sound(clip)
    
    # audio split
    if(do_split_audio_clip < 70 and audio_split and duration_ > 1):
        audio = clip.audio
        audio_insertion_duration = random.uniform(0.5, 1)
        first = audio.subclip(0, audio_insertion_duration)
        indx = get_next_index(0, do_random=True)
        counter = 0
        while(videos[indx][0].duration < audio_insertion_duration):
            indx = get_next_index(indx)
            counter += 1
            if(counter == len(videos)):
                break        
        rnd_audio = videos[indx][0].audio
        b, e = get_begin_end(clip.duration, clip.duration - audio_insertion_duration)
        second = rnd_audio.subclip(b, e)
        new_audio = concatenate_audioclips([first, second])
        clip = clip.set_audio(new_audio)
    
    # video lag
    if(do_video_lag < lag_prob and video_lag or (do_image_distortion < image_distortion_prob and clip.duration < 1.2)):
        lags_insertions = random.randint(1, max_lags)
        for ___ in range(lags_insertions):
            amount_of_repetitions = random.randint(8, 20)
            lags = []
            single_lag_duration = random.uniform(0.01, 0.04)
            b, e = get_begin_end(clip.duration, single_lag_duration)
            for _ in range(0, amount_of_repetitions):
                lags.append(clip.subclip(b,e))
            clip_beg = clip.subclip(0, b)
            clip_end = clip.subclip(e, clip.duration)
            all_clips = [clip_beg] + lags + [clip_end]
            clip = concatenate_videoclips(all_clips)
            lags.clear()
    
    # video reverse
    if(do_reverse_video < reverse_prob and reverse_video):
        reverse_amount = random.randint(1, max_reverses)        
        for ___ in range(reverse_amount):
            reverse_duration = random.uniform(0.3, 0.7)
            b, e = get_begin_end(clip.duration, reverse_duration)
            clip_to_reverse = clip.subclip(b,e)
            clip_reversed = clip_to_reverse.fx(time_mirror)
            clip_beg = clip.subclip(0, b)
            clip_end = clip.subclip(e, clip.duration)
            clip = concatenate_videoclips([clip_beg, clip_reversed, clip_to_reverse, clip_end])
    
    # random earrape
    if(do_random_earrape < random_earrape_prob and random_earrape):
        earrape_duration = random.uniform(0.4, clip.duration)
        b, e = get_begin_end(clip.duration, earrape_duration)
        clip_audio = clip.audio
        first = clip_audio.subclip(0, b)
        middle = clip_audio.subclip(b, e)
        last = clip_audio.subclip(e, clip.duration)
        middle = middle.volumex(earrape_multiplier)
        final_audio = concatenate_audioclips([first, middle, last])
        clip.audio = final_audio
    
    # video speed up/downы
    if(do_speed < speed_prob and speed_up):
        speed = random.uniform(0.6, 1.5)
        clip = clip.speedx(speed)
    
    # volume increase
    if(do_increase_volume < volume_increase_prob or (do_image_distortion > image_distortion_prob and clip.duration < 1.2)):    
        multiplier = random.randint(min_volume_mult, max_volume_mult)
        clip = clip.volumex(multiplier)
    
    # video mirroring
    if(do_mirror_x < mirror_prob and random_mirror):
        clip = mirror_x(clip)
    
    # image distortion
    if(do_image_distortion < image_distortion_prob and distort_image and clip.duration < 1.2):
        clip = clip.fl_image(change_img)
    
    # randomize parts
    if(randomize_frames and do_randomize_frames < randomize_frames_prob):
        parts_amount = random.randint(min_randomized_frames, max_randomized_frames)
        randomized_parts = []        
        for _ in range(parts_amount):
            rand_duration = random.uniform(min_frame_duration, max_frame_duration)
            b, e = get_begin_end(clip.duration, rand_duration)
            randomized_parts.append(clip.subclip(b,e))
        print(f"Randomized frames amount: {len(randomized_parts)}")
        clip = concatenate_videoclips(randomized_parts)
    
    # random song
    if(add_random_sound and do_add_random_sound < add_random_sound_prob):
        if(len(songs) != 0):
            song = songs[random.randint(0, len(songs)-1)]
            b,e = get_begin_end(song.duration, clip.duration)
            clip_audio = clip.audio
            song = song.subclip(b,e)
            final_audio = CompositeAudioClip([song, clip_audio])
            clip.audio = final_audio
    
    # random sound after edit
    if(do_insert_random_short_after_edit <= 67):
        if(add_short_sound and do_add_short_sound < add_short_sound_prob):
            clip = insert_random_sound(clip)

    return clip

def create_random_video():
    print("Randomizer start")
    global hell_mode
    global enable_all
    
    if(enable_all):
        print('Enabling everything')
        enable_all_options()
    
    if(hell_mode):
        print("Hell mode enabled")        
        switch_all_probabilities(100)
        randomize_values()

    # initial parameters printing
    print()
    print(f"random_audio: {random_audio}")
    print(f"speed_up: {speed_up}")
    print(f"reverse_video: {reverse_video}")
    print(f"video_lag: {video_lag}")
    print(f"increase_volume: {increase_volume}")
    print(f"random_earrape: {random_earrape}")
    print(f"randomize_frames: {randomize_frames}")
    print(f"add_random_sound: {add_random_sound}")
    print(f"add_short_sound: {add_short_sound}")
    print()
    print(f"reverse_prob: {reverse_prob}")
    print(f"lag_prob: {lag_prob}")
    print(f"random_audio_prob: {random_audio_prob}")
    print(f"speed_prob: {speed_prob}")
    print(f"volume_increase_prob: {volume_increase_prob}")
    print(f"mirror_prob: {mirror_prob}")
    print(f"image_distortion_prob: {image_distortion_prob}")
    print(f"random_earrape_prob: {random_earrape_prob}")
    print(f"randomize_frames_prob: {randomize_frames_prob}")
    print(f"add_random_sound_prob: {add_random_sound_prob}")
    print(f"add_short_sound_prob: {add_short_sound_prob}")
    print()
    print(f"max_lags: {max_lags}")
    print(f"threads_amount: {threads_amount}")
    print(f"min_volume_mult: {min_volume_mult}")
    print(f"max_volume_mult: {max_volume_mult}")
    print(f"earrape_multiplier: {earrape_multiplier}")
    print(f"min_short_sounds: {min_short_sounds}")
    print(f"max_short_sounds: {max_short_sounds}")
    print(f"min_randomized_frames: {min_randomized_frames}")
    print(f"max_randomized_frames: {max_randomized_frames}")
    print(f"min_frame_duration: {min_frame_duration}")
    print(f"max_frame_duration: {max_frame_duration}")
    print()

    index = get_next_index(0, do_random=True)
    clip_count = 0
    print(f"Videos: {len(videos)}")
    for _ in range(clips_amount):    
        try:        
            if(hell_mode):
                randomize_values()
                
            duration_ = random.uniform(min_duration, max_duration)
            
            if videos[index][2] > (clips_amount / len(videos)):                
                insert_current_clip = random.randint(0, 100)
                if(insert_current_clip < 60):
                    index = get_next_index(index, do_random=True)
                
            if(videos[index][0].duration < duration_):
                duration_ = random.uniform(1, videos[index][0].duration)
            beg, end = get_begin_end(videos[index][0].duration, duration_)
            clip = videos[index][0].subclip(beg, end)
            print(f"{clip_count + 1}) Clip: {videos[index][1]}\t", "Duration: {:.2f}\tStart/End: {:.2f}/{:.2f}".format(duration_, beg, end))
            clip_count += 1
            clip = randomize_clip(clip)
            videos[index][2] += 1
            vids.append(clip)
            index = get_next_index(index, do_random=True)
        except Exception as ex:
            print("Error while randoming clips: ", ex)
        
    final = concatenate_videoclips(vids)
    print("Randomizer end")
    full_filename = f'{media_path[0]}\\{filename}.mp4'
    print("Final duration: {:.2f} s.".format(final.duration))
    final.write_videofile(full_filename, threads=threads_amount)
    final.close()
    input('Press any key to exit...')

if __name__ == '__main__': # entry
    create_random_video()
    
    
    
    
    
    
    
    
    