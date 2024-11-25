from abc import ABC, abstractmethod
from typing import Any

class BaseRepository(ABC):
    @abstractmethod
    def get_all(self) -> Any:
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> Any:
        pass

    @abstractmethod
    def create(self, entity: Any) -> Any:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> Any:
        pass
