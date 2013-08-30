#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_INSTRUCTIONS 37

typedef enum bool {
  FALSE,
  TRUE
} Bool;

typedef enum argument{
  NONE,
  ADDRESS,
  LITERAL
} Argument ;

typedef struct instruction{
  char * name;
  Argument * args;
  int opcode;
} Instruction;

 Argument aan[] = {ADDRESS,ADDRESS,NONE};
 Argument ann[] = {ADDRESS,NONE,NONE};
 Argument lnn[] = {LITERAL,NONE,NONE};
 Argument lan[] = {LITERAL,ADDRESS,NONE};
 Argument laa[] = {LITERAL,ADDRESS,ADDRESS};
 Argument lal[] = {LITERAL,ADDRESS,LITERAL};
 Argument lln[] = {LITERAL,LITERAL,NONE};
 Argument aln[] = {ADDRESS,LITERAL,NONE};
 Argument aaa[] = {ADDRESS,ADDRESS,ADDRESS};
 Argument ala[] = {ADDRESS,LITERAL,ADDRESS};
 Argument aal[] = {ADDRESS,ADDRESS,LITERAL};
 Argument nnn[] = {NONE,NONE,NONE};


Instruction instructions[] = {
  {"AND", aan, 0x00},
  {"AND", aln, 0x01},
  {"OR",  aan, 0x02},
  {"OR",  aln, 0x03},
  {"XOR", aan, 0x04},
  {"XOR", aln, 0x05},
  {"NOT", ann, 0x06},
  {"MOV", aan, 0x07},
  {"MOV", aln, 0x08},
  {"RANDOM",aan,0x09},
  {"ADD",aan, 0x0a},
  {"ADD",aln, 0x0b},
  {"SUB",aan, 0x0c},
  {"SUB",aln, 0x0d},
  {"JMP",ann, 0x0e},
  {"JMP",lnn, 0x0f},
  {"JZ", aan, 0x10},
  {"JZ", aln, 0x11},
  {"JZ", lan, 0x12},
  {"JZ", lln, 0x13},
  {"JEQ",aaa, 0x14},
  {"JEQ",laa, 0x15},
  {"JEQ",aal, 0x16},
  {"JEQ",lal, 0x17},
  {"JLS",aaa,0x18},
  {"JLS",laa,0x19},
  {"JLS",aal,0x1a},
  {"JLS",lal, 0x1b},
  {"JGT",aaa,0x1c},
  {"JGT",laa,0x1d},
  {"JGT",aal,0x1e},
  {"JGT",lal,0x1c},
  {"HALT",nnn,0xff},
  {"APRINT",ann,0x20},
  {"APRINT",lnn,0x21},
  {"DPRINT",ann,0x22},
  {"DPRINT",lnn,0x23},
  {NULL,nnn,0xff}
};

void error(int linenum) {
  printf("!! ERROR line: %d!!\n",linenum);
  exit(-1);
}

void print(int index, int args[3], int numargs) {
  int i;
  printf("0x%02X ",instructions[index].opcode);
  for (i = 0; i<numargs; i++) {
    printf("0x%02X ",args[i]);
  }
  printf("\n");
}

/* function that takes a string and converts all a-z characters to
   uppercase.
*/
void strtoupper(char * str) {
  while(*str) {
    *str = (*str >= 'a' && *str <= 'z')? (*str - 'a') + 'A' : *str;
    str++;
  }
}
int match(int linenum, char * line) {
  int i,j, numparm = 0;
  char * cmd;
  char * op;
  Argument param[3] = {NONE,NONE,NONE};
  int args[3] = {0,0,0};
  strtoupper(line);
  
  cmd = strtok(line, " ");

  /* determine which parameters are addresses vs literals */
  while( op = strtok(NULL," ")) {
    if (op[0] == '[') {
      param[numparm] = ADDRESS;
      op++;
      op[strlen(op)-1] = '\0';
    } else {
      param[numparm] = LITERAL;
    }
    args[numparm++] = atoi(op);
  }
  
  /* loop through all instructions and compare the operation */
  for (i = 0; i < MAX_INSTRUCTIONS; i++) {
    if (strcmp(instructions[i].name,cmd) != 0) continue;

    for (j = 0; j < 3; j++) { /* when we found a match, see if it has the 
                                 correct arguments. Break when we've found
                                 one that doesn't match. Proceed to next 
                                 instruction.
                              */
      if (param[j] != instructions[i].args[j]) {
        break;
      }
    }
    if (j == 3)  /* we matched each parameter type. */
      break;
  }
  if (i == MAX_INSTRUCTIONS) {
    error(linenum);
  }
  print(i,args,numparm);
  return i;
}

int main(int argc, char ** argsv) {

  FILE * fp = fopen(argsv[1],"r");
  int maxline = 256;
  char line[maxline];
  int linenum = 0;
  while (fgets(line, maxline-1, fp)) {
    line[strlen(line)-1] = '\0'; /* take out the /n */
    match(linenum++,line);
  }
  fclose(fp);
  return 0;
}
