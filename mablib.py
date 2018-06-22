print("""Welcome to Mablibs
You will be asked for different nouns and verbs, try and keep them funny.""")

plural_noun = raw_input("Please provide a plural noun:")
noun1 = raw_input("Please provide a noun:")
noun2 = raw_input("Please provide a second noun:")
song = raw_input("Please provide the title of a song:")
verb = raw_input("Please provide a verb:")

madlibs = ("""Learning to drive is a tricky process. There are a few rules to follow. 
1. Keep two %s on the sterring wheel at all times. 
2. Step on the %s to speed up and the %s to slow down. 
3. Your parents will just LOVE you if you play %s on the radio. 
4. Make sure to stop when you see %s stop on a street sign.""")

print (madlibs %(plural_noun,noun1,noun2,song,verb))