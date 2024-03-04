class StemmerAndLemmatizer:
    def __init__(self, text):
        self.text = text
        self.tokens = self.tokenize(text)
        self.index = 0
        self.current_token = None
        self.EOF = '$'

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
        stemmed_and_lemmatized_words = self.process_tokens()
        print("Stemmed and Lemmatized Words:", stemmed_and_lemmatized_words)

    def match(self, expected_token):
        if self.current_token == expected_token:
            if self.current_token != self.EOF:
                self.build_token()
        else:
            print("Syntax error!")

    def process_tokens(self):
        stemmed_and_lemmatized_words = []
        for token in self.tokens:
            stemmed_word = self.stem(token)
            lemmatized_word = self.lemmatize(token)
            stemmed_and_lemmatized_words.append((token, stemmed_word, lemmatized_word))
        return stemmed_and_lemmatized_words

    def stem(self, word):
        # Simple stemming algorithm (e.g., remove 'ing' and 'ed' suffixes)
        if word.endswith('ing'):
            return word[:-3]
        elif word.endswith('ed'):
            return word[:-2]
        else:
            return word

    def lemmatize(self, word):
        # Simple lemmatization algorithm (return the word as is)
        return word

# Example usage:
def main():
    text = input("Enter a word: ")
    print("Stemmed root Lemmatized")
    processor = StemmerAndLemmatizer(text)
    processor.parse()

if __name__ == "__main__":
    main()
