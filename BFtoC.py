#!/usr/bin/python3
##########################
#Author: Brady Itkin
#Created: 2/19/15
#Last modified: 2/19/15
#Class: CS-1310 Boese
#Program: A Simple Brainfuck Compiler
#Description: Compiles a brainfuck program from sys.argv[1] to C, and optionally then from C to executable format
import sys
from brainfuckutils import *

MAXPROGRAMSIZE=90000
TAPESIZE=4096

def checkReturnStatus(returnCode):
	##Compiler/interpreter error return codes
	########################################
	#SUCCESS=0
	#MISMATCH_BRACKET=1
	#PROGRAMSIZE=2
	#MAXTAPESIZE=3
	#MAXVALUE=4
	#END=5
	if (returnCode==MISMATCH_BRACKET):
		print("Syntax error: Mismatched Brackets")
		exit(1)
	elif (returnCode==MAXTAPESIZE):
		print("Runtime error: Maximum tape-size reached")
		exit(3)
	elif (returnCode==MAXVALUE):
		print("Runtime error: Maximum cell-size reached")
		exit(4)
	elif (returnCode==END):
		print("Runtime: Program end")
		exit(0)
	else:
		return 0

def startInterpreter():
	#TODO: better file and user-input handling
	programf=open(sys.argv[1])
	program=programf.read()
	programf.close()	
	interpreter=BrainFuckInterpreter(MAXVAL_INT,TAPESIZE,program)
	while (not checkReturnStatus(interpreter.nextCommand())):
		pass
	#print("Instructions performed: "+str(ticker))
	exit(0)
		
def main():
	if (sys.argv[len(sys.argv)-1]=="-"):
		startInterpreter()
	elif (len(sys.argv)!=3):
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
