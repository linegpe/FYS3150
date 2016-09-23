import subprocess

def run_cmd(cmd):
	print ">> ", cmd
	subprocess.call(cmd,shell=True)

fname= "main"
fname2 = "main2"
header1 = "jacobi"
arma = "eigenvalues"

print "\n \n \n"

print "========== ONE ELECTRON =========="

print "\n \n \n"

print " JACOBI ALGORITHM "

run_cmd("g++ -o %s.out %s.cpp %s.cpp -larmadillo -lblas -llapack" % (fname, fname, header1))

run_cmd("./%s.out" % fname)

run_cmd("python plot1e.py")


print "\n \n \n"

print " ARMADILLO ALGORITHM "

run_cmd("g++ -o %s.out %s.cpp -larmadillo -lblas -llapack" % (arma, arma))

run_cmd("./%s.out" % arma)


print "\n \n \n"

print "========== TWO ELECTRONS =========="


print "\n \n \n"

run_cmd("g++ -o %s.out %s.cpp %s.cpp -larmadillo -lblas -llapack" % (fname2, fname2, header1))

run_cmd("./%s.out" % fname2)