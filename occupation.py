import random 

f = open("occupations.csv", 'r')
s = f.read()
data = s.split("\n")
data = data[1:-1]

jobDict = {}
for job in data:
    if job.find('"') >= 0:
        thing = job.split('"')
        jobDict[thing[1]] = float(thing[2][1:])
    else:
        thing = job.split(',')
        jobDict[thing[0]] = float(thing[1])
#print jobDict

def randJob():
    num = random.uniform(0,99.8)
    tmp = 0 
    for job, percent in jobDict.iteritems():
        tmp += percent
        if num < tmp:
            return job

for x in range(100):
    print randJob()
