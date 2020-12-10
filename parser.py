import ply.yacc as yacc
from lexer import tokens

class yyltype:
    def __init__(self, fl, fc, ll, lc, text):
    	self.first_line = fl
    	self.first_column = fc
    	self.last_line = ll
    	self.last_column = lc
    	self.text = text

class Node(object):
	def __init__(self, loc):
		self.location = loc
		self.parent = None

	def __init__(self):
		self.location = None
		self.parent = None

	def getLocation():
		return self.location

	def setParent(p):
		self.parent = p

	def getParent():
		return self.parent

	def print(indentlevel, label):
		if indentlevel == 0:
	        print(GetPrintNameForNode())
	    else:
	        for i in range(indentlevel - 1):
	            print("|   ")
	        print("+==> " + GetPrintNameForNode())
	    PrintChildren(indentlevel)

class Program(Node):
	def __init__(self, bodylist):
		self.funcbodylist = bodylist

	def getPrintName():
		return "Program"

	def printChildren(indentlevel):
		print();
	    funcbodylist.PrintAll(indentlevel+1)
	    print();

class FuncBody(Node):
	def __init__(self, ss, n):
		self.stmts = ss
		ss.setParentAll(self)
		self.name = n
		self.numArgs = -1
		self.type = None

	def getPrintName():
		return "FuncBody"

	def printChildren(indentlevel):
		print(name);
    	stmts.PrintAll(indentlevel+1)

    def setTypes(types, regs, rtype):
    	self.numArgs = len(types)
    	self.types = types
    	self.regs = regs
    	self.retType = rtype

class Stmt(Node):
	def __init__(self):
		super()

	def __init__(self, loc):
		super(loc)

class Note(Stmt):
	def __init__(self):
		super()

	def __init__(self, loc):
		super(loc)

	def getPrintName():
		return "Note"

	def printChildren(indentlevel):
		print()

class Barrier(Stmt):
	def __init__(self):
		super()

	def __init__(self, loc):
		super(loc)

	def getPrintName():
		return "Barrier"

	def printChildren(indentlevel):
		print()

class CodeLabel(Stmt):
	def __init__(self, lno):
		self.labelno = lno

	def getPrintName():
		return "CodeLabel"

	def printChildren(indentlevel):
		print()

class Integer(Node):
	def __init__(self, val):
		self.value = val

	def getPrintName():
		return "Integer"

	def printChildren(indentlevel):
		print(self.value)

class Insn(Stmt):
	def __init__(self, cmd):
		self.maincmd = cmd
		if self.maincmd:
			self.maincmd.setParent(self)

	def getPrintName():
		return "Insn"

	def printChildren(indentlevel):
		print();
	    if maincmd:
	        maincmd.Print(indentlevel+1)

class MainCmd(Node):
	def __init__(self):
		super()

	def __init__(self, loc):
		super(loc)

class PlainCmd(MainCmd):
	def __init__(self):
		super()

	def __init__(self, loc):
		super(loc)

class ParallelCmd(MainCmd):
	def __init__(self, cmds):
		self.cs = cmds
		self.cs.setParentAll(self)

	def getPrintName():
		return "ParallelCmd"

	def printChildren(indentlevel):
		print();
 	    self.cs.PrintAll(indentlevel+1);

class ClobberCmd(PlainCmd):
	def __init__(self):
		super()

	def __init__(self, loc):
		super(loc)

	def getPrintName():
		return "ClobberCmd"

	def printChildren(indentlevel):
		print()

class SetCmd(PlainCmd):
	def __init__(self, op1, op2):
		self.op1 = op1
		self.op2 = op2
		op1.setParent(self)
		op2.setParent(self)

	def getPrintName():
		return "SetCmd"

	def printChildren(indentlevel):
		print();
	    op1.Print(indentlevel+1)
	    op2.Print(indentlevel+1)

class UseCmd(PlainCmd):
	def __init__(self):
		super()

	def __init__(self, loc):
		super(loc)

	def getPrintName():
		return "UseCmd"

	def printChildren(indentlevel):
		print()

class Operand(Node):
	def __init__(self):
		super()

	def __init__(self, loc):
		super(loc)

class IntOperand(Operand):
	def __init__(self, iv):
		self.value = iv

	def getPrintName():
		return "IntOperand"

	def printChildren(indentlevel):
		print()

class ExprOperand(Operand):
	def __init__(self, li, ti, e):
		self.linfo = li
		self.tinfo = ti
		self.expr = e
		if linfo:
			linfo.setParent(self)
		if tinfo:
			tinfo.setParent(self)
		expr.setParent(self)

	def getPrintName():
		return "ExprOperand"

	def printChildren(indentlevel):
		print()
	    if linfo:
	        linfo.Print(indentlevel+1)
	    if tinfo:
	        tinfo.Print(indentlevel+1)
	    expr.Print(indentlevel+1)

class ExtendOperand(Operand):
	def __init__(self, ti, o):
		self.tinfo = ti
		self.op = o
		tinfo.setParent(self)
		op.setParent(self)

	def getPrintName():
		return "ExtendOperand"

	def printChildren(indentlevel):
		print()
	    tinfo.Print(indentlevel+1)
	    op.Print(indentlevel+1)

class DerefOperand(Operand):
	def __init__(self, li, ti, o):
		self.linfo = li
		self.tinfo = ti
		self.o = o
		linfo.setParent(self)
		tinfo.setParent(self)
		o.setParent(self)

	def getPrintName():
		return "DerefOperand"

	def printChildren(indentlevel):
		print()
	    linfo.Print(indentlevel+1)
	    tinfo.Print(indentlevel+1)
	    op.Print(indentlevel+1)