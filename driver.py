#!/bin/python
from calculator import calculate
from math import pow

RUNS=10

def prettify(number):
  return '{:5.2f}'.format(number)

totals=[]
for torment in range(1,7):
  total = []
  for runs in range(0,RUNS):
    total.append(pow(calculate(torment,runs+1), 3))
  totals.append(total)

runsString = ''
for run in range(1,RUNS+1):
  runsString += '{:6.0f}'.format(run)
print('\tTorment\\Runs ' + runsString)
for torment in range(0,len(totals)):
  row='\t     ' + str(torment+1) + ":       "
  for runs in range(0, len(totals[torment])):
    row += prettify(totals[torment][runs]*100) + ' '
  print(row)