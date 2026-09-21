"""
Simulated Event Producer Module
Publishes anomaly events into the simulated event topic/channel.
"""

from typing import Any, Optional


class Producer:
    """
    Simulated Kafka-style Event Producer.
    Sends event payloads to an underlying Topic instance, list, or queue.
    """
    def __init__(self, topic: Any, topic_name: str = "system-events"):
        self.topic: Any = topic
        self.topic_name: str = topic_name

    def send(self, first_arg: Any, second_arg: Optional[Any] = None) -> None:
        """
        Sends an event to the topic.
        Supports both signatures:
          - producer.send(event)
          - producer.send("topic-name", event)
        """
        if second_arg is None:
            # Single argument passed: producer.send(event)
            event = first_arg
        else:
            # Two arguments passed: producer.send(topic_name, event)
            dest_topic = first_arg
            event = second_arg
            # If destination topic differs from bound topic name and topic has a name
            if hasattr(self.topic, "name") and self.topic.name != dest_topic:
                # Still support sending or log channel note
                pass

        # Publish to underlying topic structure
        if hasattr(self.topic, "publish"):
            self.topic.publish(event)
        elif hasattr(self.topic, "append"):
            self.topic.append(event)
        elif hasattr(self.topic, "put"):
            self.topic.put(event)
        else:
            raise TypeError(f"Unsupported topic structure: {type(self.topic)}")

    def flush(self) -> None:
        """Mock flush for Kafka interface compatibility."""
        pass

    def close(self) -> None:
        """Mock close for Kafka interface compatibility."""
        pass
