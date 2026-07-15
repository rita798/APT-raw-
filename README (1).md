# APT Tri-Level Risk Dataset (IDS-Contextual)

Dataset for the study:

> Mishra, R., & Chaudhary, N. *Machine Learning-Based Tri-Level Risk Stratification for
> Advanced Persistent Threat Detection in Network Security Operations.*
> Journal of Trends in Computer Science and Smart Technology (TCSST).

## Overview

`risk_enhanced_dataset.csv` contains **256,010** network-flow records. Each flow has an
attack category (`threat_type`), an operational risk tier (`severity`), an IDS consequence
annotation (`impact`), and a set of derived risk-scoring attributes. The nine attack
categories follow the **UNSW-NB15** taxonomy (Moustafa & Slay, 2015).

**Study subset (important for reproducibility):** the experiments in the paper use the
**final 125,000 records** of this file. That subset is balanced across tiers
(High 33.96% / Medium 33.11% / Low 32.93%; imbalance ratio 1.0312), matching Table 2 of the
paper. Run `reproduce_stats.py` to verify this and the ANOVA pre-analysis.

## Class structure

| Risk tier (`severity`) | Attack categories (`threat_type`) |
|------------------------|-----------------------------------|
| High                   | DoS, Exploits, Backdoors          |
| Medium                 | Reconnaissance, Shellcode, Worms  |
| Low                    | Generic, Analysis, Fuzzers        |

Protocols: ICMP, IGMP, TCP, UDP.

## Files

| File | Description |
|------|-------------|
| `risk_enhanced_dataset.csv` | Full dataset (256,010 × 30) |
| `DATA_DICTIONARY.md` | Description of all 30 columns |
| `reproduce_stats.py` | Verifies the study subset + ANOVA pre-analysis |
| `figure1.png` | Framework architecture diagram (Figure 1) |
| `LICENSE` | CC BY 4.0 |

## Quick start

```bash
pip install pandas scipy
python reproduce_stats.py risk_enhanced_dataset.csv
```

## Citation

```
Mishra, R., & Chaudhary, N. (2025). APT tri-level risk dataset (IDS-contextual) [Data set].
GitHub. https://github.com/rita798/APT-raw-
```

Taxonomy: Moustafa, N., & Slay, J. (2015). UNSW-NB15: A comprehensive data set for network
intrusion detection systems. In *2015 MilCIS* (pp. 1-6). IEEE.

## License
Creative Commons Attribution 4.0 International (CC BY 4.0).
