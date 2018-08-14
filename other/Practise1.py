import math

# a generator that yields items instead of returning a list
# therefore saves ALOT of memory
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(150))
print (str(sum_of_first_n)+"\n")

# using 'range' vs 'xrange'
s = sum(range(50, 60))
p = sum(xrange(1000, 1500))

print (str(s) + "\n")
print (p)

# xrange("start", "stop" and "step")
for i in xrange(100, 120, 2):
    print(str(i)+"-")

# replaces the yeild method
my_nums = (x*x for x in [1,2,3,4,5])
# converting to list uses memory for each value stored
print list(my_nums) # [1,4,9,16,25]

print("\n" + str(math.pi * 2))

# DICTIONARIES:
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict["Age"] = 8;                # update existing entry
dict['School'] = "DPS School";  # Add new entry

# first check if key is in dictionary:
if 'Age' in dict:
    print "dict['Age']: ", dict['Age']
else:
    print "doesn't exist"

try:
    print "dict['School']: ", dict['School']
except KeyError:
    print "ERROR!"
