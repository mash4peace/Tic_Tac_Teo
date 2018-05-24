#This program is a simple movie program , and it allows the user to add a movie , delete a movie , and see list of movies in the shelf.
def display_menue():
    print("Command Menu")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()


def add(movies_list):
    movie = input("Name of the movie: ")
    movies_list.append(movie)
    print(movie + " was added.\n")
def list(movieList):
    i =1
    for movie in movieList:
        print(str(i)+ "."+ movie)
        i +=1


def delete(movies_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movies_list):
        print('Invalid movie number\n')
    else:
        movie = movies_list.pop(number -1)
        print(movie + " was deleted \n")


def main():
    movies_list = ["Monty Python and the Holy Grill",
                   "On the waterfront",
                   "Cat on a Hot Tin Roof"]

    display_menue()
    while True:
        command = input("Command: ")
        if command.lower()== 'list':
            list(movies_list)
        elif command.lower()== "add":
            add(movies_list)
        elif command.lower()== "del":
            delete(movies_list)
        elif command.lower()== "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!!!")
main()