class LibUc(object):

    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        self.__lib_name = 'LibUc'
        pass
    
    def print_args_kwargs(self, *args, **kwargs):
        print('{}: args={}, kwargs={}'.format(self.__lib_name, args, kwargs))
        pass

    def keyword(self):
        pass
