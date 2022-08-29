import os

class OutputSettings:
    out_resolution = [640, 360]

    path_output:    str = os.path.curdir + "\TestOutput"
    output_name:    str = "test"
    output_format:  str = ".mp4"