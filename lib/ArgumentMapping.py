"""
File: Runner.py
Author: JP Lehr
Email: jan.lehr@sc.tu-darmstadt.de
Github: https://github.com/jplehr
Description: Module provides mapper classes to handle argument.
"""

import sys
sys.path.append('..')


class ArgumentMapper:

  def as_list(self):
    l = []
    for p in self:
      l.append(p)

    return l


class CmdlineLinearArgumentMapper(ArgumentMapper):
  """
  Mapper to create a linear mapping of one or more commandline passed arguments.
  If given more than one argument, it acts like a zip iterator, therefore, all arguments
  must receive the same number of values.
  """

  def __init__(self, argmap):
    self._argmap = argmap
    arg_vals = self._argmap.values()
    l_elem = list(arg_vals)[0]
    for e in arg_vals:
      if len(e) is not len(l_elem):
        raise RuntimeError('CmdlineLinearArgumentMapper: All parameters need the same number of values')

  def __iter__(self):
    if len(self._argmap.keys()) is 1:
      key = list(self._argmap.keys())[0]
      for v in self._argmap[key]:
        yield (key, v)

    else:
      raise RuntimeError('Currently not supported: Only single param allowed')

  def __getitem__(self, key):
    if key is 0:
      key = list(self._argmap.keys())[0]
      return (key, self._argmap[key][0])

    else:
      raise IndexError('Only direct access to first element allowed.')


class CmdlineCartesianProductArgumentMapper(ArgumentMapper):
  """
  Mapper to create the Cartesian product of all given argument/values. All arguments passed
  via the commandline. Here, the arguments do not need to have equally many values.
  """
  pass


class ArgumentMapperFactory:
  """
  Creates the correct ArgumentMapper for the specific circumstance.
  """

  @classmethod
  def get_mapper(cls, options):
    requested_mapper = options['mapper']

    if requested_mapper == 'Linear':
      return CmdlineLinearArgumentMapper(options['argmap'])
    elif requested_mapper == 'CartesianProduct':
      return CmdlineCartesianProductArgumentMapper()
    else:
      raise RuntimeError('Unknown Mapper: ' + requested_mapper)
