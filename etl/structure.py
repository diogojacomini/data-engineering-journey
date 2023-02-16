from abc import ABC, abstractmethod


class ETL(ABC):

    def __init__(self, input, output):
        self.input = input
        self.output = output

    def controller_etl(self):
        '''This is the main method of the ETL class, this gona make Extraction, Transformation and Load'''
        self.extract()
        self.transform()
        self.load()

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def load(self):
        pass
