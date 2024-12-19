correct_password = "python123"
entered_password = ""

while entered_password != correct_password:
    entered_password = input("Enter your password: ")
    if entered_password != correct_password:
        print("Wrong password. Try again!")

print("Access granted!")
