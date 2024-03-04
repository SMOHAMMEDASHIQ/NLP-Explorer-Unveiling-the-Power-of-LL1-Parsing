class TokenizerLL1:
    def __init__(self):
        self.text = ""
        self.index = 0
        self.tokens = []

    def get_input(self):
        self.text = input("Enter a sentence: ")

    def tokenize(self):
        self.index = 0
        self.tokens = []
        self.parse()
        return self.tokens

    def parse(self):
        while self.index < len(self.text):
            if self.text[self.index].isspace():
                self.index += 1  # Skip whitespace
            elif self.text[self.index].isalpha():
                self.tokenize_word()
            elif self.text[self.index].isdigit():
                self.tokenize_number()
            else:
                self.index += 1  # Skip punctuation

    def tokenize_word(self):
        start = self.index
        while self.index < len(self.text) and self.text[self.index].isalpha():
            self.index += 1
        self.tokens.append(self.text[start:self.index])

    def tokenize_number(self):
        start = self.index
        while self.index < len(self.text) and self.text[self.index].isdigit():
            self.index += 1
        self.tokens.append(self.text[start:self.index])


# Example usage:
def main():
    tokenizer = TokenizerLL1()
    tokenizer.get_input()
    tokens = tokenizer.tokenize()
    print("Tokens:", tokens)


if __name__ == "__main__":
    main()
