
import inspect
from pprint import pprint

def introspection_info(obj):


    obj_type = type(obj).__name__

    attributes = [i for i in dir(obj) if not i.startswith('__')]

    methods = [i for i in dir(obj) if callable(getattr(obj, i)) and not i.startswith('__')]

    module = getattr(obj, '__module__', '__main__')

    result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return result

number_info = introspection_info(42)
pprint(number_info)