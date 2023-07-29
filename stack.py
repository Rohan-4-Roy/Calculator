class Stack:
	def __init__(self):
		self.stck=[]
	
	def push(self, item):
		
		self.stck.insert(0,item)

	def peek(self):
		if self.stck==[]:
			return "Error"
		return self.stck[0]
	
	def pop(self):
		n=len(self.stck)
		x=self.stck[0]
		self.stck=self.stck[1:n]
		return x
		

	def is_empty(self):
		return self.stck==[]

	def __str__(self):
		s=""
		for e in range(len(self.stck)):
			if e==len(self.stck)-1:
				s+=str(self.stck[e])
			else:
				s=s+ (str(self.stck[e]) +" ")
		return s

	def __len__(self):
		return len(self.stck)
'''if __name__ == "__main__":
	st=Stack()
	st = Stack()
	st.push(" ")
	st.push('  ')
	print(st.stck)'''

