# Write a Python program to count the occurrences of each word in a given sentence
s = "Tops Technologies Is Here To Upgrade Your Technical Skills And To Enhance Your Learing"
a = dict()
txt = s.split(" ")
for i in txt:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1 
print(a)