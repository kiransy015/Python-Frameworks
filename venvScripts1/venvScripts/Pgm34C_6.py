# Approach 1
# for i in range(1,6,1):
# 	for j in range(1,i+1,1):
# 		print("*",end="\t")
# 	print("*",end="\t")
# 	print("\n")


# Approach 2
for i in range(1,6,1):
	for j in range(1,6,1):
		if i>=j:
			print("*",end=" ")
	print("\n")
