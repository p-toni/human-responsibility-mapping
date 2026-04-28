# Triggering evaluation

This directory contains the trigger eval set and results used to verify the skill's `description` field. The recorded eval was run with `scripts/run_eval.py` via `claude -p` against the v0.3.2 description.

## Files

- `trigger-eval.json` — 12 realistic queries (6 should-trigger bullseye, 6 should-not-trigger near-misses).
- `trigger-eval-results-haiku-4.5.json` — results on `claude-haiku-4-5-20251001`, 3 runs/query.
- `trigger-eval-results-sonnet-4.6.json` — results on `claude-sonnet-4-6`, 3 runs/query.

## Result

| Model | Pass | Should-trigger recall | Specificity (no-false-positive) |
|---|---|---|---|
| Haiku 4.5 | 6/12 | 0/6 reliable | 6/6 |
| Sonnet 4.6 | 7/12 | 1/6 reliable (3/3 on the strategy memo) | 6/6 |

## Interpretation

**Specificity is perfect.** The description never false-positives on adjacent topics: marketing personas, pure data segmentation, frontend perf debugging, plain RACI without AI context, no-AI journey maps, A/B testing setup. This matters more than recall — a false-positive trigger hijacks unrelated work.

**Recall is structurally limited.** Two consecutive description rewrites stalled at the same haiku floor. The pattern matches common skill-loader behavior: smaller or more direct models often handle "how should we think about X" advisory questions by reasoning directly rather than consulting a framework file. The skill triggers more reliably when the user wants a concrete deliverable (the strategy-memo query went 0/3 -> 3/3 with the v0.3.2 description) than when they want thinking help.

## Reproducing

```bash
python3 scripts/run_eval.py \
  --eval-set evals/trigger-eval.json \
  --skill-path . \
  --runs-per-query 3 \
  --num-workers 6 \
  --model claude-sonnet-4-6 \
  --verbose
```

The eval is non-deterministic; expect ±1 query variance per run.
