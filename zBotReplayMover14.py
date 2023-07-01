import os
import requests #only needed for text lol

# TODO: check if there's a config file (DONE)
# TODO: if there is, read it and set the path variables (DONE)
# TODO: make this work (DONE)

string = requests.get('https://pastebin.com/raw/Xx56vMhm').text
print(string)

print("Made by terminite (@terminite)\n")

scriptdir = os.path.dirname(os.path.realpath(__file__))
absdir = os.path.join(scriptdir, "config.txt")
def check_file():
    check = os.path.isfile(absdir)
    if not check:
        print("Looks like this is the first time you're running this program. Now follows the setup process.")
        setup()
        
def setup():
    print("\nPlease enter the path to your zBot Replays folder.")
    print("Example: C:\\Program Files (x86)\\Steam\\steamapps\\common\\Geometry Dash\\replays \n")
    replays_path = input("Replays Path: ")
    print("\nNow enter the path to the folder that you download replays to.")
    print("Example: C:\\Users\\terminite\\Downloads\n")
    download_path = input("Download Path: ")
    if not os.path.isdir(replays_path.strip()):
        print("The Replays Path you entered is not a directory. Please try again.")
        setup()
    if not os.path.isdir(download_path.strip()):
        print("The Download Path you entered is not a directory. Please try again.")
        setup()
    print("\nPerfect! The directories exist. Now let's check if they're correct.")
    print(f"Replays Path: {replays_path}")
    print(f"Download Path: {download_path}")
    print("\nIs this correct? (y/n)")
    correct = input("Answer: ")
    if correct == "y":
        print("Great! Now saving the config file...")
        f = open(absdir, "w")
        f.write(f"{replays_path}\n")
        f.write(f"{download_path}")
        f.close()
        print("Setup complete!")
    else:
        print("Okay, let's try again.")
        setup()

def main():
    check_file()
    f = open("./config.txt", "r")
    replays_path = f.readline()
    download_path = f.readline()
    print(f"Using replay path: {replays_path.strip()}")
    print(f"Using download path: {download_path}\n")
    print("Checking for replays...")
    replays = os.listdir(download_path.strip())

    replaymoved = 0
    replayerrors = 0

    for replay in replays:
        if replay.endswith(".zbf") or replay.endswith('.zbot'):
            print(f"Found replay: {replay}")
            try:
                os.rename(os.path.join(download_path.strip(), replay), os.path.join(replays_path.strip(), replay))
                replaymoved += 1
            except FileExistsError:
                print("File already exists. Skipping...")
                replayerrors += 1
    
    print(f"\nMoved {replaymoved} replays with {replayerrors} errors.")
    f.close()
    input("Press enter to exit.")

main()