# Research Method

Turn a request into a bounded evidence set, then stop on a stated condition.

## 1. Claim inventory first

Before searching, list every claim the deliverable will make:

| ID | Claim (draft) | Type | Material? |
|---|---|---|---|
| C1 | Market grew 18% from 2023 to 2025 | statistic | yes |

Material = a reader would change a decision based on it, or it is contested. Immaterial claims need no row. Do not search before this table exists; without it, research becomes browsing.

## 2. Source tiers

| Tier | Definition | Examples |
|---|---|---|
| S1 | Primary/authoritative: produced by the source of the fact | Peer-reviewed papers, standards, official docs, source code, filings, raw datasets, court records, audited reports |
| S2 | Credible secondary: reports S1 with a named method and accountability | Systematic reviews, government statistics, corrections-policy outlets, a vendor's engineering blog about its own product |
| S3 | Weak/derivative: a lead, never sole support | Wikipedia, aggregators, SEO listicles, conference marketing, forums, LLM output, undated blogs |

Rules:
- Two independent sources per claim, ≥1 S1/S2. Independent = different origin, not two articles citing one press release.
- Count is a floor, not a weight; one S1 can outweigh five S3 sources from one origin.
- Two axes: tier = source reliability; "Supports?" = whether the claim is backed. A reliable source can fail to support your sentence.
- S3 can point to S1; it cannot end the search.
- "Official docs" = docs for the version in use, not the latest marketing page.

## 3. Query ladder

Run in order; stop when covered.

1. **Definition:** pin terms and scope; ambiguity manufactures false disagreements.
2. **Primary:** the producer—paper, docs, dataset, filing, changelog.
3. **Corroboration:** an independent S2 reporting the same fact with its own method.
4. **Adversarial:** the strongest counter-claim ("X criticism", "X replication failure", "X limitations", "why X is wrong"); read the best counter-argument, not the first.
5. **Gap:** record it, label U, adjust the deliverable; do not pad with weaker sources.

## 4. Recency

| Claim type | Rule |
|---|---|
| Software, APIs, prices, roles, org structure | Current version/period; check changelog or "last updated"; undated is suspect. |
| Statistics, market figures | Latest release; state reference period and publication date. |
| Scientific consensus | Last 5-10 years; older seminal work allowed when labeled foundational. |
| Historical fact | Age irrelevant; source quality is not. |
| Legal/regulatory | State jurisdiction and effective date; never rely on a summary of the law. |

When recency and quality conflict, prefer the newer S1/S2 and say what changed.

## 5. Conflict resolution

1. Check definitions: often two different questions in the same words.
2. Check dates: a 2019 figure and a 2025 figure are not a contradiction.
3. Check method: sample, instrument, population decide weight.
4. Check interest: who benefits if the claim is true?
5. Report both positions with your weight and why; never average silently or pick the convenient one.
6. If both sides are weak, trade up: find better coverage instead of adjudicating between two bad options.

An unresolved material conflict is stated uncertainty, not a confident midpoint.

## 6. Evidence table

Use `../assets/evidence-table.md`:

- One row per claim; do not bundle three facts.
- "Supports?" = yes/partial/no. A source that exists but does not support the claim is a no.
- Record the exact locator (page, section, line, anchor) for rechecking.
- Keep rejected sources with a note; they document the search and prevent circular re-search.

## 7. Stopping rule

Stop when all hold:

- Every material claim has two independent sources, ≥1 S1/S2, or is recorded as a gap.
- Gaps ≤20% of material claims, and never a gap carrying the main conclusion. Above the cap, narrow the deliverable or escalate.
- The adversarial rung ran for every contested claim.
- Budget reached (default 12 searches or 20 minutes, scaled to stakes) or saturation (three consecutive null searches).

A settled feeling is not a stop condition; three null searches are.

## 8. Anti-patterns

- **Citation shopping:** agreeing sources only.
- **Authority laundering:** citing a blog that cites a paper without reading it.
- **Single-source chain:** one origin, five reprints, counted as five.
- **Recency theater:** newer assumed better without checking method.
- **Scope creep:** interesting adjacent questions the deliverable does not need.
- **Unbounded search:** no budget or saturation check; research becomes the deliverable.
