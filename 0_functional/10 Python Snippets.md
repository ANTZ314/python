# Useful Python Snippets

### 1. Swap Two Variables With One Line of Code

Can you think of a way to swap two variables without the help of a third temporary variable? 
Well, here it is:

	a = 1
	b = 2
	a, b = b, a

### 2. Duplicate Strings Without Looping
```
name = "Banana"
print(name * 4)
```
Output:

	BananaBananaBananaBanana

### 3. Reverse a String
```
sentence = "This is just a test"
reversed = sentence[::-1]

print(reversed)
```
Output:

	tset a tsuj si sihT

### 4. Squash a List of Strings Into One String
```
words = ["This", "is", "a", "Test"]
combined = " ".join(words)
print(combined)
```
Output:

	This is a Test

### 5. Comparison Chains

In Python, you can combine comparisons neatly together instead of splitting the statement into two or more parts. 
For example:
```
x = 100
res = 0 < x < 1000
print(res)
```
Output:

	True 

### 6. Find the Most Frequent Element in a List
```
test = [6, 2, 2, 3, 4, 2, 2, 90, 2, 41]
most_frequent = max(set(test), key = test.count)

print(most_frequent)
```
Output:

	2

### 7. Unpack List to Separate Variables

You can neatly unpack a list of elements to separate variables as long as the number of variables remains the same as the number of elements in the list.
For example:
```
arr = [1, 2, 3]
a,b,c = arr
print(a, b, c)
```
Output:

	1 2 3

### 8. One-Liner If-Else Statements

In Python, one-liner if-else statements are known as ternary operators or conditional operators. 
For example:
```
age = 30
age_group = "Adult" if age > 18 else "Child"
print(age_group)
```
Output:

	Adult

Generally, a conditional operator follows this pattern for your convenience:

	true_expression if condition else false_expression

### 9. Loop Through a List With One Line of Code

You can use comprehensions to loop through a list with one line of code. For example, let’s raise each number in a list to the second power:
```
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)
```
Output:

	[1, 4, 9, 16, 25]

Note: 
Comprehensions are not just limited to working with lists. You can use comprehensions in a similar one-liner fashion with **dictionaries**, **sets**, and **generators** as well.

Let’s see another example by using dictionary comprehension to raise the values of a dictionary to the second power:
```
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
squared_dict = {key: num * num for (key, num) in dict1.items()}

print(squared_dict)
```
Output:

	{'a': 1, 'b': 4, 'c': 9, 'd': 16}

### 10. Simplify If Statements

Instead of this horrible mess:

	if n == 0 or n == 1 or n == 2 or n == 3 or n == 4 or n == 5:

You can simply do this:

	if n in [0, 1, 2, 3, 4, 5]
