from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import joblib
import pandas as pd


@dataclass
class AnomalyModel:
    model: object
    features: list[str]
    win_short: int
    win_long: int


def load_artifacts(model_dir: str | Path = "models") -> AnomalyModel:
    model_dir = Path(model_dir)
    model = joblib.load(model_dir / "isolation_forest.pkl")
    features = joblib.load(model_dir / "feature_list.pkl")
    config = joblib.load(model_dir / "config.pkl")
    return AnomalyModel(
        model=model,
        features=features,
        win_short=int(config["win_short"]),
        win_long=int(config["win_long"]),
    )


def build_features(values: list[float], win_short: int = 5, win_long: int = 20) -> pd.DataFrame:
    """
    Build the same rolling features used in training.
    """
    df = pd.DataFrame({"value": values})
    df["rolling_mean_5"] = df["value"].rolling(window=win_short).mean()
    df["rolling_std_5"] = df["value"].rolling(window=win_short).std()
    df["rolling_mean_20"] = df["value"].rolling(window=win_long).mean()
    df["rolling_std_20"] = df["value"].rolling(window=win_long).std()
    return df.dropna().reset_index(drop=True)


def predict_anomalies(values: list[float], artifact_dir: str | Path = "models") -> dict:
    am = load_artifacts(artifact_dir)

    # how many points are lost to rolling windows
    warmup = max(am.win_short, am.win_long) - 1

    feats = build_features(values, am.win_short, am.win_long)
    X = feats[am.features]

    scores = am.model.decision_function(X)
    preds = am.model.predict(X)

    anomaly = [1 if p == -1 else 0 for p in preds]

    # pad outputs so length matches input length
    padded_anomaly = [None] * warmup + anomaly
    padded_scores = [None] * warmup + scores.tolist()

    return {
        "warmup_points_dropped": warmup,
        "anomaly": padded_anomaly,
        "anomaly_score": padded_scores,
    }
