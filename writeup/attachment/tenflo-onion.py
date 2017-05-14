def caesar(plainText, shift): 
  cipherText = ""
  debut = shift
  for ch in plainText:
    debut = debut - 1
    if ch.isalpha():
      stayInAlphabet = ord(ch) + debut 
      if stayInAlphabet > ord('Z'):
        stayInAlphabet -= 26
      if stayInAlphabet > ord('Z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  print "Your ciphertext is: ", cipherText
  return cipherText
  
for i in range(26):
	caesar("IHTIYYQOT",i)
