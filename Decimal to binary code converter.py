dec = int(input("Enter the decimal no. to convert to binary"))
pes = []
bin = "The Binary Code for this number is: "
while dec != 0:
    b = dec//2
    a = dec % 2
    print(a)
    pes.append(a)
    dec = b
pes.reverse()
for char in pes:
    bin += str(char)
print(pes)
print(bin)
