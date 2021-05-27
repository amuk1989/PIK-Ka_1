from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass
    @abstractmethod
    def add_marker(self, request) -> Optional[bool]:
        pass
    @abstractmethod
    def insert_marker(self, request)  -> Optional[bool]:
        pass

class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def add_marker(self, request: Any, marker) -> bool:
        if self._next_handler:
            return self._next_handler.add_marker(request, marker)
        return None

    @abstractmethod
    def insert_marker(self, request: Any, marker) -> bool:
        if self._next_handler:
            return self._next_handler.insert_marker(request, marker)
        return None

    @abstractmethod
    def delete_marker(self, request: Any, marker) -> bool:
        if self._next_handler:
            return self._next_handler.delete_marker(request, marker)
        return None