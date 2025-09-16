# გაქვს სია სახელებით: ["გიო", "ანა", "საბა"]. დაწერე კოდი, რომელიც ყველა სახელს გააერთიანებს ერთ წინადადებაში მძიმით გამოყოფილს.
names = ["გიო", "ანა", "საბა"]
sentence = ", ".join(names)
print(sentence)


# შექმენი ცხოველების სია და დაამატე მასში "კუ"

animals = ["ძაღლი", "კატა", "პინგვინი"]
animals.append("კუ")

print(animals)



# დაბეჭდე სიის პირველი და ბოლო წევრი.(გამოიყენე ნეგატიური ინდექსები

animals = ["ძაღლი", "კატა", "პინგვინი", "კუ"]

print("first element:", animals[-len(animals)])
print("last element:", animals[-1])


#  დაწერე სტრინგი "მეგობრები" და გინდა გაიგე რამდენი ასოსა ამ სიაში. დაბეჭდე რაოდენობა

word = "friends"
length = len(word)

print("numbers of letters:", length)

# დაგიწერია სია [მე,მიყვარს,გოა] და გაიგე გაიგო რამდენი ელემენტია ამ სიაში. დაბეჭდე რაოდენობა

words=["მე , მიყვარს, გოა"]
sentence=len(words)
print(sentence)


# შექმენი სია შენი საყვარელი 3 სიმღერა და დაუმატე მეოთხე სიმღერა "pantera" მეორე ინდექსზე. 

musics=["mochingbrids, hit em up, in da club "]
musics.insert(2,"pantera")
print(musics)


# გადააქციე ლისტი სტრინგად და დაყავი თითოეული სტრინგი ამ ელემენტით "|"

musics=["mochingbrids, hit em up, in da club "]
m= "|".join(musics)
print(m)

# გადააკეთე სტრიქონიჯერ  დიდ ასოებად მერე პატარად და საბოლოოდ პირველ ასო გაზარდე

text ="tupac"
print(text.upper())
print(text.lower())
print(text.capitalize())

# იპოვე სიტყვა "პითონი" წინადადებაში find() ფუნქციით და დაბეჭდე მისი მდებარეობა.

sentence = "html,css,javascript py"
print(sentence.find("py"))


# შექმენი სია და ჩასვი "კომფეტი" მეორე პოზიციაზე insert()-ით

sia=["სტაფილო, ვაშლი, ბულგარული"]
sia.insert(1,"კომფეტი")
print(sia)


# დაწერე ფუნქცია double(n), რომელიც იღებს რიცხვს და აბრუნებს მის ორმაგს.
 
def double(n):
    return n*2
num=int(input("enter number:"))
print(double(num))

# დაწერე ფუნქცია is_even(n), რომელიც აბრუნებს True თუ რიცხვი ლუწია, და False თუ კენტია.

def is_even(n):
    return n % 2 == 0
print(is_even(4))
print(is_even(7))  
