f = open('notes.score', "r+")
a = open('notes.v1', "w")

data = f.read().replace('cd', '')
a.write(data)
print(data)
f.close()
a.close()

f = open('notes.v1', "r+")
b = open('notes.v2', "w")

data = f.read().replace('dc', '')
b.write(data)
print(data)
f.close()
b.close()

f = open('notes.v2', "r+")
c = open('notes.v3', "w")

data = f.read().replace('hc', '')
c.write(data)
print(data)
f.close()
c.close()

f = open('notes.v3', "r+")
d = open('notes.v4', "w")

data = f.read().replace('ch', '')
d.write(data)
print(data)
f.close()
d.close()
