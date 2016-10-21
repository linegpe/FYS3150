import subprocess

def run_cmd(cmd):
	print ">> ", cmd
	subprocess.call(cmd,shell=True)

fname= "eigenvalues"
run_cmd("g++ -o %s.out %s.cpp -llapack -lblas -larmadillo" % (fname, fname))

run_cmd("./%s.out" % fname)