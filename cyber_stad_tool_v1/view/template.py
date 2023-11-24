import logging
from colorama import Fore, Style
from abc import ABC, abstractmethod
from components import banner,loading
from weapons import reconnaisance
import sys

class Option(ABC):
    def reconnaissance_option(self):
        print("This is reconnaisance option");
    def exploit_option(self):
        print("This is exploit option")

class Template(Option):
    #list of main options
    __main_options = [1,2]
    # list of every option
    __options = [1,2,3,4,5,6,7]
    # choice
    __choice = 0
    #This method can be mutable
    def start_options(self, opt):
        if opt ==1:
            super().reconnaissance_option()
        elif opt ==2:
            loading.loading_animation();
            super().exploit_option()
        elif opt == 3 :
            print("=> Exiting tool. :)")
            sys.exit(0);
        else:
            print(Fore.RED + "=> Invalid option range, options are number 1 and number 2" + Style.RESET_ALL);
            self.choose_option();         
    # implementation of logic for choosing options
    def choose_option(self):
        try:
            self.__choice = str(input("[+] Insert an option: "));
            # check is with clear keyword
            if self.__choice.lower() == "exit":
                print("\n=> Exiting tool. :)")
                sys.exit(0);
            self.__choice = int(self.__choice);
            # fi self.__choice is an integer call the following method
            self.start_options(self.__choice);
        except ValueError:
            print(Fore.RED + "=> Invalid option as string, please check try again as number in option.!!!" + Style.RESET_ALL);
            self.choose_option();
        except KeyboardInterrupt:
            print("\n\n=> Exiting tool. :)")
            sys.exit(0);
    #display body
    def display_options(self):
        print("[" + Fore.GREEN + "*" + Style.RESET_ALL +"] " +"Choose an option to do Pentesting on the web application.")
        print("..........................................\n")
        print("1-> Start Reconnaissance")
        print("2-> Start Expliots")
        print(Fore.RED + "(3 or Ctr + C or Exit) -> " + Style.RESET_ALL +  "To Exit ")
        print("---");
        # start choosing option
        self.choose_option();
        

# start tool options 
def cyber_stad():
    banner.start_banner();
    view = Template();
    view.display_options();