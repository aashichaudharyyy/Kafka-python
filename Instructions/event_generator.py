"""
Root-level re-export for event_generator module.
Allows direct imports: `from event_generator import generate_event`
"""
from src.event_generator import generate_event, generate_events_from_anomalies

__all__ = ["generate_event", "generate_events_from_anomalies"]
