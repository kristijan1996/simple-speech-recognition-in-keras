# simple-speech-recognition-in-keras
This project was conceived as a basis for implementing real-time speech processing in order to manipulate the robot movement.
The idea was to have some kind of system attached to Roomba iRobot vacuum cleaner, which would constantly listen on microphone and upon detecting some predefined commands, it would conduct the appropriate response.

# Detailed description of the idea
Concretely, this project is heavily relied on a [Kaggle competition](https://www.kaggle.com/c/tensorflow-speech-recognition-challenge) dataset, from which couple of words interesting for this application were chosen:

   * marvin
   * up
   * down
   * left
   * right
   
These words were chosen so that upon recognizing _marvin_ (which is a suitable replacement for _hey, Roomba!_), robot starts observing the following voice command from the list above, and conducting a simple response to it, such as moving _1 m_ forward, backward, left or right.
