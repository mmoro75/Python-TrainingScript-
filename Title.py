# create title from string and display centre screen based on screen size

import os    #import os module
sz=os.get_terminal_size().columns  #get column number
title=input("give me the title:")
print(title.center(sz).title())

# create title from string and display left and right screen based on screen size

print(title.ljust(sz).title())
print(title.rjust(sz).title())
