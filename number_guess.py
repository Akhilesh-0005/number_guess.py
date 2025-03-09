import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    guesses=guesses+1
    a=int(input("Enter your guess (1,100) : "))
    if(a>n):
        print("Wrong Guess (Hint : Enter a lower number)")
    elif(a<n):
        print("Wrong Guess (Hint : Enter a bigger number)")
print(f"You have guessed the number {n} in {guesses} attempts")
