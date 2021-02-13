with open("names.txt", "r+", encoding="utf-8") as file:
    result = ""
    content = file.readlines()
    file.seek(0)
    count = len(file.readlines())
    for i in range(0,count):
        result += content[count-1-i]
    file.seek(0)
    file.write(result)
    file.seek(0)
    print(file.read())
