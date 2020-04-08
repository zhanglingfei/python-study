from os.path import abspath, isfile

import pyglet


def loadsong(filename):
   # check for file
   print("Attempting to load "+filename)
   filename = abspath(filename)
   if not ( isfile(filename) ):
      raise Exception(filename+" not found.")
   # create a player for this file
   song = pyglet.media.load(filename)
   source = song.play()
   source.eos_action = source.EOS_LOOP
   source.pause()
   return source

music = loadsong("test.mp3")
music.seek(57)
music.play()
pyglet.app.run()