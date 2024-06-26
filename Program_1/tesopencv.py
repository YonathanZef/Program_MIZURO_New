import cv2 as cv
import numpy as np
import serial
import time
from kanan import kanan_laterall

def detect_object():
    Winname_mask = 'Seleksi_Warna(Masking):'

    def nothing(x):
        pass

    cv.namedWindow('Seleksi_Warna(Masking):')
    # Variable UI
    cv.createTrackbar('H', Winname_mask, 0, 255, nothing)
    cv.createTrackbar('S', Winname_mask, 0, 255, nothing)
    cv.createTrackbar('V', Winname_mask, 0, 255, nothing)
    cv.createTrackbar('H2', Winname_mask, 0, 255, nothing)
    cv.createTrackbar('S2', Winname_mask, 0, 255, nothing)
    cv.createTrackbar('V2', Winname_mask, 0, 255, nothing)

    cap = cv.VideoCapture(0)

    while True:
        _, frame = cap.read()
        frame = cv.flip(frame, 1)  # Mirror gambar

        H = cv.getTrackbarPos('H', 'Seleksi_Warna(Masking):')
        S = cv.getTrackbarPos('S', 'Seleksi_Warna(Masking):')
        V = cv.getTrackbarPos('V', 'Seleksi_Warna(Masking):')
        H2 = cv.getTrackbarPos('H2', 'Seleksi_Warna(Masking):')
        S2 = cv.getTrackbarPos('S2', 'Seleksi_Warna(Masking):')
        V2 = cv.getTrackbarPos('V2', 'Seleksi_Warna(Masking):')

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_bound = np.array([0, 166, 117])  # Menentukan batas bawah
        upper_bound = np.array([40, 255, 255])  # Menentukan batas atas
        masking = cv.inRange(hsv, lower_bound, upper_bound)
        contours, _ = cv.findContours(masking, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv.contourArea(x), reverse=True)
        final = cv.bitwise_and(frame, frame, mask=masking)

        if len(contours) == 0:
            print("None")
            kanan_laterall()

        # Membuat bounding rectangle pada objek
        for contour in contours:
            (x, y, w, h) = cv.boundingRect(contour)
            string = ((x + w // 2))
            cv.circle(frame, (x + w // 2, y + h // 2), 2, (0, 255, 0), 2)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.rectangle(frame, (640 // 2 - 30, 480 // 2 - 30),
                         (640 // 2 + 30, 480 // 2 + 30),
                         (0, 0, 255), 2)
           # kanan_laterall()
            if string > 350:
                print("Kurang kiri")
            elif string < 290:
                print("Kurang kanan")
            else:
                print("Tengah")
                return True

            break

        cv.imshow("Seleksi_Warna(Masking):", final)
        cv.imshow("Frame", frame)

        key = cv.waitKey(1)

        if key == 27:
            break

    cap.release()
    cv.destroyAllWindows()

def main():
    if detect_object():
        print("Berhasil")
        time.sleep(2)
        detect_object()

if __name__ == "__main__":
    main()
