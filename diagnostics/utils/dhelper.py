# dhelper.py
''' This helper utility file contains functions to convert dictionaries to SimpleNamespace objects, which allow for attribute-style access. This is useful for handling configuration data in a more convenient way. '''
from types import SimpleNamespace

def to_namespace(d):
    """Recursively converts a dict to a SimpleNamespace.
    Recursively converts a dictionary to a SimpleNamespace.
    This enables dot notation: sd.dimensions.lat.LAT_BOUNDS
    """
    if isinstance(d, dict):
        return SimpleNamespace(**{k: to_namespace(v) for k, v in d.items()})
    elif isinstance(d, list):
        return [to_namespace(i) for i in d]
    return d

def load_settings(json_path):
    """Helper to load JSON and convert to namespace in one shot."""
    import json
    with open(json_path, 'r') as f:
        data = json.load(f)
    return to_namespace(data)

def dict_to_settings(data_dict):
    """Converts an existing dictionary to a Namespace."""
    return to_namespace(data_dict)