#include <Arduino.h>
#include <Servo.h>

Servo thumb;
Servo index;
Servo middle;
Servo ring;
Servo little;
Servo wrist;

String fingers;

char Cfingers[12];

char *f1,*f2,*f3,*f4,*f5,*f6;

int i1,i2,i3,i4,i5,i6;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(5);

  thumb.attach(3);
  index.attach(5);
  middle.attach(6);
  ring.attach(9);
  little.attach(10);
  wrist.attach(11);
}

void loop() {
  //wrist.write(90);
  if (Serial.available()){
    fingers=Serial.readString();
    
    fingers.toCharArray(Cfingers,12);

    f1=strtok(Cfingers,"#");
    f2=strtok(NULL,"#");
    f3=strtok(NULL,"#");
    f4=strtok(NULL,"#");
    f5=strtok(NULL,"#");
    f6=strtok(NULL,"#");

    i1=atoi(f1);
    i2=atoi(f2);
    i3=atoi(f3);
    i4=atoi(f4);
    i5=atoi(f5);
    i6=atoi(f6);

    if (i1) {
      thumb.write(150);
    } else {
      thumb.write(0);
    }

    if (i2) {
      index.write(70);
    } else {
      index.write(180);
    }

    
    if (i3) {
      middle.write(130);
    } else {
      middle.write(0);
    }

    if (i4) {
      ring.write(100); 
    } else {
      ring.write(0);
    }

     if (i5) {
      little.write(130); 
    } else {
      little.write(0);
    }

    if (i6==2) {
      wrist.write(180);
    } else if (i6==1) {
      wrist.write(90);
    } else if (i6==0) {
      wrist.write(0);
    }

  }
  fingers="";
}
