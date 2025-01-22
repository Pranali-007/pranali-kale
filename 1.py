#STRING
print('kajal')        # to write single line string
print("kajal")       # to write single line string
print('''kajal''')    #to write multiline string

# to finding length of string SLICING
name=("pranali")
pk=name[0:5]  # to print specified length og string
print(pk)
# for having any specific character to print at [position]
character1=name[1]    #it will print p at [1] position
print(name[1])

character1=name[0]  #it will print p at [0] position
print(name[0])

#NEGATIVE SLICING
pk=name[-4:-2] #output will be "na"
print(pk)


# SKIP VALUE
word = ("international")
pk = word[0:6:2]   #0=start,6=end,2=gap
print(pk)

a = ("pranalibalasahebkale")
b = a[0:15:3]
print(b)

#STRING FUNCTIONS
name=("harry")
print(len(name))     #shows length of string
print(name.endswith("rry"))    #checks end words of string
print(name.startswith("ha"))     #check weather string start with words
print(name.capitalize())         #start of words 1st latter capital

