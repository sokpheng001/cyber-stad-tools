import subprocess
from colorama import Fore, Style
from components import banner,loading
from weapons import reconnaisance
from view.exploit_options import exploit_option
import sys
from components import clear_screen_and_provide_with_banner, clear_screen,exit_message, invalid_input_option_message;
from datetime import datetime
from view.reconnaissance_options import reconnaissance_option;

shell_script = """

# Add more commands as needed
"""


def started_tool_date()-> None:
# Get the current date and time
    current_datetime = datetime.now()
    # Format the date and time as a string with the month in English
    formatted_datetime = current_datetime.strftime("%Y-%B-%d Time: %H:%M:%S %p")
    
    print("[" + Fore.GREEN + "***" + Style.RESET_ALL +"] "  + "Started Tool:", formatted_datetime);
    print("[" + Fore.GREEN + "***" + Style.RESET_ALL +"] "  + "HAPPY HACKING")
        # Print the formatted date and time

class Template(exploit_option.Exploit, reconnaissance_option.Reconnaissance):
    def start_reconnaissance(self):
        return super().start_reconnaissance();
    def exploit_option(self):
        return super().exploit_option();
    #list of main options
    __main_options = [1,2]
    # list of every option
    __options = [1,2,3,4,5,6,7]
    # choice
    __choice = 0
    #display body
    # add more options here ////////////////////////////////  
        # implementation of logic for choosing options
    def choose_option(self):
        try:
            #insert option
            self.__choice = str(input("[+] Insert an option: "));
            # check is with clear keyword
            if self.__choice.lower() == "exit" :
                exit_message.exit_tool_message();
                sys.exit(0);
            #convert option value to integer
            # self.__choice = int(self.__choice);
            # if self.__choice is an integer, then call the following method
            self.start_options(self.__choice);
            # end;
        # except ValueError:
        #     invalid_input_option_message();
        #     self.choose_option();
        except KeyboardInterrupt:
            exit_message.exit_tool_message()
            sys.exit(0);
    def display_options(self):
        print("\n[" + Fore.GREEN + "*" + Style.RESET_ALL +"] " +"Choose an option to do Pentesting on the web application.")
        print("..........................................\n")
        print("1-> Start Reconnaissance")
        print("2-> Start Social Engineering")
        print("3-> Start Exploits")
        print("8-> Generate reports")
        # print("2-> Start Expliots")
        print("---");
        print(Fore.GREEN + "(To restart or reload tools) -> " + Style.RESET_ALL +  "Use reload/restart/r commands ")
        print(Fore.GREEN + "(To clear) -> " + Style.RESET_ALL +  "Use \'clear\' command ")
        print(Fore.RED + "(99 or Ctr + C or Exit) -> " + Style.RESET_ALL +  "To Exit ")
        print("---");
        # start choosing option
        self.choose_option();
    # add more options here ////////////////////////////////  
    #////////////////////////////////////////////////////////////////////////////////////////////////

    #This method can be mutable
    # //////////////////////////////////////////////////////////////////////////
    def start_options(self, opt):
        try:
            if opt =="1":
                self.start_reconnaissance();
            elif opt == "2":
                print("Social engineering")
            elif opt =="3":
                loading.loading_animation();
                clear_screen_and_provide_with_banner.start();
                self.exploit_option();
            elif opt =="8":
                print("Generate reports");
            elif opt.lower().replace(" ", "") == "reload" or opt.lower().replace(" ", "") == "restart" or opt.lower().replace(" ", "") == "r":
                # reload our tools
                # Use subprocess to run the shell script
                print("[+] Restarting tools...");
                subprocess.run(['python','main.py'])
                # 
            elif opt.lower().replace(" ", "") == "banner":
                clear_screen_and_provide_with_banner.start();
                self.display_options();
                
            elif opt.lower().replace(" ","") == "clear":
                clear_screen.clear_screen();
                self.display_options();
            elif opt.lower().replace(" ","") == "cleear" or opt.lower() == "clea":
                print(Fore.RED + "=> Invalid command, it looks like you want to use \'clear\' command :) .!!!" + Style.RESET_ALL);
                self.choose_option();         
            elif opt == "99" :
                exit_message.exit_tool_message();
                sys.exit(0);
            else:
                invalid_input_option_message.invalid_input_option_message();
                self.choose_option();      
        except KeyboardInterrupt as error:
            exit_message.exit_tool_message()
            sys.exit(0);
               
    #//////////////////////////////////////////////////////////////// 

        

# start tool options 
def cyber_stad():
    clear_screen.clear_screen();
    started_tool_date();
    banner.start_banner();
    view1 = Template();
    while True:
        view1.display_options();