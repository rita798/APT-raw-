# APT-raw: A Simulated APT Network-Traffic Dataset with IDS Impact Annotations

This repository hosts the raw dataset used in the study:

> Mishra, R., & Chaudhary, N. *Machine Learning-Based Tri-Level Risk Stratification for
> Advanced Persistent Threat Detection in Network Security Operations.*
> Journal of Trends in Computer Science and Smart Technology (TCSST).

## Overview

`threats-3 (3)-raw dataset.csv` contains **256,010** network-flow records described by
**24 raw features**. Each flow is labelled with an attack category (`threat_type`), an
operational risk tier (`severity`), and an IDS-generated consequence annotation (`impact`).
The nine attack categories follow the **UNSW-NB15** taxonomy (Moustafa & Slay, 2015).

The experiments in the paper use a **balanced 125,000-record subset** drawn from this raw
file by stratified sampling (see Section 5.1 of the manuscript).

## Class structure

| Risk tier (`severity`) | Attack categories (`threat_type`) |
|------------------------|-----------------------------------|
| High                   | DoS, Exploits, Backdoors          |
| Medium                 | Reconnaissance, Shellcode, Worms  |
| Low                    | Generic, Analysis, Fuzzers        |

The tier is a deterministic mapping of the attack category (documented in
`DATA_DICTIONARY.md`). Protocols covered: ICMP, IGMP, TCP, UDP. The `impact` field takes
8 distinct IDS consequence strings.

## Files

| File | Description |
|------|-------------|
| `threats-3 (3)-raw dataset.zip` / `.csv` | Raw dataset (256,010 × 24) |
| `DATA_DICTIONARY.md` | Description of all 24 columns |
| `reproduce_stats.py` | Reproduces the key descriptive statistics |
| `LICENSE` | CC BY 4.0 |

## Quick start

```bash
pip install pandas scipy
python reproduce_stats.py "threats-3 (3)-raw dataset.csv"
```

## Citation

If you use this dataset, please cite the paper above and this repository:

```
Mishra, R., & Chaudhary, N. (2025). APT-raw: A simulated APT network-traffic dataset
with IDS impact annotations [Data set]. GitHub. https://github.com/rita798/APT-raw-
```

Taxonomy reference: Moustafa, N., & Slay, J. (2015). UNSW-NB15: A comprehensive data set
for network intrusion detection systems. In *2015 Military Communications and Information
Systems Conference (MilCIS)* (pp. 1–6). IEEE.

## License

Released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.
