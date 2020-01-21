h = int(input("enter tree's height:"))

# space = h-1
# stars = 1
# for x in range(h):
#     for s in range(space):
#         print(end=' ')
#     for st in range(stars):
#         print(end='*')
#     print()
#     space-=1
#     stars+=2

# print()

w = 2*h-1

for i in range(h):
    star = 2*i+1
    space = int((w-star)/2)
    for j in range(space):
        print(" ",end="")
    for k in range(star):
        print("*",end="")
    print()


(2h-1-2i-1)/2

h-i-1

    


