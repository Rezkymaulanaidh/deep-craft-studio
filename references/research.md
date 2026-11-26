# Research Method

Purpose: turn a request into a bounded evidence set, and stop on a stated condition.

## 1. Build a claim inventory first

Before searching, list the claims the deliverable will make. One line each:

| ID | Claim (draft wording) | Type | Material? |
|---|---|---|---|
| C1 | Market grew 18% from 2023 to 2025 | statistic | yes |
| C2 | Library X removed `foo()` in v4 | code | yes |

A claim is material if a reader would change a decision based on it, or if it is contested. Immaterial claims need no evidence row. Do not start searching before this table exists; without it, research turns into browsing.

## 2. Source tiers

| Tier | Definition | Examples |
|---|---|---|
| S1 | Primary or authoritative: produced by the source of the fact | Peer-reviewed papers, standards (ISO, W3C, RFC), official docs, source code, regulatory filings, raw datasets, court records, an organization's own audited report |
| S2 | Credible secondary: interprets or reports S1 with a named method and accountability | Systematic reviews, government statistics portals, outlets with a corrections policy, a vendor's engineering blog about its own product |
| S3 | Weak or derivative: useful as a lead, never as sole support | Wikipedia, aggregators, SEO listicles, conference marketing pages, forum answers, LLM output, undated blog posts |

Rules:
- A claim needs two independent sources, at least one S1 or S2. Independence means a different origin, not two articles citing the same press release.
- Count is a floor, not a weight. One S1 can outweigh five S3 sources that trace back to the same origin.
- Two axes, not one: the tier grades the source's reliability, the "Supports?" column grades whether the claim is actually backed. A reliable source can fail to support your sentence.
- S3 can point you to S1. It cannot end the search.
- "Official docs" means the docs for the version in use, not the latest marketing page.

## 3. Query ladder

Run the rungs in order. Stop climbing when the claim is covered.

1. **Definition rung.** Pin down terms and scope. Ambiguous terms manufacture false disagreements later.
2. **Primary rung.** Go to the producer: paper, docs, dataset, filing, changelog.
3. **Corroboration rung.** Find an independent S2 that reports the same fact using its own method.
4. **Adversarial rung.** Search the strongest counter-claim: "X criticism", "X replication failure", "X limitations", "why X is wrong". Read the best counter-argument, not the first.
5. **Gap rung.** If the claim stays uncovered, record the gap, label it U, and adjust the deliverable. Do not pad with weaker sources.

## 4. Recency policy

| Claim type | Freshness rule |
|---|---|
| Software behavior, APIs, prices, roles, org structure | Must reflect the current version or period. Check the changelog or "last updated". Undated means suspect. |
| Statistics and market figures | Latest release; state reference period and publication date. |
| Scientific consensus | Prefer the last 5-10 years; seminal older work is allowed when labeled as foundational. |
| Historical fact | Age is irrelevant; source quality is not. |
| Legal or regulatory | State jurisdiction and effective date. Never rely on a summary of the law. |

When recency and quality conflict, prefer the newer S1/S2 and say what changed.

## 5. Conflict resolution

When sources disagree:

1. Check definitions. A conflict is often two different questions wearing the same words.
2. Check dates. A 2019 figure and a 2025 figure are not a contradiction.
3. Check method. Sample, instrument, and population decide weight.
4. Check interest. Who benefits from the claim being true?
5. Report both positions with the weight you assign and why. Never average silently, never pick the convenient one.
6. If both sides are weak, trade up: find better coverage instead of adjudicating between two bad options.

A material conflict that stays unresolved goes into the deliverable as stated uncertainty, not as a confident midpoint.

## 6. Evidence table

Use `../assets/evidence-table.md`. Rules:

- One row per claim. Do not bundle three facts into one row.
- "Supports?" is yes, partial, or no. A source that exists but does not support the claim is a no.
- Record the exact locator (page, section, line, anchor) so the claim can be rechecked without rereading everything.
- Keep rejected sources in the table with a note. They document the search and prevent circular re-search.

## 7. Stopping rule

Stop when all of these hold:

- Every material claim has two independent sources, at least one S1/S2, or is recorded as a gap.
- Gaps stay under the cap: at most 20% of material claims, and never a gap that carries the main conclusion. Above the cap, narrow the deliverable or escalate.
- The adversarial rung has run for every contested claim.
- One of: budget reached (default 12 searches or 20 minutes, scaled to stakes), or saturation (three consecutive searches return nothing new).

A settled feeling is not a stop condition; three null searches are.

## 8. Anti-patterns

- **Citation shopping:** collecting sources that agree and skipping the ones that do not.
- **Authority laundering:** citing a blog that cites a paper without reading the paper.
- **Single-source chain:** one origin, five reprints, counted as five sources.
- **Recency theater:** assuming newer is better without checking method.
- **Scope creep:** researching interesting adjacent questions the deliverable does not need.
- **Unbounded search:** no budget, no saturation check, research becomes the deliverable.
