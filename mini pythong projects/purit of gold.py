#Make a gold checker, that should accept only 22k or 24k gold. the good good only

purity = float(input("Enter the percentage of gold."))

if purity>=91.7:
    print("Accepted")
    if purity>=99.9:
        print("Accepted")
else:
    print("unpure deska")
