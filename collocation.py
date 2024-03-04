class CollocationDetector:
    def __init__(self, text):
        self.text = text
        self.tokens = self.tokenize(text)
        self.index = 0
        self.current_token = None
        self.EOF = '$'
        self.collocations = {}

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
        self.detect_collocations()

    def match(self, expected_token):
        if self.current_token == expected_token:
            if self.current_token != self.EOF:
                self.build_token()
        else:
            print("Syntax error!")

    def detect_collocations(self):
        for i in range(len(self.tokens) - 1):
            word1 = self.tokens[i]
            word2 = self.tokens[i + 1]
            collocation = f"{word1} {word2}"
            if collocation in self.collocations:
                self.collocations[collocation] += 1
            else:
                self.collocations[collocation] = 1

    def get_collocations(self):
        return self.collocations


# Example usage:
def main():
    text = input("Enter a sentence: ")
    detector = CollocationDetector(text)
    detector.parse()
    collocations = detector.get_collocations()
    print("Collocations:", collocations)


if __name__ == "__main__":
    main()
