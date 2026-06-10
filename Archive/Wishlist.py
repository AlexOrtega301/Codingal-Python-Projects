from time import sleep
print("Games.com the best gaming store")
wishes = []
def wishlist():
    wish = input("What Gamess do you want on your Wishlist")
    if wish in wishes:
        print("This game is alredy in-listed")
        sleep(3)
    else:
        wishes.append(wish)
        print("Adding to List...")
        sleep(3)
        print("Added :)")
        print(wishes)
while True:
    wishlist()   
    

