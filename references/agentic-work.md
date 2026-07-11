# Agentic and Multi-Agent Work

Boundary states describe single responsibilities. Agentic systems — those that plan multi-step work, choose tools, delegate to other agents, or run unattended — put pressure on three places the base model does not reach: who owns the flow, who reviews the reviewer, and what happens when boundaries compose.

Do not add new boundary states for agents. The three states hold; what changes is which responsibilities you must remember to map.

---

## Orchestration is a responsibility row

When AI plans, sequences, prioritizes, or decomposes work, **planning is itself a responsibility unit**. Add `plan and sequence the work` as its own row. In agentic systems it is usually the most consequential boundary and the least examined — teams gate each action the agent takes while nobody gates the agent's choice of which actions to take.

The boundary states apply as usual:

| Orchestration boundary | Meaning |
|---|---|
| Human-owned | Human decomposes the work; AI executes assigned steps |
| AI-assisted | AI proposes a plan; human approves or edits it before execution |
| AI-executed | AI plans and re-plans as it goes; the control stack governs the plan, not just the steps |

This maps onto published agent-autonomy ladders (Feng, McDonald & Zhang 2025's operator → collaborator → consultant → approver → observer roles): in this framework's terms, an agent's "autonomy level" is the boundary state of its orchestration row combined with the control stacks on its execution rows. You do not need a separate autonomy taxonomy — you need the orchestration row filled in.

One thing the ladder framing captures that a static row does not: **control transfer is dynamic.** The movement condition for any orchestration row above Human-owned must specify the transfer mechanics, not just the resting state:

- **Takeover:** how a human reclaims control mid-plan, and what happens to in-flight actions when they do.
- **Consultation triggers:** the conditions under which the agent must stop and ask (confidence drop, novel case class, action outside precedent) — and how those triggers are customized per deployment.
- **Approval triggers:** which plan steps always require sign-off regardless of the agent's confidence.
- **Emergency stop:** a stop the operator can pull without escalation, tested like any other control (a stop drill, not a stop button).

Long-horizon and unattended agents (`observe -> hypothesize -> act -> evaluate -> reframe` loops) additionally need: a step budget or time budget, an explicit stop condition, and a defined escalation state when the loop stalls — these are movement conditions for the orchestration row.

## AI as reviewer

The control modes assume the reviewer is human. Modern practice often inserts a second model — an LLM judge, a policy checker, an automated QA pass. This is allowed, with two rules:

1. **The review is a responsibility row of its own.** It gets a boundary state, an eval (judge agreement against human judgment, on a maintained sample), and drift monitoring. An unvalidated judge is `ai_generated_hypothesis` wearing a QA badge.
2. **Accountability chains terminate in humans.** Every chain of AI-executed work — however many AI reviewers it passes through — must reach a human accountable owner who passes the oversight-viability checks (`references/oversight-viability.md`). AI reviewing AI changes the eval demands; it never absorbs accountability.

A useful pattern: AI judge handles volume under `sampling-review` semantics, and humans sample the judge — smaller volume, one level up. Write both rows into the map so the human sample of the judge is budgeted attention, not an aspiration.

## AI-to-AI handoffs

When an AI in one domain hands work to an AI in another (a support agent escalates to an engineering agent), the handoff is a boundary of its own:

- **Vocabulary consistency becomes load-bearing.** If `policy-governed` means different things in the two maps, the seam is where it breaks. See the multi-domain notes in `references/application-modes.md`.
- **The evidence packet is the contract.** Specify what the receiving agent needs, and eval the packet quality like any other AI output.
- **No accountability gap at the seam.** The sending side's accountable owner holds the case until the receiving side's accountable owner accepts it. If neither map names who owns the case mid-handoff, the answer is "nobody," discovered during an incident.

## Composition: gate paths, not just rows

The release rule gates one boundary at a time. Boundary moves compose: three individually safe AI-executed rows can chain into a case class that no human ever touches. Row-level sampling does not cover the chain — each row's sample mostly catches cases *other* rows already handled correctly.

After any move, trace the work architecture and enumerate **AI-only paths**: sequences of AI-executed steps a work item can traverse end to end with no human contact.

For each path, record entry condition, volume (mean and peak), worst plausible outcome, hazard class, and controls. **Controls must be commensurate with the hazard.** Four control types, in order of preference for serious harm:

| Type | Examples |
|---|---|
| Preventive | Entry constraints, action allowlists, permission and action budgets, runtime invariants the system cannot cross |
| Containment | Blast-radius caps (amount limits, tenant isolation, rate limits), kill switch the operator can pull without escalation |
| Corrective | Rollback with a tested path, compensating actions, bounded detection-plus-intervention time |
| Detective | End-to-end sampling of completed cases that traversed the path, periodic whole-case audits |

Detective controls only observe harm after it escapes. They are sufficient alone only when the worst outcome is reversible *and* detection latency beats the intervention window. If the worst outcome is irreversible or time-sensitive beyond detection latency, the path needs preventive or containment controls — or should be prohibited outright by inserting a human gate. The validator enforces the minimum version of this rule: an `irreversible` path with detective-only controls fails validation.

This is the core systems-safety point (Leveson 2011): accidents emerge from interactions between components that are each locally correct. For genuinely safety-critical systems, do not stop at this heuristic — run an actual hazard analysis (STPA) on the future-state work architecture. Use the AI-only path table in `references/templates.md`.

## System change invalidates evidence

Movement conditions are validated against a specific system: model version, prompts, tools, retrieval corpus, policies. Any of these changing is a refresh trigger exactly as real as behavioral drift — and unlike drift, it is known in advance, usually from a vendor changelog.

- **Pin versions in the map.** Model ID, prompt version, tool versions, corpus snapshot. The schema has a `system_dependencies` block for this.
- **Re-run required evals on change.** A boundary validated on model N is `unvalidated` on model N+1 until re-evidenced. This is cheap in practice — the eval plan already exists; the discipline is running it before the boundary keeps its state.
- **Watch for silent upgrades.** Aliased model IDs, auto-updating tools, and continuously ingested corpora change the system without an event. Prefer pinned identifiers; where impossible, treat the dependency as permanently drifting and tighten telemetry accordingly.
