import os

name = os.getenv("INPUT_NAME")
phrase = os.getenv("INPUT_PHRASE")

print(name + " says " + phrase + ".\n")

print("::set-output name=name::Python\n")
print("::set-output name=phrase::🐍🐍🐍\n")