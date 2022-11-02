from PyInquirer import prompt
import csv
import ast

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


def check_number(userInput):
    try:
        # check if is integer
        val = int(userInput)
    except ValueError:
        try:
            # check if is float
            val = float(userInput)
        except ValueError:
            #error, user's input is not a number
            raise SystemExit("The given expense 'amount' is not a number (int or float)")


def new_expense(*args):

    infos = prompt(expense_questions)

    #input validator
    check_number(infos['amount'])

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

    #print("mapped involved users list : " + str(involedChoices))

    involved = prompt(
        {
            "type":"checkbox",
            "name":"involved",
            "message":"New Expense - Involved Users: ",
            "choices": involedChoices
        },
    )

    #print(involved)
    
    #concat dict to add expense involved users
    infos.update(involved)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(infos.values())

    print("Expense Added !")

    return True

def synthetize():
    
    #initialize dict with all users names as key, and 0 as value (money balance)
    res = {}
    for user in users:
        res[user] = 0

    with open('expense_report.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                total = int(row[0])
            except ValueError:
                total = float(row[0])

            spender = row[2]
            involvedAllStr = row[3]
            involvedAll = ast.literal_eval(involvedAllStr)

            subTotal = total / (len(involvedAll) + 1) 

            #print("total:" + str(total)+ " subTotal: "+ str(subTotal))
            #print("spender"+ spender)

            res[spender]+= total - subTotal
            
            #print("involved users:")
            
            for involved in involvedAll:
                res[involved]-=subTotal

    print("All users balance (negative value mean that the user must refund someone that has a positive value, to balance everybody to 0): \n" + str(res))


    return True
