class POSTaggerLL1:
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
        pos_tags = self.tag_tokens()
        print("POS Tags:", pos_tags)

    def match(self, expected_token):
        if self.current_token == expected_token:
            if self.current_token != self.EOF:
                self.build_token()
        else:
            print("Syntax error!")

    def tag_tokens(self):
        pos_tags = []
        for token in self.tokens:
            pos_tag = self.get_pos_tag(token)
            pos_tags.append((token, pos_tag))
        return pos_tags

    def get_pos_tag(self, token):
        # LL(1) parsing rules for POS tagging
        if token in {"the", "a", "an"}:
            return "Determiner"
        elif token in {"cat", "dog", "bird", "elephant", "rabbit","ashiq"}:
            return "Noun"
        elif token in {"runs", "jumps", "flies", "swims", "walks","writes","reads","dance","table"}:
            return "Verb"
        elif token in {"quick", "lazy", "happy", "sad", "tall", "short"}:
            return "Adjective"
        elif token in {"over", "on", "in", "under", "above", "below","one","the"}:
            return "Preposition"
        else:
            return "Unknown"

# Example usage:
def main():
    text = input("Enter a sentence: ")
    tagger = POSTaggerLL1(text)
    tagger.parse()

if __name__ == "__main__":
    main()
