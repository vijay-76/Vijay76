
#include <LiquidCrystal.h>
#define trigPin1 6
#define trigPin2 7
#define trigPin3 8
#define echoPin1 6
#define echoPin2 7
#define echoPin3 8
#define led1 9
#define led2 10
#define led3 13
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

bool bool1=false;
bool bool2=false;
bool bool3=false;

  long readUltrasonicDistance(int triggerPin, int echoPin){
    pinMode(triggerPin, OUTPUT);  
    digitalWrite(triggerPin, LOW);
    delayMicroseconds(2);
    digitalWrite(triggerPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(triggerPin, LOW);
    pinMode(echoPin, INPUT);
    return pulseIn(echoPin, HIGH);
  }

void setup() {
  Serial.begin (9600);
  pinMode(trigPin1, OUTPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(echoPin2, INPUT);
  pinMode(echoPin3, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  lcd.begin(16,2);

}
void loop() {
  float distance1;
  float distance2;
  float distance3;
  lcd.setCursor(0,0);

   distance1 = (readUltrasonicDistance(6, 6) * 0.034)/2;
   Serial.println(distance1);
   if (distance1 >=320|| distance1 <= 2){
    digitalWrite(led1, HIGH);
     bool1=false;
  }
  else {
    digitalWrite(led1, LOW);
    bool1=true;
  }
    distance2 = (readUltrasonicDistance(7, 7) * 0.034)/2;
   if (distance2 >=320 || distance2 <= 2){
    digitalWrite(led2, HIGH);
     bool2=false;
  }
  else {
    digitalWrite(led2, LOW);
    bool2=true;
  }
    distance3 = (readUltrasonicDistance(8, 8) * 0.034)/2;
   if (distance3 >=320 || distance3 <= 2){
    digitalWrite(led3, HIGH);
     bool3=false;
  }
  else {
    digitalWrite(led3, LOW);
    bool3=true;
  }
  lcd.clear();

  if(!bool1&&!bool2&&!bool3)
  {
    lcd.setCursor(0, 0);
    lcd.print("All slots empty");
    lcd.clear();
  }
  else if(bool1&&!bool2&&!bool3)
  {
        lcd.setCursor(0, 0);
    lcd.print("1 Slot filled");
    lcd.setCursor(0,1);
    lcd.print("Slot 2 3 empty");
  }
  else if(!bool1&&bool2&&!bool3)
  {
        lcd.setCursor(0, 0);
    lcd.print("1 Slot filled");
    lcd.setCursor(0,1);
    lcd.print("Slot 1 3 empty");
  }
  else if(bool1&&bool2&&!bool3)
  {
        lcd.setCursor(0, 0);
    lcd.print("2 Slot filled");
    lcd.setCursor(0,1);
    lcd.print("Slot 3 empty");
  }
  else if(!bool1&&!bool2&&bool3)
  {
        lcd.setCursor(0, 0);
    lcd.print("1 Slot filled");
    lcd.setCursor(0,1);
    lcd.print("Slot 1 2 empty");
  }
  else if(bool1&&!bool2&&bool3)
  {
        lcd.setCursor(0, 0);
    lcd.print("2 Slot filled");
    lcd.setCursor(0,1);
    lcd.print("Slot 2 empty");
  }
  else if(!bool1&&bool2&&bool3)
  {
        lcd.setCursor(0, 0);
    lcd.print("2 Slot filled");
    lcd.setCursor(0,1);
    lcd.print("Slot 1 empty");
  }
  else
  {
    lcd.setCursor(0, 0);
    lcd.print("All Slots filled");
  }
  delay(500);

lcd.clear();

}
