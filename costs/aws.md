# AWS EC2 GPU Pricing

> Enterprise-grade GPU instances with on-demand pricing.

Prices shown are on-demand hourly rates. Reserved and spot options available.

---

## GPU Performance Metrics

| GPU       | Instance           | VRAM    | Price/hr | VRAM/$ | BW/$   | FP16 TFLOPS/$ |
| --------- | ------------------ | ------- | -------- | ------ | ------ | ------------- |
| H100 SXM  | p5.48xlarge (8x)   | 640GB   | $12.29   | 6.51   | 244.10 | 80.47         |
| H200 SXM  | p5e.48xlarge (8x)  | 1,128GB | $15.00   | 9.40   | 320.00 | 65.93         |
| A100 40GB | p4d.24xlarge (8x)  | 320GB   | $2.75    | 14.55  | 581.82 | 113.45        |
| A100 80GB | p4de.24xlarge (8x) | 640GB   | $3.375   | 23.70  | 592.59 | 92.44         |
| V100      | p3.2xlarge         | 16GB    | $3.06    | 5.23   | 294.12 | 40.85         |
| L40S      | g6e.xlarge         | 48GB    | $1.50    | 32.00  | 576.00 | 241.33        |
| L4        | g6.xlarge          | 24GB    | $0.80    | 30.00  | 375.00 | 75.00         |
| A10G      | g5.xlarge          | 24GB    | $1.00    | 24.00  | 600.00 | 125.00        |
| T4        | g4dn.xlarge        | 16GB    | $0.53    | 30.19  | 603.77 | 122.64        |

## Performance Scores

| GPU       | VRAM-Focused | Compute-Focused | Bandwidth-Focused |
| --------- | ------------ | --------------- | ----------------- |
| H100 SXM  | 32.49        | 33.53           | 34.95             |
| H200 SXM  | 32.16        | 30.28           | 35.86             |
| A100 40GB | 55.31        | 52.36           | 62.89             |
| A100 80GB | 54.86        | 46.81           | 60.40             |
| V100      | 22.24        | 20.33           | 27.00             |
| L40S      | 100.00       | 100.00          | 100.00            |
| L4        | 47.53        | 38.01           | 46.33             |
| A10G      | 64.20        | 58.36           | 69.23             |
| T4        | 67.06        | 58.69           | 70.41             |

## Instance Details

### P-Series (ML/HPC Optimized)

- **p5.48xlarge**: 8x H100, 3,200 Gbps EFA networking
- **p5e.48xlarge**: 8x H200, Enhanced memory bandwidth
- **p4d.24xlarge**: 8x A100 40GB, 400 Gbps networking
- **p4de.24xlarge**: 8x A100 80GB, Extended memory
- **p3 series**: V100 configurations (1-8 GPUs)

### G-Series (Graphics/Inference)

- **g6e series**: L40S configurations
- **g6 series**: L4 configurations
- **g5 series**: A10G configurations (1-8 GPUs)
- **g4dn series**: T4 configurations (1-4 GPUs)

## Regional Availability

- **P5 (H100)**: US East, US West, Asia Pacific, South America
- **G6e (L40S)**: Limited availability
- **P4d/P4de (A100)**: Most major regions

## Notes

- Prices per individual GPU calculated from multi-GPU instances
- EFA networking included on P4/P5 instances
- Capacity Blocks available for guaranteed access
- Spot instances offer up to 90% discount
