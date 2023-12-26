print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    print("Goodbye!")
    quit()

print("Okey!, Let's play :) ")
score = 0

q1 = input("what does cpu stands for? ")
if q1.lower() == "cpu":
    print('correct!')
    score += 1
else:
    print('Incorrect!')

q1 = input("what does gpu stands for? ")
if q1.lower() == "gpu":
    print('correct!')
    score += 1
else:
    print('Incorrect!')

q1 = input("what does psu stands for? ")
if q1.lower() == "psu":
    print('correct!')
    score += 1
else:
    print('Incorrect!')

q1 = input("what does ppu stands for? ")
if q1.lower() == "ppu":
    print('correct!')
    score += 1
else:
    print('Incorrect!')

print('you got ' + str(score) + ' correct answers!')
print("Awesome")
print('you got ' + str((score/4)*100) + '%.')
print("Awesome")