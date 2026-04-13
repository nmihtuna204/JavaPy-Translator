import sys
from functools import reduce

from sentiment_pipeline import (
    pipe,
    make_cleaner,
    tokenize,
    make_classifier,
    make_formatter,
    PUNCTUATION,
)


def make_ai_scorer(model_name: str = "mock-sentiment-v1", confidence_threshold: float = 0.5):
    def _mock_model_predict(tokens: list) -> dict:
        pos_words = {"amazing", "love", "great", "fantastic", "excellent", "best", "good"}
        neg_words = {"terrible", "hate", "worst", "horrible", "bad", "awful"}
        pos = sum(1 for t in tokens if t in pos_words)
        neg = sum(1 for t in tokens if t in neg_words)
        total = max(pos + neg, 1)
        return {
            "positive_conf": pos / total,
            "negative_conf": neg / total,
            "neutral_conf":  1 - (pos + neg) / max(len(tokens), 1),
        }

    def ai_score(tokens: list) -> dict:
        probs     = _mock_model_predict(tokens)
        pos_conf  = probs["positive_conf"]
        neg_conf  = probs["negative_conf"]
        pos_score = 1 if pos_conf >= confidence_threshold else 0
        neg_score = 1 if neg_conf >= confidence_threshold else 0
        return {
            "tokens":     tokens,
            "pos_score":  pos_score,
            "neg_score":  neg_score,
            "net_score":  pos_score - neg_score,
            "pos_hits":   [f"(ai:{pos_conf:.2f})"] if pos_score else [],
            "neg_hits":   [f"(ai:{neg_conf:.2f})"] if neg_score else [],
            "has_signal": any([pos_score, neg_score]),
            "model":      model_name,
            "pos_conf":   pos_conf,
            "neg_conf":   neg_conf,
        }
    return ai_score


def make_passthrough_classifier():
    return lambda scores: {**scores, "label": (
        "positive" if scores["pos_score"] > scores["neg_score"] else
        "negative" if scores["neg_score"] > scores["pos_score"] else
        "neutral"
    )}


clean      = make_cleaner(PUNCTUATION)
ai_score   = make_ai_scorer(model_name="mock-sentiment-v1", confidence_threshold=0.4)
classify   = make_classifier(pos_threshold=1, neg_threshold=1)
fmt        = make_formatter(verbose=True)

analyze_ai = pipe(clean, tokenize, ai_score, classify, fmt)


def run_file(path: str):
    sep = "─" * 56
    with open(path) as f:
        comments = [line.rstrip("\n") for line in f if line.strip()]
    for comment in comments:
        print(sep)
        print(f'Input: "{comment}"')
        print(analyze_ai(comment))
    print(sep)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "run":
        run_file(sys.argv[2])
    else:
        print("Usage: python3 sentiment_pipeline_ai.py run <file>")
        print("       python3 sentiment_pipeline_ai.py run test_01.txt")
