print("You are fighting a Giant bat!")
   
move = raw_input("Please make your move:")
if move == "attack":
    print("You hit the bat and it screeches loudly, but does next to nothing but hurt your ears.")
if move == "block":
    print("You try to block the bat's bite, but to no effect. You bleed out hours later.")
if move == "counter":
    print("You counter the bat's attack, but the sheer size of the bat knocks you down.")
if move == "run":
    print("You ran like a coward, but you lived.")
else:
    print("Please type attack,block,counter,or run")