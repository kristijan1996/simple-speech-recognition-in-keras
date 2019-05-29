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

# System
System design is depicted in the figure bellow.

<p align="center">
          <img width=600 src="/images/system.png">
</p>

Preprocessing block transforms audio signal into a matrix of fixed dimensions, using [Mel frequency cepstrum transform](http://practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/). This approach is based on the fact that the Mel transformation produces unique signal signature in the frequency domain. This is similar to Fourier transform, thanks to which we can observe signal characteristics in frequency domain, from which we can conclude various interesing information about its nature.

So, each one of the spoken words listed before has a unique stamp, i.e. unique frequency content in time. On the following image, spectrogram of word _up_ is shown.

<p align="center">
          <img width=400 src="/images/melspectrogram.png">
</p>

From this spectrogram, a _periodogram_ is obtained, which shows the spectral power dependency on the frequencies present in the signal. By filtering periodogram with Mel filter bank, we obtain information about energy content of the signal in each of the zones covered by this bank.

<p align="center">
          <img width=400 src="/images/melbank.png">
</p>

Finally, a discrete cosine transform of logarithmically compressed energy banks is performed, and only the most valuable coeffitients are kept, close to DC value.

After everything mentioned, we are left with a unique matrix of Mel coefficients with fixed dimensions, which can be directly fed into CNN.

<p align="center">
          <img width=300 src="/images/mfcc.png">
</p>
