import cv2
import os

in_directory = ""
out_dir = ""

for filename in os.listdir(in_directory):

    file = os.path.join(in_directory, filename)

    capture = cv2.VideoCapture(file)

    frameNr = 0

    while True:

        success, frame = capture.read()

        if success:
            filename_name, ext = os.path.splitext(filename)

            filename_out = f"{filename_name}_{frameNr}.jpg"
            file_out = os.path.join(out_dir, filename_out)

            cv2.imwrite(file_out, frame)

        else:
            break

        frameNr = frameNr + 1

    capture.release()
