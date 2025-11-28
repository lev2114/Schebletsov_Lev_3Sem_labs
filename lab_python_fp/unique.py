class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.used_values = set()
        self.ignore_case = kwargs.get("ignore_case", False)

    def __next__(self):
        while True:
            try:
                new_value = next(self.items)
            except StopIteration:
                raise StopIteration

            if self.ignore_case and isinstance(new_value, str):
                key = new_value.lower()
            else:
                key = new_value

            if key not in self.used_values:
                self.used_values.add(key)
                return new_value


    def __iter__(self):
        return self
