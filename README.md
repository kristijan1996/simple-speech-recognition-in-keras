# simple-speech-recognition-in-keras
This project was conceived as a basis for implementing real-time speech processing in order to manipulate the robot movement.
The idea was to have some kind of system attached to Roomba iRobot vacuum cleaner, which would constantly listen on microphone and upon detecting some predefined commands, it would conduct the appropriate response.

# Detailed description of the idea
Concretely, this project is heavily relied on a [Kaggle competition](https://www.kaggle.com/c/tensorflow-speech-recognition-challenge) dataset, from which couple of words interesting for this application were chosen:

   * _marvin_
   * _up_
   * _down_
   * _left_
   * _right_
   
These words were chosen so that upon recognizing _marvin_ (which is a suitable replacement for _hey, Roomba!_), robot starts observing the following voice command from the list above, and conducting a simple response to it, such as moving _1 m_ forward, backward, left or right.
Short spoken word would be processed through a system described in this project, by (somehow) storing the audio in _.wav_ format, which is input to the system depicted in the following sections. Main part of the system is a _CNN_ which is used to classify spoken word into one of the categories listed above, which would then trigger robot movement.

Real-time processing is yet to be implemented in the future, since it was not easily doable at the time this was written, for reasons which will be described at the end.
