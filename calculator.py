#!/bin/python
import sys
from math import pow

DEFAULT_TORMENT = 2
DEFAULT_RUNS = 5

#generate pascals triangle
def pascalsTriangle(rows):
  for rownum in range (rows):
    newValue=1
    rlist = [newValue]
    for iteration in range (rownum):
      newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
      rlist.append(int(newValue))
  return rlist

#p to drop organ given torment level
def pOrganDrop(torment):
  return .25+(torment-1)/20.0

#p to drop organ given torment level, iteration, and total iterations
def pOrganDropI(torment, i, total):
  psuccess=pow(pOrganDrop(torment), total-i)
  pnotsuccess=1
  if i > 0:
    pnotsuccess=pow(1-pOrganDrop(torment), i)
  return psuccess*pnotsuccess

#p to drop organ at given torment/run level
def calculate(torment,runs):
  triangle=pascalsTriangle(runs+1)
  p=0.0
  i=0
  for leaf in triangle:
    if i < len(triangle)-1:
      pi = pOrganDropI(torment, i, runs) * leaf
      p += pi
      print('pdrop(i):' + str(i) + ' is ' + str(pi) + ' total: ' + str(p))
      i+=1
  return p

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print('Usage: ./calculator.py <torment level> <#runs>' +
    ' using default torment level ' + str(DEFAULT_TORMENT) + ' with ' + str(DEFAULT_RUNS) + ' runs')
    torment=DEFAULT_TORMENT
    runs=DEFAULT_RUNS
  else:
    torment=int(sys.argv[1])
    runs=int(sys.argv[2])
  pdrop=calculate(torment,runs)
  print('pdrop for a given organ=' + str(pdrop) + ', pdrop for all three is=' + str(pow(pdrop,3.0)))
