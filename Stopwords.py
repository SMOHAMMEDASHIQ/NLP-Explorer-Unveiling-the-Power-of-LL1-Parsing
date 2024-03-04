class StopwordIdentifier:
    def __init__(self, text):
        self.text = text
        self.tokens = self.tokenize(text)
        self.index = 0
        self.current_token = None
        self.EOF = '$'
        self.stopwords = {"the", "is", "are", "and", "in", "on", "at", "for", "to", "of"}

    def tokenize(self, text):
        return text.lower().split()

    def build_token(self):
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
            self.index += 1
        else:
            self.current_token = self.EOF

    def parse(self):
        self.build_token()
        stopwords_found = self.identify_stopwords()
        print("Stopwords:", stopwords_found)

    def match(self, expected_token):
        if self.current_token == expected_token:
            if self.current_token != self.EOF:
                self.build_token()
        else:
            print("Syntax error!")

    def identify_stopwords(self):
        found_stopwords = []
        while self.current_token != self.EOF:
            if self.current_token in self.stopwords:
                found_stopwords.append(self.current_token)
            self.build_token()
        return found_stopwords


# Example usage:
def main():
    text = input("Enter a sentence: ")
    identifier = StopwordIdentifier(text)
    identifier.parse()

if __name__ == "__main__":
    main()
