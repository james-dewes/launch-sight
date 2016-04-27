/*
 * created by Rui Santos, http://randomnerdtutorials.wordpress.com
 * Control DC motor with Smartphone via bluetooth
 * 2013
 *
 * Launch Sight used this file as a small part of a larger VR Rocket Launch project. We did not write this file
 * ourselves and give full credit to the original author.
 * 
 * http://www.instructables.com/id/Arduino-Control-DC-Motor-via-Bluetooth/?ALLSTEPS 
 *
 *
  */
int motorPin1 = 3; // pin 2 on L293D IC
int motorPin2 = 4; // pin 7 on L293D IC
int enablePin = 5; // pin 1 on L293D IC
int state;
int flag=0;        //makes sure that the serial only prints once the state

void setup() {
    // sets the pins as outputs:
    pinMode(motorPin1, OUTPUT);
    pinMode(motorPin2, OUTPUT);
    pinMode(enablePin, OUTPUT);
    // sets enablePin high so that motor can turn on:
    digitalWrite(enablePin, HIGH);
    // initialize serial communication at 9600 bits per second:
    Serial.begin(9600);
}

void loop() {
    //if some date is sent, reads it and saves in state
    if(Serial.available() > 0){     
      state = Serial.read();   
      flag=0;
    }   
    // if the state is '0' the DC motor will turn off
    if (state == '0') {
        digitalWrite(motorPin1, LOW); // set pin 2 on L293D low
        digitalWrite(motorPin2, LOW); // set pin 7 on L293D low
        if(flag == 0){
          Serial.println("Motor: off");
          flag=1;
        }
    }
    // if the state is '1' the motor will turn right
    else if (state == '1') {
        digitalWrite(motorPin1, LOW); // set pin 2 on L293D low
        digitalWrite(motorPin2, HIGH); // set pin 7 on L293D high
        if(flag == 0){
          Serial.println("Motor: right");
          flag=1;
        }
    }
    // if the state is '2' the motor will turn left
    else if (state == '2') {
        digitalWrite(motorPin1, HIGH); // set pin 2 on L293D high
        digitalWrite(motorPin2, LOW); // set pin 7 on L293D low
        if(flag == 0){
          Serial.println("Motor: left");
          flag=1;
        }
    }
}
