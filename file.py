def series(string,begin,end):
	for i in range(begin,end+1):
		print(f"{string}{i}")
		
import sys
ar=[]
for i, arg in enumerate(sys.argv):
        ar.append(arg)

# add space 
# python file.py Chapter 1 12 whatever
# write whatever or even insert one character
if (len(ar)==5):
	ar[1]=ar[1] + ' '

series(ar[1],int(ar[2]),int(ar[3]))
