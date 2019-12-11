#rock paper and scisors
print("rock...")
print("paper...")
print("scisors...")

player1 = input("player1 make your move: ")
print("***********NO CHEATING\n\n"*40)
player2 = input("player2 make your move: ")
if player1 == "rock" and player2 == "scissor":
    print("player1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins!")
elif player1== "paper" and player2=="rock":
    print("player1 wins")
elif player1 == "paper" and player2=="scissor":
    print("player2 wins!")
elif player1=="scissor" and player2=="paper":
    print("player1 wins!") 
elif player1=="scissor" and player2=="rock":
    print("player2 wins!")      
elif player1==player2:
    print("it's a tie")
else:
    print("something went wrong!")
# so here i'm done!
