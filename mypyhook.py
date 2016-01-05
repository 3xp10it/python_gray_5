from immlib import *
class MyHook(LopBpHook):
	def __init__(self):
		LogBpHook.__init__(self)
	def run(regs):
		regs("ESP")