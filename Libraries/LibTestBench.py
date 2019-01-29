from Config import *
from LibBase import user_keyword, LibBase
from HwSim import HwSim


class LibTestBench(LibBase):
    ROBOT_LIBRARY_VERSION = 1.0
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        super(LibTestBench, self).__init__()

        if PROJECT == PROJECT_UC_MIT:
            from UcHwSim import UcHwSim
            self.__hw_sim_type = UcHwSim
            pass
        elif PROJECT == PROJECT_SLC_MIT:
            from SlcHwSim import SlcHwSim
            self.__hw_sim_type = SlcHwSim
            pass
        else:
            self.__hw_sim_type = HwSim
            pass
        self.__hw_sim = None
        self.__hw_sim_keywords = self.__hw_sim_type.collect_keywords()
        self.__collect_global_keywords()
        pass

    def __get_robot_metadata(self, name: str):
        try:
            return self.__global_keywords[name]
        except KeyError:
            raise ValueError('invalid keyword: {}'.format(name))
            pass
        pass

    def __collect_global_keywords(self):
        self.__global_keywords = {}
        for _name, _rm in self._keywords.items():
            self.__global_keywords[_name] = _rm
            pass

        for _name, _rm in self.__hw_sim_keywords.items():
            _key = 'tb_{}'.format(_name)
            if _rm.projects is None:
                self.__global_keywords[_key] = _rm
                pass
            else:
                if PROJECT in _rm.projects:
                    self.__global_keywords[_key] = _rm
                    pass
                else:
                    pass
                pass
            pass
        pass

    @property
    def _hw_sim(self) -> HwSim:
        if self.__hw_sim is None:
            raise SystemError('HwSim is invalid')
        return self.__hw_sim

    @user_keyword()
    def tb_initialize_library(self):
        print('FOR ALL PROJECTS: initialize test bench library')
        self.__hw_sim = self.__hw_sim_type()
        pass

    @user_keyword()
    def tb_clean_up_library(self):
        print('FOR ALL PROJECTS: clean up test bench library')
        self.__hw_sim = None
        pass
    
    def get_keyword_names(self):
        return self.__global_keywords.keys()

    def get_keyword_arguments(self, name):
        _rm = self.__get_robot_metadata(name)
        return _rm.args

    def get_keyword_types(self, name):
        _rm = self.__get_robot_metadata(name)
        return _rm.types

    def run_keyword(self, name: str, args, kwargs):
        _rm = self.__get_robot_metadata(name)
        _method_name = _rm.method_name
        if self.has_keyword(name):
            return self.run_self_keyword(name, args, kwargs)
        else:
            if name.startswith('tb_'):
                _name = name[3:]
                pass
            else:
                _name = name
                pass
            if self._hw_sim.has_keyword(_name):
                return self._hw_sim.run_self_keyword(_name, args, kwargs)
            else:
                pass
            raise ValueError('run invalid keyword: {}'.format(name))
        pass


def demo():
    _tb = LibTestBench()
    _tb.tb_initialize_library()
    print(_tb.get_keyword_names())
    print(_tb.get_keyword_arguments('tb_set_breaker_state'))
    print(_tb.get_keyword_types('tb_set_breaker_state'))
    _tb.run_keyword('tb_set_breaker_state', args=(), kwargs={'state': 1, 'name': 'imb'})
    pass


if __name__ == '__main__':
    demo()
    pass

