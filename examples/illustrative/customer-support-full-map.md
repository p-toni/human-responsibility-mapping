# Full Worked Example - Customer Support Ticket Handling

**Status:** Illustrative synthetic example, not research output.
**Domain:** Mid-sized SaaS customer support workflow.
**Purpose:** Show the shape of a complete Human Responsibility Map deliverable.
**Evidence policy:** Every operational claim in this file is labeled `ai_generated_hypothesis` unless replaced with real team evidence.

This example is informed by public customer-support AI patterns, but it is not a validated study of any real team or vendor implementation. Public references are used only to make the synthetic example plausible; the way this map interprets and applies them remains `ai_generated_hypothesis`:

- `public-intercom-fin-safety` - Intercom describes answer controls, confidence/safety behavior, and escalation paths for Fin AI Agent: https://www.intercom.com/help/en/articles/9929230-the-fin-ai-engine
- `public-zendesk-ai-agent-tickets` - Zendesk documents AI-agent conversations becoming visible as Support / Agent Workspace tickets for history and monitoring: https://support.zendesk.com/hc/en-us/articles/9727051305498-Announcing-the-general-availability-of-AI-agent-conversations-as-tickets-in-Support-and-Agent-Workspace
- `public-salesforce-agent-handoff` - Salesforce describes service-agent handoff patterns where AI escalates with context: https://www.salesforce.com/blog/agent-handoff/
- `public-eu-ai-act-transparency` - EU AI Act Article 50 describes transparency obligations for certain AI interactions: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50

Do not copy thresholds, rows, or release criteria into a real PRD without replacing the evidence labels and source references with team-specific research, policy, evals, telemetry, and legal review.

## How to Read This Example

If you only have two minutes, read:

1. Responsibility Boundaries
2. Release Gate
3. Open Assumptions and Contradiction Signals

The remaining sections show the supporting evidence, stakeholder coverage, eval, and telemetry detail a real team would need before moving boundaries.

## Work Domain

Customer support ticket handling for a B2B SaaS product with email, chat, and in-product support requests.

Evidence label: `ai_generated_hypothesis`

## Current Work Architecture

```text
Intake -> Triage -> Context gathering -> Initial response -> Investigation -> Resolution action -> Escalation or close -> QA sampling -> Knowledge-base update
```

Current constraints:

- Triage and routing are inconsistent across agents.
- Context gathering repeats across support, product, and engineering handoffs.
- Low-risk requests wait behind ambiguous or high-value cases.
- Support leads own QA, but QA findings arrive after the customer interaction.
- Escalations often lose context when moved from support to engineering.

Evidence label: `ai_generated_hypothesis`

## AI-Native Work Architecture Hypothesis

```text
Intake -> Policy and risk classification -> Source-linked context pack -> Risk-tiered response or human review -> Bounded reversible action -> Evidence-rich escalation or close -> QA and drift monitoring -> Map refresh
```

Main work-architecture shifts:

- Triage becomes policy-backed classification instead of agent-by-agent judgment.
- Context gathering happens before the human starts drafting.
- Low-risk work can move under bounded AI execution only when rollback, audit, and sampling controls exist.
- High-value, regulated, emotionally sensitive, or low-confidence cases stay human-gated.
- Escalation includes a structured evidence packet instead of a narrative handoff.

Evidence label: `ai_generated_hypothesis`

## Responsibility Boundaries

