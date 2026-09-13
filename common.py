"""Shared setup for the collaboration-aware-routing notebook pipeline.

Each notebook in this pipeline is one stage. A stage loads whatever the
previous stage saved into ./artifacts, does its own work, and (if later
stages need something from it) saves its own outputs back into
./artifacts. This file only holds things every stage needs: paths,
plot styling, and the two small helper functions used throughout.
"""
from pathlib import Path
import os
import tempfile

import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path.cwd()
DATA = ROOT / "Given Data"
ARTIFACTS = ROOT / "artifacts"
FIGURES = ROOT / "outputs" / "figures"
ARTIFACTS.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "atlassian-datathon-mpl"))

plt.rcParams.update({
    "figure.dpi": 110,
    "font.size": 10,
    "axes.titleweight": "bold",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

BLUE, TEAL, AMBER, PURPLE, RED, GREY, LIGHT_GREY = (
    "#1868DB", "#008DA6", "#FFAB00", "#6554C0", "#DE350B", "#6B778C", "#DFE1E6"
)
PLAN_ORDER = ["Free", "Standard", "Premium", "Enterprise"]
PLAN_COLORS = {"Free": GREY, "Standard": BLUE, "Premium": TEAL, "Enterprise": PURPLE}
PRIORITY_ORDER = ["Low", "Medium", "High", "Critical"]
PRIORITY_COLORS = {"Low": "#B3BAC5", "Medium": AMBER, "High": "#FF7452", "Critical": RED}
TIER_ORDER = ["Standard", "Elevated", "Hub"]
TIER_COLORS = {"Standard": GREY, "Elevated": AMBER, "Hub": PURPLE}


def clean_source(raw: pd.DataFrame) -> pd.DataFrame:
    """Standardise column names and strip whitespace from text fields."""
    frame = raw.copy(deep=True)
    frame.columns = frame.columns.str.strip().str.lower().str.replace(r"\s+", "_", regex=True)
    for column in frame.select_dtypes(include="object"):
        frame[column] = frame[column].str.strip().replace("", pd.NA)
    return frame


def save_show(fig, filename):
    """Save a figure to outputs/figures and display it inline."""
    fig.savefig(FIGURES / filename, dpi=180, bbox_inches="tight", facecolor="white")
    plt.show()
