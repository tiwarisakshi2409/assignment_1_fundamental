# Write a Python function to insert a string in the middle of a string.
s = 'Tops Technologies Is For Python Learning'
print("The Original String Is :" + str(s))
test = s.split()
mid_str = "Best"
mid_pos = len(test)//2
test.insert(mid_pos,mid_str)
print("New String :" +str(" ".join(test)))