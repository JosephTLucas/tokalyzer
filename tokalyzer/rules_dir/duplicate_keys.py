from tokalyzer.utils import load_tokenizer


def duplicate_keys(tokenizer):
    """
    Accept either a loaded Huggingface tokenizer or a JSON file that can be loaded as one.
    Return a list of unique duplicate keys in the tokenizer's vocab.
    """
    tokenizer = load_tokenizer(tokenizer)

    vocab = tokenizer.get_vocab()
    seen = set()
    duplicates = set()

    for key in vocab:
        if key in seen:
            duplicates.add(key)
        else:
            seen.add(key)

    print(f"Duplicate keys detected: {list(duplicates)}")


if __name__ == "__main__":
    tokenizer_path = "gpt2"
    duplicates = duplicate_keys(tokenizer_path)
    print("Duplicate keys:", duplicates)
