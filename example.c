#include <stdio.h>
#include <stdlib.h>
#define TAPESIZE 4096
/*Object file generated by the BFtoC compiler*/

int main(void) {
char * tape=malloc(sizeof(char)*TAPESIZE);
char * pointer=tape;

++*pointer;
++*pointer;
++*pointer;
++*pointer;
++*pointer;
++*pointer;
++*pointer;
++*pointer;
while (*pointer) {
++pointer;
++*pointer;
++*pointer;
++*pointer;
++*pointer;
while (*pointer) {
++pointer;
++*pointer;
++*pointer;
++pointer;
++*pointer;
++*pointer;
++*pointer;
++pointer;
++*pointer;
++*pointer;
++*pointer;
++pointer;
++*pointer;
--pointer;
--pointer;
--pointer;
--pointer;
--*pointer;
}++pointer;
++*pointer;
++pointer;
++*pointer;
++pointer;
--*pointer;
++pointer;
++pointer;
++*pointer;
while (*pointer) {
--pointer;
}--pointer;
--*pointer;
}++pointer;
++pointer;
putchar(*pointer);
++pointer;
--*pointer;
--*pointer;
--*pointer;
putchar(*pointer);
++*pointer;
++*pointer;
++*pointer;
++*pointer;
++*pointer;
++*pointer;
++*pointer;
putchar(*pointer);
putchar(*pointer);
++*pointer;
++*pointer;
++*pointer;
putchar(*pointer);
++pointer;
++pointer;
putchar(*pointer);
--pointer;
--*pointer;
putchar(*pointer);
--pointer;
putchar(*pointer);
++*pointer;
++*pointer;
++*pointer;
putchar(*pointer);
--*pointer;
--*pointer;
--*pointer;
--*pointer;
--*pointer;
--*pointer;
putchar(*pointer);
--*pointer;
--*pointer;
--*pointer;
--*pointer;
--*pointer;
--*pointer;
--*pointer;
--*pointer;
putchar(*pointer);
++pointer;
++pointer;
++*pointer;
putchar(*pointer);
++pointer;
++*pointer;
++*pointer;
putchar(*pointer);
free(tape);
return 0;
}
