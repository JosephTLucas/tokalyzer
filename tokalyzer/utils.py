from tokenizers import Tokenizer


def load_tokenizer(tokenizer):
    if isinstance(tokenizer, str):
        tokenizer = Tokenizer.from_pretrained(tokenizer)
    elif isinstance(tokenizer, dict):
        tokenizer = Tokenizer.from_pretrained(tokenizer)
    elif not isinstance(tokenizer, Tokenizer):
        raise ValueError(
            "tokenizer must be a Huggingface tokenizer or a path to a saved tokenizer"
        )

    return tokenizer
