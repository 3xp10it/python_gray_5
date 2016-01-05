from immlib import *
def main(args):
	imm=Debugger()
	address=int(args[0],16)
	shellcode="<<copy my shellcode here,from metasploit or my own exploit_code>>"
	shellcode_length=len(shellcode)
	debug_shellcode=imm.readMemory(address,shellcode_length)
	debug_shellcode=debug_shellcode.encode("HEX")
	imm.log("address:0x%08x" % address)
	imm.log("shellcode length:%d" % shellcode_length)
	imm.log("attack shellcode:%s" % shellcode[:shellcode_length])
	imm.log("in memory shellcode:%s" % debug_shellcode[:shellcode_length])
	count=0 
	while count<shellcode_length:
		if debug_shellcode[count]!=shellcode[count]:
			imm.log("bad char found at offset:%d" % count)
			bad_char_found=True
			break
		count+=1
	if bad_char_found:
		imm.log("[*************]")
		imm.log("bad char found:%s" % debug_shellcode[count])
		imm.log("origin char:%s" % shellcode[count])
		imm.log("[*************]")
	return "[*] !bad char finished,check log window."