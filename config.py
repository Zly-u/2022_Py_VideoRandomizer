from datetime import datetime
config = {
	'min_duration': '1.5',
	'max_duration': '4',
	'clips_amount': '70',
	'filename': str(datetime.now()).replace(':','_').replace('-', '_'),	
	'max_reverses': '2',
	'max_lags': '3',
	'threads_amount': '8',
	'min_volume_mult':'2',
	'max_volume_mult': '3',
	'earrape_multiplier': '6',
	'min_short_sounds': '1',
	'max_short_sounds': '3',
	'min_randomized_frames': '8',
	'max_randomized_frames': '20',
	'min_frame_duration': '0.1',
	'max_frame_duration': '0.3',	
	# 	probabilities
	'reverse_prob': '70',
	'lag_prob': '67',
	'random_audio_prob': '50',
	'speed_prob': '80',
	'volume_increase_prob': '20',
	'mirror_prob': '10',
	'image_distortion_prob': '10',
	'random_earrape_prob': '30',
	'randomize_frames_prob': '50',
	'add_random_sound_prob': '43',
	'add_short_sound_prob': '43',	
	# 	attributes
	'random_audio': 'True',
	'random_mirror': 'False',
	'speed_up': 'True',
	'audio_split': 'False',
	'reverse_video': 'True',
	'video_lag': 'True',
	'increase_volume': 'True',
	'distort_image': 'False',
	'random_earrape': 'True',
	'randomize_frames': 'True',
	'add_random_sound': 'True',
	'add_short_sound': 'True',	
	'enable_all': 'False',
	'hell_mode': 'False',
}