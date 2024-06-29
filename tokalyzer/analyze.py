from tokalyzer.rules import load_rules
from tokalyzer.utils import load_tokenizer


class Analyzer:
    def __init__(self, tokenizer):
        self.tokenizer = load_tokenizer(tokenizer)
        self.rules = load_rules()

    def run(self):
        for rule in self.rules:
            rule(self.tokenizer)


if __name__ == "__main__":
    a = Analyzer("gpt2")
    print(a.tokenizer)
    print(a.rules)
    a.run()
