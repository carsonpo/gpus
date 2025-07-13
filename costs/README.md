# GPU Cloud Pricing Analysis

Analysis based on on-demand hourly rates. Metrics calculated from vendor specifications.

---

## Top Performance Per Dollar Rankings

### Best VRAM per Dollar (GB/$)

| Rank | GPU       | Provider         | Tier      | VRAM/$ | Price/hr |
| ---- | --------- | ---------------- | --------- | ------ | -------- |
| 1    | RTX A5000 | RunPod Community | Community | 150.00 | $0.16    |
| 2    | RTX A6000 | RunPod Community | Community | 145.45 | $0.33    |
| 3    | A40       | RunPod Secure    | Secure    | 120.00 | $0.40    |
| 4    | RTX 3090  | Novita AI        | On-Demand | 114.29 | $0.21    |
| 5    | RTX 3090  | RunPod Community | Community | 109.09 | $0.22    |

### Best Bandwidth per Dollar (GB/s/$)

| Rank | GPU       | Provider         | Tier      | BW/$    | Price/hr |
| ---- | --------- | ---------------- | --------- | ------- | -------- |
| 1    | RTX A5000 | RunPod Community | Community | 4800.00 | $0.16    |
| 2    | V100      | RunPod Community | Community | 4736.84 | $0.19    |
| 3    | RTX 3080  | RunPod Community | Community | 4470.59 | $0.17    |
| 4    | RTX 3090  | Novita AI        | On-Demand | 4457.14 | $0.21    |
| 5    | RTX 3090  | RunPod Community | Community | 4254.55 | $0.22    |

### Best FP16 TFLOPS per Dollar

| Rank | GPU      | Provider   | Tier      | TFLOPS/$ | Price/hr |
| ---- | -------- | ---------- | --------- | -------- | -------- |
| 1    | H100 SXM | FluidStack | On-Demand | 496.98   | $1.99    |
| 2    | H200 SXM | FluidStack | On-Demand | 449.55   | $2.20    |
| 3    | H100 SXM | SFCompute  | Market    | 430.00   | $2.30    |
| 4    | RTX 5090 | Novita AI  | On-Demand | 419.00   | $0.50    |
| 5    | H200 SXM | SFCompute  | Market    | 395.60   | $2.50    |

## Weighted Performance Scores (Top 10)

### Balanced (33% VRAM, 33% Bandwidth, 34% TFLOPS)

| Rank | Provider         | GPU       | Score  | Price/hr |
| ---- | ---------------- | --------- | ------ | -------- |
| 1    | FluidStack       | H200 SXM  | 176.30 | $2.20    |
| 2    | Novita AI        | RTX 5090  | 176.24 | $0.50    |
| 3    | SFCompute        | H200 SXM  | 167.84 | $2.50    |
| 4    | RunPod Community | RTX A5000 | 161.43 | $0.16    |
| 5    | Novita AI        | RTX 3090  | 160.82 | $0.21    |
| 6    | RunPod Community | RTX 3090  | 159.51 | $0.22    |
| 7    | RunPod Community | RTX 4090  | 153.89 | $0.34    |
| 8    | RunPod Community | RTX A4500 | 153.21 | $0.19    |
| 9    | RunPod Community | RTX A6000 | 151.94 | $0.33    |
| 10   | Novita AI        | RTX 4090  | 151.38 | $0.35    |

### VRAM-Focused (50% VRAM, 25% Bandwidth, 25% TFLOPS)

