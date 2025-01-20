# TYPE CASTING
a = 65  # int datatype
t = type(a)  
print(t)

b = "56.7"  # it will print string bcz in "" in " we only prints string"
t  = type(b)
print(t)
# coverting datatype
e = "56.7"
c = float(e)  # the given value in e is string thr c operator will change it into float datatype
t = type(c)
print (t)

e = "56.7"
c = float(e)  # the given value in e is string thr c operator will change it into float datatype
g = int(c)     # the given value float value will change into int datatype
t = type(g)
print (t)

