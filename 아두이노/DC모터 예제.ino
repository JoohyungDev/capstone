void forward_next(int speed)
{
  analogWrite(5,speed);
  digitalWrite(2,LOW);
  digitalWrite(3,HIGH);
  delay(380);
}
void stop(){
  digitalWrite(2,LOW);
  digitalWrite(3,LOW);
  delay(4000);
}
long cur_times=0;

void setup(){
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
}
void loop(){
  cur_times=millis();
  if(cur_times % 500==0)
  {
    Serial.print(cur_times);
    forward_next(250);
    stop();
  }
}