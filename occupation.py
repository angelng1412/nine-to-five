import csv

f = open("occupations.csv", 'r')
s = f.read()
s = s.split("\r\n")
del s[0]
del s[-1]
del s[-1]

jobDict = {}

for thing in s:
    print thing 
    
#print s
