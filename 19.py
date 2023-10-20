# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
s=input("Enter The String:")
count = 0

for i in s:
    count = count + 1
s1 = s[0:2] + s[count - 2: count]

print("String = " + s)
print("New String =" + s1)