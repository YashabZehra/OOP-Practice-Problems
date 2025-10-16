#SINGLE CLASS AND SINGLE OBJECT WITH MULTIPLE METHODS
class Dog:
    def run(self):
        print("Dog is running fast")
    def bark(self):
        print("Woof! Woof! Dog is barking")
    
elis = Dog()
# dog_bark =Dog()

elis.run()
elis.bark()





#SINGLE CLASS WITH MULTIPLE OBJECTS AND METHODS
class player:
    def throw(self):
        print("watch out! i am throwing the ball")
    def catch(self):
        print("catch out!")
    def jump(self):
        print("player is jumping...")

player1 = player()
player2 = player()

player1.throw()
player2.jump()
player2.catch()






#MULTIPLE CLASSES,OBJECTS AND METHODS
class bank:
    def add_account(self):
        print("account is opened")
    def remove_account(self):
        print("account is removed")
class account:
    def current_account(self):
        print("current account is opened")
    def saving_account(self):
        print("saving account is opened")

customer1 = bank()
customer2 = bank()

customer1.add_account()
customer2.remove_account()

customer1 = account()
customer1.saving_account()