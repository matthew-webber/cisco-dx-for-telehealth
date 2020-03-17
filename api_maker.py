a = "xCommand UserInterface Extensions List"

a = a.split(" ")
b = []
c = []

for word in a:
    b.append(f"<{word}>")

for word in a[::-1]:
    c.append(f"</{word}>")

x = b + c
x = "".join(x)