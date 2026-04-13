# Comment Filtering / Sentiment Analysis System
**PPL Spring 2026 — Lab 6: Higher-Order Functions**

---

## Part (a) — System Framework Diagram

```mermaid
flowchart TB
            A[Raw Text Comment]

            S1[STAGE 1 Text Preprocessor<br/>configurable<br/>HOF make_cleaner with chars_to_remove<br/>returns clean: str to str<br/>uses lambda map str.translate]
            S2[STAGE 2 Tokenizer<br/>tokenize: str to list of str<br/>pure function and not configurable]
            S3[STAGE 3 Keyword Scorer<br/>configurable<br/>HOF make_keyword_scorer with pos_words and neg_words<br/>returns score: token list to dict<br/>uses filter any reduce]
            S4[STAGE 4 Classifier<br/>configurable<br/>HOF make_classifier with pos_threshold and neg_threshold<br/>returns classify: dict to dict<br/>uses lambda and conditional logic]
            S5[STAGE 5 Formatter<br/>configurable<br/>HOF make_formatter with verbose<br/>returns format_result: dict to str]

            Z[Sentiment Label<br/>positive or negative or neutral]

            A -->|raw text| S1
            S1 -->|cleaned text| S2
            S2 -->|token list| S3
            S3 -->|score dict pos neg hits| S4
            S4 -->|result dict plus label| S5
            S5 --> Z

            H[HOF boundaries<br/>make_cleaner<br/>make_keyword_scorer<br/>make_classifier<br/>make_formatter]
            P[Composition<br/>pipe chains all stages left to right]
            D[Data flow<br/>output of one stage is input of next stage]

            H -.-> S1
            H -.-> S3
            H -.-> S4
            H -.-> S5
            P -.-> S1
            D -.-> S2

            classDef configurable fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px,color:#1b5e20;
            classDef fixed fill:#e3f2fd,stroke:#1565c0,stroke-width:1px,color:#0d47a1;
            classDef note fill:#fff8e1,stroke:#ef6c00,stroke-width:1px,color:#e65100;

            class S1,S3,S4,S5 configurable;
            class S2 fixed;
            class H,P,D note;
```

---

## Part (b) — Implementation

The pipeline is assembled in `sentiment_pipeline.py` using four HOFs and a `pipe()` utility:

| HOF | Returns | HOF features used |
|---|---|---|
| `make_cleaner(chars)` | `clean : str → str` | `lambda`, `str.maketrans` |
| `make_keyword_scorer(pos, neg)` | `score : list → dict` | `filter`, `map`, `reduce`, `any` |
| `make_classifier(pos_t, neg_t)` | `classify : dict → dict` | closure over thresholds |
| `make_formatter(verbose)` | `fmt : dict → str` | closure over flag |

`pipe(*fns)` is itself built with `reduce`:

```python
pipe = lambda *fns: reduce(lambda f, g: lambda x: g(f(x)), fns)
analyze = pipe(clean, tokenize, score, classify, fmt)
```

---

## Part (c) — Explanation

**How the pipeline works**
`analyze(text)` threads the input through 5 functions sequentially. Each stage receives one value and returns one value; no stage knows about the others.

**Where function composition is used**
`pipe()` uses `reduce` to fold a list of functions into one combined function. Calling `analyze(text)` is exactly `fmt(classify(score(tokenize(clean(text)))))`.

**Where functions are passed as arguments or returned**
- `make_cleaner`, `make_keyword_scorer`, `make_classifier`, `make_formatter` all *return functions* — the core HOF pattern.
- `pipe()` *accepts functions as arguments* and returns a new composed function.
- `filter(lambda t: t in pos_words, tokens)` passes a lambda as an argument.
- `reduce(lambda f, g: lambda x: g(f(x)), fns)` passes and returns functions simultaneously.

**Why this is more flexible than a procedural design**
- Reconfiguring the pipeline requires only swapping one factory call. For example, `make_classifier(pos_threshold=2)` produces stricter classification with zero changes to other stages.
- Each stage is independently testable — `score(["great", "terrible"])` works without running the full pipeline.
- A procedural version would bury thresholds, keyword lists, and formatting as hardcoded values inside one monolithic function, making any change risky and spread across the codebase.

---

## Part (d) — AI Model Refactoring

### Refactored Framework Diagram

```mermaid
flowchart TB
            A[Raw Text Comment]

            S1[STAGE 1 Text Preprocessor<br/>UNCHANGED<br/>make_cleaner with chars_to_remove returns clean: str to str]
            S2[STAGE 2 Tokenizer<br/>UNCHANGED<br/>tokenize: str to list of str]
            S3[STAGE 3 AI Sentiment Scorer<br/>REPLACED<br/>HOF make_ai_scorer with model_name and confidence_threshold<br/>returns ai_score: list of str to dict<br/>same output dict shape as keyword scorer]
            S4[STAGE 4 Classifier<br/>UNCHANGED<br/>make_classifier with thresholds]
            S5[STAGE 5 Formatter<br/>UNCHANGED<br/>make_formatter with verbose returns string output]
            Z[Sentiment Label<br/>positive or negative or neutral]

            A -->|raw text| S1
            S1 -->|cleaned text| S2
            S2 -->|token list| S3
            S3 -->|score dict pos neg net| S4
            S4 -->|result dict plus label| S5
            S5 --> Z

            N[Only Stage 3 is swapped<br/>pipeline wiring and other stages are reused]
            N -.-> S3

            classDef unchanged fill:#e3f2fd,stroke:#1565c0,stroke-width:1px,color:#0d47a1;
            classDef replaced fill:#ffebee,stroke:#c62828,stroke-width:1px,color:#b71c1c;
            classDef note fill:#fff8e1,stroke:#ef6c00,stroke-width:1px,color:#e65100;

            class S1,S2,S4,S5 unchanged;
            class S3 replaced;
            class N note;
```
### What changed and what did not

| Stage | Status | Reason |
|---|---|---|
| Stage 1 — Cleaner | **Unchanged** | Text cleaning is model-agnostic |
| Stage 2 — Tokenizer | **Unchanged** | Tokenization is model-agnostic |
| Stage 3 — Scorer | **Replaced** | `make_ai_scorer` swaps in for `make_keyword_scorer` |
| Stage 4 — Classifier | **Unchanged** | Receives the same dict shape |
| Stage 5 — Formatter | **Unchanged** | Reads the same dict keys |

### How the HOF-based design supports this change

`make_ai_scorer` returns a function with an identical signature (`list[str] → dict`) and an identical output dict shape. The pipeline becomes:

```python
analyze_ai = pipe(clean, tokenize, ai_score, classify, fmt)
```

Only one slot changes. No other stage is aware that Stage 3's internals were replaced — this is the Open/Closed principle realised through higher-order functions. The boundary contract (input/output types) is all that matters, not the implementation behind it.
