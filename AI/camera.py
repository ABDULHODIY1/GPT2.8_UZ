# import cv2
#
# c = cv2.VideoCapture("http://192.168.43.1:8080/video")
# c.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# c.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#
# fourrc = cv2.VideoWriter_fourcc('m','p','4','v')
# writter = cv2.VideoWriter("recording.mp4", fourrc,30.0,(1280,720))
# recording=False
#
#
# while(True):
#     _, frame = c.read()
#     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR5552GRAY)
#     if frame is not None:
#         cv2.imshow('Hacker\'s App', frame)
#     else:
#         print("Videoni o'qib olishda xatolik yuz berdi!")
#     if cv2.waitKey(1) == ord("q"):
#         break
#     if recording:
#         writter.write(frame)
#
#     elif cv2.waitKey(1) == ord("r"):
#         recording= not recording
#         print(f"Recording: {recording}")
#
#
#
# c.release()
# writter.release()
# cv2.destroyAllWindows()
import cv2

# Create a VideoCapture object that connects to a video stream at the specified URL
c = cv2.VideoCapture("http://192.168.43.1:8080/video")

# Set the frame width and height to 1280x720
c.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
c.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Define the codec for the VideoWriter to create an MP4 file
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')


# Create a VideoWriter object to save the video frames to a file named "recording.mp4"
writter = cv2.VideoWriter("recording.mp4", fourcc, 30.0, (1280, 720))

# Initialize a boolean variable for recording
recording = False

while True:
    # Read a frame from the video stream
    _, frame = c.read()

    if frame is not None:
        # Display the frame in a window named "Hacker's App"
        cv2.imshow("Hacker's App", frame)
    else:
        print("Error reading the video frame!")

    # Check for user key presses
    key = cv2.waitKey(1)

    if key == ord("q"):
        # If 'q' is pressed, break out of the loop and exit the program
        break
    elif key == ord("r"):
        # If 'r' is pressed, toggle the recording status
        recording = not recording
        print(f"Recording: {recording}")

    if recording:
        # If recording is enabled, write the frame to the VideoWriter
        writter.write(frame)

# Release the VideoCapture and VideoWriter objects
c.release()
writter.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
