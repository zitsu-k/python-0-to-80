#copyfile() = copies contents of a file 
#copy() = copyfile() + permission mode + destination can be a directory
# copy2() =copy() + copies metadata (file's creation and modifiacation time )

import shutil

shutil.copyfile('copy.txt','text.txt')