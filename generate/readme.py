import glob
l= glob.glob("*")

k=[i.split(".")[0].upper() for i in l]
k.remove("README")
k.remove("GENERATE")
k.sort()
for i in range(1,len(k)+1):
	print i,k[i-1]