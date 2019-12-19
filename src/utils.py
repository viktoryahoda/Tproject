def combine(a, b):
    if len(a) < len(b):
        ls = [x for x in zip(a, b[:-1*(len(b) - len(a))]) for x in x]
        return ls + b[-1*(len(b) - len(a)):]
    if len(a) > len(b):
        ls = [x for x in zip(a[:-1 * (len(a) - len(b))], b) for x in x]
        return ls + a[-1*(len(a) - len(b)):]
    if len(a) == len(b):
        ls = [x for x in zip(a, b) for x in x]
        return ls
