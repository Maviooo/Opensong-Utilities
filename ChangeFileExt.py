import os
#program whitch changes all files extentions in directory 
input_path = input('Input directory of files to change their extentions: ')
input_ext = input('Input the extention (with dot): ')
for inFile in os.listdir(input_path):
    try:
        if os.path.splitext(inFile)[0]:
            base = os.path.splitext(inFile)[0]
        else:
            base = os.path
        base = input_path + "/" + base
        inFile = input_path + "/" + inFile
        os.rename(inFile, base + input_ext)
    except:
        print("Error handling file: " + inFile)
print("DONE!")
