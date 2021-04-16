# Fungsi Min dan Max
a = 0.0000000005678
b = -0.0000000004568
c = -0.0000000005678
print("bilangan a= ", a)
print("bilangan b = ", b)
print("bilangan c= ", c)
print("nilai maximum ketiga bilangan tersebut adalah ", max(a,b,c))
print("nilai minimum ketiga bilangan tersebut adalah ", min(a,b,c))

print("\n", "asik"*8)

# Fungsi Choice
import random
list = [a, b, c]
print("\nundian 1")
print("hasil= ", random.choice(list))
print("undian 2")
print("hasil= ", random.choice(list))
print("undian 3")
print("hasil= ", random.choice(list))

print("\n", "asik"*8)

# Fungsi ceil
import math
print("\na ceil= ", math.ceil(a))
print("b ceil= ", math.ceil(b))
print("c ceil= ", math.ceil(c))

print("\n", "asik"*8)

# Fungsi abs
print("\n|a|= ", abs(a))
print("|b|= ", abs(b))
print("|c|= ", abs(c))
