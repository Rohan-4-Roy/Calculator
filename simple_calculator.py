from stack import Stack

class SimpleCalculator:
	def __init__(self):
		
		self.l=[]
	
	def is_operator(self,ch):
		if  ch in ['+','-','/','*']:
			return True
		return False


	def evaluate_expression(self, e):
		s=1
		s1=1
		res="#"
		x1=""
		op2=False
		op=""
		x2=""
		for i in e:
			if x2!="" and self.is_operator(i)==True:
				res="Error"
			
			if self.is_operator(i)==False and op2==False:
				x1=x1+i
				continue
			if self.is_operator(i)==True and x1!="":
				op2=True
				if op!="":
					if (op=='+' or op=='-') and (i=='*'or i=='/'):
						res="Error"
						continue
					elif (op=='*' or op=='/') and (i=='*'or i=='/'):
						res="Error"
						continue
					elif i=='-':
						s1=-1
						continue
					elif i=='+':
						s1=1
						continue

				op=i
				continue
			if self.is_operator(i)==False and op2==True:
				x2=x2+i
				continue
			if self.is_operator(i)==True and x1=="":
				if i=='-':
					s=-1
				elif i=='+':
					s=1
				else:
					res="Error"
					break
				continue
		c=False
		sp=False
		for i in x1:
			if i==" " and c==True:
				sp=True
			elif c==True and sp==True and ord(i)<=56 and ord(i)>=48:
				res="Error"
			elif ord(i)<=56 and ord(i)>=48:
				c=True
		c=False
		sp=False
		for i in x2:
			if i==" " and c==True:
				sp=True
			elif c==True and sp==True and ord(i)<=56 and ord(i)>=48:
				res="Error"
			elif ord(i)<=56 and ord(i)>=48:
				c=True
		

		if x1=="" or x2=="":
			res="Error"
		if res!="Error":
			x1=float(x1)*s
			x2=float(x2)*s1
		if res!="Error":
			if op=="+" :
				res=x1+x2
			elif op=='-':
				res=x1-x2
			elif op=='*':
				res=x1*x2
			elif op=="/":
				if x2==0:
					res="Error"
				else:
					res=x1/x2
			else:
				res="Error"

		self.l.insert(0,(e,res))
		return res
	

	def get_history(self):
		return self.l
