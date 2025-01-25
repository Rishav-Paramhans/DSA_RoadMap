"""
    Task: Write a program that takes an input of age and prints if you are
    an adult or not
"""
"""Thought process:
    1. Takes an input- so input the age--> since age so integer datatype should be enough
    2. Conditional- comparision if input age is >=18 or not
    3.Print Statemnt based on the conditional
"""

def is_adult(age):
    if age >= 18:
        print("You are an adult")
    else:
        print("You are not an adult, you are just {} years far from becomeing adult".format(18-age))



if __name__ == "__main__":
    Age = int(input ("Please enter your Age :"))
    is_adult(age=Age)