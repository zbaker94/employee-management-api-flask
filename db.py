from models.employee import Employee

_in_memory_db = {
    "employees": [
        Employee("John Doe", "", 1),
        Employee("Jane Doe", "", 2),
        Employee("Alice", "", 3),
        Employee("Bob", "", 4),
    ]
}

def get_next_id_for_key(key: str):
    return max([item["id"] for item in _in_memory_db[key]]) + 1

def get(key: str):
    return _in_memory_db[key]

def get_by_id(key: str, item_id: int):
    return next((item for item in _in_memory_db[key] if item["id"] == item_id), None)

def insert(key: str, item):
    item["id"] = get_next_id_for_key(key)
    _in_memory_db[key].append(item)
    return item

def update(key: str, item_id: int, item):
    item_to_update = next((item for item in _in_memory_db[key] if item["id"] == item_id), None)
    if not item_to_update:
        return None
    item_to_update = { **item_to_update, **item }
    _in_memory_db[key] = [item if item["id"] != item_id else item_to_update for item in _in_memory_db[key]]
    return item_to_update