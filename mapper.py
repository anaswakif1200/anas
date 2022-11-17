import sys
for line in sys.stdin:
	line=line.strip(",")
	line1=line.strip("(")
	line2=line1.strip(")")
	words=line2.split()
	for word in words:
		print('%s\t%s'%(word,1))
