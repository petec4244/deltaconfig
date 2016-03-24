import sys
import string
import time
import csv
import os
import os.path

def ReadGcode(testFile, outfile):
	startTime = time.time()
	print("DB = " + dbName + "\n\nOutput File = " + outfile+"\n");
	f= open(outfile, 'w')
	#f.write(headerRow)
	for row in rows:
		s = str(row)
		s = s.replace(')', '')
		s = s.replace('(', '')
		s = s+'\n'
		f.write(s)
	f.close()
	elapsedTime = time.time() - startTime
	m, s = divmod(elapsedTime, 60)
	h, m = divmod(m, 60)
	print("The operations took: %02d:%02d:%02d (H:M:S)" % (h, m, s))
	print("Finished!")

def main():
	#you can hard code a DB and query or pass them as arguments
	testFile = "path to File"
	testOutputcsv = "file.csv here"
	if len(sys.argv) == 3:
		testFile = sys.argv[1]
		testOutputcsv = sys.argv[2]
	if len(sys.argv) == 1:
		print("\n###USING HARD CODED VALUES###\n")
	else:
		print("IMPROPER ARGUMENTS!!!\n\n Expected format:\n Database\n Query \n output csv file\n (quotations are your friend)")
		
	if(os.path.isfile(testFile) and os.access(testFile, os.R_OK)):
		ReadGcode(testFile, tempStr, testOutputcsv)
	else:
		print("\n!!!!Database missing or unreadable!!!\n")
		print("File Tried: " + str(testFile))
	sys.exit()
	
if __name__ == "__main__":
	main()
