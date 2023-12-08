from abc import abstractmethod

class SPAlgorithm():

    @abstractmethod
    def calc_sp(self, graph, source, dest):
        pass