class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# Метод __call__ был неправильно написан как str, это должен быть __call__.
# В условии if cls in cls._instances проверяли, если класс уже присутствует в _instances, 
# но должно быть наоборот: if cls not in cls._instances.