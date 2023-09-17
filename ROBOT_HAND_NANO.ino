#include <Arduino.h>

String fingers;

char Cfingers[12];

char *f1,*f2,*f3,*f4,*f5,*f6;

int i1,i2,i3,i4,i5,i6;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(2);

  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
}

void loop() {
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

    digitalWrite(2,i1);
    digitalWrite(3,i2);
    digitalWrite(4,i3);
    digitalWrite(5,i4);
    digitalWrite(7,i5);

    if (i6==2) {
      analogWrite(6,1023);
    } else if (i6==1) {
      analogWrite(6,800);
    } else if (i6==0) {
      analogWrite(6,0);
    }

  }
  fingers="";
}
