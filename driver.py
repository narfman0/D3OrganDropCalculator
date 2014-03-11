#!/bin/python
from calculator import calculate

RUNS=10

def prettify(number):
  return '{0:.2f}'.format(number)

totals=[]
for torment in range(1,7):
  total = []
  for runs in range(0,RUNS):
    total.append(calculate(torment,runs+1))
  totals.append(total)

runsString = ''
for run in range(1,RUNS+1):
  runsString += str(run) + '     '
print('\tTorment\\Runs ' + runsString)
for torment in range(0,len(totals)):
  row='\t     ' + str(torment+1) + ":  "
  for runs in range(0, len(totals[torment])):
    row += prettify(totals[torment][runs]*100) + ' '
  print(row)