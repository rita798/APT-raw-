# Data Dictionary — APT-raw (24 columns)

| # | Column | Type | Description |
|---|--------|------|-------------|
| 1 | `timestamp` | datetime | Flow capture time (DD-MM-YYYY HH:MM). Decomposed into hour/minute/second during preprocessing. |
| 2 | `src_ip` | string | Source IP address. **Removed before modelling** (identifier). |
| 3 | `src_port` | int | Source port. |
| 4 | `dst_ip` | string | Destination IP address. **Removed before modelling** (identifier). |
| 5 | `dst_port` | int | Destination port. |
| 6 | `protocol` | categorical | Network protocol: ICMP, IGMP, TCP, UDP. |
| 7 | `service` | categorical | Application service (e.g., ssh, ftp, dns). |
| 8 | `threat_type` | categorical | Attack category — ground-truth label (9 classes, UNSW-NB15 taxonomy). |
| 9 | `severity` | categorical | **Target.** Operational risk tier: High / Medium / Low. Deterministic mapping of `threat_type` (see README). |
| 10 | `confidence` | float | IDS detection-confidence score (range 0.70–0.88). |
| 11 | `impact` | categorical | IDS-generated consequence annotation (8 distinct strings), associated with the detected attack category. |
| 12 | `packet_size` | int | Mean packet/segment size (bytes). Behavioural feature. |
| 13 | `duration` | float | Flow duration (seconds). Behavioural feature. |
| 14 | `packet_rate` | float | Packets per second. Behavioural feature. |
| 15 | `load` | float | Throughput (bits per second). Behavioural feature. |
| 16 | `state` | categorical | Raw connection-state code (merged into `connection_state`). |
| 17 | `ttl` | int | IP time-to-live. Behavioural feature. |
| 18 | `connection_state` | categorical | Connection state (e.g., INT, CON, FIN, CLO, ACC, REQ). |
| 19 | `bytes_sent` | int | Source→destination bytes. Behavioural feature. |
| 20 | `bytes_received` | int | Destination→source bytes. Behavioural feature. |
| 21 | `packets_sent` | int | Source→destination packet count. Behavioural feature. |
| 22 | `packets_received` | int | Destination→source packet count. Behavioural feature. |
| 23 | `feature_no` | string | UNSW-NB15 feature indices referenced for the record (provenance metadata). |
| 24 | `feature_name` | string | UNSW-NB15 feature names referenced for the record (provenance metadata). |

**Behavioural features audited by ANOVA (Table 4/5 of the paper):** packet_size, duration,
packet_rate, load, ttl, bytes_sent, bytes_received, packets_sent, packets_received — all
read directly from the raw dataset (not derived).
