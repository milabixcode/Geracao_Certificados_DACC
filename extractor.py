from entities import Certificate
from typing import List
from abc import (
    ABC,
    abstractmethod,
)

# ABC = abstract base classes

# Padrão strategy

class BaseExtractor(ABC):
    @abstractmethod
    def extract(self, file_path, identifier) -> List[Certificate]:
        pass

# ...

class ArquivoNormalExtractor(BaseExtractor):
    def extract(self, file_path, identifier) -> List[Certificate]:
        pass
