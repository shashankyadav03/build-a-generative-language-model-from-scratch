
import random
from string import punctuation
from collections import defaultdict


class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        return (
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def train(self, text):
        tokens = self._tokenize(text)
        # loop through the tokens and build the graph
        for current, next in zip(tokens[1:], tokens[:-1]):
            self.graph[current].append(next)
               

    def generate(self, prompt, length=10):
        # get the lask token from the prompt
        current = self._tokenize(prompt)[-1]
        # initialize the output
        output = prompt
        for i in range(length):
            # look up the options in the graph dictionary
            options = self.graph.get(current, [])
            if not options:
                continue
            # use random.choice method to pick a current option
            current = random.choice(options)
            # add the random choice to the output string
            output += " " + current
        return output
    
def main():
    with open("01/song.txt") as f:
        text = f.read()
    mc = MarkovChain()
    mc.train(text)
    print(mc.generate("Don't ya"))

if __name__ == "__main__":
    main()