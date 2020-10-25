# Approach 1
# for i in range(1,6,1):
# 	for j in range(6,1,-1):
# 		if(i>=j):
# 			print("*",end="\t")
# 		else:
# 			print(end="\t")
# 	print("LL",end="\n")


# Approach 2
for i in range(1,6,1):
	for j in range(1,6,1):
		if i+j>=6:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print("\n")
