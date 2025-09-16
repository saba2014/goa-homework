# შექმენით ფუნქიცა, manual_find, რომელსაც გადაეცემა არგუმენტად სთრინგი და ერთი სიმბოლო, რომელიც უნდა ვიპოვოთ ამ სთრინგში. თუ სიმბოლო მოიძებნა დააბრუნეთ მისი ინდექსი, სხვა შემთხვევაში დააბრუნეთ -1

def manual_find(text, symbol):
    index = 0
    for i in text:
        if char == symbol:
            return index
        index += 1
    return -1

