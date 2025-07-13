# AWS EC2 GPU Pricing

> Enterprise-grade GPU instances with on-demand pricing.

Prices shown are on-demand hourly rates. Reserved and spot options available.

---

## GPU Performance Metrics

| GPU       | Instance                | Price/hr | VRAM/$ | BW/$   | FP16 TFLOPS/$ |
| --------- | ----------------------- | -------- | ------ | ------ | ------------- |
| H100 SXM  | p5.48xlarge (per GPU)   | $12.29   | 6.51   | 272.58 | 80.47         |
| H200 SXM  | p5e.48xlarge (per GPU)  | $15.00   | 9.40   | 320.00 | 65.93         |
| A100 40GB | p4d.24xlarge (per GPU)  | $4.10    | 9.77   | 390.60 | 76.17         |
| A100 80GB | p4de.24xlarge (per GPU) | $5.10    | 15.70  | 392.45 | 61.22         |
| V100      | p3.2xlarge              | $3.06    | 5.23   | 294.12 | 10.26         |
| L40S      | g6e.xlarge              | $7.22    | 6.65   | 119.67 | 12.69         |
| L4        | g6.xlarge               | $0.99    | 24.24  | 303.03 | 30.61         |
| A10G      | g5.xlarge               | $1.01    | 23.76  | 594.06 | 30.89         |
| T4        | g4dn.xlarge             | $0.53    | 30.19  | 603.77 | 122.64        |

## Performance Scores

| GPU       | Balanced | VRAM-Focused | Compute-Focused | Bandwidth-Focused |
| --------- | -------- | ------------ | --------------- | ----------------- |
| T4        | 60.70    | 60.61        | 60.85           | 60.61             |
| A10G      | 40.54    | 42.48        | 34.46           | 45.45             |
| A100 80GB | 33.72    | 33.16        | 32.97           | 35.12             |
| A100 40GB | 32.28    | 29.05        | 33.69           | 33.93             |
| L4        | 31.20    | 35.64        | 27.35           | 31.10             |
| H200 SXM  | 27.97    | 25.64        | 29.18           | 28.94             |
| H100 SXM  | 26.97    | 23.38        | 30.19           | 26.94             |
| V100      | 14.90    | 13.86        | 12.53           | 18.60             |
| L40S      | 10.49    | 11.23        | 9.49            | 10.89             |

## Instance Details

### P-Series (ML/HPC Optimized)

- **p5.48xlarge**: 8x H100, 3.2 Tbps EFA networking
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
- **P5e (H200)**: Limited availability
- **G6e (L40S)**: Limited availability
- **P4d/P4de (A100)**: Most major regions

## Notes

- Prices per individual GPU calculated from multi-GPU instances
- EFA networking included on P4/P5 instances
- Capacity Blocks available for guaranteed access
- Spot instances offer up to 90% discount
- T4 offers best value for inference workloads
