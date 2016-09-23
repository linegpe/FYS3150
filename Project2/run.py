import subprocess

def run_cmd(cmd):
	print ">> ", cmd
	subprocess.call(cmd,shell=True)

fname= "main"
header1 = "jacobi"
run_cmd("g++ -o %s.out %s.cpp %s.cpp" % (fname, fname, header1))

run_cmd("./%s.out" % fname)