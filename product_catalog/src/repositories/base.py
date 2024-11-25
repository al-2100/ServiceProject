from abc import ABC, abstractmethod
from typing import Any, List, Optional

class BaseRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Any]:
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[Any]:
        pass

    @abstractmethod
    def create(self, data: Any) -> Any:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> Optional[Any]:
        pass
