def simple_pos_tagger(sentence):
    """A very basic rule-based POS tagger."""
    tagged_sentence = []
    word_to_tag = {
        "the": "DET",
        "a": "DET",
        "dog": "NOUN",
        "cat": "NOUN",
        "barks": "VERB",
        "meows": "VERB",
        "runs": "VERB",
        "quickly": "ADV",
        "slowly": "ADV",
        "big": "ADJ",
        "small": "ADJ"
    }
    for word in sentence.split():
        tag = word_to_tag.get(word.lower(), "UNKNOWN")  # Assign UNKNOWN for unseen words
        tagged_sentence.append((word, tag))
    return tagged_sentence
if __name__ == "__main__":
    sentence1 = "The big dog barks quickly"
    tagged1 = simple_pos_tagger(sentence1)
    print(f"Sentence: {sentence1}, Tagged: {tagged1}")

    sentence2 = "A small cat meows slowly"
    tagged2 = simple_pos_tagger(sentence2)
    print(f"Sentence: {sentence2}, Tagged: {tagged2}")

    sentence3 = "The house is big"
    tagged3 = simple_pos_tagger(sentence3)
    print(f"Sentence: {sentence3}, Tagged: {tagged3}")