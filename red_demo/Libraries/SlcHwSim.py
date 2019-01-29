from Config import *
from LibBase import user_keyword
from HwSim import HwSim


class SlcHwSim(HwSim):
    def __init__(self):
        super(SlcHwSim, self).__init__()
        pass

    @user_keyword(projects=(PROJECT_SLC_MIT,))
    def set_main_1_voltage(self, l1: float, l2: float, l3: float):
        print('FOR SLC: set main 1 voltage ({}, {}, {})'.format(l1, l2, l3))
        pass

    @user_keyword(projects=(PROJECT_SLC_MIT,))
    def set_output_relay_state(self, name: str, state: int):
        print('FOR SLC: set output relay ({}, {})'.format(name, state))
        pass

    pass