| Responsibility | Current human owner | AI role now/next | Boundary state now | Target state | Control mode if AI-executed | Movement condition | Human still owns | Evidence label | Source ref |
|---|---|---|---|---|---|---|---|---|---|
| Classify ticket intent and product area | Support agent | Classify from ticket text, customer metadata, and product taxonomy | Human-owned | AI-executed | `policy-governed` | Team-defined confidence threshold; taxonomy eval; visible routing rationale; exception queue for low-confidence cases | Taxonomy policy, exception handling, misroute review | `ai_generated_hypothesis` | `public-intercom-fin-safety`; `internal-routing-eval-placeholder` |
| Classify risk tier | Support lead | Flag high-value account, compliance-sensitive request, emotional tone, refund/cancel intent, or unsafe action | Human-owned | AI-assisted | n/a | Risk policy reviewed by support, legal/compliance, and product; false-negative review on historical cases | Risk policy and final override | `ai_generated_hypothesis` | `internal-risk-policy-placeholder` |
| Gather context | Support agent | Build source-linked context pack from ticket history, account state, known incidents, docs, and recent releases | AI-assisted | AI-assisted | n/a | Source fidelity eval; every generated claim links to an inspectable source; agent can remove bad context | Final interpretation of context | `ai_generated_hypothesis` | `public-zendesk-ai-agent-tickets`; `internal-context-eval-placeholder` |
| Draft initial response | Support agent | Draft response with source links, policy checks, and uncertainty notes | AI-assisted | AI-assisted | n/a | Response correctness eval; policy-compliance eval; agent edit distance tracked; no auto-send for high-risk cases | Customer-facing send decision for reviewed cases | `ai_generated_hypothesis` | `internal-response-eval-placeholder` |
| Send low-risk acknowledgement | Support agent | Send acknowledgement or status update for low-risk, reversible, non-sensitive cases | Human-owned | AI-executed | `sampling-review` | Eligibility policy; customer-visible AI disclosure where required; sample review; confidence/risk blocklist; easy escalation path | Policy definition, sampled QA, escalation rules | `ai_generated_hypothesis` | `public-eu-ai-act-transparency`; `internal-sampling-policy-placeholder` |
| Investigate likely cause | Support agent / product support engineer | Suggest investigation plan and likely cause with source links | Human-owned | AI-assisted | n/a | Plan cites logs/docs/traces; agent approves or edits before action; hallucinated-cause eval | Investigation judgment | `ai_generated_hypothesis` | `internal-investigation-eval-placeholder` |
| Execute bounded reversible fix | Support agent / engineer | Apply approved reversible action such as session reset, feature-flag refresh, or resend invite | Human-owned | AI-executed | `approve-before-action` | Human approval before execution; action allowlist; audit log; rollback path; post-action customer-impact check | Approval, accountability, exception decision | `ai_generated_hypothesis` | `internal-action-allowlist-placeholder` |
| Escalate to product or engineering | Support lead | Route with evidence packet, reproduction steps, customer impact, and suspected owner | AI-assisted | AI-executed | `policy-governed` | Escalation-quality eval; owner taxonomy; confidence threshold; human exception queue | Priority tradeoff and exception handling | `ai_generated_hypothesis` | `public-salesforce-agent-handoff`; `internal-escalation-eval-placeholder` |
| Close ticket and update case record | Support agent | Draft closure summary and knowledge-base candidate | Human-owned | AI-assisted | n/a | Summary cites transcript and actions; human approves close; reopened-ticket monitoring | Close decision and knowledge-base publication | `ai_generated_hypothesis` | `internal-close-qa-placeholder` |
| Accept policy exception or residual customer risk | Support lead / product owner | Provide evidence packet only | Human-owned | Human-owned | n/a | Not movable under this map; accountability is organizational, not model-owned | Decision and accountability | `ai_generated_hypothesis` | `internal-risk-acceptance-placeholder` |

## Stakeholder Coverage

| Role | Sampled count | Saturation status | Evidence types collected | Gaps | Evidence label |
|---|---:|---|---|---|---|
| Operator: support agents | 0 | `unsampled` | None | Need workflow shadowing and ticket walkthroughs | `ai_generated_hypothesis` |
| Reviewer: support leads / QA | 0 | `unsampled` | None | Need QA rubric and sampled review history | `ai_generated_hypothesis` |
| Decision owner: support manager | 0 | `unsampled` | None | Need policy and staffing tradeoff input | `ai_generated_hypothesis` |
| Accountable owner: support leadership | 0 | `unsampled` | None | Need accountability and escalation acceptance | `ai_generated_hypothesis` |
| Beneficiary: customers / account teams | 0 | `unsampled` | None | Need customer tolerance for AI disclosure and handoff | `ai_generated_hypothesis` |
| Governance owner: legal/compliance/security | 0 | `unsampled` | None | Need privacy, transparency, and sector-specific review | `ai_generated_hypothesis` |
| Exception handler: support lead on call | 0 | `unsampled` | None | Need exception queue SLA and stop authority | `ai_generated_hypothesis` |

Coverage implication: this example is not ready for a boundary move. A real team would keep claims about these roles `inferred` or `unvalidated` until research replaces the synthetic rows.

Evidence label: `ai_generated_hypothesis`

## Evidence Ledger

| Claim | Evidence label | Source | Confidence | Decision impact | Validation plan |
|---|---|---|---:|---|---|
| Risk-tiered support automation is a plausible operating pattern for this workflow. | `ai_generated_hypothesis` | Public pattern refs listed above | Low | Supports testing tiered boundaries instead of all-or-nothing automation | Review comparable vendor docs, internal policy, and pilot results |
| Low-confidence or policy-sensitive cases should route to humans. | `ai_generated_hypothesis` | `public-intercom-fin-safety`; `internal-risk-policy-placeholder` | Low | Keeps target states reversible and accountable | Define risk taxonomy; replay historical tickets; measure false negatives |
| Escalations need a full context packet to avoid handoff loss. | `ai_generated_hypothesis` | `public-salesforce-agent-handoff`; `internal-escalation-eval-placeholder` | Low | Drives product requirement for evidence packet | Compare escalation quality before/after pilot |
| Customer-visible AI disclosure may be required or trust-preserving in some interactions. | `ai_generated_hypothesis` | `public-eu-ai-act-transparency`; legal review placeholder | Low | Adds compliance and UX requirement before auto-send | Legal/compliance assessment by market and channel |
| Exact confidence thresholds and sampling rates are not known yet. | `ai_generated_hypothesis` | No team telemetry | Low | Prevents hard-coding arbitrary thresholds in release criteria | Establish thresholds from shadow-mode baseline and risk appetite |

