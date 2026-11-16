def normalize_items(items):
    clean_list = [item.strip().upper() for item in items]
    unique_set = set(clean_list)
    return unique_set