from moviepy.editor import *

files = ['solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png',
         'solar_00H.png', 'solar_03H.png', 'solar_06H.png', 'solar_09H.png']

clip = ImageSequenceClip(files, fps = 7)
clip.write_videofile("solar_video.mp4", fps = 250)