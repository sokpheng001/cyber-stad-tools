import os
import sys
from abc import ABC
from colorama import Fore, Style

from termcolor import colored
from components import loading,banner, clear_screen_and_provide_with_banner
from weapons.information_gathering import website_information, mail_server, port_scanning, security_header, whois_scanning
from view import template

class Option(ABC):
    @staticmethod
    def item(number):
        return f"{number}->"

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
        print(self.item(0), "Back to previous options")
        print(self.item(1), "Website Information ")
        # print(self.item(2), "Phone Number Information ")
        print(self.item(2), "Find IP Address And E-mail Server ")
        print(self.item(3), "Port Scanning")
        print(self.item(4), "Security Headers ")
        print(self.item(5), "Whois Scanning")
        print(Fore.RED + "(99 or Ctr + C or Exit) -> " + Style.RESET_ALL +  "To Exit ")
        print("---");
        
    def choose_option(self):
        clear_screen_and_provide_with_banner.cstad_banner_();
        print("\n[" + Fore.GREEN + "*" + Style.RESET_ALL +"] " + "Choose reconnaissance option.")
        print("..........................................\n")
        self.reconnaissance_option();
        opt = str(input("[+] Insert an option: "))
        self.exploit_option(opt);
        
        
    def exploit_option(self, opt):
        opt = str(opt);
        if opt == "1":
            # self.clear()
            clear_screen_and_provide_with_banner.cstad_banner_();
            website = input("[+] Enter Website :")
            loading.loading_animation()
            website_information.get_ip_info(website)
            print("...............................")
            print(" ")
            input("Press key to continues...")
            self.reconnaissance_option()
            opt = int(input("Choose an option (1-5, 99 to back): "))
            self.exploit_option(opt)
        elif opt == "2":
            self.clear()
            cstad_banner.start_banner();
            website = input("[+] Enter Website :")
            loading.loading_animation()
            mail_server.find_mx_records(website)
            print("...............................")
            print(" ")
            input("Press key to continues...")
            self.reconnaissance_option()
            opt = int(input("Choose an option (1-5, 99 to back): "))
            self.exploit_option(opt)
        elif opt == "3":
            self.clear()
            banner.start_banner();
            website = input("[+] Enter Website :")
            port_scanning.perform_port_scan(website)
            print("...............................")
            print(" ")
            input("Press key to continues...")
            self.reconnaissance_option()
            opt = int(input("Choose an option (1-5, 99 to back): "))
            self.exploit_option(opt)
        elif opt == "4":
            self.clear()
            banner.start_banner();
            website = input("[+] Enter Website :")
            security_header.security_header_scan(website)
            print("...............................")
            print(" ")
            input("Press key to continues...")
            self.reconnaissance_option()
            opt = int(input("Choose an option (1-5, 99 to back): "))
            self.exploit_option(opt)
        elif opt == "5":
            self.clear()
            banner.start_banner();
            website = input("[+] Enter Website :")
            whois_scanning.whios_scan(website)
            print("...............................")
            print(" ")
            input("Press key to continues...")
            self.reconnaissance_option()
            opt = int(input("Choose an option (1-5, 99 to back): "))
            self.exploit_option(opt)
        elif opt == "0" or opt.lower().replace(" ","") =="back":
            template.cyber_stad();
        elif opt == "99":
            print("=> Exited tool. :)")
            sys.exit(0);
            
        elif opt.lower().replace(" ","") == "clear":
            clear_screen_and_provide_with_banner.start();
            self.choose_option();
        else:
            print(Fore.RED + "=> Invalid option range, options are number 1 and number 5" + Style.RESET_ALL)
            self.choose_option();
