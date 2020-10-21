def function1():
    print("Case 1 selected")

def function2():
    print("Case 2 selected")

def default():
    print("Value default")

num = int(input("numero: "))

if __name__ == "__main__":
    switch = {
        1: function1,
        2: function2
    }

    case = switch.get(num)
    case()