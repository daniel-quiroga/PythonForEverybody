# 9.4
# Liu Li
# 18 Nov, 2015

'''
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
import re
# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
fname = "mbox-short.txt"
with open(fname, 'r') as fh:
    dir = {}
    for line in fh:
        if re.search("From ", line):
            key = re.findall('[^ ]+@[^ ]+', line)[0]
            dir[key] = dir.get(key, 0)+ 1

key = list(dir.keys())
value = list(dir.values())

print  key[value.index(max(value))], max(value)
#############################################################
# Desired Output
# cwen@iupui.edu 5
