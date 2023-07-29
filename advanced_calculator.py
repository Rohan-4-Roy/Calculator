from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):



	def __init__(self):
		
		SimpleCalculator.__init__(self)
		self.l1=[]


	def evaluate_expression(self, input_expression):
		s=input_expression
		s.strip()
		w=""
		for i in range(len(s)):
			if str(s[i]).isnumeric or s[i]==" ":
				w=w+s[i]
			else:
				try:
					int(w)
				except:
					return "Error"
			

		try:
			L=self.tokenize(input_expression)
			
		
			res=self.evaluate_list_tokens(L)
		
			
			self.l1.insert(0,(input_expression,res))
			return res
		except:
			return "Error"
		


	def infixToPostfix(self,exp): 
		op = set(['+', '-', '*', '/', '(', ')'])  
		pri = {'+':1, '-':1, '*':2, '/':2}
		stck = []
		out = [] 
		for e in exp:
			if e=="{":
				e="("
			elif e=="}":
				e=")"
			if e not in op:
				out.append(e)
			elif e=='(':
				stck.append('(')
			elif e==')':

				while stck and stck[-1]!= '(':
					out.append(stck.pop())
				stck.pop()
			else: 

				while stck and stck[-1]!='(' and pri[e]<=pri[stck[-1]]:
					out.append(stck.pop())
				stck.append(e)
		while stck:
			out.append(stck.pop())
		return out

    		
		
	def tokenize(self, input_expression):
		
		l=[]
		
		s=input_expression
		n=len(s)
		w=""
		for i in range(n):
			if s[i] in ["1","2","3","4","5","6","7","8","9","0"]:
				w+=s[i]
			elif s[i]==" ":
				if len(w)!=0:
					l.append(int(w))
					w=""
			else:
				if len(w)!=0:
					l.append(int(w))
					w=""
				l.append(s[i])
		if len(w)!=0:
			l.append(int(w))


		return l


	def check_brackets(self, list_tokens):
			st=Stack()
			for e in list_tokens:
				if e=='(' or e==")" or e=="{" or e=="}":
					st.push(e)
			parent=0
			curly=0
			for e in list_tokens:
				if e=='(' or e==")" or e=="{" or e=="}":
					if e=="(":
						parent+=1
					elif e==")" :
						if parent==0:
							return False
						else:
							parent-=1
					if e=="{":
						if parent>0:
							return False
						curly+=1
					if e=="}":
						if curly==0:
							return False
						else:
							curly-=1
			if parent!=0 or curly!=0:
				return False
			return True


	def evaluate_list_tokens(self, list_tokens):
		if self.check_brackets(list_tokens)==False:
			return "Error"
		
		op=['+','-','*','/','(',')','{','}']
		
		for i in range(0,len(list_tokens)-1):
			if str(list_tokens[i]).isnumeric() and list_tokens[i+1] in "{(":
				return "Error"
			if str(list_tokens[i+1]).isnumeric() and list_tokens[i] in "})":
				return "Error"
			
		for e in list_tokens:
			if e not in op:
				try:
					x=int(e)
				except:
					return "Error"
		l=self.infixToPostfix(list_tokens)
		#print(l)
		st=[]
		for e in l:
			if e not in op:
				st.append(e)
			
			if e in op:
				
				first=st.pop()
				
				sec=st.pop()
				
				
				if e=='+':
					res=float(sec + first)
				if e=='-':
					res=float(sec-first)
				if e=='*':
					res=float(sec *first)
				if e=='/':
					if first==0:
						return "Error"
					res=float(sec/first)
					
				st.append(res)
		res=st.pop()
		return res


	def get_history(self):
		return self.l1
	
'''
if __name__ == "__main__":
	calc=AdvancedCalculator()
	res = calc.evaluate_expression("5(3+3)")
	print(res)
'''	