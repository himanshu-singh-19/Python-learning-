# # a = "18"
# # b = 12
# # print(a + b)




# # a = "18"
# # b = "12"
# # print(a + b)




# # age = input("Enter a age: ")

# # age = int(age)

# # if age < 18:
# #     print("The age is can't vote")
# # else:
# #     print("The age is eligible to vote")
# #     for i in range(4):
# #         print("Himanshu")


# #Veena@3091
# #multiline string not possible with "" or ''
# name = "pranay himanshu"

# '''
# Fruits
#     banana
#     apple
#         green apple
#         red apple

# # Vegetables
# #     ladij finger
# #     bangan


# # '''






# # # #https://www.crazygames.com/game/racing-limits?czy_invite=true&utm_source=invite&ROOMID=1306096

# # # num1 = int(input("Enter first number: "))
# # # num2 = int(input("Enter second number: "))



# # # print("1. Add")
# # # print("2. Subtract")
# # # print("3. Multiply")
# # # print("4. Divide")

# # # choice = input("Choose 1, 2, 3, or 4: ")

# # # if choice == "1":
# # #     print("Answer:", num1 + num2)

# # # elifsecret_number choice == "2":
# # #     print("Answer:", num1 - num2)

# # # elif choice == "3":
# # #     print("Answer:", num1 * num2)

# # # elif choice == "4":
# # #     print("Answer:", num1 / num2)

# # secret_number = 7


# # guess = int(input("Guess a number between 1 and 10: "))

# # if guess == secret_number:
# #     print("Correct! You won!")
# # else:
# #     print("Wrong! Try again later.")

secret_number = 7
import random
# secret_number = random.randint(1, 10)

# count = 0
# while True:
#     count = count + 1 # count = 1 + 1 = 2
#     guess = int(input("Guess a number between 1 and 10: ")) # 8

#     if guess == secret_number : # 8 == 7
#         print("🎉 Correct! You won!" )
#         print (f" You took {count} attempts")
#        # print (" You took" + guess +" attempts")
#         break

#     elif guess > secret_number: # 8 > 7
#         print("Too high!")

#     elif guess < secret_number:
#          print("Too low!")
 
count = 1
while True:
    print (f" Attempt number:  {count}")
    guess = int(input("Guess a number between 1 and 10: ")) # 7

    if guess == secret_number : # 7 == 7
        print("🎉 Correct! You won!" )
        print (f" You took {count} attempts") # 1
        break

    elif guess > secret_number: # 8 > 7
        print("Too high!")

    elif guess < secret_number:
        print("Too low!")
    
    # continue

    count = count + 1 # count = 1 + 1 = 2
 









