#This will read 2 input Simplify3d Files and output differences among the files. 
import sys
import string
import time
import csv
import os
import os.path

def ReadGcode(testFile1, testFile2, outfile):
	LastLine = 185 #where the actual Gcode begins. 
	startTime = time.time()
	print("File1 = " + testFile1 + "\nFile2 = "+ testFile2+"\nOutput File = " + outfile+"\n");
	# f1= open(testFile1, 'r')
	# f2= open(testFile2, 'r')
	# for i in range(LastLine):
		# line_f1=f1.next().strip()
		# line_f2=f2.next().strip()
	with open(testFile1) as myFile1:
		readLines1 = myFile1.readlines()[0:LastLine]
		print(readLines1)
		#with open(t
		
		#print(line_f1 + " | " + line_f2)

	# f1.close()
	# f2.close()
	elapsedTime = time.time() - startTime
	m, s = divmod(elapsedTime, 60)
	h, m = divmod(m, 60)
	print("The operations took: %02d:%02d:%02d (H:M:S)" % (h, m, s))
	print("Finished!")

def main():
	#you can hard code a DB and query or pass them as arguments
	testFile1 = r"C:\Users\peter.t.copeland\Documents\Python\HandOfThe_King.gcode" #"File1.gcode"
	testFile2 = r"C:\Users\peter.t.copeland\Documents\Python\HandOfThe_King2.gcode"#"File2.gcode"
	testOutputcsv = "outputfile here"
	if len(sys.argv) == 3:
		testFile1 = sys.argv[1]
		testFile2 = sys.argv[2]
		testOutputcsv = sys.argv[3]
	if len(sys.argv) == 1:
		print("\n###USING HARD CODED VALUES###\n")
	else:
		print("IMPROPER ARGUMENTS!!!\n\n Expected format:\n File1\n File2\n output file\n (quotations are your friend with complicated names/paths)")
		
	if(os.path.isfile(testFile1) and os.access(testFile1, os.R_OK)
	and os.path.isfile(testFile2) and os.access(testFile2, os.R_OK)):
			ReadGcode(testFile1, testFile2, testOutputcsv)
	else:
		print("\n!!!!File missing or unreadable!!!\n")
		print("File1 Tried: " + str(testFile1))
		print("File2 Tried: " + str(testFile2))
	sys.exit()
	
if __name__ == "__main__":
	main()
