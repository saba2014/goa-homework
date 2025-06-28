# მომხარებელს შემოატანინებ  სადაც თავის ასაკს, input ის საშუალებით, და მერე შეამოწმე მეტია ის თუ არა 18 ზე, გამოიყენეტ შედარების ოპერატორები


age = int(input("11: "))

if age > 18:
    print("თქვენ ასაკით სრულწლოვანები ხართ!")
else:
    print("თქვენ ასაკით არასრულწლოვანი ხართ.")


# რას გამოიტანს ეს კოდი(ახენით დეტალურად კომენტარებით) print(True and False or 5>2 and False or False and True)


True and False = False
or 5 > 2 = True
False and True = False
True and False = False
#გამოიტანს საბოლოოდ False