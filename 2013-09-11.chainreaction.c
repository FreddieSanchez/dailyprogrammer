#include <stdio.h>
#include <string.h>
#include <stdlib.h>
/*
Input Description
On standard console input, you will be given two space-delimited integers 
N and M, where N is the number of element types, and M is the grid size in 
both dimensions. N will range inclusively between 1 and 20, while M ranges 
inclusively from 2 to 10. This line will then be followed by N element definitions.

An element definition has several space-delimited integers and a string in the 
form of "X Y R D". X and Y is the location of the element. The grid's origin 
is the top-left, which is position (0,0), where X grows positive to the right 
and Y grows positive down. The next integer R is the radius, or number of 
tiles this element propagates outwardly from. As an example, if R is 1, then 
the element can only interact with directly-adjacent elements. The string D at 
the end of each line is the "propagation directions" string, which is formed 
from the set of characters 'u', 'd', 'l', 'r'. These represent up, down, left, 
right, respectively. As an example, if the string is "ud" then the element can 
only propagate R-number of tiles in the up/down directions. Note that this string
can have the characters in any order and should not be case-sensitive. This means
"ud" is the same as "du" and "DU".

Only the first element in the list is "activated" at first; all other elements 
are idle (i.e. do not propagate) until their positions have been activated by 
another element, thus causing a chain-reaction.

Sample Input
------------
4 5
0 0 5 udlr
4 0 5 ud
4 2 2 lr
2 3 3 udlr

*/

#define MAX_PROPIGATIONS 4
#define MAX_LINE_LEN 100
#define False 0
#define True 1
typedef enum direction {
  NONE = 0, UP ='u', DOWN = 'd', LEFT = 'l', RIGHT = 'r'
} Direction;

typedef struct point {
  int x;
  int y;
} Point;

typedef struct element {
  Point location;
  int radius;
  Direction propigation[MAX_PROPIGATIONS];
  int active;
} Element;

/* Macros */
#define CHAR_TO_DIRECTION(c) \
  ((c == 'u' || c == 'U')?UP:\
   (c == 'd' || c == 'D')?DOWN:\
     (c == 'l' || c == 'L')?LEFT:\
       (c == 'r' || c == 'r')?RIGHT:NONE)

int createElement(Element ** e, Point p, int radius, char * direction) {
  int i; 

  *e = (Element *)malloc(sizeof(Element));
  if (*e == NULL) return -1;
  

  (*e)->location = p;
  (*e)->radius = radius;
  
  for(i = 0; i < MAX_PROPIGATIONS; i++) {
    (*e)->propigation[i] = CHAR_TO_DIRECTION(direction[i]);
  }
  (*e)->active = False;
  return 1;
}

