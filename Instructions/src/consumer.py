"""
Simulated Event Consumer Module
Retrieves events from the simulated topic for downstream AIOps processing.
"""

from typing import Any, Optional


class Consumer:
    """
    Simulated Kafka-style Event Consumer.
    Retrieves events from the underlying Topic channel.
    """
    def __init__(self, topic: Any, topic_name: str = "system-events"):
        self.topic: Any = topic
        self.topic_name: str = topic_name

    def receive(self, topic_name: Optional[str] = None) -> Optional[Any]:
        """
        Retrieves the next event from the topic.
        Returns None when the topic is empty or if topic channel mismatches.
        """
        # If specific topic name requested and topic instance has a conflicting name
        if topic_name is not None and hasattr(self.topic, "name") and self.topic.name != topic_name:
            return None

        # Retrieve from underlying topic
        if hasattr(self.topic, "consume"):
            return self.topic.consume()
        elif hasattr(self.topic, "pop"):
            if self.topic:  # Safe empty check preventing IndexError
                return self.topic.pop(0)
            return None
        elif hasattr(self.topic, "get_nowait"):
            try:
                return self.topic.get_nowait()
            except Exception:
                return None
        elif hasattr(self.topic, "get"):
            try:
                return self.topic.get(block=False)
            except Exception:
                return None
        else:
            raise TypeError(f"Unsupported topic structure: {type(self.topic)}")

    def poll(self, timeout_ms: int = 1000) -> Optional[Any]:
        """Mock poll method for Kafka consumer interface similarity."""
        return self.receive()

    def close(self) -> None:
        """Mock close for Kafka interface compatibility."""
        pass
