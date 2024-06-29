from tokalyzer.utils import load_tokenizer


def duplicate_token_ids(tokenizer):
    """
    Accept either a loaded Huggingface tokenizer or a JSON file that can be loaded as one.
    Return a list of duplicate token IDs in the tokenizer's vocab.
    """
    tokenizer = load_tokenizer(tokenizer)

    vocab = tokenizer.get_vocab()
    seen_ids = set()
    duplicates = set()

    for _, token_id in vocab.items():
        if token_id in seen_ids:
            duplicates.add(token_id)
        else:
            seen_ids.add(token_id)

    print(f"Duplicate token IDs detected: {list(duplicates)}")


if __name__ == "__main__":
    tokenizer_path = "gpt2"
    duplicate_ids = duplicate_token_ids(tokenizer_path)
    print("Duplicate token IDs:", duplicate_ids)
