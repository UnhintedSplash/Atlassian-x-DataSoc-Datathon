# Atlassian Customer Experience Analysis

## Mission

Use the supplied synthetic customer, support-ticket, and product-usage data to build one clear, evidence-led customer-experience story for business decision-makers.

The active problem is:

> Does Atlassian's ticket priority account for collaboration reach, particularly when highly collaborative customers are concentrated on commercial plans?

The business proposal is a small collaboration-impact layer beside technical priority. It is not a new severity model.

The active analytical deliverable is a single numbered notebook:

- `0_customer_experience_analysis.ipynb`

Do not recreate or reuse the multi-notebook `datathon_v2` architecture. Do not add separate EDA, feature, or modelling notebooks unless the user explicitly changes the scope.

## Required notebook scope

The notebook must cover the whole workflow in this order:

1. business question and evidence boundaries;
2. data loading and audit;
3. clearly defined analysis views and row grains;
4. baseline EDA covering population size, every plan tier, rating evidence, and queue mix;
5. problem-discovery EDA using exact collaborator counts;
6. Standard (≤17), Elevated (18–19), and Hub (≥20) collaboration tiers;
7. two one-feature logistic relationship checks;
8. stratified customer evaluation and customer-grouped ticket evaluation;
9. a routing workload simulation;
10. an executable pilot-readiness check;
11. reviewed findings, limitations, and a prospective pilot.

Keep the notebook readable. Prefer a small number of useful cells, tables, and charts over reusable frameworks or technical scaffolding.

## Evidence boundaries

- Treat all supplied data as synthetic.
- A support ticket is not a unique customer; aggregate before changing grain.
- Satisfaction ratings exist only for a subset of closed tickets. Always show rated and total denominators.
- Do not infer sentiment from resolution text; it is not verified customer language.
- Do not calculate SLA or response durations because ticket creation time is absent.
- Do not call unresolved status, declining usage, or a low rating "churn".
- Product usage and ticket outcomes overlap in time. Models are retrospective association checks, not validated forecasts.
- Keep every customer's records in one validation fold.
- Separate observed findings from proposed hypotheses and pilots.
- Treat non-Free plan membership as a commercial-plan proxy, not realised revenue.
- Treat `collaborators` as a monthly product-usage count, not collaborators per support session.
- Preserve technical ticket priority. Any uplift changes only the simulated pilot queue.
- Preserve raw data frames and show why no rows are dropped or imputed.

## Project organisation

```text
Datathon/
├── 0_customer_experience_analysis.ipynb
├── AGENTS.md
├── README.md
├── requirements.txt
├── 2026 UNSW DataSoc X Atlassian Datathon.pdf
├── Given Data/                 # immutable supplied inputs
├── outputs/
│   └── figures/                # notebook-generated charts only
└── archive/                    # preserved superseded work and outputs
```

- Every active notebook filename starts with a number.
- Save charts only under `outputs/figures/`; do not leave PNG files in the project root.
- Do not generate intermediate CSVs by default.
- Preserve raw CSVs exactly as supplied.
- Archive superseded work rather than mixing it into the active workflow.
- Ignore and remove disposable caches such as `.DS_Store`, `__pycache__`, and notebook checkpoints.

## Coding standard

- Use pandas, NumPy, Matplotlib, and scikit-learn only where needed.
- Use Matplotlib for all charts, with direct labels, honest axes, and no more than two panels per figure.
- Avoid plotting helper layers unless one tiny helper removes genuine repetition.
- Validate join cardinality and row counts with assertions.
- Fit preprocessing inside each training fold.
- Compare ROC AUC with the 0.500 no-skill reference.
- Report fold variation, coefficient direction, observed group rates, and denominators.
- Limit regularisation sensitivity to `C = [0.01, 0.1, 1, 10]`.
- Compare maximum with mean collaborator count, then choose based on stability and operational meaning.
- A weak result is a result. Do not tune until a preferred story appears.
- Do not train a model on an invented ideal queue; that would be circular.

## Definition of done

- The single active notebook executes from top to bottom in the project `.venv` with zero errors.
- Every analysis view states its row grain.
- Every percentage has a visible denominator where selection matters.
- All figures are both embedded in the executed notebook and saved under `outputs/figures/`.
- Model claims match the validation design and data timing.
- Recommendations are directly linked to observed evidence and distinguish immediate action from a proposed experiment.
- The project root contains no duplicate active notebooks or loose generated files.
- Exactly seven primary figures are embedded and saved under `outputs/figures/`.

## Agent behaviour

Be a critical sparring partner. Verify factual claims, expose weak evidence, and say when the available data cannot support the desired conclusion. Do not add architectural complexity without a concrete analytical need.
