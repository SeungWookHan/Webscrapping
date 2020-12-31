import requests
import os

running = True
while running:
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLS you want to check. (separted by comma)")
    input_string = str(input())
    chunks = input_string.replace(" ", "").lower().split(",")

    for chunk in chunks:
        result_string = ""
        if chunk[-4:] != ".com":
            print(chunk, "is not a valid URL.")
        else:
            if chunk[0:7] != "http://":
                chunk = "http://" + chunk
            try:
                res = requests.get(chunk)
            except:
                print(chunk, "is down!")
            else:
                if res.status_code == requests.codes.ok:
                    print(chunk, "is up!")

    while True:
        isExit = input("Do you want to start over? y/n ")
        if isExit == "y":
            os.system("clear")
            break

        elif isExit == "n":
            print("k. bye!")
            running = False
            break

        else:
            print("That's not a valid answer.")
