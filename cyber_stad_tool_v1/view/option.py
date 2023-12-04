import os
import sys
from abc import ABC

from colorama import Fore, Style
from termcolor import colored
from components import loading,banner
from information_gethering import website_information, mail_server
from view import template
class Option(ABC):
    @staticmethod
    def item(number):
        return f"{number})"

    @staticmethod
    def color(style):
        if style in colored('', style):  # Check if the color is available
            return lambda text: colored(text, style)
        else:
            return lambda text: text

    @staticmethod
    def clear():
        # Clear console screen based on the operating system
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Linux and macOS
            os.system('clear')
    def reconnaissance_option(self):
        print(self.item(1), "Website Information ")
        # print(self.item(2), "Phone Number Information ")
        print(self.item(2), "Find IP Address And E-mail Server ")
        print(self.item(3), "Domain Whois Lookup ")
        print(self.item(4), "Find Website/IP Address Location ")

    def exploit_option(self, opt):
        if opt == 1:
            self.clear()
            banner.start_banner();
            website = input("[+] Enter Website :")
            loading.loading_animation()
            website_information.get_ip_info(website)
            print("...............................")
            print(" ")
            opt = int(input("Choose an option (1-2, 99 to back): "))
            self.exploit_option(opt)
        elif opt == 2:
            self.clear()
            banner.start_banner();
            website = input("[+] Enter Website :")
            loading.loading_animation()
            mail_server.find_mx_records(website)
            print("...............................")
            print(" ")
            opt = int(input("Choose an option (1-2, 99 to exit): "))
            self.exploit_option(opt)
        elif opt == 99:
            print("=> Exited tool. :)")
            template.cyber_stad();
        else:
            print(Fore.RED + "=> Invalid option range, options are number 1 and number 2" + Style.RESET_ALL)
            opt = int(input("Choose an option (1-2, 99 to exit): "))
            self.exploit_option(opt)
