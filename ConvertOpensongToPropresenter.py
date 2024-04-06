import os
import re

# Inputs
in_path = input("Specify directory where files are located: ")

# Change extention to txt
for inFile in os.listdir(in_path):
    try:
        if os.path.splitext(inFile)[0]:
            base = os.path.splitext(inFile)[0]
        else:
            base = os.path
        base = in_path + "/" + base
        if os.path.isdir(base):
            continue
        inFile = in_path + "/" + inFile
        
        os.rename(inFile, base + ".txt")
    except:
        print("Error handling file: " + inFile)

# Remove opensong formating and add PP labels for better import
# Ref: https://support.renewedvision.com/hc/en-us/articles/360011789393-How-do-I-import-plain-text-files-into-ProPresenter
for inFile in os.listdir(in_path):
    try:
        global_path = in_path + "/" + inFile
        print(global_path)

        content = ""
        f = open(global_path,mode= "r" ,encoding="utf8")
        content = f.read()
        f.close()
    except:
        print("Error opening the file ", global_path)

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
        content_striped2 = content_striped2.replace("[V1]", "Verse 1")
        content_striped2 = content_striped2.replace("[V2]", "Verse 2")
        content_striped2 = content_striped2.replace("[V3]", "Verse 3")
        content_striped2 = content_striped2.replace("[V4]", "Verse 4")
        content_striped2 = content_striped2.replace("[V5]", "Verse 5")
        content_striped2 = content_striped2.replace("[V6]", "Verse 6")
        content_striped2 = content_striped2.replace("[V7]", "Verse 7")
        content_striped2 = content_striped2.replace("[V8]", "Verse 8")
        content_striped2 = content_striped2.replace("[V9]", "Verse 9")
        content_striped2 = content_striped2.replace("[C1]", "Chorus 1")
        content_striped2 = content_striped2.replace("[C2]", "Chorus 2")
        content_striped2 = content_striped2.replace("[C3]", "Chorus 3")
        content_striped2 = content_striped2.replace("[C4]", "Chorus 4")
        content_striped2 = content_striped2.replace("[B1]", "Bridge 1")
        content_striped2 = content_striped2.replace("[B2]", "Bridge 2")
        content_striped2 = content_striped2.replace("[B3]", "Bridge 3")
        content_striped2 = content_striped2.replace("[T]", "Tag")
        content_striped2 = content_striped2.replace("[T1]", "Tag 1")
        content_striped2 = content_striped2.replace("[T2]", "Tag 2")
        content_striped2 = content_striped2.replace("[TAG1]", "Tag 1")
        content_striped2 = content_striped2.replace("[TAG2]", "Tag 2")
        content_striped2 = content_striped2.replace("[P1]", "PreChorus 1")
        content_striped2 = content_striped2.replace("[P2]", "PreChorus 2")

    except:
        print("Error processing file ", global_path)

    try:
        f= open(global_path,mode="w",encoding="utf8")
        f.write(content_striped2)
        f.close()
    except:
        print("Error closing the file ", global_path)
print("Done!")

