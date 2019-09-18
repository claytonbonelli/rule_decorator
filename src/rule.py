from functools import wraps


def rule(order=0):
    """
    Decorator for methods.
    :param order: define the execution order
    """
    # "order" not informed
    if callable(order):
        @wraps(order)
        def wrapper(self):
            order(self)

        wrapper.__ruled = True
        wrapper.__order = 0
        return wrapper

    # "order" eh um valor inteiro
    else:
        def real_rule(method):
            @wraps(method)
            def wrapper(self):
                method(self)

            wrapper.__ruled = True
            wrapper.__order = (order or 0)
            return wrapper
        return real_rule


def validate(rule_class, *args, **kwargs):
    """
    Execute each method decorated with "@rule".
    :param data:
    :param rule_class:
    """
    instance = rule_class(*args, **kwargs)

    # Get all decorated methods with "@rule"
    dictionary = {}
    for method in dir(instance):
        attr = getattr(instance, method)
        if callable(attr) and '__ruled' in dir(attr):
            dictionary.setdefault(attr.__order, []).append(attr)

    # No one method?
    if not len(dictionary):
        return

    # Execution order
    ordered_keys = sorted(dictionary)

    # Execute each method
    for key in ordered_keys:
        methods = dictionary.get(key)
        for method in methods:
            method()
