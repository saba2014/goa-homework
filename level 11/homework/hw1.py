#  ახსენით კომენტარებით while loop და for loop განსხვავება

# while loop — გამოიყენება სანამ პირობა True-ა (ანუ არ ვიცით ზუსტად რამდენჯერ)

# for loop — გამოიყენება როდესაც წინასწარ ვიცით რამდენჯერ გვინდა კოდის გამეორება



# მომხმარებელს შეჰყავს რიცხვი და თუ ის 18-ზე მეტია — დაიბეჭდოს "you are big adult"

ge = int(input("11: "))

if age > 18:
    print("you are not big adult")


# გააკეთე 2 დავალება while ციკლით

i = 1
while i <= 5:
    print(i)
    i += 1


i = 1
total = 0
while i <= 20:
    if i % 2 == 0:
        total += i
    i += 1
print("ლუწი რიცხვების ჯამი 1-დან 20-მდე არის:", total)