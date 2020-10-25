import re

# Program: Write a program to check the given number is a prime number or not?

# def primenos(no):
#     for i in range(2,int(no/2)+1,1):
#         if no%i==0:
#             return False
#     return True
#
# print("Is 5 prime no? :",primenos(6))



# Program: Find out duplicate number between 1 to N

# lst = [3,4,5,3,5,7]
#
# def duplicatenos(lst):
#     st = set()
#
#     for i in lst:
#         if i in st:
#             print("Duplicate no :",i)
#         else:
#             st.add(i)
#
# duplicatenos(lst)



# Program: Write a program to reverse a string using recursive algorithm

# str = "Program"
#
# def reversestring(str):
#     temp = ""
#     for i in range(len(str)-1,-1,-1):
#         temp=temp+str[i]
#     return temp
#
# print("Reverse of string :",reversestring(str))



# Program: Write a program to reverse a number

# def reverseno(num):
#     reverse = 0
#     while num!=0:
#         reverse = int((reverse*10)+(num%10))
#         num = int(num/10)
#
#     return reverse
#
# print("Reverse of number :",reverseno(12345))


# Program: Write a program to find perfect number or not

# def perfno(perf):
#     perfsum=0
#     for i in range(1,int(perf/2)+1,1):
#         perfsum = perfsum+i
#
#     if (perf == perfsum):
#         print("Its Perfect no!!!")
#     else:
#         print("Not a Perfect no!!!")
#
# perfno(7)


# Program: Write a program to find out duplicate characters in a string

# def duplicatechar(str):
#
#     for i in str:
#         val = 1;
#         if i in a:
#             a[i]=val+1
#         else:
#             a[i]=1
#
#     print(a)
#
# str = "Perfect"
# a = {}
#
# duplicatechar(str)



# Program: Write a program to find top two maximum numbers in a array

# lst = [1,5,2,7,9,10]
#
# def twomaxnos(lst):
#     max1=0
#     max2=0
#     temp=0
#
#     for i in range(0,len(lst)):
#         print(lst[i])
#         if lst[i]>max1:
#             temp=max1
#             max1=lst[i]
#             max2=temp
#
#     print("First max no :",max1)
#     print("Second max no :",max2)
#
# twomaxnos(lst)



# Program: Write a program to find common elements between two arrays

# a = [1,5,2,7,9,10]
# b = [3,6,7,5]
#
# def commonnos(a,b):
#     for i in range(0,len(a)):
#         if a[i] in b:
#             print("Duplicate no :",a[i])
#
# commonnos(a,b)



# Program: Write a program to print fibonacci series

# lst = []
# cnt = 5
#
# def fibseries(cnt):
#     lst.append(0)
#     lst.append(1)
#
#     for i in range(2,cnt):
#         sum = lst[i-1]+lst[i-2]
#         lst.append(sum)
#
#     return lst
#
# print("fibseries :",fibseries(cnt))


# Program: Write a program to find sum of each digit in the given number using recursion

# class InterviewPgms:
#
#     def __init__(self):
#         print("object creation")
#
#     def sumofeachdigit(self,num):
#         if num==0:
#             return num
#         else:
#             return int(num%10)+self.sumofeachdigit(num/10)
#
# ref = InterviewPgms()
# print(ref.sumofeachdigit(223))



# Program: Write a program to check the given number is binary number or not?

# class isbinary:
#     def __init__(self):
#         print("object creation")
#
#     def binarycheck(self,num):
#         status = True;
#
#         while True:
#             if num==0:
#                 return status
#             elif int(num%10)>1:
#                 status=False
#                 return status
#             else:
#                 num=int(num/10)
#
# ref = isbinary()
# print("is this binary? ",ref.binarycheck(10300111))


# Program: Write a program for Bubble Sort

# class bubblesort:
#
#     def bubble_srt(self,lst):
#         lnt = len(lst)
#         for i in range(lnt,-1,-1):
#             for j in range(0,lnt-1,1):
#                 k = j+1
#                 if lst[j]>lst[k]:
#                     self.swapnos(j,k,lst)
#
#         print(lst)
#
#     def swapnos(self,i,j,lst):
#         temp = lst[i]
#         lst[i] = lst[j]
#         lst[j] = temp
#
# lst = [5,3,7,1,8,4,9]
# ref = bubblesort()
# ref.bubble_srt(lst)



