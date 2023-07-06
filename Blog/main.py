string = ""
for i in ["{data}", "{data}"]:
    string += i.format(data='hello')
print(string)