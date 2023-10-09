print("napisz 5 ocen z matmy które myślisz że miałbyś")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

x = [a,b,c,d,e]
print("twoja srednia to "+str( sum(x)/len(x)))