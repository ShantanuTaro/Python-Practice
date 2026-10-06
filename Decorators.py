def decorator(my_gift):
    def wrapper():
        print("Before opening gift!!")
        my_gift()
        print("Gift is now opened!")
    return wrapper

@decorator
def gift():
    print("Your gift are shoes!!")

gift()