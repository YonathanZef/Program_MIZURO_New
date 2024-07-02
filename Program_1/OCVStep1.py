import cv2 as cv
import numpy as np
import time
#from kanan import kanan_laterall
from maju import maju_fwd

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

    # Inisialisasi koneksi serial dengan ESP32
    # esp32_serial = serial.Serial('COM4', 9600, timeout=0.1)  # Sesuaikan port dan baudrate

    time.sleep(1)

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
        lower_bound = np.array([5, 100, 100])  # Menentukan batas bawah warna oranye
        upper_bound = np.array([15, 255, 255])  # Menentukan batas atas warna oranye
        masking = cv.inRange(hsv, lower_bound, upper_bound)
        contours, _ = cv.findContours(masking, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv.contourArea(x), reverse=True)
        final = cv.bitwise_and(frame, frame, mask=masking)

        if len(contours) == 0:
            print("maju1")
           # kanan_laterall()
            maju_fwd()
            continue

        # Membuat bounding rectangle pada objek
        for contour in contours:
            area = cv.contourArea(contour)
            (x, y, w, h) = cv.boundingRect(contour)
            # Mengirim data X dan Y melalui komunikasi serial ke ESP32
            string = (x + w // 2)
            # Plot titik tengah pada objek
            cv.circle(frame, (x + w // 2, y + h // 2), 2, (0, 255, 0), 2)
            # Plot ROI
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Plot kotak di tengah layar
            cv.rectangle(frame, (640 // 2 - 30, 480 // 2 - 30),
                         (640 // 2 + 30, 480 // 2 + 30),
                         (0, 0, 255), 2)
            if area > 2000:  # Asumsikan objek dekat jika area kontur besar
                print("berhasil")
                return True  # Objek dekat, hentikan program
            else:
                print("maju")
                maju_fwd()

            break

        # Menampilkan di antarmuka
        cv.imshow("Seleksi_Warna(Masking):", final)
        cv.imshow("Frame", frame)

        key = cv.waitKey(1)

        if key == 27:
            break

    cap.release()
    cv.destroyAllWindows()

def main_stp1():
    if detect_object():
        print("Program dihentikan karena objek terdeteksi dekat")
        # Tidak ada pemanggilan ulang detect_object() karena kita ingin program berhenti

if __name__ == "__main__":
    main_stp1()
