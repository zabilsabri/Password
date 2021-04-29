password = "Put your Password in here!"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != password and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter your Password: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("PASSWORD INVALID")
else:
    print("WELCOME!")