import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # '0' is the index of the camera; use appropriate index if you have multiple cameras

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Write the frame to the video file
        out.write(frame)

        # Display the resulting frame (optional)
        cv2.imshow('frame', frame)

        # Press 'q' on the keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything when job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
