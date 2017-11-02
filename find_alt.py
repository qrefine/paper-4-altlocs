
import os
import sys

list = [[]for i in range(50)]
# search the word in file
def search(path, word,i):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp):
            with open(fp) as f:
                for line in f:
                    if word in line:
                        alt = line.split(":")[1]
                        count(alt,i,filename)

        elif os.path.isdir(fp):
            search(fp, word,i)
            
def count(alt,i,filename):
    if int(alt) == i:
        # shutil.copy(fp,"E:\\work_qr\\"+filename)
        list[i].append(filename[3:7])
        #print filename[3:7]
        #print list

for ids in range(50):
    search("/home/pdb/log", "  alt. conf.",ids)

print list
#print len(list[0])
for id in range(50):
    print "the num of %d alt is: %d" % (id,len(list[id]))