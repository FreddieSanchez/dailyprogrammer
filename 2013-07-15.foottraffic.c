/* Reddit 2013-07-15 Dailyprogrammer Problem
**
** Input Description
**
** You will be first given an integer N which represents the following N-number of 
** lines of text. Each line represents either a visitor entering or leaving a room:
** it starts with an integer, representing a visitor's unique identifier. Next on 
** this line is another integer, representing the room index. Note that there are 
** at most 100 rooms, starting at index 0, and at most 1,024 visitors, starting at 
** index 0. Next is a single character, either 'I' (for "In") for this visitor 
** entering the room, or 'O' (for "out") for the visitor leaving the room. Finally,
** at the end of this line, there is a time-stamp integer: it is an integer 
** representing the minute the event occurred during the day. This integer will 
** range from 0 to 1439 (inclusive). All of these elements are space-delimited.
** 
** You may assume that all input is logically well-formed: for each person entering
** a room, he or she will always leave it at some point in the future. A visitor 
** will only be in one room at a time.
** 
** Note that the order of events in the log are not sorted in any way; it shouldn't 
** matter, as you can solve this problem without sorting given data. Your output 
** (see details below) must be sorted by room index, ascending.
** 
** Sample Input 1
** 4
** 0 0 I 540
** 1 0 I 540
** 0 0 O 560
** 1 0 O 560
*/

#include <stdio.h>

void readinput();
void printoutput();

#define MAX_ROOMS    100
#define MAX_VISITORS 1024
#define IN 'I'
#define OUT 'O'

struct room {
  char timeinroom[MAX_VISITORS];
};

struct room ROOMS[MAX_ROOMS] = {0};

void readinput() 
{
  int lines,visitorid,roomid,timestamp,linesread = 0;
  char direction;

  scanf("%d",&lines);
  while (linesread < lines) 
  {
    scanf("%d %d %c %d",&visitorid,&roomid,&direction,&timestamp);
    // printf("Line Read: %d %d %c %d\n",visitorid,roomid,direction,timestamp); 
    if (direction == IN) {
      ROOMS[roomid].timeinroom[visitorid] += timestamp;
    } else if (direction == OUT) {
      ROOMS[roomid].timeinroom[visitorid] -= timestamp;
    }
    linesread++;
  }
}

void printoutput()
{
  int room,visitor;
  int sum, visitors;

  for (room = 0; room < MAX_ROOMS; room++) {
    visitors = sum = 0;
    for (visitor = 0; visitor < MAX_VISITORS; visitor++) {
     if (ROOMS[room].timeinroom[visitor] == 0 ) {
       continue;
     }
     sum += ROOMS[room].timeinroom[visitor];
     visitors++;
    }
    if (visitors != 0) {
      printf("Room %d, %d minute average visit, %d visitor%stotal\n",
             room,-sum / visitors, visitors,(visitors > 1)?"s ": " ");
    }
  }
}
main()
{
  readinput();
  printoutput();

}
