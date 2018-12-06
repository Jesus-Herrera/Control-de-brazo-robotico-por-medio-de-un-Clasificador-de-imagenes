#define LED 13
#include <Servo.h>
Servo myservo; 
int x = 0;


void setup() {
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
    myservo.attach(9);

    
}

void loop() {
    if (Serial.available()) {
        char serialListener = Serial.read();
        if (serialListener == 'A') {
            digitalWrite(LED, HIGH);
            myservo.write(135);
            delay(2000);
            myservo.write(5);
            delay(2000);
            myservo.write(135);
            delay(2000);
            myservo.write(5);
        }
        else if (serialListener == 'B') {
            digitalWrite(LED, LOW);
            myservo.write(80);
            delay(100);
            myservo.write(120); 
            delay(100);
            myservo.write(80);
            delay(100);
            myservo.write(120); 
        }

         else if (serialListener == 'C') {
            digitalWrite(LED, LOW);
            myservo.write(5);
            delay(500);
            myservo.write(135); 
            delay(500);
            myservo.write(5);
            delay(500);
            myservo.write(135); 
            delay(500);
            myservo.write(5);
            delay(500);
            myservo.write(135); 
            delay(500);
            myservo.write(5);
            delay(500);
            myservo.write(135); 
            delay(500);
            myservo.write(5);
            delay(500);
            myservo.write(135); 
        }

        
    }
}
