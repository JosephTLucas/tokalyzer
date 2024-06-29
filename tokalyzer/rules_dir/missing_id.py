from tokalyzer.utils import load_tokenizer


def missing_ids(tokenizer):
    """
    Accept either a loaded Huggingface tokenizer or a JSON file that can be loaded as one.
    Return a list of missing token IDs in the tokenizer's vocab.
    """
    tokenizer = load_tokenizer(tokenizer)

    vocab = tokenizer.get_vocab()
    seen_ids = set()
    duplicates = set()
    keys, token_ids = zip(*vocab.items())
    highest = max(token_ids)
    missing = set(range(highest + 1)) - set(token_ids)
    if missing:
        print(f"Missing token IDs detected: {list(missing)}")


if __name__ == "__main__":
    tokenizer_path = "gpt2"
    missing_ids(tokenizer_path)
