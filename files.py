import os

os.path.join('folder1', 'folder2', 'folder3', 'file.png') #will join based on OS
os.sep #will show OS separator
os.getcwd() #current working directory, default is python folder
os.chdir('c:\\') #change directory
os.getcwd() #will show c:\\

os.path.abspath('spam.png') #will return current dir, which is c:\\ + spam.png
os.path.abspath('..\\..\spam.png') #will return 2 folders above

os.path.isabs('..\\..\\spam.png') #False

os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1') #parameter 2 is the current dir
#will return folder2\\spam.png

os.path.dirname('c:\\folder1\\folder2\\spam.png') #will return c:\\folder1\\folder2
os.path.basename('c:\\folder1\\folder2') #will return folder2

os.path.exists('c:\\windows\\system32\\calc.exe') #True
os.path.isdir('c:\\windows\\system32') #True

os.path.getsize('c:\\windows\\system32\\calc.exe')

#listdir shows all files inside the said dir
for filename in os.listdir('c:\\documents'):
    if not os.path.isfile(os.path.join('c:\\documents', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\documents', filename))
#shows totalSize of files inside the dir

os.makedirs('c:\\documents\\yes123') #will create a folder


#open files
helloFile = open('c:\\documents\sample.txt')
content = helloFile.read()
print(content) #will return how you see it in text file | 1 string
helloFile.close() # once you close, you need to open again

helloFile.open('c:\\documents\sample.txt')
helloFile.readlines() #this will return array with separator of new line

#write files
helloFile = open('c:\\documents\\hello2.txt', 'w') #parameter 2 (w), means write, if we use this, it will rewrite the entire txt file
helloFile.write('Hello!')
helloFile.write('Hello!')
helloFile.write('Hello!')
#this is only in one line, without new lines
hello.close()

#append
baconFile = open('c:\\documents\\hello2.txt', 'a')
baconFile.write('\nYes!')
baconFile.close()

#shelve
import shelve #shelve is like session or cookie, this saves a file on your current dir

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['a', 'b', 'c']
shelfFile.close()

shelfFile = shelve.open('mydata')
shelfFile['cats'] #will return the array at the top

#advantages of this is, you can use this data saved on this anytime since it is written on your harddrive



#copy files / moving
import shutil
shutil.copy('c:\\documents\\test1.txt', 'c:\\documents\\yes123') #will copy file to second param
shutil.copytree('c:\\documents\\yes123', 'c:\\documents\\newfol') #will copy entire folder
shutil.move('c:\\documents\\yes123\\test1.txt', 'c:\\documents\\newfol') #will move to new folder
shutil.move('c:\\documents\\newfol\\test1.txt', 'c:\\documents\\newfol\\test2.txt') #rename file



#deleting files
import os
os.getcwd()
os.unlink('filename.ext') #delete single file in current working directory


