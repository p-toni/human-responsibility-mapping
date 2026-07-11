# Application Modes and Work Shapes

Use the smallest artifact that can change the decision.

| Mode | Use when | Output |
|---|---|---|
| Lightweight | Early exploration, low-stakes work, unclear fit, creative/strategy work | Human Responsibility Snapshot |
| Standard | AI changes responsibility, trust, delegation, or workflow shape | Human Responsibility Map |
| Full | High-stakes, multi-role, agentic, regulated, safety-critical, or accountability-heavy systems | Full map + evidence ledger + eval plan + telemetry plan + release gate |

## Dynamic objective work

Use for red-team exercises, incident response, research, strategy, creative exploration, and long-horizon agentic tasks. Map `observe -> hypothesize -> act -> evaluate -> reframe -> continue / stop / escalate` instead of linear steps.

## System-facing domains

Use for infrastructure, simulation testing, eval platforms, developer tooling, observability, security automation, data pipelines, and internal control systems. If persona language feels forced, map operators, accountable owners, system states, control surfaces, failure modes, evidence, and release gates.

## Creative work

Use lightly. AI may generate options, critique structure, test clarity, or suggest alternatives. The human owns meaning, taste, commitment, and publication.

## Strategy artifacts

For VP decks, MBR narratives, strategy memos, and investment theses, use a lightweight snapshot unless tied to real operating-model changes.

## Multi-domain initiatives

For company-wide AI initiatives spanning multiple work domains (support + legal + security + ops, etc.), do not invent a portfolio mode inside this framework. Run Standard or Full mode per domain and use the team's existing portfolio tooling (Linear, Asana, spreadsheets, planning docs) for status, dependencies, and rollup.

Two cross-domain concerns are framework-shaped:

1. **Vocabulary consistency.** If `AI-executed` or `policy-governed` mean different things in the support map vs. the security map, resolve the drift before aggregating cross-domain findings.
2. **Coverage rollup.** A portfolio with one domain at `theme-stable` and four at `initial` is not ready for broad boundary moves. Aggregate stakeholder coverage status, not just map status.
