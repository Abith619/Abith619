"""Unix-based operating systems typically include a tool named cat, which is short for concatenate. 
Its purpose is to concatenate and display one or more files whose names are provided as command 
line parameters. The files are displayed in the same order that they appear on the command line.
Create a Python program that performs this task. It should generate an appropriate error message
for any file that cannot be displayed, and then proceed to the next file. Display an appropriate
error message if your program is started without any command line parameters"""

filenames = ['123.txt', '124.txt']
  
with open('file3.txt', 'w') as outfile:
    for names in filenames:
        with open(names) as infile:
            outfile.write(infile.read())
        outfile.write("\n")