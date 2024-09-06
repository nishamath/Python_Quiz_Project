print("""
WELCOME TO ABC QUIZ PROGRAMME
""")
q1=q2=q3=q4=q5=5
Total_Marks=0
a=input("Can we start the quiz   y/n").upper()
if a=="Y":
    print("Here is your First question")
    q1=input("What is the keyword for defining a function").upper()
    if q1=="DEF":
        print("You are rewarded 5 scores")
        Total_Marks+=5

    else:
        print('Wrong, Your are rewarded 0 pints')

    b=input("Do you want to continue  y/n ")
    if b=="y":
        print("Here is your next question")


        q2= input('What data type is this {"name": "John"} in Python').upper()
        if q2=="DICTIONARY":
            print("You are rewarded 5 scores")
            Total_Marks += 5
        else:
            print('Wrong, Your are rewarded 0 pints')
        b = input("Do you want to continue  y/n ").upper()
        if b == "Y":
            print("Here is your next question")


            q3=input("What data type is a decimal number").upper()
            if q3 == "FLOAT":
                print("You are rewarded 5 scores")
                Total_Marks += 5
            else:
                print('Wrong, Your are rewarded 0 points')
            b = input("Do you want to continue  y/n ").upper()
            if b == "Y":
                print("Here is your next question")


                q4 = input("What is the syntax for a Python comment").upper()
                if q4 == "#":
                    print("You are rewarded 5 scores")
                    Total_Marks += 5
                else:
                    print('Wrong, Your are rewarded 0 points')

                b = input("Do you want to continue  y/n ").upper()
                if b == "Y":
                    print("Here is your next question")

                    q5 = input("What is the keyword for conditional statements").upper()
                    if q5 == "IF":
                        print("You are rewarded 5 scores")
                        Total_Marks += 5

                        b = input("You have completed all the questions ")
                        # print("Your total rewarded point is", Total_Marks)


                    else:
                        print('Wrong, Your are rewarded 0 points')

                else:
                    print("Thank you")
            else:
                print("Thank you")

        else:
                print('Thank you')
    else:
        print("thank you")


print("Final Total Marks:", Total_Marks)

