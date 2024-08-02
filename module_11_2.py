import inspect
import pprint


class Unknown:
    def __init__(self):
        self.__x = 0

    def getInfo(self):
        return 'Не скажу ' + str(self.__x)


def introspection_info(obj):
    type_object = type(obj)
    attr_object = inspect.getmembers(obj)
    methods_object = inspect.getmembers(obj)
    module = inspect.getmodule(obj)
    doc = inspect.getdoc(obj)
    info = {'type': type_object,
            'attributes': attr_object,
            'methods': methods_object,
            'module': module,
            'documentation': doc}
    return info


unknown = Unknown()
number_info = introspection_info(unknown)
pprint.pprint(number_info)
