# Snake, Water, Gun Game

def gamePlay():
    # keeping track of points - we are considering who reaches 3 points first wins the game
    computerCount = 0
    personCount = 0

    while True:
        # exiting the loop once either of the player reaches 3 points
        if computerCount == 3 or personCount == 3:
            break
        # taking inputs of the moves
        computer = input("Computer - Enter your move: ")
        person = input("Person - Enter your move: ")
        # populating the score
        if((computer.lower() == "snake" and person.lower() == "water") or (computer.lower() == "water" and person.lower() == "snake")):
            if computer.lower() == "snake":
                computerCount += 1
            else:
                personCount += 1
        elif((computer.lower() == "snake" and person.lower() == "gun") or (computer.lower() == "gun" and person.lower() == "snake")):
            if computer.lower() == "gun":
                computerCount += 1
            else:
                personCount += 1
        elif((computer.lower() == "water" and person.lower() == "gun") or (computer.lower() == "gun" and person.lower() == "water")):
            if computer.lower() == "water":
                computerCount += 1
            else:
                personCount += 1
        else:
            pass
        # keeping track of points
        print("Computer: ", computerCount)
        print("Person: ", personCount)

    if(computerCount == 3):
        return "Computer"
    else:
        return "Person"

print("Let the game begin!")
winner = gamePlay()
print("Winner is:", winner)