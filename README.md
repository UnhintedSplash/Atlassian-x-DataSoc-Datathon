# Atlassian Customer Experience Datathon

This project uses one executed notebook to test a focused customer-support question and translate the result into a feasible pilot.

## Active deliverable

- `0_customer_experience_analysis.ipynb` — audit, analysis views, EDA, feature sensitivity, model validation, routing simulation, and recommendation.

Run from the project root:

```bash
source .venv/bin/activate
jupyter lab 0_customer_experience_analysis.ipynb
```

Or execute non-interactively:

```bash
.venv/bin/jupyter nbconvert --to notebook --execute --inplace 0_customer_experience_analysis.ipynb
```

The notebook embeds its seven Matplotlib figures and saves copies under `outputs/figures/`.

## Problem and scope

> Does Atlassian's ticket priority account for collaboration reach, particularly when highly collaborative customers are concentrated on commercial plans?

The notebook tests two relationships before simulating a routing policy:

1. maximum collaborator count and non-Free plan membership at customer grain;
2. maximum collaborator count and High/Critical technical priority at ticket grain.

It then estimates how many historical tickets would move if Hub customers on Premium or Enterprise plans received a one-level queue uplift for Low or Medium tickets.

In scope:

- raw-data and join-cardinality checks;
- visible cleaning decisions with raw-to-cleaned row reconciliation;
- opening EDA covering dataset size, every plan tier, Free versus non-Free share, rating coverage and distribution, and technical-priority mix by plan;
- exact-count EDA showing why the Blast Radius problem was selected;
- customer and ticket analysis views with explicit row grains;
- Standard, Elevated, and Hub collaboration tiers;
- two interpretable one-feature logistic regressions;
- five-fold stratified and customer-grouped validation;
- limited `C` and maximum-versus-mean sensitivity checks;
- routing workload simulation and a prospective pilot design;
- an executable pilot-readiness check showing which missing fields block impact evaluation.

Out of scope:

- realised revenue, churn, retention, or causal-impact claims;
- SLA calculations without ticket creation time;
- changing technical severity labels;
- production deployment or a multi-notebook architecture.

## Evidence limits

The data is synthetic. `collaborators` is a monthly product-usage count, not collaborators per support session. Plan labels do not include price or realised revenue, so non-Free membership is a commercial-plan proxy. Ticket creation time is absent, so queue waiting time and SLA compliance cannot be measured from the supplied files.

## Superseded code audit

| Item | Why it is not used | Simpler replacement |
|---|---|---|
| Archived multi-notebook work | More architecture than this focused story needs. | One numbered, executed notebook. |
| Usage-trajectory rating models | They answer a different problem and previously produced weak retrospective signal. | Two one-feature diagnostic regressions tied to the Blast Radius question. |
| K-means clustering | No operational target and tier coverage is already defined. | Transparent collaboration thresholds with a sensitivity table. |
| Random forest | Adds opacity for a one-feature relationship check. | Scaled logistic regression with grouped folds. |
| Reusable plotting frameworks | Hide a small number of presentation charts behind unnecessary scaffolding. | Seven direct Matplotlib figures. |
| Generated intermediate CSVs | Duplicate notebook tables and clutter the active project. | Embedded tables; figures only under `outputs/figures/`. |

Archived files remain references and are not imported by the active notebook.

## Project layout

```text
.
├── 0_customer_experience_analysis.ipynb
├── AGENTS.md
├── README.md
├── requirements.txt
├── 2026 UNSW DataSoc X Atlassian Datathon.pdf
├── Given Data/                 # immutable supplied CSVs
├── outputs/
│   └── figures/                # seven notebook-generated charts
└── archive/                    # preserved superseded work and outputs
```
