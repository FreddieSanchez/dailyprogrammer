#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void genevent(int * room, int * timein, int * timeout, int timestart, int timeend);


int main(int argc, const char * argv[])
{
  int event,visitor;
  int numEvents,numVisitors,numRooms,timeStart,timeEnd = 0;
  int enter, duration, room = 0;
  struct room {
    int room;
    int enter;
    int duration;
  };
  struct room * rooms;
  struct room * r;

  srand(time(NULL)); /* seed the random number generator */

  scanf("%d %d %d %d %d", &numEvents,&numVisitors,
                          &numRooms,&timeStart,&timeEnd);
  printf("%d\n",numEvents * 2);
  numVisitors += 1;
  rooms = (struct room *)malloc(numVisitors  * sizeof (struct room));
  for (event = 0; event < numEvents/numVisitors; event++) {
    r = rooms;
    for (visitor = 0; visitor < numVisitors; visitor++) {
      enter = rand() % (timeEnd - timeStart) + timeStart;
      duration = rand() % (timeEnd - enter);
      room = rand() % (numRooms);

      r->room = room;
      r->duration = duration;
      r->enter = enter;

      printf ("%d %d I %d\n",visitor,room,enter);
      r++;
    }
    r = rooms;
    for(visitor = 0; visitor < numVisitors; visitor++) {
      printf ("%d %d O %d\n\0",visitor,r->room,r->enter + r->duration);
      r++;
    }
  }
  free(rooms);

}
