"""Init module utils"""

const NEO = 'c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b'
const GAS = '602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7'



def Main(operation, args):
	
	"""
	Main definition of the smart contract
	
	:param operation: the operation to be performed
	:type operation: str
	
	:param args: list of arguments.
		args[0] is always developer address 	
		args[1] is always amount for tip
		args[2] is the address of the player
		args[3] gameID for cross reference
	:param type: str
	
	:return:
		bytearray: The result of the operation
	"""
	
	if operation == 'tip':
		NEOBalance = nos.getBalance(NEO,args[2])
		GASBalance = nos.getBalance(GAS, args[2])

		if NEOBalance >= args[1]:
			if GASBalance != 0:
				nos.send
				canPlay = [args[2],True]
				return canPlay
		
		canPlay = False
		return canPlay
