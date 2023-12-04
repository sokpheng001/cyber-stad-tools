import logging
from colorama import Fore, Style
from components import banner,loading
from weapons import reconnaisance
from view import option
import sys


class Template(option.Option):
    #list of main options
    __main_options = [1,2]
    # list of every option
    __options = [1,2,3,4,5,6,7]
    # choice
    __choice = 0
    #display body
    # add more options here ////////////////////////////////  
    def display_options(self):
        print("[" + Fore.GREEN + "*" + Style.RESET_ALL +"] " +"Choose an option to do Pentesting on the web application.")
        print("..........................................\n")
        print("1-> Start Reconnaissance")
        print("2-> Start Exploits")
        # print("2-> Start Expliots")
        print(Fore.RED + "(99 or Ctr + C or Exit) -> " + Style.RESET_ALL +  "To Exit ")
        print("---");
        # start choosing option
        self.choose_option();
    # admore options here ////////////////////////////////  
    #////////////////////////////////////////////////////////////////////////////////////////////////
    # implementation of logic for choosing options
    def choose_option(self):
        try:
            #insert option
            self.__choice = str(input("[+] Insert an option: "));
            # check is with clear keyword
            if self.__choice.lower() == "exit":
                print("\n=> Exited tool. :)")
                sys.exit(0);
            #convert option value to integer
            self.__choice = int(self.__choice);
            # if self.__choice is an integer, then call the following method
            self.start_options(self.__choice);
            # end;
        except ValueError:
            print(Fore.RED + "=> Invalid option as string, please check try again as number in option.!!!" + Style.RESET_ALL);
            self.choose_option();
        except KeyboardInterrupt:
            print("\n\n=> Exited tool. :)")
            sys.exit(0);
    #This method can be mutable
    # //////////////////////////////////////////////////////////////////////////
    def start_options(self, opt):
        if opt ==1:
            super().reconnaissance_option()
            opt = int(input("Choose an option (1-2, 99 to exit): "))
            super().exploit_option(opt)
        elif opt ==2:
            loading.loading_animation();
            super().exploit_option()
        elif opt == 99 :
            print("=> Exited tool. :)")
            sys.exit(0);
        else:
            print(Fore.RED + "=> Invalid option range, options are number 1 and number 2" + Style.RESET_ALL);
            self.choose_option();         
    #//////////////////////////////////////////////////////////////// 

        

# start tool options 
def cyber_stad():
    banner.start_banner();
    view = Template();
    view.display_options();