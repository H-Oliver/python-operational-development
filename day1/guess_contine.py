age_of_oldboy = 56
count = 0
while count < 3:
    guess_age = int(input("guess age :"))
    if guess_age == age_of_oldboy:
        print("Yes,you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("Think smaller...")
    else:
        print("Think bigger!")
    count += 1
    if count == 3:
        countine_confirm = input("do you want to keep guessing...?")
        if countine_confirm != 'n':
            count = 0
'''else:
    print("You have tried too many times...fuck off")'''