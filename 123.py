print("hallo world")
print("tiantian")
"python"
import math
math.pi
s = set()
for x in range(2,100000):
    for y in range(2, x-1):
        c = x/y
        if (str(c)[2]=="0"):
            s.add(x)

print(s)


