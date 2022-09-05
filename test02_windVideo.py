from moviepy.editor import *

files = ['wind_00H.png', 'wind_03H.png', 'wind_06H.png', 'wind_09H.png',
         'wind_12H.png', 'wind_15H.png', 'wind_18H.png', 'wind_21H.png']
clip = ImageSequenceClip(files, fps = 2)
clip.write_videofile("wind_video.mp4", fps = 2)