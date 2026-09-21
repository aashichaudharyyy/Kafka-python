"""
Root-level re-export for aiops_processor module.
Allows direct imports: `from aiops_processor import process_event, format_alert`
"""
from src.aiops_processor import process_event, format_alert, process_events

__all__ = ["process_event", "format_alert", "process_events"]
