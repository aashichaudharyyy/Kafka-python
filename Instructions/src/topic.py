"""
Simulated Topic Module
Provides in-memory event channels mimicking Kafka topic functionality without
requiring external brokers, ZooKeeper, or Docker.
"""

from queue import Queue, Empty
from typing import Any, List, Optional, Dict


class Topic:
    """
    Simulated Kafka topic using an in-memory message buffer.
    Supports publish-consume FIFO semantics.
    """
    def __init__(self, name: str = "system-events"):
        self.name: str = name
        self.messages: List[Any] = []

    def publish(self, event: Any) -> None:
        """Publishes an event to the topic channel."""
        self.messages.append(event)

    def consume(self) -> Optional[Any]:
        """
        Consumes the next event from the channel in FIFO order.
        Returns None if no events remain.
        """
        if self.messages:
            return self.messages.pop(0)
        return None

    def append(self, event: Any) -> None:
        """Alias for publish to maintain compatibility with list-like simulations."""
        self.publish(event)

    def pop(self, index: int = 0) -> Optional[Any]:
        """Alias for consume to maintain compatibility with list-like simulations."""
        if self.messages and index == 0:
            return self.consume()
        elif self.messages:
            return self.messages.pop(index)
        return None

    def is_empty(self) -> bool:
        """Returns True if the topic currently contains no unconsumed messages."""
        return len(self.messages) == 0

    def size(self) -> int:
        """Returns the number of unconsumed messages in the topic."""
        return len(self.messages)

    def clear(self) -> None:
        """Clears all unconsumed messages."""
        self.messages.clear()

    def __len__(self) -> int:
        return len(self.messages)

    def __repr__(self) -> str:
        return f"<Topic name='{self.name}' pending_messages={len(self.messages)}>"


class QueueTopic:
    """
    Thread-safe Queue-based topic simulation using Python's built-in queue.Queue.
    """
    def __init__(self, name: str = "system-events"):
        self.name: str = name
        self._queue: Queue = Queue()

    def publish(self, event: Any) -> None:
        self._queue.put(event)

    def consume(self, block: bool = False, timeout: Optional[float] = None) -> Optional[Any]:
        try:
            return self._queue.get(block=block, timeout=timeout)
        except Empty:
            return None

    def put(self, event: Any) -> None:
        self.publish(event)

    def get(self, block: bool = False, timeout: Optional[float] = None) -> Optional[Any]:
        return self.consume(block=block, timeout=timeout)

    def is_empty(self) -> bool:
        return self._queue.empty()

    def size(self) -> int:
        return self._queue.qsize()
