"""
General utility functions.
"""


def make_hashable(obj):
    """
    Recursively converts a dictionary or list to a hashable equivalent.
    
    This is useful for deduplication of nested data structures.
    
    Args:
        obj: Object to convert (dict, list, or other)
        
    Returns:
        Hashable equivalent (frozenset for dict, tuple for list, or original object)
    """
    if isinstance(obj, dict):
        return frozenset((k, make_hashable(v)) for k, v in sorted(obj.items()))
    if isinstance(obj, list):
        return tuple(make_hashable(e) for e in obj)
    return obj


def deduplicate_items(items):
    """
    Removes duplicate items from a list by converting them to hashable form.
    
    Args:
        items: List of items (typically dictionaries or lists)
        
    Returns:
        List of unique items
    """
    unique_items = {}
    for item in items:
        hashable_item = make_hashable(item)
        if hashable_item not in unique_items:
            unique_items[hashable_item] = item
    return list(unique_items.values())

