def unique_in_order(iterable):return [i for i in [c if i==0 else list(iterable) if len(list(iterable))==1 else c if not i==0 and not list(iterable)[i-1]==c else None for i,c in enumerate(list(iterable))] if not i is None]