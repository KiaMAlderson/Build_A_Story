import os

def clear_screen():
    os.system('cls')

def main():
    line_store = []
    line = ""
    end_words = ["the end", "end", "fin"]
    
    print("Welcome to Build-A-Story! Every turn, a player writes a line, then presses ENTER.\r\n")
    print("The next player is then shown the previous line and writes their own!\r\n")
    print("To end the story, simply press ENTER when prompted for another line\r\n\n")

    title = input("Enter the name for the story: ")
    filename = title + ".txt"

    story_file = open(filename, "a")
    story_file.write("This story is called [" + title + "]\n")

    while(1):
        if len(line_store) > 0:
            print("Title: " + title + "\n")
            print("Previous line: " + line_store[-1])
        line = input()

        if line.lower() in end_words:
            clear_screen()
            reader = input("Enter R to read the whole story, any other key to close\n\n")
            if(reader.lower() == "r"):
                print(title)
                for l in line_store:
                    print(l)
                story_file.close()
                print("That's the story! Bye!\n")
                exit()
            else:
                story_file.close()
                exit()
        else:
            line_store.append(line)
            story_file.write(line)
        
        clear_screen()
        
main()
    
    
