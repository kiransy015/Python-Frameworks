# Approach 1

# for i in range(1,6,1):
# 	for j in range(i,6,1):
# 		print("*",end=" ")
# 	print("\n")


# Approach 2
for i in range(1,6,1):
	for j in range(1,6,1):
		if i+j<=6:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print("\n")
