#Make a gold checker, that should accept only 22k or 24k gold. the good good only

purity = float(input("Enter the percentage of gold."))

if purity>=99.9:
    print("24K")
elif (purity<99.9  and purity>=91.7):
    print("22K")
elif (purity<91.7 and purity>=83.3):
    print("20K")
elif (purity<83.3 and purity>=75):
    print("18K")
elif purity<75:
    print("too low")
