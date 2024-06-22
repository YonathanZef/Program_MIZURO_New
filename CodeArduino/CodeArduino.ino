#include <ESP32Servo.h>

Servo servoMotor; // Inisialisasi objek servo

void setup() {
  Serial.begin(9600); // Inisialisasi komunikasi serial dengan kecepatan 9600 bps
  servoMotor.attach(18); // Hubungkan servo motor ke pin 9
}

void loop() {
  if (Serial.available() > 0) { // Periksa apakah data tersedia dari komunikasi serial
    String data = Serial.readStringUntil('\n'); // Baca data yang diterima hingga karakter newline (\n)

    // Pisahkan data posisi X dan Y
    int posX = data.substring(data.indexOf('X') + 1, data.indexOf('Y')).toInt();
    int posY = data.substring(data.indexOf('Y') + 1).toInt();

    // Lakukan sesuatu berdasarkan posisi objek
    moveServo(posX);
  }
}

// Fungsi untuk menggerakkan servo motor berdasarkan posisi X
void moveServo(int posX) {
  // Map posisi X dari rentang piksel layar (0-640) menjadi rentang sudut servo (0-180)
  int angle = map(posX, 0, 640, 0, 180);
  
  servoMotor.write(angle); // Gerakkan servo ke posisi yang dihitung
}