| Rank | Provider         | GPU          | Score  | Price/hr |
| ---- | ---------------- | ------------ | ------ | -------- |
| 1    | RunPod Community | RTX A5000    | 171.64 | $0.16    |
| 2    | Novita AI        | RTX 3090     | 171.19 | $0.21    |
| 3    | RunPod Community | RTX 3090     | 170.23 | $0.22    |
| 4    | RunPod Community | RTX A4500    | 165.59 | $0.19    |
| 5    | RunPod Community | RTX A6000    | 164.66 | $0.33    |
| 6    | FluidStack       | H200 SXM     | 164.09 | $2.20    |
| 7    | Novita AI        | RTX 5090     | 164.00 | $0.50    |
| 8    | RunPod Community | RTX A4000    | 158.24 | $0.17    |
| 9    | RunPod Community | RTX 3090 Ti  | 157.41 | $0.27    |
| 10   | RunPod Community | RTX 4000 Ada | 156.56 | $0.20    |

### Compute-Focused (50% TFLOPS, 25% VRAM, 25% Bandwidth)

| Rank | Provider         | GPU      | Score  | Price/hr |
| ---- | ---------------- | -------- | ------ | -------- |
| 1    | FluidStack       | H200 SXM | 182.05 | $2.20    |
| 2    | Novita AI        | RTX 5090 | 182.00 | $0.50    |
| 3    | SFCompute        | H200 SXM | 175.10 | $2.50    |
| 4    | FluidStack       | H100 SXM | 162.19 | $1.99    |
| 5    | SFCompute        | H100 SXM | 153.80 | $2.30    |
| 6    | RunPod Community | H100 NVL | 151.25 | $2.59    |
| 7    | RunPod Community | RTX 5090 | 149.09 | $0.69    |
| 8    | RunPod Community | RTX 4090 | 146.03 | $0.34    |
| 9    | Novita AI        | H100 SXM | 144.92 | $2.56    |
| 10   | Novita AI        | RTX 4090 | 143.29 | $0.35    |

### Bandwidth-Focused (50% Bandwidth, 25% VRAM, 25% TFLOPS)

| Rank | Provider         | GPU       | Score  | Price/hr |
| ---- | ---------------- | --------- | ------ | -------- |
| 1    | FluidStack       | H200 SXM  | 182.05 | $2.20    |
| 2    | Novita AI        | RTX 5090  | 182.00 | $0.50    |
| 3    | SFCompute        | H200 SXM  | 173.65 | $2.50    |
| 4    | RunPod Community | RTX A5000 | 171.64 | $0.16    |
| 5    | Novita AI        | RTX 3090  | 171.19 | $0.21    |
| 6    | RunPod Community | RTX 3090  | 170.23 | $0.22    |
| 7    | RunPod Community | RTX 4090  | 165.66 | $0.34    |
| 8    | RunPod Community | RTX A4500 | 165.59 | $0.19    |
| 9    | RunPod Community | RTX A6000 | 164.66 | $0.33    |
| 10   | Novita AI        | RTX 4090  | 163.79 | $0.35    |

## Price Comparison by GPU Model

| GPU      | Provider (Low)   | Low Price | Provider (High) | High Price | Range |
| -------- | ---------------- | --------- | --------------- | ---------- | ----- |
| H200 SXM | FluidStack       | $2.20     | AWS             | $15.00     | 6.8x  |
| H100 SXM | FluidStack       | $1.99     | AWS/GCP         | $12.29     | 6.2x  |
| RTX 5090 | Novita AI        | $0.50     | RunPod Secure   | $0.89      | 1.8x  |
| RTX 4090 | RunPod Community | $0.34     | Novita AI HF    | $0.69      | 2.0x  |
| RTX 3090 | Novita AI        | $0.21     | RunPod Secure   | $0.43      | 2.0x  |
| A100 SXM | RunPod Community | $1.19     | AWS             | $4.10      | 3.4x  |
| L40S     | Novita AI        | $0.55     | AWS             | $7.22      | 13.1x |

## Notes

- Prices change frequently, especially spot/community tiers
- Performance metrics based on theoretical maximums
- Network costs and egress fees not included
- Some providers require minimum commitments
- Scores use absolute thresholds: 50 GB/$, 1000 GB/s/$, 200 TFLOPS/$ as "good" benchmarks
