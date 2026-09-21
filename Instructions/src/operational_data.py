"""
Operational Data Loader Module
Handles loading, parsing, and validating operational metrics and logs.
Converts raw string data to numeric measurements to prevent comparison errors.
"""

import csv
import json
import os
from typing import Dict, List, Any, Optional


def _resolve_path(filepath: str) -> str:
    """Helper to locate data file relative to cwd or script location."""
    if os.path.isabs(filepath) and os.path.exists(filepath):
        return filepath
    
    # Try direct relative path
    if os.path.exists(filepath):
        return filepath

    # Try relative to current file's directory / parent
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    
    candidate1 = os.path.join(parent_dir, filepath)
    if os.path.exists(candidate1):
        return candidate1
    
    candidate2 = os.path.join(base_dir, filepath)
    if os.path.exists(candidate2):
        return candidate2

    return filepath


def load_metrics_csv(filepath: str = "data/metrics.csv") -> List[Dict[str, Any]]:
    """
    Reads operational metrics from a CSV file.
    Converts numeric columns (cpu, memory, latency) to float values.
    """
    resolved = _resolve_path(filepath)
    metrics_list = []
    
    with open(resolved, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cleaned_row = dict(row)
            # Safe float conversion as highlighted in assessment guide
            for key in ["cpu", "memory", "latency", "error_rate"]:
                if key in cleaned_row and cleaned_row[key] is not None:
                    try:
                        cleaned_row[key] = float(cleaned_row[key])
                    except (ValueError, TypeError):
                        pass
            metrics_list.append(cleaned_row)
            
    return metrics_list


def load_logs(filepath: str = "data/logs.txt") -> List[str]:
    """
    Reads operational log lines from a text file.
    """
    resolved = _resolve_path(filepath)
    with open(resolved, mode="r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def filter_errors(logs: List[str]) -> List[str]:
    """
    Filters and returns only log entries marked with ERROR.
    """
    return [line for line in logs if "ERROR" in line]


def load_operational_json(filepath: str = "data/operational_data.json") -> List[Dict[str, Any]]:
    """
    Loads operational metrics structured in JSON format.
    """
    resolved = _resolve_path(filepath)
    with open(resolved, mode="r", encoding="utf-8") as file:
        data = json.load(file)
        if isinstance(data, list):
            return data
        return [data]


def get_sample_data() -> Dict[str, Any]:
    """
    Returns default sample operational metrics for simulation.
    """
    return {
        "timestamp": "10:02",
        "cpu": 95.0,
        "memory": 68.0,
        "latency": 650.0,
        "error_rate": 9.4
    }
