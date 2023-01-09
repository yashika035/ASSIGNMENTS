string = "Python is a case sensitive language"

length = len(string)
print(length)

reverse = "Python is a case sensitive language"[::-1]
print(reverse)

sliced = string[10:27]
print(sliced)

replaced_string = string.replace("a case sensitive language","object oriented")
print(replaced_string)

index = string.index("a")
print(index)

new = string.replace(" ","")
print(new)