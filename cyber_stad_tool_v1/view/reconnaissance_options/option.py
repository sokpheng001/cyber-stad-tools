import os
import sys
import time
from abc import ABC
from colorama import Fore, Style

from termcolor import colored
from components import exit_message,one_second_loading,clear_screen_and_provide_with_banner, cstad_banner, clear_screen, check_is_domain_name, invalid_input_option_message
from weapons.information_gathering import website_information, mail_server, port_scanning, security_header, whois_scanning
from view import template
import subprocess

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
        print("\n[" + Fore.GREEN + "*" + Style.RESET_ALL +"] " + "Choose reconnaissance option.")
        print("..........................................\n")
        print(self.item(0), "Back to previous options")
        print(self.item(1), "Website Information ")
        # print(self.item(2), "Phone Number Information ")
        print(self.item(2), "Find IP Address And E-mail Server ")
        print(self.item(3), "Port Scanning")
        print(self.item(4), "Security Headers ")
        print(self.item(5), "Whois Scanning")
        print("---")
        print(Fore.RED + "(99 or Ctr + C or Exit) -> " + Style.RESET_ALL +  "To Exit ")
        print("---");
        
    def press_enter_to_continue(self):
        print("...............................")
        print(" ")
        input("Press key to continues...")
        print("---")
        
    def choose_option(self, clear_screen_type=None)->None:
        if clear_screen_type != None:
            clear_screen_and_provide_with_banner.cstad_banner_();
        else:
            clear_screen.clear_screen();
        self.reconnaissance_option();
        try:
            opt = str(input("[+] Insert an option: "))
            self.exploit_option(opt, "provide  a banner");
        except KeyboardInterrupt as error:
            exit_message.exit_tool_message();
            sys.exit(0);
            
    def verify_domain_name_and_exploit_choice(self,option, banner=None, content=None) ->None:
        # self.clear()
            if banner == None:
                clear_screen.clear_screen();
            else:
                clear_screen_and_provide_with_banner.cstad_banner_();
            print(f"[*] {content}");
            print("[!] Type "+Fore.GREEN + "\'back/b\' or \'exit/e\' " + Style.RESET_ALL + "to Return");
            website = str(input("[+] Input target IP address/domain name: "))
            if website.lower().replace(" ", "") == "exit" or website.lower().replace(" ", "") == "back" or website.lower().replace(" ", "") == "e" or website.lower().replace(" ", "") == "b":
                print("[*] Return back...")
                time.sleep(0.5)
                self.choose_option("Provide a banner");
            elif website.lower().replace(" ", "") == "reload" or website.lower().replace(" ", "") == "restart" or website.lower().replace(" ", "") == "r" or website.lower().replace(" ", "") == "re":
                # reload our tools
                # Use subprocess to run the shell script
                print("[+] Restarting tools...");
                subprocess.run(["python", "main.py"]);
            # check is domain name
            if check_is_domain_name.is_valid_domain_name(website):
                # 
                if option==1:
                    one_second_loading.loading_animation_for_reconnaissance_feature(1, content="Scannign IP address")
                    website_information.get_ip_info(website);
                    print("...............................")
                    print(" ")
                    input("Press key to continues...")
                    print("---")
                elif option == 2:
                    one_second_loading.loading_animation_for_reconnaissance_feature(1,content="Finding MX records") 
                    mail_server.find_mx_records(website);
                    self.press_enter_to_continue()
                # 
                elif option == 3:
                    port_scanning.perform_port_scan(website);
                    self.press_enter_to_continue()
                elif option == 4:
                    security_header.security_header_scan(website)
                    self.press_enter_to_continue()
                elif option == 5:
                    whois_scanning.whios_scan(website)
                    self.press_enter_to_continue()
                # end
                self.reconnaissance_option();
                opt = str(input("[+] Insert an option: "))
                self.exploit_option(opt, "provide  a banner")
            else:
                print(Fore.RED + "=> Invalid domain name. Please enter a domain name once again." + Style.RESET_ALL);
                time.sleep(2);
                self.exploit_option(opt=option,banner="provide a banner");      

    def exploit_option(self, opt, banner=None):
        opt = str(opt);
        if opt == "1":
            self.verify_domain_name_and_exploit_choice(option=1, banner=banner, content="Gather IP Address information from website.");
            # 
        elif opt == "2":
            self.verify_domain_name_and_exploit_choice(option=2, banner=banner,content="Finding MX record");
        elif opt == "3":
            self.verify_domain_name_and_exploit_choice(option=3, banner=banner, content="Port scanning");
        elif opt == "4":
            self.verify_domain_name_and_exploit_choice(option=4, banner=banner,content="Security HTTP header");
        elif opt == "5":
            self.verify_domain_name_and_exploit_choice(option=5, banner=banner, content="Whois scanning");
        elif opt.lower().replace(" ", "") == "clear" or opt.lower().replace(" ","") == "cls":
            self.choose_option();
        elif opt.lower().replace(" ", "") == "banner":
            self.choose_option("Provide a banner");        
        elif opt == "0" or opt.lower().replace(" ","") =="back" or opt.lower().replace(" ","") =="b":
            template.cyber_stad();
        elif opt.lower().replace(" ", "") == "reload" or opt.lower().replace(" ", "") == "restart" or opt.lower().replace(" ", "") == "r":
                # reload our tools
                # Use subprocess to run the shell script
                print("[+] Restarting tools...");
                subprocess.run(['python','main.py'])
                
        elif opt == "0":
            exit_message.exit_tool_message();
            sys.exit(0);
        else:
            print(Fore.RED + "=> Invalid option range, options are number 1 and number 5" + Style.RESET_ALL)
            time.sleep(1);
            self.choose_option(clear_screen_type="providing a banner");
