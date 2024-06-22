#include <Wire.h>
#include <Servo.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(11,10); // RX, TX 
// connect yellow wire to D10 and White wire to D11

unsigned char data[4]={};
float distance;
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

Servo myservo;
int servoPin = 3;

void setup()
{
  Serial.begin(115200);
  mySerial.begin(9600); 
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  delay(2000);
  myservo.attach(servoPin);
  display.clearDisplay();
  display.setTextColor(WHITE);
  delay(1000);
}

void loop()
{
    do{
     for(int i=0;i<4;i++)
     {
       data[i]=mySerial.read();
     }
  }while(mySerial.read()==0xff);

  mySerial.flush();

  if(data[0]==0xff)
    {
      int sum;
      sum=(data[0]+data[1]+data[2])&0x00FF;
      if(sum==data[3])
      {
        distance=(data[1]<<8)+data[2];
         distance=distance / 10;
  Serial.println(distance);
  display.clearDisplay();
  display.setCursor(10,0);  
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.print("Distance");
  display.setCursor(10,30);
  display.setTextSize(2);
  display.print(String(distance)+" cm");
  display.display();

  if(distance >= 20){
    myservo.write(90);
  }
      }
     }
     delay(100);
}