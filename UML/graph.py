from abc import abstractmethod

class Graph():

    @abstractmethod
    def get_adj_nodes(self,node):
        pass

    @abstractmethod
    def add_node(self, node):
        pass

    @abstractmethod
    def add_edge(self, start, end):
        pass

    @abstractmethod
    def get_num_of_nodes(self):
        pass
