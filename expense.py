from PyInquirer import prompt
import csv

users = []

with open('users.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        users.append(row[0])

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": users,
    },

]


def new_expense(*args):

    infos = prompt(expense_questions)

    involedChoices = []
    spender = infos['spender']

    for user in users:
        if spender == user :
            involedChoices.append({
                'name' : user,
                'checked': 'true',
                'disabled': 'true'
            })
        else :
            involedChoices.append(dict(zip(['name'], [user])))

    #print("mapped involved users liss : " + str(involedChoices))

    involved = prompt(
        {
            "type":"checkbox",
            "name":"involved",
            "message":"New Expense - Involved Users: ",
            "choices": involedChoices
        },
    )

    print(involved)
    infos.update(involved)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(infos.values())

    print("Expense Added !")

    return True