# Program: Write a program to find the sum of the first 1000 prime numbers

# class primenos:
#
#     def printprimenos(self):
#         sum1 = 0
#         num = 2
#         count = 1
#         while count<=1001:
#             if self.isPrimenos(num):
#                 print(num)
#                 count = count+1
#                 sum1 = sum1 +num
#             num = num+1
#         print("Sum of first 1000 prime nos :",sum1)
#
#
#     def isPrimenos(self,num):
#         for i in range(2,int(num/2),1):
#             if int(num%i)==0:
#                 return False
#         return True
#
# ref = primenos()
# ref.printprimenos()



# write a program to check whether a year is leap year or not

# class leapyr:
#
#     def leapyr(self,yr):
#         if (yr%400==0) or (yr%4==0) and (yr%100!=0):
#             print("Its Leap year !!!")
#         else:
#             print("Its not Leap year !!!")
#
# ref = leapyr()
# ref.leapyr(2005)



# Program: Write a program to find Palindrome

# class palindromecheck:
#
#     def ispalindrome(self,str):
#         temp=""
#         for i in range(len(str)-1,-1,-1):
#             temp = temp+str[i]
#
#         if(str==temp):
#             print("Its Palindrome!!!")
#         else:
#             print("Not a Palindrome!!!")
# ref = palindromecheck()
# ref.ispalindrome("srti")


# Program: Write a program for binary search

# class binarysearch:
#
#     def binarysrch(self,lst,val):
#         start = 0
#         end = len(lst)
#
#         while(start<=end):
#             mid = (start + end) / 2
#             mid = int(mid)
#             if val==int(lst[mid]):
#                 return mid
#             elif val<int(lst[mid]):
#                 end = mid-1
#             else:
#                 start=mid+1
#         return -1
#
# lst = [2, 4, 6, 8, 10, 12, 14, 16]
# ref = binarysearch()
# print(ref.binarysrch(lst,14))



# Program: Write a program to find factorial of a number

# class factorialno:
#
#     def factsno(self,val):
#         fact = 1
#         if val<0:
#             print("No should be positive!!!")
#         else:
#             for i in range(1,val+1,1):
#                 fact=fact*i
#         return fact
#
# ref = factorialno()
# print(ref.factsno(13))



# Program: How to swap two numbers without using temporary variable?

# class swapnos:
#
#     def swap_nos(self,temp1,temp2):
#         print("temp1 value before swap :",temp1)
#         print("temp2 value before swap :", temp2)
#
#         sum = temp1+temp2
#         temp1 = sum-temp1
#         temp2 = sum-temp1
#
#         print("temp1 value after swap :", temp1)
#         print("temp2 value after swap :", temp2)
#
# ref = swapnos()
# ref.swap_nos(5,7)



# Program: How to get distinct elements from an array by avoiding duplicate elements?

# class duplicateelements:
#
#     def dupelements(self,lst):
#         for i in range(0,len(lst)):
#             isdistinct = False
#             for j in range(0,len(lst)):
#                 if i==j:
#                     isdistinct=True
#                 elif lst[i]==lst[j]:
#                     isdistinct = False
#                     break
#
#             if (isdistinct):
#                 print(lst[i])
#
# lst = [5,3,7,2,4,7,8,2,3]
# ref = duplicateelements()
# ref.dupelements(lst)



# Program: Write a program to remove duplicates from sorted array

# class removeDuplicates:
#
#     def rmvduplicates(self,lst):
#         st = set()
#         for i in range(0,len(lst)):
#             st.add(lst[i])
#
#         print("Unique nos :",st)
#
# lst = [5,3,7,2,4,7,8,2,3]
# ref = removeDuplicates()
# ref.rmvduplicates(lst)


# Str = input("Enter emailid :")
# rs = re.findall()
#
# if rs:
#     print("Its valid emailid!!!")
# else:
#     print("Not a valid emailid!!!")












