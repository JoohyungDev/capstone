// Include the Arduino Stepper Library
#include <Stepper.h>
int incomingByte;       // a variable to read incoming serial data into

// Number of steps per output rotation
const int stepsPerRevolution = 200 ; // 디스크가 끝에 있을떄 반대 끝편 까지가는 축의 회전 (4.4바퀴를 돌아야 끝점까지 이동) 

// Create Instance of Stepper library
Stepper myStepper(stepsPerRevolution, 4, 5, 6, 7);
// Stepper myStepper_2()

void setup()
{
	// set the speed at 60 rpm:
	myStepper.setSpeed(400);
	// initialize the serial port:
	Serial.begin(9600);
}

void loop() 
{
  incomingByte=Serial.read();

  if (incomingByte == '2') {
	Serial.println("clockwise");
	myStepper.step(stepsPerRevolution*4.4);
	delay(50);
	Serial.println("counterclockwise");
	myStepper.step(-stepsPerRevolution*4.4);
	delay(50);

  }

  // if(incomingByte=='2'){
  // myStepper.setSpeed(0);
  //   }

  //   else if(incomingByte=='3'){
	// Serial.println("clockwise");
	// myStepper.step(stepsPerRevolution);
	// delay(50);
	// Serial.println("counterclockwise");
	// myStepper.step(-stepsPerRevolution);
	// delay(50);
  // myStepper.setSpeed(0);
  //   }
  
}
