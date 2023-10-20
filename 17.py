# Write a Python function that takes a list of words and returns the length of the longest one.
def longestlength(l):
    max = len(l[0])
    temp = l[0]

    for i in l:
        if(len(i) > max):

            max = len(i)
            temp = i
            
    print("The word with longest length is:", temp, "and lenght is", max)
l = ["Tops", "Techno", "Technology", "Technologies", "Tech", "Logical"]
longestlength(l)