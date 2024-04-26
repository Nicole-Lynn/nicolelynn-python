import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()  #To get a list of available fonts


# For zero command line arguments
if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts)) #To set the font with code, where f is the font’s name as a str

# For two command line arguments
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        figlet.setFont(font = sys.argv[2])
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")


msg = input("Input: ")
output = figlet.renderText(msg)

#Output text in that font like this, where s is that text as a str
print("Output:\n", output)
