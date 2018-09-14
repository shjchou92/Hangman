import turtle
import random
s = turtle.Screen()

def face():
    shelly = turtle.Turtle(shape = 'turtle')
    shelly.hideturtle()
    shelly.up()
    shelly.goto(50,115)
    shelly.down()
    shelly.circle(60)
    shelly.up()
    shelly.goto(30,185)
    shelly.down()
    shelly.dot(15)
    shelly.up()
    shelly.goto(70,185)
    shelly.down()
    shelly.dot(15)
    shelly.up()
    shelly.goto(15,155)
    shelly.down()
    shelly.setheading(-60)
    shelly.circle(40, 120)
    return

def body():
    shelly = turtle.Turtle(shape = 'turtle')
    shelly.hideturtle()
    shelly.up()
    shelly.goto(50,115)
    shelly.down()
    shelly.setheading(0)
    shelly.right(90)
    shelly.forward(125)
    return

def left():
    shelly = turtle.Turtle(shape = 'turtle')
    shelly.hideturtle()
    shelly.up()
    shelly.goto(50,110)
    shelly.down()
    shelly.setheading(270)
    shelly.right(45)
    shelly.forward(100)
    shelly.backward(100)
    return

def right():
    shelly = turtle.Turtle(shape = 'turtle')
    shelly.hideturtle()
    shelly.up()
    shelly.goto(50,110)
    shelly.down()
    shelly.setheading(270)
    shelly.left(45)
    shelly.forward(100)
    shelly.backward(100)
    return

def l_leg():
    shelly = turtle.Turtle(shape = 'turtle')
    shelly.hideturtle()
    shelly.up()
    shelly.goto(50,-10)
    shelly.down()
    shelly.setheading(270)
    shelly.right(30)
    shelly.forward(150)
    shelly.backward(150)
    return

def r_leg():
    shelly = turtle.Turtle(shape = 'turtle')
    shelly.hideturtle()
    shelly.up()
    shelly.goto(50,-10)
    shelly.down()
    shelly.setheading(270)
    shelly.left(30)
    shelly.forward(150)
    shelly.backward(150)
    shelly.hideturtle()
    return

def death():
    shelly = turtle.Turtle(shape = 'turtle')
    shelly.hideturtle()
    shelly.up()
    shelly.goto(50,175)
    shelly.dot(110,'white')
    shelly.goto(30,185)
    shelly.down()
    shelly.setheading(0)
    shelly.right(45)
    shelly.pensize(3)
    shelly.forward(10)
    shelly.backward(20)
    shelly.up()
    shelly.goto(70,185)
    shelly.down()
    shelly.forward(10)
    shelly.backward(20)
    shelly.forward(10)
    shelly.left(90)
    shelly.forward(10)
    shelly.backward(20)
    shelly.up()
    shelly.goto(30,185)
    shelly.down()
    shelly.forward(10)
    shelly.backward(20)
    shelly.up()
    shelly.goto(85,145)
    shelly.down()
    shelly.setheading(130)
    shelly.circle(40,110)
    return

