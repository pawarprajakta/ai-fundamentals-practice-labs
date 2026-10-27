
from app.analyzer import analyze_text
from app.config import load_config


def main():
    config = load_config()

    print(f"\n{config['app_name']}")
    print("Enter a sentence to analyze.")
    print("Type 'exit' to close the application.")

    while True:
        text = input("\nYour text: ")

        if text.strip().lower() == "exit":
            print("Application closed.")
            break

        try:
            if not text.strip():
                raise ValueError("Please enter some text.")

            if len(text.strip()) > config["max_text_length"]:
                raise ValueError(
                    f"Text cannot exceed {config['max_text_length']} characters."
                )

            result = analyze_text(text)

            print("\nAnalysis Result")
            print("----------------")
            print(f"Word count: {result['word_count']}")
            print(f"Character count: {result['character_count']}")
            print(f"Sentiment: {result['sentiment']}")

            if config["show_word_list"]:
                print(f"Words: {', '.join(result['words'])}")

        except (TypeError, ValueError) as error:
            print(f"Input error: {error}")


if __name__ == "__main__":
    main()
