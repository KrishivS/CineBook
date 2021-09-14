x = open('data.json', 'r')
y = x.read()[:-1]
z = open('data.json', 'w')
z.writelines(y+"\n")
z.write("}")