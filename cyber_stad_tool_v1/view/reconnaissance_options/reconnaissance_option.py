from abc import ABC
from weapons.information_gathering import website_information


class Reconnaissance(ABC):
    def reconnsiassance_more_options():
        pass
    def start_reconnaissance(self):
        website_information.start_ip_scanning();