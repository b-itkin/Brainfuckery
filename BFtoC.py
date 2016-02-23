#!/usr/bin/python3
##########################
#Author: Brady Itkin
#Created: 2/19/15
#Last modified: 2/23/15
#Class: CS-1310 Boese
#Program: A Simple Brainfuck Compiler
#Description: Compiles a brainfuck program from sys.argv[1] to C and then to an executable using GCC
#Also will interpret a brainfuck program with the - option.
import os
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
		return 5
	else:
		return 0

def startInterpreter():
	if (len(sys.argv)==3 or len(sys.argv)==4):
		programf=open(sys.argv[1])
		program=programf.read()
		programf.close()	
		interpreter=BrainFuckInterpreter(MAXVAL_INT,TAPESIZE,program)
		while (not checkReturnStatus(interpreter.nextCommand())):
			pass
		#print("Instructions performed: "+str(ticker))
		if (len(sys.argv)==3):
			exit(0)
		
	else:
		print("Usage: brainfucktoc Infile.bf [Outfile.c] [-]")
	
def main():
	if (sys.argv[len(sys.argv)-1]=="-"):
		startInterpreter()
	elif (len(sys.argv)!=3):
		print("Usage: brainfucktoc Infile.bf [Outfile.c] [-]")
		exit()
	
	print("Opening and reading " + sys.argv[1] + " .....")
	programFile=open(sys.argv[1],"r") #Open file for reading
	program=programFile.read() #Read it in
	print("Compiling to " + sys.argv[2] + " ........")
	parser=BrainFuckParser(program,MAXPROGRAMSIZE,TAPESIZE) #Get a BrainFuckParser instance
	returnTuple=parser.compileProgram() #Compile
	checkReturnStatus(returnTuple[0]) #Make sure nothing died	
	
	output=open(sys.argv[2],"w+") #All went well since we didn't exit out, so open up a file to write
	output.write(returnTuple[1]) #Write the compiled C
		
	output.close() #Tidy up	
	programFile.close()
	
	print("Running gcc on " + sys.argv[2] + " .....") 
	os.system("gcc {0} -o {1}.out".format(sys.argv[2],sys.argv[2].strip(".c")))
	print("Done! Have a nice day :)")
	
if __name__=="__main__":
	main()
