# Data Dictionary (30 columns)

## Raw flow attributes (24)
| # | Column | Type | Description |
|---|--------|------|-------------|
| 1 | `timestamp` | datetime | Flow capture time. Decomposed into hour/minute/second in preprocessing. |
| 2 | `src_ip` | string | Source IP. Removed before modelling (identifier). |
| 3 | `src_port` | int | Source port. |
| 4 | `dst_ip` | string | Destination IP. Removed before modelling (identifier). |
| 5 | `dst_port` | int | Destination port. |
| 6 | `protocol` | categorical | ICMP, IGMP, TCP, UDP. |
| 7 | `service` | categorical | Application service (ssh, ftp, dns, ...). |
| 8 | `threat_type` | categorical | Attack category (9 classes, UNSW-NB15 taxonomy) — ground-truth label. |
| 9 | `severity` | categorical | **Target.** Risk tier High / Medium / Low (fixed mapping of `threat_type`, see README). |
| 10 | `confidence` | float | IDS detection-confidence score (0.70-0.88). |
| 11 | `impact` | categorical | IDS-generated consequence annotation (8 categories) associated with the detected attack. |
| 12 | `packet_size` | int | Mean packet size (bytes). Behavioural. |
| 13 | `duration` | float | Flow duration (s). Behavioural. |
| 14 | `packet_rate` | float | Packets/second. Behavioural. |
| 15 | `load` | float | Throughput (bits/s). Behavioural. |
| 16 | `state` | categorical | Raw connection-state code (merged into `connection_state`). |
| 17 | `ttl` | int | IP time-to-live. Behavioural. |
| 18 | `connection_state` | categorical | Connection state (INT, CON, FIN, CLO, ...). |
| 19 | `bytes_sent` | int | Source->destination bytes. Behavioural. |
| 20 | `bytes_received` | int | Destination->source bytes. Behavioural. |
| 21 | `packets_sent` | int | Source->destination packets. Behavioural. |
| 22 | `packets_received` | int | Destination->source packets. Behavioural. |
| 23 | `feature_no` | string | UNSW-NB15 feature indices referenced (provenance metadata). |
| 24 | `feature_name` | string | UNSW-NB15 feature names referenced (provenance metadata). |

## Derived risk-scoring attributes (6)
| # | Column | Type | Description |
|---|--------|------|-------------|
| 25 | `persistence` | int | Attacker-persistence factor. |
| 26 | `stealth` | int | Stealth factor. |
| 27 | `criticality` | int | Attack/asset criticality factor. |
| 28 | `risk_score` | float | Composite risk score derived from the factors above. |
| 29 | `probability` | int | Estimated exploitation probability (0-100). |
| 30 | `risk_level` | categorical | Derived risk level. |

**Behavioural features audited by ANOVA (paper Table 4/5):** packet_size, duration,
packet_rate, load, ttl, bytes_sent, bytes_received, packets_sent, packets_received —
read directly from the raw capture (not derived).