## Trust / Accountability Requirements

| Role | Responsibility | Trust requirement | Trust breaker | Evidence/control needed | Boundary implication |
|---|---|---|---|---|---|
| Support agent | Review source-linked context and drafts | Can inspect sources quickly and correct bad context | Draft looks polished but cites wrong policy or account state | Source fidelity eval; edit controls; source inspection telemetry | Keep context/drafting AI-assisted until source fidelity is proven |
| Support lead | Own QA and exceptions | Can stop automation and inspect audit trail | Exceptions pile up or sampled QA misses harmful cases | Exception dashboard; audit log; QA sampling by risk tier | AI-executed work requires visible exception handling |
| Customer | Receive accurate, respectful help | Can reach a human and understand when AI is involved where required | "Feels robotic" feedback, unresolved issue, hidden automation | Escalation path; disclosure policy; CSAT / sentiment monitoring | Tone and high-empathy cases stay human-gated until evidence improves |
| Compliance / legal | Preserve privacy and transparency obligations | Can review policy, logs, disclosure, retention, and high-risk assessment | AI sends sensitive, regulated, or misleading content | Compliance review; privacy impact review; disclosure requirements | Regulated or sensitive categories stay Human-owned or approve-before-action |
| Product / engineering | Receive actionable escalations | Gets reproduction steps, evidence, and customer impact | Escalations are faster but less actionable | Escalation-quality eval; owner taxonomy; engineering feedback loop | Routing can move only when evidence packet quality is measured |

Evidence label for all rows: `ai_generated_hypothesis`

## Product Implications

- Risk-tier classifier with inspectable rationale and human override.
- Source-linked context pack for agents and escalation owners.
- Policy blocklist for sensitive, regulated, high-value, emotional, refund/cancel, or low-confidence cases.
- AI disclosure and handoff UX where required by policy or law.
- Audit log for AI-generated drafts, sent messages, actions, approvals, and rollbacks.
- Exception queue with clear owner, SLA, and stop control.
- QA dashboard segmented by boundary state, risk tier, confidence band, and customer segment.

Evidence label: `ai_generated_hypothesis`

## Eval Plan

| Boundary movement or work shift | Eval scenario | Success criteria | Failure criteria | Required evidence | Owner |
|---|---|---|---|---|---|
| AI-executed ticket classification | Replay historical tickets with known routing outcomes | Meets team-defined accuracy and false-negative bounds by product area and risk tier | Misroutes high-risk or high-value cases above agreed tolerance | Labeled historical set; confusion matrix; reviewer notes | Support ops + product |
| AI-assisted context pack | Compare generated context against ticket history, account state, docs, incidents | Source fidelity meets team-defined threshold; agents can remove bad context | Unsupported claims, stale docs, missing incident context | Source-fidelity eval; agent edit logs | Support ops |
| AI-assisted response drafting | Human review of generated drafts across risk tiers | Correct, policy-compliant, editable drafts with acceptable edit distance | Policy violation, unsupported promise, inappropriate tone | Draft review set; policy rubric; edit distance | Support QA |
| AI-executed low-risk acknowledgement | Shadow-mode run against live-like tickets | No sends during shadow; would-have-sent set passes QA and disclosure review | High-risk or sensitive cases enter eligible set | Shadow-mode logs; eligibility review | Support lead + compliance |
| AI-executed reversible action | Sandbox or limited pilot for allowlisted actions | Approved actions succeed and rollback path works | Action outside allowlist, missing approval, rollback failure | Audit logs; rollback test; action replay | Support engineering |
| AI-executed escalation routing | Compare AI route and evidence packet to expert triage | Owner and priority match reviewer judgment within agreed tolerance | Wrong owner, missing reproduction steps, uninspectable rationale | Escalation review set; engineering feedback | Product support |

Evidence label for all rows: `ai_generated_hypothesis`

## Telemetry Plan

