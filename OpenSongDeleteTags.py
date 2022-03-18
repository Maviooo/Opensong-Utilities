import os
import re
in_path = input("Specify directory where files are located: ")
for inFile in os.listdir(in_path):
    try:
        global_path = in_path + "\\" + inFile
        print(global_path)

        content = ""
        f = open(global_path,mode= "r" ,encoding="utf8")
        content = f.read()
        f.close()
    except:
        print("Error opening the file")

    try:
        content_striped = ""
        content_striped2 = ""
        content_striped = re.sub(r'[\s\S]*(<lyrics>)','',content)
        content_striped2 = re.sub(r'(</lyrics>)(.|\n)*','',content_striped, flags=re.DOTALL)
        content_striped2 = content_striped2.replace("||", "")
        content_striped2 = content_striped2.replace("|", "")
        content_striped2 = re.sub(r'\..*\n',"",content_striped2)
        content_striped2 = content_striped2.replace(":/ ", "")
        content_striped2 = content_striped2.replace(":/", "")
        content_striped2 = content_striped2.replace("/:", "")

    except:
        print("Error processing file")

    try:
        f= open(global_path,mode="w",encoding="utf8")
        f.write(content_striped2)
        f.close()
    except:
        print("Error closing the file")
print("Done!")

