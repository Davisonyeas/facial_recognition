import cv2
import face_recognition
import numpy as np

def generate_frames():
    # read frames continuously, that is why we loop

   
    camera = cv2.VideoCapture(0)

    # Load a sample picture and learn how to recognize it.
    andrew_image = face_recognition.load_image_file("faces/Andrew_ng.png")
    andrew_face_encoding = face_recognition.face_encodings(andrew_image)[0]

    # Load a second sample picture and learn how to recognize it.
    bill_image = face_recognition.load_image_file("faces/Bill_gates.webp")
    bill_face_encoding = face_recognition.face_encodings(bill_image)[0]

    # Load a sample picture and learn how to recognize it.
    davis_image = face_recognition.load_image_file("faces/Davis.png")
    davis_face_encoding = face_recognition.face_encodings(davis_image)[0]

    # Load a second sample picture and learn how to recognize it.
    elon_image = face_recognition.load_image_file("faces/Elon_Musk.jpeg")
    elon_face_encoding = face_recognition.face_encodings(elon_image)[0]

    # Load a sample picture and learn how to recognize it.
    guido_image = face_recognition.load_image_file("faces/Guido_rossum.jpeg")
    guido_face_encoding = face_recognition.face_encodings(guido_image)[0]

    # Load a second sample picture and learn how to recognize it.
    jeff_image = face_recognition.load_image_file("faces/Jeff_bezos.jpeg")
    jeff_face_encoding = face_recognition.face_encodings(jeff_image)[0]

    # Load a sample picture and learn how to recognize it.
    mark_image = face_recognition.load_image_file("faces/Mark_zuckerberg.webp")
    mark_face_encoding = face_recognition.face_encodings(mark_image)[0]

    # Load a second sample picture and learn how to recognize it.
    oprah_image = face_recognition.load_image_file("faces/Oprah_winfery.jpeg")
    oprah_face_encoding = face_recognition.face_encodings(oprah_image)[0]

    # Load a sample picture and learn how to recognize it.
    sergey_image = face_recognition.load_image_file("faces/Sergey_brin.jpeg")
    sergey_face_encoding = face_recognition.face_encodings(sergey_image)[0]

    # Load a second sample picture and learn how to recognize it.
    steve_image = face_recognition.load_image_file("faces/Steve_jobs.webp")
    steve_face_encoding = face_recognition.face_encodings(steve_image)[0]

    # Load a sample picture and learn how to recognize it.
    tim_image = face_recognition.load_image_file("faces/Tim_berners_lee.webp")
    tim_face_encoding = face_recognition.face_encodings(tim_image)[0]

    # Load a second sample picture and learn how to recognize it.
    warren_image = face_recognition.load_image_file("faces/Warren_buffet.webp")
    warren_face_encoding = face_recognition.face_encodings(warren_image)[0]

    # Load a second sample picture and learn how to recognize it.
    wozniak_image = face_recognition.load_image_file("faces/Wozniak.webp")
    wozniak_face_encoding = face_recognition.face_encodings(wozniak_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        andrew_face_encoding,
        bill_face_encoding,
        davis_face_encoding,
        elon_face_encoding,
        guido_face_encoding,
        jeff_face_encoding,
        mark_face_encoding,
        oprah_face_encoding,
        sergey_face_encoding,
        steve_face_encoding,
        tim_face_encoding,
        warren_face_encoding,
        wozniak_face_encoding
    ]
    known_face_names = [
        "Andrew Ng",
        "Bill Gates",
        "Davis Onyeoguzoro",
        "Elon Musk",
        "Guido van Rossum",
        "Jeff Bezos",
        "Mark Zuckerberg",
        "Oprah Winfery",
        "Sergey Brin",
        "Steve Jobs",
        "Tim Berners Lee",
        "Warren Buffet",
        "Steve Wozniak",
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True


    while True:
        # read the camera frame, save frame to variable
        success, frame = camera.read()
        if not success:
            # if no frame, e.g camera is not working, then end code
            break
        else:
             
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
            
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        # process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
        cv2.imshow("Recognizing face", frame)

        if cv2.waitKey(1) == 27:
            break
    
    cv2.destroyAllWindows()



