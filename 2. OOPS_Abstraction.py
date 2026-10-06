class CoffeeMachine:
    def startCoffee(self):
        print("Making a cup of Coffee for you.....")
        self.__grindCoffee()
        self.__boilWater()
        print("You coffee cup is now ready....")

    def __grindCoffee(self):
        print("Grinding Coffee Beans!!")

    def __boilWater(self):
        print("Boiling water for your coffee!!")


makeCoffee = CoffeeMachine()
makeCoffee.startCoffee()