# Brainfuck to C
This is a little python3 program that will interpret the Brainfuck language (www.en.wikipedia.org/wiki/Brainfuck) and also compile it to an executable format.

Usage goes as follows:
If you just want to interpret a program, use
./BFtoC.py inputprogram.bf -

If you just want to compile a program to C and then an executable format, use the following:
./BFtoC.py inputprogram.bf output.c

To interpret a program (to check for bugs) and then compile it if the program did not have a runtime or syntax error, use
./BFtoC.py inputprogram.bf outputprogram.c -

When compiling, Brainfuck to C will convert "inputprogram.bf" to C by using a simple dictionary lookup and a static header and footer.

It will write the converted file to "outputprogram.c", then call GCC on the file with an output flag of "outputprogram.out"

Protip: if ya just wanna type a brainfuck program into the interpreter, run "./BFtoC.py /dev/stdin -"  
