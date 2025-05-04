def simple_named_entity_recognizer(text):
    """A very basic named entity recognizer."""
    named_entities = []
    words = text.split()

    people_keywords = ["Mr.", "Ms.", "Dr.", "Professor"]
    place_keywords = ["City", "State", "Country", "River", "Mountain"]
    organization_keywords = ["Inc.", "Corp.", "Ltd.", "University", "Company"]

    i = 0
    while i < len(words):
        word = words[i]

        # Check for People (very basic)
        if word in people_keywords and i + 1 < len(words):
            named_entities.append((f"{word} {words[i+1]}", "PERSON"))
            i += 2
            continue

        # Check for Places (very basic)
        if word.endswith("City") or word.endswith("State") or word.endswith("Country"):
            named_entities.append((word, "PLACE"))
            i += 1
            continue
        if word in place_keywords and i + 1 < len(words):
            named_entities.append((f"{word} {words[i+1]}", "PLACE"))
            i += 2
            continue

        # Check for Organizations (very basic)
        if i + 1 < len(words) and words[i+1] in organization_keywords:
            named_entities.append((f"{word} {words[i+1]}", "ORGANIZATION"))
            i += 2
            continue
        if word.endswith("University") or word.endswith("Company"):
            named_entities.append((word, "ORGANIZATION"))
            i += 1
            continue

        i += 1

    return named_entities
if __name__ == "__main__":
    text = "Mr. John Smith visited New York City. The Amazon Corp. is headquartered in Seattle City. Professor Jane Doe works at Stanford University near the Rocky Mountain range."

    print("Simplified Named Entity Recognition:")
    entities = simple_named_entity_recognizer(text)
    for entity, entity_type in entities:
        print(f"Entity: '{entity}', Type: {entity_type}")