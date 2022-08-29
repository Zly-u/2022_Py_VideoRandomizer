class GenerationSettings:
    chances = {
        "reverse_whole_video": 1,
        "reverse_part_of_the_video": 1,
        "doube_reverse_part_of_the_video": 1,

        "lag": 1,
    }

    amount_of_random_parts_per_video = {
        "reverses": [1, 3],

        "lags": [3, 4],
        "lag_segments": [10, 30],

        "random_audios": [2, 4],
    }

    lengths = {
        "lag_lengths_in_frames": [4, 10]
    }

    pick_unique = False