# შექმენით manual_replace ფუნქცია, რომელიც იქნება .replace() ფუნქციის კლონი. ამ ფუნქციამ სთრინგში არსებული sapce-ები უნდა შეცვალოს ტირეებად.


def manual_replace(text):
    
    new_text = ''
    
    for i in text:
        if i == ' ':
            new_text += '-'
        else:
          new_text += char
          return new_text




print(manual_replace("hello world"))   
print(manual_replace("no spaces"))     