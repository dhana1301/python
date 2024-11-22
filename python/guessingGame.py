import random 

random_num = random.randint(1,100) 

print ("Welcome to the Number guessing game") 
print("Can you guess it?") 

while True : 
    print(random_num)
    guess_num = int(input("Enter your guess number: ")) 

    if (guess_num < random_num):
        print("Too Low, Try again!") 
    elif (guess_num > random_num):
        print("Too High, Try again!") 

    else: 
        print("congratulation! you guessed the number")
        break