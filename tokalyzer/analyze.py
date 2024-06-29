from tokalyzer.rules import load_rules
from tokalyzer.utils import load_tokenizer


class Analyzer:
    def __init__(self, tokenizer):
        self.tokenizer = load_tokenizer(tokenizer)
        self.rules = load_rules()

    def run(self):
        for rule in self.rules:
            rule(self.tokenizer)

def main():
    a = Analyzer("gpt2")
    a.run()

if __name__ == "__main__":
    main()
