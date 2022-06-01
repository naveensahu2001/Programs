# Python program to reverse a string using stack
def createStack():
	stack=[]
	return stack

def size(stack):
	return len(stack)


def isEmpty(stack):
	if size(stack) == 0:
		return true


def push(stack,item):
	stack.append(item)


def pop(stack):
	if isEmpty(stack): return
	return stack.pop()


def reversing(string):
	n = len(string)
	
	stack = createStack()

	for i in range(0,n,1):
		push(stack,string[i])

	string=""

	for i in range(0,n,1):
		string+=pop(stack)
		
	return string
	

string=input()
string = reversing(string)
print(string)
