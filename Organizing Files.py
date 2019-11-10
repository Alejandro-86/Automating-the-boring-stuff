import os, zipfile

file = 'C:\\Users\Alex\\PycharmProjects\\MsC in AI SOTON\AutomatingTheBoringStuff\\venv\\Chapters ATBS\\ch9 Organizing Files'
for folderName, subfolders, filenames in os.walk(file):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE: '+ filename)

    print('')

os.chdir(file)
exampleZip = zipfile.ZipFile('test.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('tumblr_maj5a0DHgQ1qexgkbo1_500.png')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
   .compress_size, 2)))
exampleZip.extractall()

exampleZip.close()
