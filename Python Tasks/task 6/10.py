import numpy
N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(storage, axis=1), axis=0))