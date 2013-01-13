#include "SevSeg.h"

//Create an instance of the object.
SevSeg disp;

void setup()
{

  int displayType = COMMON_CATHODE; //Your display is either common cathode or common anode


/*
//This pinout is for a regular display
//Declare what pins are connected to the digits
int digit1 = 2; //Pin 12 on my 4 digit display
int digit2 = 3; //Pin 9 on my 4 digit display
int digit3 = 4; //Pin 8 on my 4 digit display
int digit4 = 5; //Pin 6 on my 4 digit display
//Declare what pins are connected to the segments
int segA = 6; //Pin 11 on my 4 digit display
int segB = 7; //Pin 7 on my 4 digit display
int segC = 8; //Pin 4 on my 4 digit display
int segD = 9; //Pin 2 on my 4 digit display
int segE = 10; //Pin 1 on my 4 digit display
int segF = 11; //Pin 10 on my 4 digit display
int segG = 12; //Pin 5 on my 4 digit display
int segDP= 13; //Pin 3 on my 4 digit display
*/

  //This pinout is for OpenSegment PCB layout
  //Declare what pins are connected to the digits
  int digit1 = 9; //Pin 12 on my 4 digit display
  int digit2 = 16; //Pin 9 on my 4 digit display
  int digit3 = 17; //Pin 8 on my 4 digit display
  int digit4 = 3; //Pin 6 on my 4 digit display

  //Declare what pins are connected to the segments
  int segA = 14; //Pin 11 on my 4 digit display
  int segB = 2; //Pin 7 on my 4 digit display
  int segC = 8; //Pin 4 on my 4 digit display
  int segD = 6; //Pin 2 on my 4 digit display
  int segE = 7; //Pin 1 on my 4 digit display
  int segF = 15; //Pin 10 on my 4 digit display
  int segG = 4; //Pin 5 on my 4 digit display
  int segDP= 5; //Pin 3 on my 4 digit display

  int numberOfDigits = 4; //Do you have a 1, 2 or 4 digit display?

  disp.Begin(displayType, numberOfDigits, digit1, digit2, digit3, digit4, segA, segB, segC, segD, segE, segF, segG, segDP);

  disp.SetBrightness(100); //Set the display to 100% brightness level

}

void loop()
{
  //Example ways of displaying a decimal number
  //char tempString[10]; //Used for sprintf
  //sprintf(tempString, "%4d", deciSecond); //Convert deciSecond into a string that is right adjusted
  //sprintf(tempString, "%d", deciSecond); //Convert deciSecond into a string that is left adjusted
  //sprintf(tempString, "%04d", deciSecond); //Convert deciSecond into a string with leading zeros
  //sprintf(tempString, "%4d", deciSecond * -1); //Shows a negative sign infront of right adjusted number
  //sprintf(tempString, "%4X", deciSecond); //Count in HEX, right adjusted

  //Produce an output on the display
  //myDisplay.DisplayString(tempString, 3); //(numberToDisplay, decimal point location)

  //Other examples
  //myDisplay.DisplayString(tempString, 0); //Display string, no decimal point
  //disp.DisplayString("-23b", 3); //Display string, decimal point in third position

    //snippet;

}
