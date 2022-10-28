import os
in_path = input("Specify directory where files are located: ")
content = ""
for inFile in os.listdir(in_path):
    try:
        global_path = in_path + "/" + inFile
        print(global_path)

        f = open(global_path,mode= "r" ,encoding="utf8")
        content = f.read()
        f.close()

    except:
        print("IO Error!!!")

    try:
        sep = "[V1]"
        lyrics_1 = content.split(sep, 1)
        sep_2 = "<"
        lyrics_2 = lyrics_1[1].split(sep_2, 1)
        fin = content.replace(lyrics_2[0], lyrics_2[0].upper())

    except:
        continue
    try:
        f= open(global_path,mode="w",encoding="utf8")
        f.write(fin)
        f.close()
    
    except:
        print("IO Error!!!")
print("Done!")