void printGrid(Element ** e, int N, int M) {
  int i,j,k;
  for (i = 0; i < M; i++) {
    for (j = 0; j < M; j++) {
      for (k = 0; k < N; k++) {
        if (e[k]->location.x == j && 
            e[k]->location.y == i) {
          printf ("%c",(e[k]->active)?'X':'A'+k);
          break;
        }
      }
      if (k == N) printf (".");
    }
    printf("\n");
  }
}
void inline activateElement(Element * e) {
  e->active = True;
}
int areNeighbors(Element * e1, Element * e2) {
  int i;
  if (e2->active || e1 == e2) return False; /* saying that active Elements are not neighbors */
  
  for (i = 0; i<MAX_PROPIGATIONS; i++) {
    switch(e1->propigation[i]) {
    case NONE: /* do nothing */
      break;
    case UP:
      {
        /* if they are on the same col, 
           and e1 is below e2, and e1's activation radius
           spans the distance between e1 and e2  */
        if (e1->location.x == e2->location.x &&
            e1->location.y < e2->location.y &&
            e1->radius >= (e1->location.y - e2->location.y)) {
          return True;
        }
      } break;
    case DOWN:
      { 
        /* if they are on the same col, 
           and e1 is above e2, and e1's activation radius
           spans the distance between e1 and e2  */
        if (e1->location.x == e2->location.x &&
            e1->location.y > e2->location.y &&
            e1->radius >= (e1->location.y - e2->location.y)) {
          return True;
        }
      }break;
    case LEFT:
      {
        /* if they are on the same row, 
           and e1 is to the right of e2, and e1's activation radius
           spans the distance between e1 and e2  */
        if (e1->location.y == e2->location.y &&
            e1->location.x > e2->location.x &&
            e1->radius >= (e1->location.x - e2->location.x)) {
          return True;
        }
      }break;
    case RIGHT:
      {

        /* if they are on the same row, 
           and e1 is to the left of e2, and e1's activation radius
           spans the distance between e1 and e2  */
        if (e1->location.y == e2->location.y &&
            e1->location.x < e2->location.x &&
            e1->radius >= (e1->location.x - e2->location.x)) {
          return True;
        }
      }break;
    }
  }
  return False;

}
int activateNeighbors(Element ** elements, Element *e, int N, int M, int step) {
  int i = 0,j = 0, k= 0, curCntActivated = 0, prevCntActivated = 0;
  Element ** prevActivated;
  Element ** curActivated;
  Element ** temp;


  prevActivated = (Element *)malloc(sizeof(Element *) * N);
  curActivated = (Element *)malloc(sizeof(Element *) * N);
  printf("Step %d\n",step++);
  printGrid(elements,N,M);
  prevActivated[prevCntActivated++] = e;
  activateElement(e);
  sleep(1);
  system("cls");
  while (prevCntActivated) {
    printf("Step %d prev: %d\n",step++,prevCntActivated);

    printGrid(elements,N,M);
    sleep(1);
    system("clear");
    for (i = 0; i < prevCntActivated; i++) {
      for (k = 0; k < N; k++) {
        if (areNeighbors(prevActivated[i],elements[k])) {

          activateElement(elements[k]);
          curActivated[curCntActivated++] = elements[k];
        }
      }
    }
    /* switch the buffers */
    temp = prevActivated;
    prevActivated = curActivated;
    curActivated = temp;

    prevCntActivated = curCntActivated;
    curCntActivated = 0;


  }
  free(prevActivated);
  free(curActivated);
  return i;
}
int simulation(Element ** elements, int N, int M ) {
  activateNeighbors(elements,elements[0], N,M,0);
}
void printElement(Element * e) {
  int i = 0;
  printf ("Element @ (%d,%d)\n",e->location.x,e->location.y);
  printf ("radius: %d\n",e->radius);
  printf ("Direction:");
  for (;i< MAX_PROPIGATIONS; i++) 
    if (e->propigation[i] != NONE)
      printf("%c",e->propigation[i]);
  printf("\n");
}
int main(int argsc, char ** args) {
  int N, M, r, i,j;
  char line[MAX_LINE_LEN];
  Point p;
  char * tok;
  Element ** elements;

  /* read in the first line */
  if(!fgets(line,MAX_LINE_LEN,stdin)) return -1;
  tok = strtok(line," ");
  N = atoi(tok);
  tok = strtok(NULL," ");
  M = atoi(tok);
  
  /* make a list of M pointers to the ELements */
  elements = malloc(sizeof(Element *) * N);

  /* read the element informationand create the elements */
  for (i = 0; i < N; i++) {
    if(!fgets(line,MAX_LINE_LEN,stdin)) return -1;
    p.x = atoi(tok = strtok(line, " "));
    p.y = atoi(tok = strtok(NULL," "));
    r = atoi(tok = strtok(NULL," ")); 
    tok = strtok(NULL, " ");
    createElement(&elements[i],p,r,tok);
  }
  
  simulation(elements,N,M); 

  for (i = 0; i<N; i++)
    free(elements[i]);
  free(elements);
}
