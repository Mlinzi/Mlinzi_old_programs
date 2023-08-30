def encrypter():
  
	# declaration
	key = int(input("enter cypher(NUMBERS ONLY) "))
  
	code = ""
	# input
	name = input(str("enter a letter "))
	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLOMNOPQRSTUVWXYZ"

  	# logic
	for x in range(len(str(name))):
			if(name[x] in lower) :
				if((ord(name[x]) + key) < 122  ):
					code = code + chr ((ord(name[x]) + key))
				else:
					code = code + chr ((ord(name[x]) - (26 - key)))
					
			else :
				if((ord(name[x]) + key) < 90  ):
					code = code +  chr (ord(name[x]) + key)
				else :
					code = code + chr (ord(name[x]) - (26 - key))
					
	
  
	print(code)

  
  	# output
	
# calls
encrypter()
