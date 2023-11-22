#!/usr/bin/env python3
import sys, random, re

# Read participants file
infile = open('retreat_participants.txt', 'r')
listoflists = list()
for line in infile:
    if line.startswith("# GROUP"):
        listoflists.append([])
    elif line.strip() == "":
        pass
    elif line.lstrip().startswith("#"):
        pass
    elif len(listoflists) == 0:
        pass
    else:
        listoflists[-1].append(' '.join(line.split()))
infile.close()

# Get groups
reobj = re.match(r"(groups|size)=(\d+)", sys.argv[-1])
if reobj is None:
    print("Usage: makegroups.py groups=<no> | size=<no>")
    sys.exit(1)
if reobj.group(1) == "groups":
    groupcount = int(reobj.group(2))
else:
    total = sum([len(x) for x in listoflists])
    groupcount = total // int(reobj.group(2))

# Create random groups with people from all lists.
listoflists.sort(key=len)
biglist = list()
for i in range(len(listoflists)):
    random.shuffle(listoflists[i])
    biglist.extend(listoflists[i])
groups = list()
for i in range(groupcount):
    groups.append([])
i = 0
for name in biglist:
    groups[i].append(name)
    i = (i+1) % groupcount

# Print
for i in range(0, groupcount-1, 2):
    print("{:30s}{:30s}".format("Group " + str(i+1), "Group " + str(i+2)))
    if len(groups[i]) > len(groups[i+1]):
        groups[i+1].append('')
    for j in range(len(groups[i])):
        print("{:30s}{:30s}".format(groups[i][j], groups[i+1][j]))
    print()
if groupcount % 2 == 1:
    print("{:30s}".format("Group " + str(groupcount)))
    for j in range(len(groups[-1])):
        print("{:30s}".format(groups[-1][j]))


