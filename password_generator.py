first_name = "Davis"
last_name = "Kabaka"

def username_generator(first_name, last_nama):
    return first_name[:3] + last_name[:4]
username = username_generator(first_name, last_name)
print(username)


def password_generator(username):
    password = ""
    for i in range(0, len(username)):
        password += username [i-1]
    return password
print(password_generator(username))
