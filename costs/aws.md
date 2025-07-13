# AWS EC2 GPU Pricing

> Enterprise-grade GPU instances with on-demand, reserved, and spot pricing options.

Prices shown are on-demand hourly rates unless noted. Significant price cuts (up to 45%) announced June 2025.

---

## P-Series (ML/HPC Optimized)

| Instance          | GPU Config   | VRAM    | On-Demand  | Notes                      |
| ----------------- | ------------ | ------- | ---------- | -------------------------- |
| **p5.48xlarge**   | 8x H100      | 640GB   | $98.32/hr  | 3,200 Gbps EFA networking  |
| **p5e.48xlarge**  | 8x H200      | 1,128GB | ~$120/hr   | 141GB per GPU              |
| **p5en.48xlarge** | 8x H200      | 1,128GB | ~$125/hr   | Enhanced CPU-GPU bandwidth |
| **p4d.24xlarge**  | 8x A100 40GB | 320GB   | ~$22/hr    | After 33% price cut        |
| **p4de.24xlarge** | 8x A100 80GB | 640GB   | ~$27/hr    | Extended memory variant    |
| **p3.2xlarge**    | 1x V100      | 16GB    | ~$3.06/hr  | Previous gen               |
| **p3.8xlarge**    | 4x V100      | 64GB    | ~$12.24/hr | Multi-GPU                  |
| **p3.16xlarge**   | 8x V100      | 128GB   | ~$24.48/hr | Max V100 config            |

## G-Series (Graphics/Inference)

| Instance          | GPU Config | VRAM  | On-Demand  | Notes                    |
| ----------------- | ---------- | ----- | ---------- | ------------------------ |
| **g6e.xlarge**    | 1x L40S    | 48GB  | ~$1.50/hr  | Latest inference GPU     |
| **g6e.12xlarge**  | 4x L40S    | 192GB | ~$6.00/hr  | Multi-GPU                |
| **g6.xlarge**     | 1x L4      | 24GB  | ~$0.80/hr  | Cost-effective inference |
| **g5.xlarge**     | 1x A10G    | 24GB  | ~$1.00/hr  | Graphics workloads       |
| **g5.12xlarge**   | 4x A10G    | 96GB  | ~$5.00/hr  | Multi-GPU graphics       |
| **g5.48xlarge**   | 8x A10G    | 192GB | ~$16.00/hr | Max A10G config          |
| **g4dn.xlarge**   | 1x T4      | 16GB  | ~$0.53/hr  | Entry-level inference    |
| **g4dn.12xlarge** | 4x T4      | 64GB  | ~$3.91/hr  | Multi T4                 |

## Pricing Options

**On-Demand**

- Highest flexibility, pay per hour
- No upfront commitment
- Prices shown above

**Savings Plans**

- 1-year: Up to 31% discount
- 3-year: Up to 45% discount
- Requires commitment

**Spot Instances**

- Up to 90% discount
- Interruptible workloads
- Best for fault-tolerant jobs

**Capacity Blocks**

- Reserved GPU time slots
- p5.48xlarge: $31.464/hr
- Guaranteed availability

## Regional Availability

**P5 (H100)**: US East (N. Virginia), US West (Oregon), Asia Pacific (Mumbai, Tokyo, Jakarta), South America (São Paulo)

**G6e (L40S)**: Limited availability, check specific regions

**P4d/P4de (A100)**: Most major regions

## Notes

- EFA networking included on P4/P5 instances
- EC2 UltraClusters available for P5 (up to 20,000 GPUs)
- June 2025: 33-45% price cuts on P4/P5 instances
- P6-B200 (Blackwell) instances available via Capacity Blocks
