import subprocess
import sys

def run_cmd(cmd):
	print ">> ", cmd
	subprocess.call(cmd,shell=True)

fname= "main"
fname2 = "plot_results"

run_cmd("g++ -o %s.out %s.cpp -llapack -lblas -larmadillo" % (fname, fname))



run_cmd("./%s.out" % fname)

runplot = raw_input("Do you want to make a plot now? [y/n]")

if runplot == "y":
	run_cmd(("python %s.py") % fname2)
elif runplot == "n":
	print "Program ended. Your results is saved to the designated file. To plot them, please run plot3.py. Have a nice day!"
	sys.exit(0)
else:
	print "Sorry, I cannot understand that. Please run again or simply run the file plot_results.py."
	sys.exit(0)