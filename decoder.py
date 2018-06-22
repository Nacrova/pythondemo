plaintext = raw_input('Enter a lowercase only message to be decoded:  ')
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = int(raw_input('Enter the key used:  '))
cipher = ''

for c in plaintext:
    if c in alphabet: 
        cipher += alphabet[(alphabet.index(c)-key)%(len(alphabet))]
    else:
        cipher = cipher + c
print('Your decrypted message is:' + cipher)