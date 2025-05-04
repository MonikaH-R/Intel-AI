import random
def build_ngram_model(corpus, n=2):
    """Builds a simple N-gram language model from a list of sentences."""
    ngrams = {}
    for sentence in corpus:
        tokens = sentence.lower().split()
        if len(tokens) < n:
            continue
        for i in range(len(tokens) - n + 1):
            ngram = tuple(tokens[i:i+n-1])
            next_word = tokens[i+n-1]
            if ngram not in ngrams:
                ngrams[ngram] = []
            ngrams[ngram].append(next_word)
    return ngrams
def generate_text(model, n=2, max_length=50, start_ngram=None):
    """Generates text using the N-gram model."""
    if not model:
        return "No model to generate from."

    if start_ngram is None:
        start_ngram = random.choice(list(model.keys()))
    elif len(start_ngram) != n - 1:
        return "Starting ngram must be of length n-1."

    current_ngram = tuple(start_ngram)
    generated_text = list(current_ngram)

    for _ in range(max_length):
        if current_ngram in model:
            next_possible_words = model[current_ngram]
            next_word = random.choice(next_possible_words)
            generated_text.append(next_word)
            current_ngram = tuple(generated_text[-(n-1):])
        else:
            break  # Stop if the current ngram is not in the model

    return " ".join(generated_text)
if __name__ == "__main__":
    text_corpus = [
        "The quick brown fox jumps over the lazy dog.",
        "A quick brown rabbit hops quickly.",
        "The lazy cat sleeps soundly.",
        "Brown foxes are quick animals.",
        "Lazy dogs often sleep."
    ]

    n_value = 3  # Let's build a 3-gram model
    ngram_model = build_ngram_model(text_corpus, n=n_value)
    print(f"{n_value}-gram Model:", ngram_model)

    print("\nGenerated Text:")
    generated_text_1 = generate_text(ngram_model, n=n_value)
    print(f"Generation 1: {generated_text_1}")

    generated_text_2 = generate_text(ngram_model, n=n_value, start_ngram=("the", "quick"))
    print(f"Generation 2 (starting with 'the quick'): {generated_text_2}")