def simple_english_to_french(english_text):
    """
    A very basic English to French translation using a dictionary.
    This method is highly limited and not suitable for accurate translation.
    """
    word_mapping = {
        "hello": "bonjour",
        "how": "comment",
        "are": "allez",
        "you": "vous",
        "today": "aujourd'hui",
        "what": "quoi",
        "is": "est",
        "your": "votre",
        "name": "nom",
        "thank": "merci",
        "yes": "oui",
        "no": "non",
        "goodbye": "au revoir"
        # Add more word mappings as needed
    }

    words = english_text.lower().split()
    french_words = []
    for word in words:
        if word in word_mapping:
            french_words.append(word_mapping[word])
        else:
            french_words.append(word)  # Keep the original word if not found

    return " ".join(french_words)
if __name__ == "__main__":
    text_to_translate = input("Enter the English text you want to (very simply) translate to French: ")
    french_text = simple_english_to_french(text_to_translate)
    print(f"\nEnglish Text: {text_to_translate}")
    print(f"French Translation (very basic): {french_text}")