def get_method():
    return {'passive': True, 'active': False}

def passive(benchmark, **kwargs):
    return 'time ./local-flav1'+ ' -p'+kwargs['compiler']



def active(benchmark, **kwargs):
    pass
