
POSITIVE_WORDS = {"good", "great", "love", "happy", "useful", "excellent", "easy"}
NEGATIVE_WORDS = {"bad", "hate", "sad", "poor", "difficult", "terrible", "hard"}


def analyze_text(text):
    """Analyze text and return basic statistics and sentiment."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    text = text.strip()

    if not text:
        raise ValueError("Input text cannot be empty.")

    words = text.lower().split()
    positive_count = sum(word.strip(".,!?") in POSITIVE_WORDS for word in words)
    negative_count = sum(word.strip(".,!?") in NEGATIVE_WORDS for word in words)

    if positive_count > negative_count:
        sentiment = "positive"
    elif negative_count > positive_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "word_count": len(words),
        "character_count": len(text),
        "sentiment": sentiment,
        "words": words,
    }
