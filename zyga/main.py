active_entities = {}
temp_playerinv = {
    "poison": {
        "name": "Poison",
        "id": "poison",
        "tags": ["consumable", "liquid"],
        "on_consume": {
            "effect": "damage",
            "target": "self",
            "strength": 20
        }
    }
}
