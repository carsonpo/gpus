# RunPod GPU Pricing

> Flexible pay-as-you-go GPU rentals with Secure Cloud and Community Cloud options.

Prices shown are hourly rates, billed by the minute. Zero fees for ingress/egress.

---

## GPU Pricing

| GPU              | VRAM  | Secure Cloud | Community Cloud | Notes               |
| ---------------- | ----- | ------------ | --------------- | ------------------- |
| **H200 SXM**     | 141GB | $3.99/hr     | $3.59/hr        | Extreme throughput  |
| **H100 SXM**     | 80GB  | $2.99/hr     | $2.69/hr        | 125GB RAM, 20 vCPUs |
| **H100 NVL**     | 94GB  | $2.79/hr     | $2.59/hr        | 94GB RAM, 16 vCPUs  |
| **H100 PCIe**    | 80GB  | $2.39/hr     | $1.99/hr        | 188GB RAM, 16 vCPUs |
| **A100 SXM**     | 80GB  | $1.89/hr     | -               | 125GB RAM, 16 vCPUs |
| **A100 PCIe**    | 80GB  | $1.64/hr     | $1.19/hr        | 117GB RAM, 8 vCPUs  |
| **L40S**         | 48GB  | $0.86/hr     | $0.79/hr        | 62GB RAM, 16 vCPUs  |
| **L40**          | 48GB  | $0.99/hr     | $0.69/hr        | 94GB RAM, 8 vCPUs   |
| **RTX 6000 Ada** | 48GB  | $0.77/hr     | $0.74/hr        | 62GB RAM, 14 vCPUs  |
| **RTX A6000**    | 48GB  | $0.49/hr     | $0.33/hr        | 50GB RAM, 8 vCPUs   |
| **A40**          | 48GB  | $0.40/hr     | -               | 48GB RAM, 9 vCPUs   |
| **RTX 5090**     | 32GB  | $0.89/hr     | $0.69/hr        | 62GB RAM, 14 vCPUs  |
| **RTX 4090**     | 24GB  | $0.69/hr     | $0.34/hr        | 29GB RAM, 6 vCPUs   |
| **L4**           | 24GB  | $0.43/hr     | -               | 50GB RAM, 12 vCPUs  |
| **RTX A5000**    | 24GB  | $0.26/hr     | $0.16/hr        | 25GB RAM, 3 vCPUs   |
| **RTX 3090**     | 24GB  | $0.43/hr     | $0.22/hr        | 24GB RAM, 5 vCPUs   |
| **RTX 3090 Ti**  | 24GB  | -            | $0.27/hr        | Community only      |
| **A30**          | 24GB  | -            | $0.22/hr        | Community only      |
| **RTX A4500**    | 20GB  | $0.34/hr     | $0.19/hr        | 31GB RAM, 8 vCPUs   |
| **RTX 4000 Ada** | 20GB  | $0.34/hr     | $0.20/hr        | 31GB RAM, 4 vCPUs   |
| **RTX A4000**    | 16GB  | $0.29/hr     | $0.17/hr        | 20GB RAM, 6 vCPUs   |
| **RTX 2000 Ada** | 16GB  | $0.28/hr     | -               | 31GB RAM, 6 vCPUs   |
| **Tesla V100**   | 16GB  | -            | $0.19/hr        | Community only      |
| **RTX 3080**     | 10GB  | -            | $0.17/hr        | Community only      |

## Storage Pricing

**Pod Storage (Running/Idle)**

- Volume: $0.10/$0.20 per GB/month
- Container Disk: $0.10/$0.20 per GB/month

**Network Storage**

- Under 1TB: $0.07/GB/month
- Over 1TB: $0.05/GB/month

## Serverless Pricing (per second)

| GPU                      | Flex     | Active   |
| ------------------------ | -------- | -------- |
| **H200**                 | $0.00155 | $0.00124 |
| **H100**                 | $0.00116 | $0.00093 |
| **A100**                 | $0.00076 | $0.00060 |
| **L40/L40S/6000 Ada**    | $0.00053 | $0.00037 |
| **A6000/A40**            | $0.00034 | $0.00024 |
| **4090**                 | $0.00031 | $0.00021 |
| **L4/A5000/3090**        | $0.00019 | $0.00013 |
| **A4000/A4500/RTX 4000** | $0.00016 | $0.00011 |

## Notes

- Secure Cloud: Dedicated hardware with 99.99% uptime
- Community Cloud: Shared resources, lower cost
- 30+ regions globally
- Custom Docker containers supported
- Startup and researcher credit programs available
