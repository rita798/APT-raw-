"""Reproduce the key descriptive statistics of the APT-raw dataset.

Usage:
    python reproduce_stats.py "threats-3 (3)-raw dataset.csv"
"""
import sys
import pandas as pd
from scipy import stats

path = sys.argv[1] if len(sys.argv) > 1 else "threats-3 (3)-raw dataset.csv"
beh = ["packet_size", "duration", "packet_rate", "load", "ttl",
       "bytes_sent", "bytes_received", "packets_sent", "packets_received"]
df = pd.read_csv(path)

print(f"Records: {len(df)} | Columns: {df.shape[1]}")
print("\nSeverity (target) distribution:\n", df["severity"].value_counts())
print("\nAttack category -> risk tier mapping:")
print(pd.crosstab(df["threat_type"], df["severity"]))
print("\nProtocols:\n", df["protocol"].value_counts())
print(f"\nDistinct IDS impact annotations: {df['impact'].nunique()}")

print("\nOne-way ANOVA (behavioural features vs severity):")
for f in beh:
    groups = [df[df.severity == s][f].values for s in ["High", "Medium", "Low"]]
    F, p = stats.f_oneway(*groups)
    grand = df[f].mean()
    ss_b = sum(len(g) * (g.mean() - grand) ** 2 for g in groups)
    eta2 = ss_b / ((df[f] - grand) ** 2).sum()
    print(f"  {f:18s} F={F:8.3f}  p={p:.3f}  eta^2={eta2:.2e}")
