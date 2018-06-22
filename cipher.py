plaintext = raw_input('Enter a lowercase only message to be encoded:  ')
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = int(raw_input('Enter an interger between 1-26:  '))
cipher = ''

for c in plaintext:
    if c in alphabet: 
        cipher += alphabet[(alphabet.index(c)+key)%(len(alphabet))]
    else:
        cipher = cipher + c
print('Your encrypted message is:' + cipher)

