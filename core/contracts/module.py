from abc import ABC, abstractmethod


class I34Module(ABC):

    @abstractmethod
    def handle(self, request):
        pass
