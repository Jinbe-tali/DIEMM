# baasic function arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} and its name is {pet_name}.")

# call function three times
describe_pet("dog", "Buddy")
describe_pet("cat", "Milo")
describe_pet("parrot", "Polly")


# posi keyword
# positional
describe_pet("hamster", "Nugget")

# keyword reverse
describe_pet(pet_name="Brownie", animal_type="rabbit")


# default
def describe_pet_default(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} and its name is {pet_name}.")

describe_pet_default("Brownie")
describe_pet_default("Nugget", "chicken")


# own function
def order_drink(drink, size="medium", iced=False):
    size_text = size
    iced_text = "iced " if iced else ""
    return f"Your order: {size_text} {iced_text}{drink}"

print(order_drink("coffee"))                    
print(order_drink("hot chocolate", size="large", iced=False)) 
print(order_drink("milk tea", size="small", iced=True))     


def compute(operation, num1, num2=1):
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operation"

print("compute add:", compute("add", 5, 10))
print("compute multiply:", compute("multiply", num1=3, num2=4))
print("compute subtract (using default num2=1):", compute("subtract", 20))
print("compute invalid:", compute("divide", 10, 2))