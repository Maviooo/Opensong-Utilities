import os
import re
in_path = input("Specify directory where files are located: ")
content = ""
for inFile in os.listdir(in_path):
    try:
        global_path = in_path + "\\" + inFile
        print(global_path)

        f = open(global_path,mode= "r" ,encoding="utf8")
        content = f.read()
        f.close()

    except:
        print("IO Error!!!")
    
    content_striped = re.sub(r'[\s\S]*(<lyrics)[\s\S]','',content)
    
    content_striped2 = re.sub(r'(</lyrics>).*','',content_striped, flags=re.DOTALL)

    try:
        f= open(global_path,mode="w",encoding="utf8")
        f.write(content_striped2)
        f.close()
    
    except:
        print("IO Error!!!")
print("Done!")

