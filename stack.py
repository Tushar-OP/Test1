class Stack():
	
	
	def __init__(self, limit=10):
		self.stack=[]
		self.limit=limit
		
	def __str__(self):
		return str(self.stack)
		
	def __bool__(self):
		return not bool(self.stack)
	
	def push(self, val):
		if len(self.stack) >= self.limit:
			return "Full"
		self.stack.append(val)
	
	def pop(self, val):
		if len(self.stack) == self.limit:
			return self.stack.pop()
		else:
			return "nothing"
			
	def peep(self, val):
		if len(self.stack) == self.limit:
			return self.stack[-1]
		
if __name__ == '__main__':
	stack=Stack()
	for i in range(10):
		stack.push(i)
		
print("Stack: " + str(stack))

		
