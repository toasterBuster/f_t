from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def query(self, **kwargs):
        pass
    
    @property
    @abstractmethod
    def name(self):
        pass