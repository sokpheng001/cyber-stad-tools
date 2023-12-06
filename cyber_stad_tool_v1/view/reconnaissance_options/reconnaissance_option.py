from abc import ABC
from weapons.information_gathering import website_information
from view.reconnaissance_options import option
from components import one_second_loading


class Reconnaissance(ABC):
    def reconnsiassance_more_options():
        pass
    def start_reconnaissance(self):
        one_second_loading.loading_animation(1);
        option1 = option.Option();
        option1.choose_option();
