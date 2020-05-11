#Basic Data Types: Letter Counter App
print("Welcome to the Letter counter App")

#Get user input
name = input("\nWhat is your name: ").title().strip()
print("Hello, " + name + "!")

print("I will count the number of times that a specific letter occurs in a message.")
msg = input("\nEnter a message:  ")
let = input("\nWhich letter would you like to count the occurences of: ")

#Standardize to lower case
msg = msg.lower()
let = let.lower()

#Get the count and display thr results
let_count = msg.count(let)
print("\n" + name + ", Your message has " + str(let_count) + " " + let  + "'s in it.")
