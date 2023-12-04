
from string import punctuation
from collections import Counter
from collections import defaultdict

post_comments_with_labels = [
    ("I love this post.", "pos"),
    ("This post is your best work.", "pos"),
    ("I really liked this post.", "pos"),
    ('I agree 100 percent. This is true', 'pos'),
    ("This post is spot on!", "pos"),
    ("So smart!", "pos"),
    ("What a good point!", "pos"),
    ("Bad stuff.", "neg"),
    ("I hate this.", "neg"),
    ("This post is horrible.", "neg"),
    ("I really disliked this post.", "neg"),
    ("What a waste of time.", "neg"),
    ("I do not agree with this post.", "neg"),
    ("I can't believe you would post this.", "neg"),
    ("I'm not sure I agree with this.", "neg"),
    ("This post is wrong.", "neg"),
    ("This post is not good.", "neg"),
    ("This is not your best work.", "neg"),
    ("This is not your best post.", "neg"),
    ("I don't like this post.", "neg"),
    ("I don't agree with this post.", "neg"),
    ("I don't like this.", "neg"),
    ("I don't agree with you.", "neg"),
    ("I don't like you.", "neg"),
    ("I don't like this.", "neg"),
    ("I don't like your post.", "neg"),
    ("I don't like your blog.", "neg"),
    ("I don't like your writing.", "neg"),
    ("I don't like your work.", "neg"),
    ("I don't like your point of view.", "neg"),
    ("I don't like your opinion.", "neg"),
    ("I don't like your ideas.", "neg"),
    ("I don't like your views.", "neg"),
    ("I don't like your perspective.", "neg"),
    ("I don't like your attitude.", "neg"),
    ("I don't like your thoughts.", "neg"),
    ("I don't like your arguments.", "neg"),
    ("I don't like your analysis.", "neg"),
    ("I don't like your thoughts.", "neg"),
    ("I don't like your tone.", "neg"),
    ("I don't like your reasoning.", "neg"),
    ("I don't like your logic.", "neg"),
    ("I don't like your conclusions.", "neg"),
    ("I don't like your ideas.", "neg"),
    ("I don't like your conclusions.", "neg"),
    ("I don't like your conclusions.", "neg"),
    ("I don't like your conclusions.", "neg"),
    ("I like this post.", "pos"),
    ("I like this.", "pos"),
    ("I like you.", "pos"),
    ("I like your post.", "pos"),
    ("I like your blog.", "pos"),
    ("I like your writing.", "pos"),
    ("I like your work.", "pos"),
    ("I like your point of view.", "pos"),
    ("I like your opinion.", "pos"),
    ("I like your ideas.", "pos"),
    ("I like your views.", "pos"),
    ("I like your perspective.", "pos"),
    ("I like your attitude.", "pos"),
    ("I like your thoughts.", "pos"),
    ("I like your arguments.", "pos"),
    ("I like your analysis.", "pos"),
    ("I like your thoughts.", "pos"),
    ("I like your tone.", "pos"),
    ("I like your reasoning.", "pos"),
    ("I like your logic.", "pos"),
    ("I like your conclusions.", "pos"),
    ("I like your ideas.", "pos"),
    ("I like your conclusions.", "pos"),
    ("I like your conclusions.", "pos"),
    ("I like your conclusions.", "pos"),
    ("I love this post.", "pos"),
    ("I love this.", "pos"),
    ("I love you.", "pos"),
    ("I love your post.", "pos"),
    ("I love your blog.", "pos"),
    ("I love your writing.", "pos"),
    ("I love your work.", "pos"),
    ("I love your point of view.", "pos"),
    ("I love your opinion.", "pos"),
    ("I love your ideas.", "pos"),
    ("I love your views.", "pos"),
    ("I love your perspective.", "pos"),
    ("I love your attitude.", "pos"),
    ("I love your thoughts.", "pos"),
    ("I love your arguments.", "pos"),
    ("I love your analysis.", "pos"),
    ("I love your thoughts.", "pos"),
    ("I love your tone.", "pos"),
    ("I love your reasoning.", "pos"),
    ("I love your logic.", "pos"),
    ("I love your conclusions.", "pos"),
    ("I love your ideas.", "pos"),
    ("I love your conclusions.", "pos"),
    ("I love your conclusions.", "pos"),
    ("I love your conclusions.", "pos")
]

class NaiveBayesClassifier:
    def __init__(self, samples):
        self.mapping = {"pos": [], "neg": []}
        self.sample_count = len(samples)
        for text, label in samples:
            self.mapping[label] += self.tokenize(text)
        self.pos_counter = Counter(self.mapping["pos"])
        self.neg_counter = Counter(self.mapping["neg"])

    @staticmethod
    def tokenize(text):
        return (
            text.lower().translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def classify(self, text):
        tokens = self.tokenize(text)
        pos = []
        neg = []
        for token in tokens:
            pos.append(self.pos_counter[token]/self.sample_count)
            neg.append(self.neg_counter[token]/self.sample_count)
        # rerturn "neg", "pos" or "nutral"
        if sum(pos) > sum(neg):
            return "pos"
        elif sum(pos) < sum(neg):
            return "neg"
        else:
            return "neutral"
        

cl = NaiveBayesClassifier(post_comments_with_labels)

show_expected_result = False
show_hints = False

def get_sentiment(text):
    cl = NaiveBayesClassifier(post_comments_with_labels)
    return cl.classify(text)

def main():
    #real time input and real time sentiment output with each word
    while True:
        text = input("Enter text: ")
        sentiment = get_sentiment(text)
        print(sentiment)

if __name__ == "__main__":
    main()
