import os
#program whitch changes all files extentions in directory 
imput_path = input('Input directory of files to change their extentions: ')
imput_ext = input('Input the extention (with dot): ')
for inFile in os.listdir(imput_path):
    try:
        base = os.path.splitext(inFile)[0]
        base = imput_path + "\\" + base
        inFile = imput_path + "\\" + inFile
        os.rename(inFile, base + imput_ext)
    except:
        print("Error handling file: " + inFile)
print("DONE!")
