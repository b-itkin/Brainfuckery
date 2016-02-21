#!/usr/bin/python3
##########################
#Author: Brady Itkin
#Created: 2/19/15
#Last modified: 2/19/15
#Program: Simple Brainfuck Compiler
#Description: Compiles a brainfuck program from sys.argv[1] to C, and optionally then from C to executable format
import sys
from brainfuckutils import *

MAXPROGRAMSIZE=90000
TAPESIZE=1024
def checkReturnStatus(returnCode):
	if (returnCode==MISMATCH_BRACKET):
		print("Syntax error: Mismatched Brackets")
		exit(1)
	else:
		return 0
def main():
	if (len(sys.argv)!=3):
		print("Usage: brainfucktoc Infile.bf Outfile.c")
		exit()
	#TODO: error handling on file open
	programFile=open(sys.argv[1],"r")
	program=programFile.read()
	parser=BrainFuckParser(program,MAXPROGRAMSIZE,TAPESIZE)
	returnTuple=parser.compileProgram()
	checkReturnStatus(returnTuple[0])	
	
	output=open(sys.argv[2],"w+")
	output.write(returnTuple[1])
		
	output.close()	
	programFile.close()
	

if __name__=="__main__":
	main()
