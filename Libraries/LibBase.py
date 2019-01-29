from types import FunctionType
import inspect


class RobotKeywordAttr(object):
    def __init__(self, func: FunctionType, projects=None, name: str = None):
        _name = func.__name__ if name is None else name
        self.__name = self.format_name(_name)
        self.__args, self.__types = self.__parse_func(func)
        self.__projects = projects
        self.__method_name = func.__name__
        self.is_static_method = False
        pass

    @staticmethod
    def format_name(name: str):
        name = name.strip()
        name = name.lower()
        name = name.replace(' ', '_')
        return name

    @property
    def name(self):
        return self.__name

    @property
    def args(self):
        return self.__args if self.is_static_method else self.__args[1:]

    @property
    def types(self):
        return self.__types

    @property
    def projects(self):
        return self.__projects

    @property
    def method_name(self):
        return self.__method_name

    @staticmethod
    def __parse_func(func: FunctionType):
        _sig = inspect.signature(func)
        _args = []
        _types = {}
        for _i, _param in enumerate(_sig.parameters.values()):
            if _param.default is not _param.empty:
                _name = '{}={}'.format(_param.name, repr(_param.default))
                pass
            else:
                _name = _param.name
                pass

            if _param.kind == _param.VAR_POSITIONAL:
                _name = '*' + _name
                pass
            elif _param.kind == _param.VAR_KEYWORD:
                _name = '**' + _name
                pass
            else:
                pass
            _args.append(_name)
            if _param.annotation is not _param.empty:
                _types[_param.name] = _param.annotation
                pass
            pass
        return _args, _types
        pass

    def __str__(self):
        _ret = 'name: {}\n'.format(self.__name)
        _ret += 'args: {}\n'.format(self.__args)
        _ret += 'types: {}\n'.format(self.__types)
        _ret += 'projects: {}\n'.format(self.__projects)
        _ret += '{}method name: {}'.format('static ' if self.is_static_method else '', self.method_name)
        return _ret
    pass


def user_keyword(projects: tuple = None, name: str = None):
        def decorator(func: FunctionType):
            func.robot_metadata = RobotKeywordAttr(func, projects, name)
            return func
        return decorator
        pass


class LibBase(object):
    def __init__(self):
        self._keywords = self.collect_keywords()
        pass

    def has_keyword(self, name: str) -> bool:
        if name in self._keywords.keys():
            return True
        else:
            return False
        pass

    def run_self_keyword(self, name: str, args, kwargs):
        _rm = self._keywords[name]
        if isinstance(_rm, RobotKeywordAttr):
            _fun = getattr(self, _rm.method_name)
            return _fun(*args, **kwargs)
        else:
            raise SystemError('invalid keyword: {}'.format(name))
        pass

    @staticmethod
    def _not_implement(*args, **kwargs):
        _frame = inspect.stack()[1]
        print('********** CALL INFO **********')
        print('function: {}'.format(_frame.function))
        print('args    : {}'.format(args))
        print('kwargs  : {}'.format(kwargs))
        raise SystemError('the method({}: {} in line {}) is not implemented'.format(
            _frame.function,
            _frame.filename,
            _frame.lineno))
        pass

    @property
    def keywords(self) -> dict:
        return self._keywords

    @classmethod
    def collect_keywords(cls) -> dict:
        _ret = {}

        for _name, _ in inspect.getmembers(cls, inspect.isroutine):
            _fun = getattr(cls, _name)
            if hasattr(_fun, 'robot_metadata'):
                _ret[_fun.robot_metadata.name] = _fun.robot_metadata
                for _b in inspect.getmro(cls):
                    try:
                        _obj = _b.__dict__[_name]
                        _fun.robot_metadata.is_static_method = isinstance(_obj, staticmethod)
                        break
                        pass
                    except KeyError:
                        pass
                    pass
                pass
            else:
                pass
            pass
        return _ret
    pass

# ======================================================================================================================
# Demo


class LibDemo(LibBase):
    def __init__(self):
        super(LibDemo, self).__init__()
        pass

    @user_keyword(name='this is the first keyword')
    def my_keyword(self):
        print('*****')
        print('run my keyword')
        print('=====')
        pass

    @staticmethod
    def test_fun(arg1: int):
        pass

    @classmethod
    @user_keyword()
    def class_method(cls, arg: int):
        pass
    pass


def demo():
    _lib_type = LibDemo
    for _item in _lib_type.collect_keywords().items():
        print('******************************')
        print(_item[0])
        print('------------------------------')
        print(_item[1])
        print('')
        pass
    _lib = _lib_type()
    if _lib.has_keyword('this_is_the_first_keyword'):
        _lib.run_self_keyword('this_is_the_first_keyword', (), {})
        pass
    pass


if __name__ == '__main__':
    demo()
    pass
