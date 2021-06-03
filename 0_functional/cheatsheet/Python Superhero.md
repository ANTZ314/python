#Python — From Intermediate to Superhero

####[LINK](https://blog.usejournal.com/python-from-intermediate-to-superhero-1a86e518bb77)

The purpose of this article is to serve as a tiny handbook for anyone who already completed a Python tutorial, has a pretty good grasp on the basics and would like to take their skills to the next level. Becoming a good Python developer has a lot to do with getting yourself familiar with the language’s quirks and the pythonic way of thinking and doing things. I will go below through 6 points that will help a beginner-to-intermediate comfortably step into the domain of more advanced Python:

* more complex list comprehensions
* map, filter, and reduce with lambdas
* locals and globals
* context managers
* decorators and class decorators
* generators

Note: Some code snippets you are about to see above are images instead of text. Anyone can copy, paste, and run working code from the internet and I believe it is of more value when introducing new concepts to firstly read and understand what’s going on and then write examples yourself, changing things and experimenting

##List Comprehensions
You have already probably seen list comprehensions that generate numbers from the **range()** function like this:

	results = [number for number in range(0, 100)]
	# outputs to a list where every element is an int
	# from 0 to 99 inclusively

You can complement your comprehension with an **if** condition to do a very simple filtering (and iterate over things other than range):

	evens = [number for number in results if number % 2 == 0]
	# gets all the even numbers from the previous set

If you want to make more complex conditionals you can chain if statements or use **and** inside the comprehension. In our case below, the two expressions return lists with the same values

	new = [number for number in results if number % 3 == 0 and number > 50]
	# OR
	new_two = [number for number in results if number % 3 == 0 if number > 50]
	# [51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

Naturally, you can also make transformations to the variable you use to iterate:

	squared = [number**2 for number in results if number % 3 == 0 if number % 4 == 0]

A list comprehension is a more pythonic way of re-writing a specific for loop. Any one of the examples above could have been written as such. However, it is worth keeping in mind that **nested for loops** can be expressed as a single comprehension. There are many incredible articles on Medium on how to write clean, human read-able code so I will not insist on that here, but we should make sure our comprehensions don’t become too convoluted for others to follow. That being said, the two structures below are equivalent:

**image**

As you can see, line 9 is dangerously close to getting a little out of hand. Comprehensions can themselves be nested:

	comp = [x**2 + y for x in [number for number in range(0, 5)] for y in [number for number in range(20, 41)]]

Although ugly and not recommended, the line above is valid.
So why bother? Knowing what is possible will equip you with a better understanding of the language and will prevent you from being taken off guard when you encounter such things

##Lambdas, map(), filter(), and reduce()
A lambda, also called an **anonymous function**, is a simple, function that we can define ad-hoc. The **def** keyword is no longer needed and we will not name it (hence, the anonymous part); instead, we will use the **lambda** keyword. Just like a regular function, it can have any number of arguments. So what’s the catch? Well, it can only evaluate one expression. Think of the one expression as something we can write on one line. Here’s an example:

	foo = lambda n: n**2 if n % 2 == 0 else n**3
	
The _n_ after the **lambda** keyword represents the arguments. We then add a column and insert our logic. No **return** is needed to make this work and we also have some simple conditional logic in there, so that’s pretty neat. Now, if Python is your only language, the foo = part may seem a little odd at first; JavaScript programmers, however, will feel right at home with this. Instead of saying **def foo(n)** we “stored” the function logic into the variable named foo. In order to call it, we would have to do something like:

	foo(5) 
	# returns 125

**Note:** As I’m sure everyone already told you, everything in Python is an object: including functions. You can treat functions just as you would any other variable. You could, for example, store several functions in a list, iterate over it and apply them to a variable, like below:

**image2**
Iterate over functions in a list

**map()** is a special function in many programming languages that allows us to iterate over a collection, and apply a function to every element of that collection. This process is sometimes referred to as mapping a function to _something_. Let’s discuss the following snippet:

	def maximize(n):
	    return n * 10
	col = [10, 15, 19]
	results = map(maximize, col)

As you can see, **map()** takes the function as its first argument and the collection as its second. We apply the function _maximize_ to every element of our list and store the results in the appropriately named variable. However, if we try to access results, we will get something like this:

	<map at 0x2adc5ceac88>

Why don’t we see the list of numbers we expect? That is because map() works with something called lazy evaluation. Which simply means that the results are not computed right away, but will be when we need them. To access the values from the map object (they are all objects, yes) we can use a for loot to iterate over it or use the built-in list() function where we declared the results variable:

	results = list(map(maximize, col))
	# OR
	for element in results:
	    print(element)
    
If the transformation we want to map to the collection allows for this, we can write a lambda directly in the argument parenthesis:

	col = [10, 15, 19]
	results = map(lambda x: x*10, col)

filter() is used to iterate over a collection, apply a condition, expressed as a function, to every element, and return only those elements that pass that condition. Just like in the case of map(), you can define the function ad-hoc as a lambda expression:

	col = [10, 124, 897, 6, 14, 5, 9, 51]
	filtered = filter(lambda x: x % 2 == 0 and x > 25, col)
	for element in filtered:
	    print(element)
	# will output 124

As for reduce(), you can think about it like a generalization of the sum operation. With sum, we take every element of the collection/list and add them together. You could also re-phrase and say we take every element, “apply the add function” and return the final result. What is different here is that this is done incrementally: we take the first two elements, apply the add function, obtain a result which will pass again as an argument of the add function along with the 3rd element and so on. Let’s take a look at the example:

	from functools import reduce
	example = [2, 9, 7, 65, 100, 34]
	result = reduce(lambda x, y: x* y+ 10, example)

