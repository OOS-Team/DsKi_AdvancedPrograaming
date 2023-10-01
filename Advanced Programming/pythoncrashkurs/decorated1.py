def display(func):
    def inner():
        print("The current user is : ", end="")
        func()
    return inner

@display
def who():
    print("Alice")
         
if __name__ == "__main__":
    who()                    #The current user is : Alice