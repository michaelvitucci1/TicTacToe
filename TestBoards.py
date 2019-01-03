import numpy
import StartGame

scratch_board = numpy.byte([[1, 0, 1], [2, 1, 1], [2, 1, 2]])
print(StartGame.is_scratch(scratch_board))
