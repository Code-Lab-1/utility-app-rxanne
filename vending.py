vending=[
{"id":1,"name":'Snickers bar','amnt':3,'stock':10},
{'id':2,'name':'Pop-Tarts','amnt':4,'stock':10},
{'id':3,'name':'Reese peanut butter cups','amnt':5,'stock':5},
{'id':4,'name':'Granola Bar','amnt':5,'stock':10},
{'id':5,'name':'Water bottle','amnt':1,'stock':3},
{'id':6,'name':'Red Bull energy','amnt':10,'stock':10},
{'id':7,'name':'Monster energy','amnt':8,'stock':10},
{'id':8,'name':'Iced Tea','amnt':3,'stock':10},
{'id':9,'name':'Coffee','amnt':3,'stock':10},
{'id':10,'name':'Mountain Dew','amnt':3,'stock':10}]

def list():
    print(
        "------Rockstar Vending Machine------\n"
        "---------------Snacks---------------\n"
        "1 - Snickers Bar               3AED \n"
        "2 - Pop-Tarts                  4AED \n"
        "3 - Reese Peanut Butter Cup    5AED \n"
        "4 - Granola Bar                5AED \n"
        "------------------------------------\n"
        "---------------Drinks---------------\n"
        '5 - Water Bottle               1AED \n'
        "6 - Red Bull Monster Energy   10AED \n"
        "7 - Monster Energy             8AED \n"
        "8 - Iced Tea                   3AED \n"
        "9 - Coffee                     3AED \n"
        "10- Mountain Dew               3AED \n"
        "------------------------------------\n")


def vend():
    a=0
    while a==0:
        list()
        money = int(input("enter the amount of money to insert-"))
        if money<=0:
            print("Invalid Amount! enter an amount of 1AED or more")
            vend()
        input_id=int(input("enter the code of the item you wish to purchase-"))
        if input_id>10 or input_id<1:
            print("Invalid Code")
            vend()
        total=0
        for i in vending:
            if input_id==i["id"] and money<i["amnt"]:
                print("You have insufficient funds, please try again")
                vend()
            if input_id==i["id"] and i["stock"]<0:
                print("sorry, there is no available stock for this item, please enter a different id")
                vend()
            if input_id==i["id"] and money>=i["amnt"]:
                print("you have selected",i["name"])
                i["stock"]=i["stock"]-1
                total=total+i['amnt']
                balance=money-total
                print("-------------Reciept------------")
                print(i['id'],')', i["name"],"       ",i["amnt"])
                print("--------------------------------")
                print("Total",'-----',total)
                print("Balance",'----',balance)
                print("--------------------------------")
                b=input("do you wish to purchase more? yes/no")
                if b=="yes":
                    vend()
                elif b=='no':
                    a=1
                else:
                    print("invalid option")
                    vend()

vend()