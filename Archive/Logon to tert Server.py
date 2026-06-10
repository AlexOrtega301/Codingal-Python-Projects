from time import sleep
print("Tert.com.. The ONLINE server for free storage for your files & Games")
user = "Alex"
passw = "Tanooki"

for a in range(5, 0, -1):
    usert = input("Username: ")
    passwt = input("Password: ")
    if usert == user and passwt == passw:
        print("Welcome to the Server of tert Alex")
        sleep(3)
        print("Files: kinitopet.exe, icons.txt, familie.png, craziy music.flac, funny video.mp4, ULTRA_IMAPORTANT_WORK.docks")
        break
    else:
        print("Incorrect Password or Username")
        print("You only have", a-1, "Tries left")

if a == 1 and usert != user and passwt != passw:
    print("Tert Server Blocked")
b = input("©️Tert.com")
