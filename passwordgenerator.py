from flask import Flask
import string
import random

app = Flask(__name__)
@app.route('/')
def index():
    return "Yo wazzup"

if __name__ == "__main__":
    app.run(debug=True)

letters = string.ascii_letters
nums = string.digits
punc = string.punctuation

def get_password_lenght():
    lenght = input("How long do you want your password to be?")
    return int(lenght)

def password_gen(lenght=8):
    printable = f'{letters}{nums}{punc}'
    printable = list(printable)
    random.shuffle(printable)
    
    random_pass = random.choices(printable, k=lenght)
    random_pass = ''.join(random_pass)
    return random_pass

password_lenght = get_password_lenght()
password = password_gen(password_lenght)

print("Password (" + str(len(password)) + "): \t\t" + password)



