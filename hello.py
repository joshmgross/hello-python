import os

name = os.getenv("INPUT_NAME")
phrase = os.getenv("INPUT_PHRASE")

print(f'{name} says {phrase}.\n')

print("::set-output name=name::Python\n")
print("::set-output name=phrase::🐍🐍🐍\n")