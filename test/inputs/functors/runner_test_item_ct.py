def get_method():
  return {'passive': True, 'active': False}


def passive(benchmark, **kwargs):
  return 'Runner'


def active(benchmark, **kwargs):
  pass
