class player():
    def __init__(self, name: str, age:int, balance:float = 0, num_of_plays:int = 0) -> None:
        self.name = name
        self.age = age
        self.balance = balance
        self.num_of_plays = num_of_plays


    def deposit(self) -> None:
        while True:
            amount = input("Enter amount to deposit: ")

            try:
                amount = float(amount)
        
                if amount < 0:
                    raise ValueError
        
                self.balance = amount
                break        
        
            except ValueError:
                print ("Not a valid amount !")


    def __str__(self) -> str: 
        return f"\nName: {self.name} \nAge: {self.age} \nBalance: ${self.balance} \nNumber of plays: {self.num_of_plays}\n"


"""p1 = player("Dagur", 19)

print (p1)

p1.deposit()

print (p1)"""