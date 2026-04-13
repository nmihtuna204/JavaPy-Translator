import sys
from functools import reduce


def pipe(*fns):
    return reduce(lambda f, g: lambda x: g(f(x)), fns)


def make_cleaner(chars_to_remove: str):
    table = str.maketrans("", "", chars_to_remove)
    return lambda text: text.lower().translate(table)


def tokenize(text: str) -> list:
    return text.split()


def make_keyword_scorer(positive_words: set, negative_words: set):
    def score(tokens: list) -> dict:
        pos_hits = list(filter(lambda t: t in positive_words, tokens))
        neg_hits = list(filter(lambda t: t in negative_words, tokens))
        all_hits = list(map(lambda t: 1, pos_hits)) + list(map(lambda t: -1, neg_hits))
        net = reduce(lambda acc, v: acc + v, all_hits, 0)
        return {
            "tokens":     tokens,
            "pos_score":  len(pos_hits),
            "neg_score":  len(neg_hits),
            "net_score":  net,
            "pos_hits":   pos_hits,
            "neg_hits":   neg_hits,
            "has_signal": any([pos_hits, neg_hits]),
        }
    return score


def make_classifier(pos_threshold: int = 1, neg_threshold: int = 1):
    def classify(scores: dict) -> dict:
        pos = scores["pos_score"]
        neg = scores["neg_score"]
        conditions = [
            (lambda: pos >= pos_threshold and pos > neg, "positive"),
            (lambda: neg >= neg_threshold and neg > pos, "negative"),
        ]
        label = next((lbl for cond, lbl in conditions if cond()), "neutral")
        return {**scores, "label": label}
    return classify


def make_formatter(verbose: bool = False):
    def format_result(result: dict) -> str:
        label = result["label"].upper()
        if not verbose:
            return f"Sentiment: {label}"
        return (
            f"Sentiment : {label}\n"
            f"Net score : {result['net_score']:+d}\n"
            f"Positive  : {result['pos_hits'] or ['—']}\n"
            f"Negative  : {result['neg_hits'] or ['—']}\n"
            f"Tokens    : {result['tokens']}"
        )
    return format_result


PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "love", "best",
    "fantastic", "wonderful", "happy", "enjoy", "like", "nice",
    "superb", "brilliant", "awesome", "perfect", "pleased",
}
NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "hate", "worst", "horrible",
    "disappointing", "poor", "ugly", "boring", "annoying",
    "disgusting", "dreadful", "mediocre", "unpleasant",
}

clean    = make_cleaner(PUNCTUATION)
score    = make_keyword_scorer(POSITIVE_WORDS, NEGATIVE_WORDS)
classify = make_classifier(pos_threshold=1, neg_threshold=1)
fmt      = make_formatter(verbose=True)

analyze = pipe(clean, tokenize, score, classify, fmt)


def run_file(path: str):
    sep = "─" * 56
    with open(path) as f:
        comments = [line.rstrip("\n") for line in f if line.strip()]
    for comment in comments:
        print(sep)
        print(f'Input: "{comment}"')
        print(analyze(comment))
    print(sep)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "run":
        run_file(sys.argv[2])
    else:
        print("Usage: python3 sentiment_pipeline.py run <file>")
        print("       python3 sentiment_pipeline.py run test_01.txt")
