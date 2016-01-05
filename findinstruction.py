from immlib import *
def main(args):
	imm=Debugger()
	search_code="".join(args)
	search_bytes=imm.assemble(search_code)
	search_results=imm.search(search_bytes)
	for hit in search_results:
		code_page=imm.getMemoryPageByAddress(hit)
		access=code_page.getAccess(human=True)
		if "execute" in access.lower():
			imm.log("[*]found:%s (0x%08x)" % (search_code,hit),address=hit)
	return "[*]finished searching for instructions,check the Log window."