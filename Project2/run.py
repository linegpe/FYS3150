import subprocess
import os

rows, columns = os.popen('stty size','r').read().split()
tsize = int(columns)
halft = tsize/2


def run_cmd(cmd):
	print ">> ", cmd
	subprocess.call(cmd,shell=True)

fname= "main"
fname2 = "main2"
header1 = "jacobi"
header2 = "functions"
arma = "eigenvalues"

print "\n"
print "=" * tsize
print " " * (halft-6) + "ONE ELECTRON" + " " * (halft-6)
print "=" * tsize

print "\n"
print " " * (halft-8) + "JACOBI ALGORITHM" + " " * (halft-8)
print "\n \n"

run_cmd("g++ -L/usr/local/lib -I/usr/local/include -o %s.out %s.cpp %s.cpp %s.cpp" % (fname, fname, header1, header2))

run_cmd("./%s.out" % fname)

run_cmd("python plot1e.py")


print "\n \n \n"

print " " * (halft-10) + "ARMADILLO ALGORITHM " + " " * (halft-10)
print "\n \n"

run_cmd("g++ -L/usr/local/lib -I/usr/local/include -o %s.out %s.cpp -larmadillo" % (arma, arma))

run_cmd("./%s.out" % arma)


print "\n"
print "=" * tsize
print " " * (halft-7) + "TWO ELECTRONS " + " " * (halft-7)
print "=" * tsize

print "\n"
print " " * (halft-8) + "JACOBI ALGORITHM" + " " * (halft-8)
print "\n \n"


run_cmd("g++ -L/usr/local/lib -I/usr/local/include -o %s.out %s.cpp %s.cpp %s.cpp" % (fname2, fname2, header1, header2))

run_cmd("./%s.out" % fname2)

run_cmd("python plot2e.py")