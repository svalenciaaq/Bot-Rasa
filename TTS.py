# Import the required module for text 
# to speech conversion
from gtts import gTTS
import pyglet


# This module is imported so that we can 
# play the converted audi


class tts():

    mytext = 'Welcome to geeksforgeeks!'
    # Language in which you want to convert
    language = 'es'
  
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)
    file = "file.mp3"  
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save(file)
    
    # Playing the converted file


    music = pyglet.resource.media('file.mp3')
    music.play()

    pyglet.app.run()