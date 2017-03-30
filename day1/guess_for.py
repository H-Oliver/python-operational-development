age_of_oldboy = 56
for i in range(3):
    guess_age = int(input("guess age :"))
    if guess_age == age_of_oldboy:
        print("Yes,you got it.")
        break
    elif guess_age > age_of_oldboy:
        print("Think smaller...")
    else:
        print("Think bigger!")
else:
    print("You have tried too many times...fuck off")