#LAB - PIG

import random

#1. One Automated Turn of Pig
def holdAt20(limit=20):
    turnTotal = 0
    while turnTotal < limit:
        roll = random.randint(1,6)
        #print("Roll: ", roll)
        if roll == 1:
            turnTotal = 0
            #print("Turn Total: ", turnTotal)
            return turnTotal
        else:
            turnTotal += roll
    #print("Turn Total: ", turnTotal)
    return turnTotal


#2. Hold-at-20 Outcomes
def holdAt20outcomes(trials):
    outcomes = {0:0}
    for val in range(20,26):
        outcomes[val] = 0
    for x in range(trials):
        score = holdAt20()
        outcomes[score] += 1

    for score in outcomes:
        print(score, outcomes[score]/trials)


#3. Hold-at-X Outcomes
def holdAtXoutcomes(trials, limit):
    outcomes = {0:0}
    for val in range(limit,limit+6):
        outcomes[val] = 0
    for x in range(trials):
        score = holdAt20(limit)
        outcomes[score] += 1

    for score in outcomes:
        print(score, outcomes[score]/trials)


#4. Hold-at-20-or-Goal Turn
def holdAt20orGoal(score):
    turnTotal = 0
    while turnTotal < 20:
        roll = random.randint(1,6)
        print("Roll: ", roll)
        if roll == 1:
            turnTotal = 0
            print("Turn Total: ", (score + turnTotal))
            return (score + turnTotal)
        else:
            turnTotal += roll
            if (turnTotal + score) >= 100:  
                pass
    print("Turn Total: ", (score +turnTotal))
    return (score + turnTotal)


#5. Hold-at-20-or-Goal Game
def holdAt20_Or_GoalGame():
    total = 0
    score = 0
    while total < 20 or score < 100:
        roll = random.randint(1,6)
        print("Roll:", roll)
        total = total + roll
        if roll == 1:
            total = 0
            print('Turn total:', total)
            print('New score:', score)
        elif total > 20:
            score = score + total
            print('Turn total:', total)
            print('New score:', score)

#6. Average Pig Turns

#7. Two-Player Pig
def twoPlayerPig():
    turnCount = 0
    playerOneScore = 0
    playerTwoScore = 0
    print("Player 1 score: 0")
    print("Player 2 score: 0")
    while playerOneScore < 100 and playerTwoScore < 100:
        dice = 0
        playerOneTotal = 0
        playerTwoTotal = 0
        print("It is player 1's turn")
        while dice != 1 and playerOneTotal < 20:
            dice = random.randint(1,6)
            print("Roll:", dice)
            if dice != 1:
                playerOneTotal += dice
            else:
                total = 0
                break
        print("Player 1 turn total:", playerOneTotal)
        playerOneScore += playerOneTotal
        print("Player 1 score total:", playerOneScore)
        dice = 0
        print("It is player 2's turn")
        while dice != 1 and playerTwoTotal < 20:
            dice = random.randint(1,6)
            print("Roll:", dice)
            if dice != 1:
                playerTwoTotal += dice
            else:
                playerTwoTotal = 0
                break
        print("Player 2 turn total:", playerTwoTotal)
        playerTwoScore += playerTwoTotal
        print("Player 2 score total:", playerTwoScore)

#8. Pig Game
def game():
    turnCount = 0
    playerOneScore = 0
    playerTwoScore = 0
    
    
    pick = random.randint(1,2)

    if pick == 1:
        print("You will be player 1.")
        print("Player 1 score: 0")
        print("Player 2 score: 0")
        while playerOneScore < 100 and playerTwoScore < 100:
            if playerOneScore >= 100 or playerTwoScore >= 100:
                break
            dice = 0
            playerOneTotal = 0
            playerTwoTotal = 0
            
            #YOU
            print("It is player 1's turn")
            ask = input("Enter nothing to roll; enter anything to hold. ")

            while ask == "":
                dice = random.randint(1,6)
                print("Roll:", dice)
                if dice != 1 and playerOneTotal < 20:
                    ask = input("Enter nothing to roll; enter anything to hold. ")
                    playerOneTotal += dice
                else:
                    playerOneTotal = 0
                    break
            print("Turn total:", playerOneTotal)
            playerOneScore += playerOneTotal
            print("New score:", playerOneScore)
            if playerOneScore >= 100:
                print("The computer wins!")
            elif playerTwoScore >= 100:
                print("You win!")
        

            #COMPUTER
            dice = 0
            print("It is player 2's turn")
            while dice != 1 and playerTwoTotal < 20:
                dice = random.randint(1,6)
                print("Roll:", dice)
                if dice != 1:
                    playerTwoTotal += dice
                else:
                    playerTwoTotal = 0
                    break
            print("Turn total:", playerTwoTotal)
            playerTwoScore += playerTwoTotal
            print("New score:", playerTwoScore)
        if playerOneScore >= 100:
            print("You win!")
        elif playerTwoScore >= 100:
            print("The computer wins!")

    else:
        print("You will be player 2.")
        print("Player 1 score: 0")
        print("Player 2 score: 0")
        while playerOneScore < 100 and playerTwoScore < 100:
            if playerOneScore >= 100 or playerTwoScore >= 100:
                break
            dice = 0
            playerOneTotal = 0
            playerTwoTotal = 0
            #YOU
            print("It is player 1's turn")
            while dice != 1 and playerOneTotal < 20:
                dice = random.randint(1,6)
                print("Roll:", dice)
                if dice != 1:
                    playerOneTotal += dice
                else:
                    playerOneTotal = 0
                    break
            print("Turn total:", playerOneTotal)
            playerOneScore += playerOneTotal
            print("New score:", playerOneScore)
        

            #COMPUTER
            dice = 0
            print("It is player 2's turn")
            ask = input("Enter nothing to roll; enter anything to hold. ")

            while ask == "":
                dice = random.randint(1,6)
                print("Roll:", dice)
                if dice != 1 and playerTwoTotal < 20:
                    ask = input("Enter nothing to roll; enter anything to hold. ")
                    playerTwoTotal += dice
                else:
                    playerTwoTotal = 0
                    break
            print("Turn total:", playerTwoTotal)
            playerTwoScore += playerTwoTotal
            print("New score:", playerTwoScore)
        if playerOneScore >= 100:
            print("The computer wins!")
        elif playerTwoScore >= 100:
            print("You win!")

game()
#twoPlayerPig()         
#holdAt20_Or_GoalGame()
#holdAt20orGoal(int(input('Score?: ')))            
#holdAtXoutcomes(100, 50)
#x = holdAt20()
#print(x)
#holdAt20outcomes(100)

