# GPU Cloud Pricing Summary

> Best providers for each GPU and use case across major cloud platforms.

Analysis based on on-demand hourly rates. Last updated: July 2025.

---

## Best Price by GPU

| GPU              | Best Provider    | Price/hr | Runner-up        | Price/hr |
| ---------------- | ---------------- | -------- | ---------------- | -------- |
| **H200**         | RunPod Community | $3.59    | AWS P5e          | ~$15.00  |
| **H100**         | FluidStack       | ~$1.99   | SFCompute        | ~$2.30   |
| **A100 80GB**    | Novita AI        | $0.35    | RunPod Community | $1.19    |
| **A100 40GB**    | GCP              | ~$3.67   | AWS P4d          | ~$2.75   |
| **RTX 6000 Ada** | RunPod Community | $0.74    | RunPod Secure    | $0.77    |
| **RTX 5090**     | RunPod Community | $0.69    | RunPod Secure    | $0.89    |
| **RTX 4090**     | RunPod Community | $0.34    | RunPod Secure    | $0.69    |
| **L40S**         | RunPod Community | $0.79    | GCP G6e          | ~$1.50   |
| **L4**           | GCP G2           | ~$1.00   | AWS G6           | ~$0.80   |
| **RTX 3090**     | RunPod Community | $0.22    | RunPod Secure    | $0.43    |

## Best for Memory (96GB+)

1. **B200 (192GB)** - Coming soon on enterprise clouds
2. **H200 (141GB)** - RunPod @ $3.59/hr
3. **H100 NVL (94GB)** - RunPod @ $2.59/hr
4. **RTX PRO 6000 (96GB)** - Enterprise only

## Best for Bandwidth

1. **B200 (8.0 TB/s)** - Coming soon
2. **H200 (4.8 TB/s)** - Multiple providers ~$3.59+/hr
3. **H100 NVL (3.9 TB/s)** - RunPod @ $2.59/hr
4. **H100 SXM (3.0 TB/s)** - FluidStack @ $1.99/hr

## Best TFLOPS per Dollar (FP16)

| GPU              | Provider         | TFLOPS | $/hr  | TFLOPS/$ |
| ---------------- | ---------------- | ------ | ----- | -------- |
| **RTX 4090**     | RunPod Community | 330    | $0.34 | **970**  |
| **A100**         | Novita AI        | 312    | $0.35 | **891**  |
| **RTX 3090**     | RunPod Community | 142    | $0.22 | **645**  |
| **RTX 6000 Ada** | RunPod Community | 330    | $0.74 | **446**  |
| **L40S**         | RunPod Community | 362    | $0.79 | **458**  |

## Provider Strengths

**RunPod**

- Widest GPU selection
- Best community cloud prices
- Serverless options
- No egress fees

**AWS**

- Enterprise features
- Global availability
- Integrated services
- Expensive but reliable

**GCP**

- Good spot pricing (60-91% off)
- L4 availability
- Integrated with GCP services
- Limited H100 access

**SFCompute**

- Market-based pricing
- InfiniBand included
- Large cluster support
- No vendor lock-in

**FluidStack**

- Cheapest H100s
- Thousands available
- Great for 100+ GPUs
- InfiniBand standard

**Novita AI**

- Cheapest A100s
- Up to 50% savings claimed
- Simple deployment
- Good for startups

## Recommendations

**For Hobbyists/Prototyping**

- RunPod Community Cloud (RTX 3090/4090)
- Novita AI (A100)

**For Startups**

- FluidStack (H100 at scale)
- RunPod Secure Cloud (variety)
- Novita AI (cost-effective)

**For Enterprise**

- AWS/GCP (SLAs, support)
- SFCompute (large clusters)
- CoreWeave (custom configs)

**For Best Value**

- RTX 4090 on RunPod (970 TFLOPS/$)
- A100 on Novita (891 TFLOPS/$)
- Avoid hyperscalers for cost

## Notes

- Prices change frequently, especially spot/community
- Consider startup credits when comparing
- Network costs can add up on hyperscalers
- InfiniBand crucial for multi-GPU training
