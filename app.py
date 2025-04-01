#simpe Math
x = 2
y = 3
z = x + y
print(x)
print(y)

#Python is using indents
a = 10
b = 5
c = a / b
d = a * b
e = a % b
name = "Anna"
surname = "grey"
student_name = name + " " + surname
print(student_name)
#TASK
#1. write IF ELSE statement to validate if x is larger than y . Return TRUE if YES

def compare(x, y):  # Changer le nom de la fonction pour éviter les conflits
    if x > y:
        return True  # Utiliser True avec majuscule
    return False  # Utiliser False avec majuscule

print(compare(300, 200))

#2. #1. write IF ELSE statement to validate if x is larger than y and less than b. Return TRUE if YES

def compare(x, y, b):  # Changer le nom de la fonction pour éviter les conflits
    if (x > y) and (x < b):
        return True  # Utiliser True avec majuscule
    return False  # Utiliser False avec majuscule

print(compare(300, 200, 500))
