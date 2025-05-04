def simple_tokenizer(text):
    """A very basic tokenizer that splits on whitespace and punctuation."""
    tokens = []
    current_token = ""
    for char in text:
        if char.isalnum():
            current_token += char
        elif current_token:
            tokens.append(current_token)
            current_token = ""
        if char in ['.', ',', '!', '?']:  # Basic punctuation as separate tokens
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        elif char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
    if current_token:
        tokens.append(current_token)
    return tokens
def simple_stopword_remover(tokens):
    """A very basic stopword remover using a hardcoded list."""
    stopwords = ["the", "a", "is", "are", "and", "of", "in", "to"]
    filtered_tokens = [token for token in tokens if token.lower() not in stopwords]
    return filtered_tokens
def simple_pos_tagger(tokens):
    """A very basic rule-based POS tagger."""
    tagged_tokens = []
    word_to_tag = {
        "dog": "NOUN",
        "cat": "NOUN",
        "barks": "VERB",
        "runs": "VERB",
        "quickly": "ADV",
        "slowly": "ADV",
        "big": "ADJ",
        "small": "ADJ",
        "the": "DET",
        "a": "DET"
    }
    for token in tokens:
        tag = word_to_tag.get(token.lower(), "UNKNOWN")
        tagged_tokens.append((token, tag))
    return tagged_tokens
if __name__ == "__main__":
    text = "The big dog barks quickly. A small cat runs slowly!"

    print("Original Text:", text)

    # Tokenization
    tokens = simple_tokenizer(text)
    print("Tokens:", tokens)

    # Stopword Removal
    filtered_tokens = simple_stopword_remover(tokens)
    print("Tokens after Stopword Removal:", filtered_tokens)

    # POS Tagging
    tagged_tokens = simple_pos_tagger(filtered_tokens)
    print("POS Tagged Tokens:", tagged_tokens)