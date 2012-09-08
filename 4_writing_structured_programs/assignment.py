def change_reference():
	print "#" * 10 + "Change Reference Demo" + "#" * 10 +"\n"
	foo = "change"
	bar = "reference"
	print "foo = %s , bar = %s" %(foo,bar)
	foo = "yes, do it"
	print "after assign another reference to foo.."
	print "foo = %s , bar = %s" %(foo,bar)
	print "foo changes but bar doesn't change"
	print
def change_internally():
	print "#" * 10 + "Demo: Change the Content Reference refers to " + "#" * 10 +"\n"
	foo = ["change" , "reference"]
	bar = foo
	print "foo = %s, bar = %s" %(repr(foo) , repr(bar))
	print "change the 1st item in the list to 'modify'"
	foo[0] = "modify"
	print "foo = %s, bar = %s" %(repr(foo) , repr(bar))
	print "this is internal change"
	print 

def nested_list_demo():
	print "#" * 10  + "nested list example" + "#" * 10 
	inner_list = []
	nested = [inner_list , inner_list , inner_list ,]
	print """
	executing....
	inner_list = []
	nested = [inner_list , inner_list , inner_list ,]
	"""
	print "the initial state of var nested: %s" %repr(nested)
	nested[1].append("I am the fashion, you copy me!")
	print "after changing the content of the first item(not the reference, NOTICE), it becomes: %s" %repr(nested)
	for item in nested:
		print "the id of %d th item is %s" %(nested.index(item),id(item))
	print

def another_nested_list_demo():
	print  "#" * 10 + "another nested list example" + "#" * 10 
	nested = [[]] * 3
	print """
	executing...
	nested = [[]] * 3
	"""
	print "the initial state of var nested: %s" %repr(nested)
	nested[1].append("I am the fashion, you copy me!")
	print "after changing the content of the first item(not the reference, NOTICE), it becomes: %s" %repr(nested)
	for item in nested:
		print "the id of %d th item is %s" %(nested.index(item),id(item))
					
	print "Notice: the reference of the first item (a list)in the list is copied, not the content inside it"
	print "So, out of no surprise, the three items change together"
	print "and changing the reference of the second item"
	nested[1] = "I don't want to follow you, I have my own style"
	print "nested becomes: %s" %repr(nested)
	print

def shallow_and_deep_copy():
	print  "#" * 10 + "shallow and deep copy example" + "#" * 10 
	import copy
	print """
	performing shallow copy
	inner_list = []
	foo = [inner_list]
	bar = copy.copy(foo)
	"""
	inner_list = []
	foo = [inner_list]
	bar = copy.copy(foo)
	print "the first element of both foo and bar are referring to the same thing, inner_list"
	foo[0].append("Yes, it is!")
	print "modify foo's first item"
	print "foo and bar becomes %s , %s" %(repr(foo) , repr(bar))
	print "foo and bar's common item changes, this is shallow copy!"

	print "next comes to deep copy...."
	inner_list = []
	foo = [inner_list]
	bar = copy.deepcopy(foo)
	print """
	performing shallow copy
	inner_list = []
	foo = [inner_list]
	bar = copy.deepcopy(foo) #notice here!
	"""
	foo[0].append("I am alone")
	print "modify foo's first item"
	print "foo and bar becomes %s , %s" %(repr(foo) , repr(bar))
	print "as you can see, foo changes while bar stays the same"
change_reference()
change_internally()
nested_list_demo()
another_nested_list_demo()
shallow_and_deep_copy()
