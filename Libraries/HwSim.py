from Config import *
from LibBase import user_keyword, LibBase


class HwSim(LibBase):
    def __init__(self):
        super(HwSim, self).__init__()
        pass

    @user_keyword(projects=(PROJECT_SLC_MIT, PROJECT_UC_MIT))
    def set_main_1_voltage(self, l1: float, l2: float, l3: float):
        self._not_implement(l1, l2, l3)
        pass

    @user_keyword(projects=(PROJECT_SLC_MIT, PROJECT_UC_MIT))
    def set_main_2_voltage(self, l1: float, l2: float, l3: float):
        self._not_implement(l1, l2, l3)
        pass

    @user_keyword(projects=(PROJECT_SLC_MIT, PROJECT_UC_MIT))
    def set_breaker_state(self, name: str, state: int):
        self._not_implement(name, state)
        pass

    @user_keyword()
    def print_log(self, level: int, fmt: str = '', *args, **kwargs):
        print('LOG[{:0>2}]: {}'.format(level, fmt.format(*args, **kwargs)))
        pass
    pass