def hangman():
    play = True
    while(play):
        func = 0
        print("------------------------------------------------------------------------")
        print("Looks like you got into a real mess, you been put to trial to be hanged.")
        print("You must be able to correctly guess the word to save yourself.")
        print("Good Luck.")
        print("------------------------------------------------------------------------")
        infile = open('hangman_words.txt' , 'r')
        file = infile.read()
        wordList = file.split()
        for i in range(0, len(wordList)):
            r = random.randint(0, i)
        word = wordList[r]
        # print(word)
        if len(word) <= 7:
            print('Length of the word: ' + str(len(word)))
            print('Difficulty: easy')
            print('You have six tries to guess a letter!')
        elif len(word) > 7 and len(word) <= 9:
            print('Length of the word: ' + str(len(word)))
            print('Difficulty: Intermediate')
            print('You have six tries to guess a letter!')
        elif len(word) > 9:
            print('Length of the word: ' + str(len(word)))
            print('Difficulty: Challenging')
            print('You have six tries to guess a letter!')
        s.clearscreen()
        shelly = turtle.Turtle(shape = 'turtle')
        shelly.hideturtle()
        shelly.up()
        shelly.goto(-300,-200)
        shelly.down()
        shelly.forward(400)
        shelly.backward(250)
        shelly.left(90)
        shelly.forward(500)
        shelly.right(90)
        shelly.forward(200)
        shelly.right(90)
        shelly.forward(65)
        p_letter = []
        s_list = []
        c = '_,' * len(word)
        plate = c.split(',')
        plate.pop()
        for i in word:
        	p_letter.append(i)
        s1 = input('Enter a letter: ')
        if s1 in p_letter:
            for i in range(len(word)):
                if p_letter[i] == s1:
                    acc = 0
                    acc+=i
                    plate[acc] = s1
            print(' '.join(plate))
            s_list.append(s1)
        elif s1 not in p_letter:
            func += 1
            face()
        s2 = input('Enter a letter: ')
        if s2 in p_letter:
            for i in range(len(word)):
                if p_letter[i] == s2:
                    acc = 0
                    acc+=i
                    plate[acc] = s2
            print(' '.join(plate))
            s_list.append(s2)
        elif s2 not in p_letter:
            func += 1
            if s1 in p_letter:
            	face()
            elif s1 not in p_letter:
            	body()
        s3 = input('Enter a letter: ')
        if s3 in p_letter:
            for i in range(len(word)):
                if p_letter[i] == s3:
                    acc = 0
                    acc+=i
                    plate[acc] = s3
            print(' '.join(plate))
            s_list.append(s3)
        elif s3 not in p_letter:
            func += 1
            if (s1 not in p_letter and s2 in p_letter) or (s1 in p_letter and s2 not in p_letter):
            	body()
            elif s1 and s2 not in p_letter:
            	left()
            elif s1 and s2 in p_letter:
            	face()
        s4 = input('Enter a letter: ')
        if s4 in p_letter:
            for i in range(len(word)):
                if p_letter[i] == s4:
                    acc = 0
                    acc+= i
                    plate[acc] = s4
            print(' '.join(plate))
            s_list.append(s4)
        elif s4 not in p_letter:
            func += 1
            if len(s_list)==2:
            	body()
            elif len(s_list)==1:
            	left()
            elif s1 and s2 and s3 not in p_letter:
            	right()
            elif s1 and s2 and s3 in p_letter:
            	face()
        s5 = input('Enter a letter: ')
        if s5 in p_letter:
            for i in range(len(word)):
                if p_letter[i] == s5:
                    acc = 0
                    acc += i
                    plate[acc] = s5
            print(' '.join(plate))
            s_list.append(s5)
            if plate == p_letter:
                s.clearscreen()
                shelly = turtle.Turtle()
                face()
                body()
                left()
                right()
                l_leg()
                r_leg()
                shelly.hideturtle()
                print('Good job! You saved yourself! :)')
                outcome = "w"
        elif s5 not in p_letter:
            func += 1
            if len(s_list)==3:
            	body()
            elif len(s_list)==2:
            	left()
            elif len(s_list)==1:
            	right()
            elif s1 and s2 and s3 and s4 not in p_letter:
            	l_leg()
            elif s1 and s2 and s3 and s4 in p_letter:
            	face()
        s6 = input('Enter the last letter: ')
        if s6 in p_letter:
            for i in range(len(word)):
                if p_letter[i] == s6:
                    acc = 0
                    acc += i
                    plate[acc] = s6
            print(' '.join(plate))
            if plate == p_letter:
                s.clearscreen()
                shelly = turtle.Turtle()
                face()
                body()
                left()
                right()
                l_leg()
                r_leg()
                shelly.hideturtle()
                print('Good job! You saved yourself! :)')
                outcome = "w"
            else:
                s7 = input('The word is...: ')
                if s7 == word:
                    s.clearscreen()
                    shelly = turtle.Turtle()
                    face()
                    body()
                    left()
                    right()
                    l_leg()
                    r_leg()
                    shelly.hideturtle()
                    print('Good job! You saved yourself! :)')
                    outcome = "w"
                else:
                    if (func == 0):
                        face()
                        body()
                        left()
                        right()
                        l_leg()
                        r_leg()
                        death()
                    elif (func == 1):
                        body()
                        left()
                        right()
                        l_leg()
                        r_leg()
                        death()
                    elif (func == 2):
                        left()
                        right()
                        l_leg()
                        r_leg()
                        death()
                    elif (func == 3):
                        right()
                        l_leg()
                        r_leg()
                        death()
                    elif (func == 4):
                        l_leg()
                        r_leg()
                        death()
                    else:
                        r_leg()
                        death()
                    shelly.hideturtle()
                    print('You died... :(')
                    outcome = "l"
                    print(word)
        elif s6 not in p_letter:
            func += 1
            if len(s_list) == 4:
            	body()
            elif len(s_list) == 3:
            	left()
            elif len(s_list) == 2:
            	right()
            elif len(s_list) == 1:
            	l_leg()
            elif (s1 and s2 and s3 and s4 and s5 not in p_letter):
            	r_leg()
            elif (s1 and s2 and s3 and s4 and s5 in p_letter):
            	face()
            s7 = input('The word is...: ')
            if s7 == word:
                s.clearscreen()
                shelly = turtle.Turtle()
                face()
                body()
                left()
                right()
                l_leg()
                r_leg()
                shelly.hideturtle()
                print('Good job! You saved yourself! :)')
                outcome = "w"
            else:
                if (func == 0):
                    face()
                    body()
                    left()
                    right()
                    l_leg()
                    r_leg()
                    death()
                elif (func == 1):
                    body()
                    left()
                    right()
                    l_leg()
                    r_leg()
                    death()
                elif (func == 2):
                    left()
                    right()
                    l_leg()
                    r_leg()
                    death()
                elif (func == 3):
                    right()
                    l_leg()
                    r_leg()
                    death()
                elif (func == 4):
                    l_leg()
                    r_leg()
                    death()
                elif (func == 5):
                    r_leg()
                    death()
                else:
                    death()
                shelly.hideturtle()
                print('You died... :(')
                outcome = "l"
                print(word)
        infile.close()
        if (outcome == "w"):
            print("Nice, looks like that wasn't hard enough, want a new challenge?")
            prompt = input("Type y or yes to play again, or press enter to exit: ")
            if (prompt == "y" or prompt == "yes"):
                continue
            elif (prompt != "y" or prompt != "yes"):
                play = False
        elif (outcome == "l"):
            print("Ohh too bad.. Was that too difficult? Try it again!")
            prompt = input("Type gg, n, or no if you give up, otherwise press enter to play again: ")
            if (prompt == "gg" or prompt == "n" or prompt == "no"):
                play = False
            elif (prompt != "gg" or prompt != "n" or prompt != "no"):
                continue

hangman()
