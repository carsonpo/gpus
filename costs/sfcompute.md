# SFCompute GPU Pricing

> Marketplace for large-scale GPU clusters with InfiniBand interconnect.

Market-based pricing with contract trading capabilities.

---

## GPU Performance Metrics

| GPU  | VRAM  | Price/hr | VRAM/$ | BW/$    | FP16 TFLOPS/$ |
| ---- | ----- | -------- | ------ | ------- | ------------- |
| H100 | 80GB  | $2.30    | 34.78  | 1304.35 | 430.00        |
| H200 | 141GB | $2.50    | 56.40  | 1920.00 | 395.60        |

## Performance Scores

| GPU  | VRAM-Focused | Compute-Focused | Bandwidth-Focused |
| ---- | ------------ | --------------- | ----------------- |
| H100 | 89.95        | 98.62           | 86.80             |
| H200 | 100.00       | 100.00          | 100.00            |

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
