w = int(input("Enter upto number:"))

stars = 1
xstars = w-1
space = w-1
xspace = 1

for i in range(2*w-1):
    if stars <= w:
        for m in range(space):
            print(" ",end="")
        for x in range(stars):
            print("*",end="")
        print()
        space -= 1
        stars += 1
    else:
        for n in range(xspace):
            print(" ",end="")
        for y in range(xstars):
            print("*",end="") 
        print()
        xspace += 1
        xstars -= 1