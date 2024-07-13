# Speech-To-Text
This repository for Second task in Web Development track.

Task Requerements:

1- Build a user interface to convert voice to text (speech to text)

2- Save the text output to database

---------------------------------------
To build Speech to Text recognition system, I prefer to use Python Programming Language with PocketSphinx and save the generated text to MySql database.

What is PocketSphinx ?

PocketSphinx is one of Carnegie Mellon University's open source large vocabulary, speaker-independent continuous speech recognition engines. t's designed to run on resource-constrained devices and can be used for offline speech recognition.

Limitation:

Accuracy: May not be as accurate as online services like Google’s speech recognition, especially for diverse and complex language patterns. So some words is not recognized well but we can say the result is acceptable.

--------------------------------------------
Install used libraries:

pip install mysql-connector-python

pip install pyaudio

 pip install SpeechRecognition
 
---------------------------------------------

Database query:

    CREATE DATABASE speech_text_db;

    USE speech_text_db;

    CREATE TABLE speech_text (

    id INT AUTO_INCREMENT PRIMARY KEY,
    
    text TEXT NOT NULL  );

-----------------------------------------
User Interface:

![image](https://github.com/user-attachments/assets/510cbcee-f997-4d01-be33-66db685fb0ad)

Results:

![image](https://github.com/user-attachments/assets/dcc958e1-ce29-455b-aa1c-f30eb68f4f48)

Database:

![image](https://github.com/user-attachments/assets/ef12dcb5-29ee-44b1-a44d-a116cd43f4b1)