| Assumption | Telemetry signal | Expected pattern | Contradiction signal | Refresh action |
|---|---|---|---|---|
| Low-risk tickets can be handled with post-hoc sampling | Override rate, reopen rate, sampled QA fail rate, CSAT by risk tier | Stable or improved outcomes vs. baseline | Reopens or QA failures concentrate in AI-executed cases | Move affected categories back to AI-assisted or Human-owned |
| Customers tolerate AI disclosure in simple support interactions | CSAT, "feels robotic" tags, escalation requests after disclosure | No material trust drop in eligible low-risk category | Empathy-related CSAT drop or increased human-request rate | Rework disclosure, tone handling, and eligibility policy |
| Context packs reduce handoff loss | Engineering clarification requests, time to first useful response, escalation reopen rate | Fewer clarification loops and faster owner action | Engineers ignore packets or request missing context | Revise evidence packet schema and source requirements |
| Confidence and risk policy catches sensitive cases | Human overrides, policy blocks, false-negative review | Sensitive cases are routed to humans | Sensitive cases enter auto-send or auto-action paths | Tighten blocklist and require approve-before-action |
| Boundary state remains stable after launch | Percent of tickets by boundary state, override rate, sample pass rate | Distribution remains inside agreed operating envelope | Any state drifts more than team-defined tolerance from map | Refresh map and release gate before widening rollout |

Evidence label for all rows: `ai_generated_hypothesis`

## Release Gate

Boundary or work-architecture shift: low-risk support ticket classification, acknowledgement, escalation, and bounded reversible action.

## Capability

[ ] Capability demonstrated in realistic historical replay and shadow-mode scenarios.
[ ] Known limitations documented by risk tier and product area.
[ ] Failure modes understood, including misrouting, bad source citation, inappropriate tone, policy violation, and rollback failure.

## Trust and Evidence

[ ] Evidence is inspectable from each generated claim to its source artifact.
[ ] Confidence or uncertainty is visible to agents and reviewers where relevant.
[ ] Customer disclosure and handoff policy is reviewed for applicable markets and channels.
[ ] High-risk, high-value, sensitive, emotional, and low-confidence cases are blocked from auto-send and auto-action paths.

## Accountability

[ ] Accountable owner is explicit for each AI-executed boundary.
[ ] Exception handler has stop authority and an escalation SLA.
[ ] Human-only decisions are preserved for policy exceptions, residual risk, empathy-heavy cases, and regulated/sensitive categories.

## Evals

[ ] Required evals are defined and pass against agreed thresholds.
[ ] Regression coverage exists for routing, policy compliance, source fidelity, and action allowlist.
[ ] Shadow-mode review shows no unresolved severity-1 or severity-2 failures.

## Telemetry

[ ] Adoption, overrides, reopens, sampled QA failures, customer sentiment, escalation quality, rollback, and drift are measurable.
[ ] Boundary-state distribution is monitored by risk tier.
[ ] Contradiction signals have owners and refresh actions.

Decision: `validate further` until real team evidence replaces the synthetic assumptions.

Evidence label: `ai_generated_hypothesis`

## Open Assumptions and Contradiction Signals

| Assumption | Contradiction signal | Boundary response | Evidence label |
|---|---|---|---|
| Low-risk support cases can move to sampled AI execution without harming customer trust. | Reopen rate, "feels robotic" feedback, or sampled QA failures rise in AI-executed cases. | Move affected categories back to AI-assisted or Human-owned; tighten eligibility. | `ai_generated_hypothesis` |
| Confidence and risk policy can identify cases that need humans. | High-value, sensitive, emotional, or compliance-relevant cases appear in auto-send paths. | Add policy block; require approve-before-action or Human-owned state. | `ai_generated_hypothesis` |
| Source-linked context packs improve handoffs. | Engineering asks for the same missing context or ignores the packet. | Redesign packet schema and source requirements. | `ai_generated_hypothesis` |
| Customer disclosure preserves trust. | Customers request humans more often after disclosure or CSAT drops for disclosed interactions. | Test disclosure language and move tone-sensitive responses back to human review. | `ai_generated_hypothesis` |
| Reversible actions remain reversible in practice. | Rollback fails, audit trail is incomplete, or customer impact is unclear. | Pause AI-executed actions; return to Human-owned until rollback and audit pass. | `ai_generated_hypothesis` |

## What a Real Team Must Replace

- Replace every `ai_generated_hypothesis` label with `observed`, `interview_derived`, `telemetry_derived`, `artifact_derived`, `inferred`, or `unvalidated`.
- Replace placeholder source refs with actual interview notes, ticket IDs, policy docs, eval runs, telemetry queries, audit logs, legal reviews, and release decisions.
- Replace all team-defined thresholds and sampling rules with values chosen from baseline data, risk appetite, and accountable-owner sign-off.
- Re-run the release gate after pilot telemetry and stakeholder coverage update the map.
