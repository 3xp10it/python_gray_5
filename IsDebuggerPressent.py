one:


from immlib import *
imm=Debugger()
imm.writeMemory(imm.getPEBAddress()+0x2,"\x00")

input above codes to python shell offered by immunity debugger



----------------------------------------------------------------
two:

from immlib import * 
process32first=imm.getAddress("kernel32.Process32FirstW")
process32next=imm.getAddress("kernel32.Process32NextW")
function_list=[process32first,process32next]
patch_bytes=imm.Assemble("SUB EAX,EAX\nRET")
for address in function_list:
	opcode=imm.disasmForward(address,nlines=10)
	imm.writeMemory(opcode.address,patch_bytes)
