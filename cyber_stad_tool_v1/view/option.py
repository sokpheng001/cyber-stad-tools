import sys
from abc import ABC
from weapons import sql_injection

option = None;

#what to do with
class Option(ABC):
    global option
    def reconnaissance_option(self):
        print("This is reconnaisance option");
    def exploit_option(self):
        print("1. SQL Injection.")
        print("99. To Exit.")
        try:
            option = int(input("[+] Insert an option: "));
            # check is with clear keyword
            if option == 99:
                print("\n=> Exited tool. :)")
                sys.exit(0);
            elif option==1:
                sql_injection.start_sql_injection();
        except ValueError as error: 
            self.exploit_option();