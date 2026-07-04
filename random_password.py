import secrets
import string

print("Hi, Welcome to my random password generator.")

pool = string.ascii_letters + string.digits + string.punctuation

for i in range (15):
    variable = secrets.choice(pool)
    variable1 = secrets.choice(pool)
    variable2 = secrets.choice(pool)
    variable3 = secrets.choice(pool)
    variable4 = secrets.choice(pool)
    variable5 = secrets.choice(pool)
    variable6 = secrets.choice(pool)
    variable7 = secrets.choice(pool)
    variable8 = secrets.choice(pool)
    variable9 = secrets.choice(pool)
    variable10 = secrets.choice(pool)
    variable11 = secrets.choice(pool)
    variable12 = secrets.choice(pool)
    variable13 = secrets.choice(pool)
    variable14 = secrets.choice(pool)
    variable15 = secrets.choice(pool)

print(f"Your Generated Password Is: {variable + variable1 + variable2 + variable3 + variable4 + variable5 + variable6 + variable7 + variable8+ variable9 + variable10 + variable11 + variable12 + variable13 + variable14 + variable15}")
    