#include<stdio.h>
#include<time.h>
#include<string.h>
int timerlowerbound=1;
int timerupperbound;
time_t currenttime;
int messagelength;
char sorc;
int nsuccesses=0;
int ncollisions=0;
int messagesent = 1;
int waittime;
const char *NATOBet[26] = {"ALPHA","BRAVO", "CHARLIE", "DELTA", "ECHO", "FOXTROT",
                           "GOLF", "HOTEL", "INDIA", "JULIETT", "KILO", "LIMA",
                           "MIKE", "NOVEMBER", "OSCAR", "PAPA", "QUEBEC", "ROMEO",
                         "SIERRA", "TANGO", "UNIFORM", "VICTOR", "WHISKEY", "X-RAY",
                         "YANKEE", "ZULU"};

int main(){
//Test to print the NATO alphabet
for(int i=0;i<26;i++){
  printf("%s \n",NATOBet[i]);
}
printf("\n\n\n\n\n");
//Simple introduction and instructions
printf("When prompted about whether you have had a success or collision, \n");
printf("enter 's' for a success or 'c' for a collision.\n");
srand(time(NULL));
timerlowerbound = 1;
printf("What is the timer's upper bound? Please enter an integer number of seconds greater than 1.   ");
scanf("%d", &timerupperbound);

printf("Please enter the message length as an integer: ");
scanf("%d", &messagelength);

currenttime = time(NULL);
printf("\n\n\n\n\n");
printf("Begin!\n\n\n");



//Infinite loop - generate wait time, wait until expiry, print message.
//Repeat ad infinitum.

while(1){

  if(messagesent == 1){ //If we sent our message, we need a new one
    waittime = rand()%timerupperbound + 1; //Generate a random time between 1 and timerupperbound
    printf("Wait time is: %d \n", waittime); //Just to see
    messagesent=0; //clear message sent flag
  }


  if(time(NULL) >= currenttime+waittime){

    for(int i=0;i<messagelength;i++){ //Print the message
          printf("%s   ", NATOBet[rand()%26]);
          messagesent=1; //We've sent our message and need a new one.
    }

    printf("\n Success or collision?   "); //What's it gonna be?
    scanf(" %c",&sorc);

    switch(sorc){ //Switch on input

      case 'c': //Collision
      ncollisions++;
      break;

      case 's': //Success
      nsuccesses++;
      break;

      default: //Catch case
      printf("Invalid input! \n");
      fflush(stdin);
      break;

    }

    printf("You have had %d successes and %d collisions",nsuccesses,ncollisions); //Display total

    printf("\n\n");
    currenttime = time(NULL);

  }
}

  printf("END");
  return 0;
}
