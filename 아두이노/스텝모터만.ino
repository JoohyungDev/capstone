// MultiStepper.pde
// -*- mode: C++ -*-
// Use MultiStepper class to manage multiple steppers and make them all move to
// the same position at the same time for linear 2d (or 3d) motion.
 
#include <AccelStepper.h>
#include <MultiStepper.h>
 
// EG X-Y position bed driven by 2 steppers
// Alas its not possible to build an array of these with different pins for each :-(
AccelStepper stepper1(AccelStepper::FULL4WIRE, 4, 5, 6,7);
AccelStepper stepper2(AccelStepper::FULL4WIRE, 10, 11, 12, 13);
 
// Up to 10 steppers can be handled as a group by MultiStepper
MultiStepper steppers;
 
void setup() {
  Serial.begin(9600);
 
  // Configure each stepper
  stepper1.setMaxSpeed(1000);
  stepper2.setMaxSpeed(1000);
  stepper1.setSpeed(800);
  stepper2.setSpeed(800);
 
  // Then give them to MultiStepper to manage
  steppers.addStepper(stepper1);
  steppers.addStepper(stepper2);
}
 
void loop() {
  long positions[2]; // Array of desired stepper positions
 
  positions[0] = 1270;  // 최적의 파라미터를 찾았다!
  positions[1] = -1270;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  delay(1000);
 
  // Move to a different coordinate
  positions[0] = -1350; //
  positions[1] = 1350;
  steppers.moveTo(positions);
  steppers.runSpeedToPosition(); // Blocks until all are in position
  delay(1000);
}