from Config import *
from LibBase import user_keyword
from HwSim import HwSim


class UcHwSim(HwSim):
    def __init__(self):
        super(UcHwSim, self).__init__()
        pass

    @user_keyword(projects=(PROJECT_UC_MIT,))
    def set_main_1_voltage(self, l1: float, l2: float, l3: float):
        print('FOR UC: set main 1 voltage ({}, {}, {})'.format(l1, l2, l3))
        pass

    @user_keyword(projects=(PROJECT_UC_MIT,))
    def set_dc_voltage(self, l1: float, l2: float, l3: float):
        print('FOR UC: set dc voltage ({}, {}, {})'.format(l1, l2, l3))
        pass
    pass
