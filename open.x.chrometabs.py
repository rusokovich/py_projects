import webbrowser
import ssl
from webbrowser import Chrome

count = 0
url = input("enter your desired url: ")
tries = 3

while True:
    times = input("How many times would you like to open the url: ")

    try:
        times = int(times)
        break
    except ValueError:

        print("You didnt enter a number you still have:", tries, "tries" )
        tries = tries - 1
        if tries == -1:
            print("no more chances")
            print("open the program again")
            exit()
        continue

times=int(times)
while True:
    count=count+1
    webbrowser.open_new_tab(url)
    if count == times: break
print("count them")
