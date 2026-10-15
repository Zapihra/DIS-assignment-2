import postgresConnect as postgre
import mongodbConnect as mongo

def main():
    loop = True
    print("Welcome to the assignment 2 code")

    while(loop == True):
        print("What do you want to do?")
        print("1) Read from database")
        print("2) Write to database")
        print("3) Modidy database")
        print("0) exit")
        print("please give the number: ")

        choise = int(input())

        if (choise == 0):
           print("Thanks for using")
           loop = False 

        elif (choise == 1):
            print("1) Owners")
            print("2) Dogs")
            print("3) Cats")

            print("Which database do you want to read from? ")

            choise2 = int(input())

            if (choise2 == 1):
                postgre.postgreRead("owner")

            elif (choise2 == 2):
                mongo.mongodbConnection()

            elif (choise2 == 3):
                postgre.postgreRead("cat")


        elif(choise == 2):
            print("1) Owners")
            print("2) Dogs")
            print("3) Cats")

            print("Which database do you want to write to? ")
            choise2 = int(input())

            if (choise2 == 1):
                name = input("Owner name: ")
                email = input("Email: ")

                postgre.postgreWrite("owner", [name, email])

            elif (choise2 == 2):
                mongo.mongodbConnection()

            elif (choise2 == 3):
                name = input("Cat name: ")
                breed = input("Cat breed: ")
                age = int(input("Cat's age: "))

                postgre.postgreWrite("cat", [name, breed, age])
            

        elif(choise == 3):
            print("1) Owners")
            print("2) Dogs")
            print("3) Cats")

            print("Which database do you want to modify? ")
            choise2 = int(input())

            if (choise2 == 1):
                postgre.postgreRead("owner")

                email = input("What is the email? ")
                
                newName = input("New name: ")
                newEmail = input("New email: ")

                postgre.postgreUpdate("owner", [email, newName, newEmail])

            elif (choise2 == 2):
                mongo.mongodbConnection()

            elif (choise2 == 3):
                postgre.postgreRead("cat")

                name = input("What is the cats name? ")
                age = input("What is the cats age? ")

                newName = input("New name: ")
                newBreed = input("New breed: ")
                newAge = input("New age: ")

                postgre.postgreUpdate("cat", [name, age, newName, newBreed, newAge])
main()