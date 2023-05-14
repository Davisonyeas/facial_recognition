
# Facial Recognition System

Face recognition technology is a biometric technology, which is based on the identificationof facial features of a person. It is a technology in which computers use to recognize faces


![](mask_det.gif)  

## Acknowledgements

 - [A Review of Face Recognition Technology](https://www.researchgate.net/publication/343118558_A_Review_of_Face_Recognition_Technology)
 - [Design and Implementation of a Real-Time Face Recognition System Based on Artificial Intelligence Techniques](https://www.researchgate.net/publication/366113631_Design_and_Implementation_of_a_Real-Time_Face_Recognition_System_Based_on_Artificial_Intelligence_Techniques)



## Advantages

This solution provides the following:

- Face recognition accuracy 99.38% 
- Ability to identify multiple people at once in real time based on one or more reference images.
- Ability to track and assign a unique identifier to each person in the camera image or video. 
- Ability to return a similarity measured between detected faces and reference faces.
## Business Case
​
Can be used in access control systems or Online Proctoring systems for student authentication or bank authentication
## Technical details 

**Input 1 (video or image to process, capable of processing):** ​​

- mjpeg stream

- rtsp stream

- USB camera devices

- video files (avi, mp4, mkv formats supported)

- standalone image files (.png, .jpg formats supported)

 

**Input 2:**

Reference images to which the system compares the faces in the image. (.png, .jpg formats supported)


**Outputs:**

- Processed video frame

- The faces in the frame (bounding boxes)

**For each face:**

- Unique Tracking ID (when processing a video file, the same ID on each frame belongs to the same person)

- The most similar reference face ID

- Degree of similarity to the reference face

- Up to 5 facial landmark points

- The system is able to to write the processed video to a video file. 
## Used By

This project is used by the following:

- Kaduna State University
- Daton


## Tech Stack

- Dlib, Numpy, OpenCV, Flask
## How to use 

- pip install requirements.txt

- python app.py


## Connect

For support, email davisonyeas1@gmail.com

Follow me on LinkedIn, https://www.linkedin.com/in/davis-onyeoguzoro/