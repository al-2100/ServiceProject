from abc import ABC, abstractmethod
from typing import Any

class BaseService(ABC):
    @abstractmethod
    def get_all(self) -> Any:
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> Any:
        pass

    @abstractmethod
    def create(self, data: Any) -> Any:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> Any:
        pass
