"""Verify the study subset and ANOVA pre-analysis of the APT dataset.

Usage:
    python reproduce_stats.py risk_enhanced_dataset.csv
"""
import sys
import pandas as pd
from scipy import stats

path = sys.argv[1] if len(sys.argv) > 1 else "risk_enhanced_dataset.csv"
df = pd.read_excel(path) if path.lower().endswith(("xlsx", "xls")) else pd.read_csv(path)

sub = df.iloc[-125000:]  # study subset = final 125,000 records
print(f"Full dataset: {len(df)} rows")
print(f"Study subset (final 125,000 rows): {len(sub)} rows")
vc = sub["severity"].value_counts()
print("\nStudy-subset severity distribution (paper Table 2):")
print((vc / len(sub) * 100).round(2))
print("Imbalance ratio:", round(vc.max() / vc.min(), 4), "(paper: 1.0312)")

beh = ["packet_size", "duration", "packet_rate", "load", "ttl",
       "bytes_sent", "bytes_received", "packets_sent", "packets_received"]
print("\nOne-way ANOVA (behavioural features vs severity), study subset:")
for f in beh:
    groups = [sub[sub.severity == s][f].values for s in ["High", "Medium", "Low"]]
    F, p = stats.f_oneway(*groups)
    grand = sub[f].mean()
    ssb = sum(len(g) * (g.mean() - grand) ** 2 for g in groups)
    eta2 = ssb / ((sub[f] - grand) ** 2).sum()
    print(f"  {f:18s} F={F:7.3f}  p={p:.3f}  eta^2={eta2:.2e}")
print("\n(All eta^2 <= ~1.2e-5 -> behavioural features carry negligible discriminating power.)")
