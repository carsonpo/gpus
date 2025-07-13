# GPU Cloud Pricing Analysis

Analysis based on on-demand hourly rates. Metrics calculated from vendor specifications.

---

## Top Performance Per Dollar Rankings

### Best VRAM per Dollar (GB/$)

| Rank | GPU       | Provider  | Tier      | VRAM/$ | Price/hr |
| ---- | --------- | --------- | --------- | ------ | -------- |
| 1    | A100 80GB | Novita AI | On-Demand | 228.57 | $0.35    |
| 2    | RTX A5000 | RunPod    | Community | 150.00 | $0.16    |
| 3    | RTX A6000 | RunPod    | Community | 145.45 | $0.33    |
| 4    | A40       | RunPod    | Secure    | 120.00 | $0.40    |
| 5    | RTX 3090  | RunPod    | Community | 109.09 | $0.22    |

### Best Bandwidth per Dollar (GB/s/$)

| Rank | GPU       | Provider  | Tier      | BW/$    | Price/hr |
| ---- | --------- | --------- | --------- | ------- | -------- |
| 1    | A100 80GB | Novita AI | On-Demand | 5714.29 | $0.35    |
| 2    | RTX A5000 | RunPod    | Community | 4800.00 | $0.16    |
| 3    | V100      | RunPod    | Community | 4736.84 | $0.19    |
| 4    | RTX 3080  | RunPod    | Community | 4470.59 | $0.17    |
| 5    | RTX 3090  | RunPod    | Community | 4254.55 | $0.22    |

### Best FP16 TFLOPS per Dollar

| Rank | GPU       | Provider  | Tier      | TFLOPS/$ | Price/hr |
| ---- | --------- | --------- | --------- | -------- | -------- |
| 1    | RTX 4090  | RunPod    | Community | 970.59   | $0.34    |
| 2    | A100 80GB | Novita AI | On-Demand | 891.43   | $0.35    |
| 3    | RTX 3080  | RunPod    | Community | 700.00   | $0.17    |
| 4    | V100      | RunPod    | Community | 657.89   | $0.19    |
| 5    | RTX 4090  | Novita AI | On-Demand | 660.00   | $0.50    |

## Weighted Performance Scores

### VRAM-Focused (50% VRAM, 25% TFLOPS, 25% Bandwidth)

| Rank | Provider         | GPU              | Score  | Price/hr |
| ---- | ---------------- | ---------------- | ------ | -------- |
| 1    | RunPod Community | RTX 4090         | 100.00 | $0.34    |
| 2    | RunPod Community | RTX A5000        | 99.94  | $0.16    |
| 3    | V100             | RunPod Community | 92.47  | $0.19    |
| 4    | RTX 3090         | RunPod Community | 91.69  | $0.22    |
| 5    | A40              | RunPod Secure    | 91.17  | $0.40    |

### Compute-Focused (50% TFLOPS, 25% VRAM, 25% Bandwidth)

| Rank | Provider         | GPU       | Score  | Price/hr |
| ---- | ---------------- | --------- | ------ | -------- |
| 1    | RunPod Community | RTX 4090  | 100.00 | $0.34    |
| 2    | RunPod Secure    | RTX A5000 | 100.00 | $0.26    |
| 3    | SFCompute        | H200 SXM  | 100.00 | $2.50    |
| 4    | FluidStack       | H200 SXM  | 99.70  | $2.20    |
| 5    | SFCompute        | H100 SXM  | 98.62  | $2.30    |

### Bandwidth-Focused (50% Bandwidth, 25% VRAM, 25% TFLOPS)

| Rank | Provider         | GPU              | Score  | Price/hr |
| ---- | ---------------- | ---------------- | ------ | -------- |
| 1    | RunPod Secure    | RTX A5000        | 100.00 | $0.26    |
| 2    | RunPod Community | RTX A5000        | 100.00 | $0.16    |
| 3    | SFCompute        | H200 SXM         | 100.00 | $2.50    |
| 4    | FluidStack       | H200 SXM         | 100.00 | $2.20    |
| 5    | V100             | RunPod Community | 97.38  | $0.19    |

## Price Comparison by GPU Model

| GPU       | Provider (Low)   | Low Price | Provider (High) | High Price | Range |
| --------- | ---------------- | --------- | --------------- | ---------- | ----- |
| H200 SXM  | FluidStack       | $2.20     | AWS             | ~$15.00    | 6.8x  |
| H100 SXM  | FluidStack       | $1.99     | AWS             | $12.29     | 6.2x  |
| A100 80GB | Novita AI        | $0.35     | GCP             | $7.50      | 21.4x |
| RTX 4090  | RunPod Community | $0.34     | RunPod Secure   | $0.69      | 2.0x  |
| L40S      | RunPod Community | $0.79     | AWS             | $1.50      | 1.9x  |

## Provider Analysis

### RunPod

- **GPUs Available**: 20+ models
- **Price Range**: $0.16-$3.99/hr
- **Strongest Metrics**: Consumer GPUs (RTX series)
- **Tiers**: Secure Cloud, Community Cloud

### AWS

- **GPUs Available**: 9 models
- **Price Range**: $0.53-$15.00/hr
- **Strongest Metrics**: Enterprise features
- **Instance Types**: P5, P4, G6, G5, G4

### GCP

- **GPUs Available**: 6 models
- **Price Range**: $0.35-$11.06/hr
- **Strongest Metrics**: Spot pricing discounts
- **Instance Types**: A3, A2, G2, N1+GPU

### FluidStack

- **GPUs Available**: 4 models
- **Price Range**: $1.20-$2.20/hr
- **Strongest Metrics**: H100/H200 pricing
- **Features**: InfiniBand included

### SFCompute

- **GPUs Available**: 2 models
- **Price Range**: ~$2.30-$2.50/hr
- **Strongest Metrics**: Market-based pricing
- **Features**: 3.2Tb/s InfiniBand

### Novita AI

- **GPUs Available**: 3 models
- **Price Range**: $0.35-$2.99/hr
- **Strongest Metrics**: A100 value
- **Features**: Quick deployment

## Notes

- Prices change frequently, especially spot/community tiers
- Performance metrics based on theoretical maximums
- Network costs not included in analysis
- Some providers require minimum commitments
