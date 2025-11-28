def field(items, *args):
    if not args:
        return
    if len(args) == 1:
        key = args[0]
        for d in items:
            val = d.get(key)
            if val is not None:
                yield val
    else:
        for d in items:
            new_dict = {}
            for key in args:
                val = d.get(key)
                if val is not None:
                    new_dict[key] = val

            if new_dict:
                yield new_dict
