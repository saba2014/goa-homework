# ახსენით რას შვება not და in და რაში გამოიყენება

#in ამოწმებს, არის თუ არა კონკრეტული ელემენტი რომელიმე კოლექციაში და გამოიყენება სიაში სტრიქონში ტაპლში ლექსიკონში და სხვა კოლექციებში

# not აბრუნებს წინააღმდეგებულს გამოიყენება პირობის უარყოფისთვის.

# შექმენით ფუქნქცია, manual_capitalize რომელიც იქნება title ფუქციის კლონი (არ გამოიყენოთ title ) 

def manual_capitalize(word):
    if len(word)==0:
        return ""
    return word[0].upper()+word[1:]
word="dexter"
print(manual_capitalize(word))


def manual_capitalize_sentence(sentence):
    words=sentence.split()
    capitalize_words=[]
    for word in words:
        if len(word)>0:
            capitalize_word=word[0].upper()+word[1:]
            capitalize_words.append(capitalize_word)
        else:
            capitalize_words.append(word)
    return " ".join(capitalize_words)
sentence="biney moser and dexter" 
print(manual_capitalize_sentence(sentence)) 



    