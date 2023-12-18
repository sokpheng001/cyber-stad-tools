from pyfiglet import Figlet
from termcolor import colored
from components import loading
import random

color_  = ['grey',
'red',
'green',
'yellow',
'blue',
'magenta',
'cyan']

def create_banner(text, font='standard'):
    # Create a Figlet object
    fig = Figlet(font=font, width=150, justify="left")
    
    # Use the Figlet object to convert the text to ASCII art
    banner = fig.renderText(text)
    color = colored(banner,color_[random.randint(0,len(color_)-1)] );
    return color







def start_banner(banner_text="CYBER-STAD"):
    # for i in fonts_list:
    #         # Your text and font choice
    #     banner_text = "CYBER-STAD"
    #     # banner_font = "banner3-D"
    #     banner_font = i;
    
    #     # Create the banner
    #     banner = create_banner(banner_text, banner_font)
    #     # fig = Figlet()
    
    #     # # Get the list of available fonts
    #     # fonts = fig.getFonts()
    
    #     # Print the list of fonts
    #     # for font in fonts:
    #     #     print(font)
    #     # Print the banner
    #     print(banner)
    #     print("Font name: {}".format(i))
    banner_text = banner_text
    # banner_font = "banner3-D"

    banner_font = "dos_rebel";
    
    
    # Create the banner
    banner = create_banner(banner_text, banner_font)

    # fig = Figlet()

    # # Get the list of available fonts
    # fonts = fig.getFonts()

    # Print the list of fonts
    # for font in fonts:
    #     print(font)
    # Print the banner
    print("\n\n\n\n");
    print(banner)
    print("\t\t\t================================================================================");
    print("\t\t\t . This tool was implemented by the CSTAD cybersecurity student™ in 2023");
    print("\t\t\t . Credit to CSTAD");
    print("\t\t\t . CYBER-STAD Group™");
    print("\t\t\t . Github: https://github.com/sokpheng001/cyber-stad-tools.git")
    print("\t\t\t================================================================================");
    print()
    # loading 
    # loading.loading_animation();