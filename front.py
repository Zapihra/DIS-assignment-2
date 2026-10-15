import postgresConnect as postgre

def main():
    loop = True
    while(loop == True):
        print("Welcome to the assignment 2 code")
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
            print("1) postgres")
            print("2) mongodb")
            #

            print("Which database do you want to read from? ")

            choise2 = int(input())

            if (choise2 == 1):
                postgre.postgreConnection()


        elif(choise == 2):
            print("1) postgres")
            print("2) mongodb")
            #

            print("Which database do you want to write to? ")
            choise2 = int(input())


        elif(choise == 3):
            print("1) postgres")
            print("2) mongodb")
            #

            print("Which database do you want to modify? ")
            choise2 = int(input())
main()