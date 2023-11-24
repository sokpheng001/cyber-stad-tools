from abc import ABC

class Option(ABC):
    def reconnaissance_option(self):
        print("This is reconnaisance option");
    def exploit_option(self):
        print("This is exploit option")