As opposed to the other 2 functions, we have to import this one first, so keep that in mind. Also, remember that the function we pass to reduce() should take two arguments, since reduce works with something called an accumulator: at the first iteration the accumulator becomes the result of the computation of the function we pass with the first 2 arguments in our list. That accumulator and the 3rd element in our list get processed at the next iteration and the result becomes the new accumulator.

##locals() and globals()
Introspection in Python is a more subtle topic, and generally speaking we would want to introspect our classes, but, for the purposes of testing or debugging (never in production: if you have to do introspection in production application, you need to rethink the design or engineering) we have some simple tools to examine objects of built-in types. One of them is the type() function, which returns the class of an object:

	>>> v = 5
	>>> print(type(v))
	<class 'int'>
	>>>

We can also check if an object/variable is of a certain class and take action accordingly using the isinstance() function. The first argument is the object, the second is the class (do not write it as a string) and it returns a boolean:

	>>> stuff = [5, 9, 8]
	>>> isinstance(stuff, list)
	True
	>>>

**image3**

Besides these two, we can also check, by name, if a variable exists in either the local or the global namespace using the locals() and globals() functions respectively. They take no arguments and return dictionaries that describe the namespace.

##Context managers
You probably already know that you can use a with block to deal with files and you no longer have to worry about closing said file. Something like this:

	with open("example.txt", "w") as file:
	    # logic
    
What happens here is that a special object is created, called a **context manager** that works with the **with** keyword and automatically does something before and after the execution of the logic you have in the block: in this case, creates and opens the file and closes it respectively. What’s cool about all this is that Python allows us to create our own context managers by writing a class that implements two special methods: **__enter__()** and **__after__()**. They take care of, you guessed it, what happens when execution enters and exits your with block respectively. Methods with **“__”** before and after their names, such as **“__init__”** (the constructor), are special and have to do with they way Python implements some of its functionalities. Let’s take a look at the example below:

**image4**
custom made context manager

On line 18, our context managers initializes with a variable called file as None. We could also have used arguments in the constructor and passed them on line 18 (with DataManager(arg1, arg2) as …). It then gets to the special **enter** method where it gets the current time and date, creates a file using that as the file name, opens it in write mode and returns the file. That file object is then bound to the data variable we also created on the same line. This is not compulsory. If, in enter we returned self, then the variable would have been bound to an instance of our class. In the block, we execute the simple logic of writing something to the file. The **exit** method closes the file automatically and prints that line just so we see it execute successfully. Besides self you have to pass those 3 other arguments to **exit**.
Line 8 is an amazing candidate for a refactoring, if you get the chance to try this out yourself and experiment with the concept.

##Decorators
We mentioned that anything in Python is an object and that we can treat functions as we would any other object, including adding them in a list. That means that we can pass functions as arguments to other functions! Those of you coming from the (now gone) JavaScript callback hell understand this all to well.
With a decorator, we will create a function that takes a second function as argument, modifies its behaviour in some way, and gives us back also a function **with the same signature** as the function we passed as argument. Python has special syntax that makes sure the function we decorate (pass as argument to the decorator function) will be replaced (same name, same signature) with what the decorator returns. The syntax consists of adding @ and the decorator’s name right before our function definition:

	@awesome_decorator
	def my_function(agr1, agr2):
	    return arg1 + arg2
    
The above snippet is the same as saying:

	def my_function(arg1, arg2):
	    # logic
	my_function = awesome_decorator(my_function)

This has some obvious advantages. The decorator can be used on any number of functions it is compatible with, from the point of view of the signature of the argument function it works with, and it can extend the functionality of existing functions without modifying them. A common use case for decorators is performing validations. Let’s assume that we want to write functions that make some sort of operations on numbers, but we have to make sure that the numbers are positive. We can write a decorator to validate our arguments. Let’s create our own example and investigate:

**image5**
custom made decorator

We mentioned that a decorator has to return a function (to be replaced with the one we decorate). Hence, inside our decorator function, we have to create an inner function and return that. The inner function mimics the functions that we want to decorate in the future: this is why it is defined generically with **"*args"** and **"(double asterisk)kwargs"**. We check to see if any of the unnamed arguments is below zero and raise an exception if any are. We then call the func function that the decorator got as argument, let it compute what it has to compute and return the result of that (just like it would do). We have successfully created our own decorator!
A decorator in Python can also be a class. In order to achieve that, we will pass the function to be decorated in **__init__** and we will also have to implement a special method, **__call__**. The call special method allows us to call the object of the class as we would call a function. Let’s refactor what we have above:

**image6**
using a class as a decorator

##Generators
We talked above about lazy evaluation, where we don’t compute the results right away, but when needed. That is exactly what a generator is and, if you have been using the range() function, you have been using them all along. We can create our own generators by writing functions that use the yield keyword instead of return. Return will fetch something, give it back to us and exit the function. With yield we can create a sequence and then we iterate over it when we need to. Yield does not stop the execution of the function, we can have logic after it too and it ‘remembers’ its previous value. Let’s take a look by implementing our own range, that will give us squares of the numbers we pass as arguments:

	def squares(a, b):
	    i = a
	    while i < b:
		yield i**2
		i += 1

Of course, we can use **for** to iterate, just like any other sequence we have seen before, or we can use the **next()** function to access the next element in our sequence, after we bind it to a variable. This is similar to the **.next()** special iterator method we have in Java. Try running the following snippets:

	for num in squares(5, 10):
	    print(num)
	sequene = squares(5, 10
	print(next(sequene))
	print(next(sequene))
