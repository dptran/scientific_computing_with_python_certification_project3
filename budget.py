class Category:  
    
    
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []
        
    def __str__(self):
        string = ""
        string += '{:*^30}\n'.format(self.name.title())
        for i in self.ledger:
            string += '{:<23.23}{:>7.2f}\n'.format(i['description'], i['amount'])
        string += 'Total: {:.2f}'.format(self.balance)
        return string
        
        
    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
        
    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        
    def withdraw(self, amount, description=""):
        self.amount = amount
        self.description = description
        if self.check_funds(amount) == True:
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def transfer(self, amount, recipient):
        self.amount = amount
        self.recipient = recipient
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {self.recipient.name.title()}")
            recipient.deposit(amount, f"Transfer from {self.name.title()}")
            return True
        else:
            return False

        
def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    heights = {}
    withdrawals = 0

    for i in categories:
        for j in i.ledger:
            if j['amount'] < 0:
                withdrawals += j['amount']
    
    for i in categories:
        for j in i.ledger:
            heights[i.name] = round(j['amount'] / withdrawals, 1)

    chart += "100| "
    for k in heights.values():
        if k > 0.9:
            chart += "o  "
        else:
            chart += "   "
    chart += "\n"

    chart += " 90| "
    for k in heights.values():
        if k > 0.8:
            chart += "o  "
        else:
            chart += "   "
    chart += "\n"

    chart += " 80| "
    for k in heights.values():
        if k > 0.7:
            chart += "o  "
        else:
            chart += "   "
    chart += "\n"

    chart += " 70| "
    for k in heights.values():
        if k > 0.6:
            chart += "o  "
        else:
            chart += "   "
    chart += "\n"

    chart += " 60| "
    for k in heights.values():
        if k > 0.5:
            chart += "o  "
        else:
            chart += "   "
    chart += "\n"

    chart += " 50| "
    for k in heights.values():
        if k > 0.4:
            chart += "o  "
        else:
            chart += "   "
    chart += "\n"

    chart += " 40| "
    for k in heights.values():
        if k > 0.3:
            chart += "o  "
        else:
            chart += "   "
    chart += "\n"

    chart += " 30| "
    for k in heights.values():
        if k > 0.2:
            chart += "o  "
        else:
            chart += "   "
    chart += "\n"

    chart += " 20| "
    for k in heights.values():
        if k > 0.1:
            chart += "o  "
        else:
            chart += "   "
    chart += "\n"
    
    chart += " 10| "
    for k in heights.values():
        if k > 0.1:
            chart += "o  "
        else:
            chart += "   "
    chart += "\n"

    chart += "  0| "
    for k in heights.values():
        if k > 0:
            chart += "o  "
        else:
            chart += "   "
    chart += "\n    -"
    
    category = list(heights.keys())

    for i in range(len(category)):
        chart += "---"

    arr = []
    
    def myFunc(e):
        return len(e)
    
    category.sort(key=myFunc)
    
    for i in category[-1]:
        arr.append([])
    
    for i in heights.keys():
        for j, k in enumerate(i.title()):
            arr[j].append(k)
    
    for i in arr:
        if len(i) == 1:
            for j in range(len(category) - 1):
                i.insert(0, " ")
        elif len(i) == 2:
            for j in range(len(category) - 2):
                i.insert(1, " ")
                
    for i in range(len(arr)):
        chart += "\n     "
        for j in arr[i]:
            chart += j + "  "
        

    return chart
