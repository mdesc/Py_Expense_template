from PyInquirer import prompt
import csv
from expense import users

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)

    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(infos.values())

    #to dynamicaly add the new user to the displayed name when creating an new expense 
    users.append(infos['name'])

    print("User Added !")

    return True