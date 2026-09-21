"""
Root-level re-export for topic module.
Allows direct imports: `from topic import Topic, QueueTopic`
"""
from src.topic import Topic, QueueTopic

__all__ = ["Topic", "QueueTopic"]
