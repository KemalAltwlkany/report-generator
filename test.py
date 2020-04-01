x = "selam == =hello"
y = x.split("==")
print(type(y))
print(y)
print(y[1:])

for i in y[1:]:
    print(i)