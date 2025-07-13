# SFCompute GPU Pricing

> Marketplace for large-scale GPU clusters with InfiniBand interconnect.

Market-based pricing with contract trading capabilities.

---

## GPU Performance Metrics

| GPU  | VRAM  | Price/hr | VRAM/$ | BW/$    | FP16 TFLOPS/$ |
| ---- | ----- | -------- | ------ | ------- | ------------- |
| H100 | 80GB  | $2.30    | 34.78  | 1456.52 | 430.00        |
| H200 | 141GB | $2.50    | 56.40  | 1920.00 | 395.60        |

## Performance Scores

| GPU  | Balanced | VRAM-Focused | Compute-Focused | Bandwidth-Focused |
| ---- | -------- | ------------ | --------------- | ----------------- |
| H200 | 167.84   | 153.85       | 175.10          | 173.65            |
| H100 | 139.02   | 121.20       | 153.80          | 140.22            |

## Key Features

- **H200 SXM**: Top-tier performance with 141GB VRAM
- **H100 SXM**: Excellent compute performance at competitive price
- **InfiniBand**: 3.2Tb/s interconnect included
- **Kubernetes**: Full cluster support

## Deployment Options

- **Kubernetes Clusters**: Full InfiniBand fabric (3.2Tb/s)
- **Virtual Machines**: No InfiniBand support yet
- **Bare Metal**: Custom configurations available

## Market-Based Pricing

- Buy at your maximum price
- Sell unused capacity
- No fixed rates
- Contract trading enabled

Example usage:

```bash
# Buy 256 H100s for 3 days at max $2.30/GPU/hr
$ sf buy -n 256 -d 3d -p 2.3

# Sell unused capacity
$ sf sell -c <contract> -s tomorrow -d 1d -p 2.1
```
