import os
startup_parameters = {
    "clips_amount"          :    100       ,   # amount of clips that we will insert into our video
    "min_duration"          :    0.1       ,   # minimum duration of a single clip (in seconds, can be decimal i.e. 1.5)
    "max_duration"          :    10        ,   # maximum duration of a single clip (in seconds, can be decimal i.e. 1.5)
    "max_reverses"          :    10        ,   # maximum reverses that we want to be in a single clip
    "max_lags"              :    2         ,   # maximum lags that we want to be in a single clip
    "threads_amount"        :    20        ,   # amount of threads that this program will use to render video
    "min_volume_mult"       :    1         ,   # minimum volume multiplication
    "max_volume_mult"       :    2         ,   # maximum volume multiplication
    "earrape_multiplier"    :    2         ,   # earrape volume multiplication
    "min_short_sounds"      :    1         ,   # minimum amount of short sound that will be inserted in a single clip
    "max_short_sounds"      :    2         ,   # maximum amount of short sound that will be inserted in a single clip
    "min_randomized_frames" :    5         ,   # if a clip wiil be randomized in a small parts (frames) it will use this as a minimum amount
    "max_randomized_frames" :    10        ,   # same as previuos
    "min_frame_duration"    :    0.1       ,   # minimum duration of a frame (don"t set this parameter too big)
    "max_frame_duration"    :    1         ,   # maximum duration of a frame don"t set this parameter too big)
    "reverse_prob"          :    30        ,   # probability of reverse in a single clip (0-100)
    "lag_prob"              :    15        ,   # probability of lag in a single clip (0-100)
    "random_audio_prob"     :    30        ,   # probability of random audio in a single clip (0-100)
    "speed_prob"            :    44        ,   # probability of increasing speed of a single clip (0-100)
    "volume_increase_prob"  :    30        ,   # probability of increasing volume of a single clip (0-100)
    "mirror_prob"           :    12        ,   # probability of mirror the image in a single clip (0-100)
    "image_distortion_prob" :    99        ,   # probability of image dirstortion ( don"t use it) (0-100)
    "random_earrape_prob"   :    30        ,   # probability of earrape in a single clip (0-100)
    "randomize_frames_prob" :    10        ,   # probability of randomized frames in a single clip (0-100)
    "add_random_sound_prob" :    10        ,   # probability of adding random sound(music etc) in a single clip (0-100)
    "add_short_sound_prob"  :    60        ,   # probability of adding random short sound (1-4 seconds) in a single clip (0-100)
    "random_audio"          :    True      ,   # add random audio in a clip
    "random_mirror"         :    True      ,   # mirror the image in a clip
    "speed_up"              :    True      ,   # speed up a clip
    "audio_split"           :    False     ,   # split audio in a single clip (don"t use this, result is really bad)
    "reverse_video"         :    True      ,   # reverse clip
    "video_lag"             :    True      ,   # add lags in a clip
    "increase_volume"       :    False     ,      # increase volume of a clip
    "distort_image"         :    False     ,      # distort image in a clip (don"t use this)
    "random_earrape"        :    True      ,      # add random earrape
    "randomize_frames"      :    True      ,      # randomze frames of a clip
    "add_random_sound"      :    True      ,      # add random sound in a clip
    "add_short_sound"       :    True      ,    # add short sound in a clip
    "enable_all"            :    False     ,    # enables all settings except experimental stuff
    "hell_mode"             :    False          # sets all probabilities of enabled parameters to 100 and randomizes other values
}

os.system("py rand_video.py {:s}".format(str(startup_parameters).replace("{","").replace("}","").replace("\"","").replace(":","").replace(",","")))