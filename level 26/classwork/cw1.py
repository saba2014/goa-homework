
#bშექმენი ფუნქცია is_positive, რომელიც იღებს ერთ რიცხვს არგუმენტად. თუ ეს რიცხვი დადებითია, დააბრუნოს True, სხვა შემთხვევაში კი False.

def is_posirive (number):
    if number > 0 :
        return True
    else:
        return False


    
# დაწერე ფუნქცია max_of_two, რომელიც იღებს ორ რიცხვს და აბრუნებს მათგან დიდს. გამოიყენე მხოლოდ if,else. 


def max_of_two(a , b ) :
    if a > b:
        return a
    else :
        return b

# დაწერე ფუნქცია max_of_three, რომელიც იღებს სამ მთელ რიცხვს და აბრუნებს მათგან უდიდეს

def max_of_three (a, b, c):
    if a>= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

    # დაწერე ფუნქცია is_hot, რომელიც იღებს ერთ რიცხვს (ტემპერატურა გრადუსებში) და აბრუნებს True, თუ ტემპერატურა 30 ან მეტია, ხოლო False — სხვა შემთხვევაში.





def is_hot(temperature):
    if temperature >= 30:
        return True
    else:
        return False
