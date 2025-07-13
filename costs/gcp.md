# Google Cloud Platform GPU Pricing

> Accelerator-optimized VMs with integrated GPU pricing and flexible attachment options.

Prices shown are on-demand hourly rates. Spot instances offer 60-91% discounts.

---

## Accelerator-Optimized VMs (GPU Included)

| Instance Type      | GPU Config    | VRAM  | Price/hr | Notes                     |
| ------------------ | ------------- | ----- | -------- | ------------------------- |
| **a3-megagpu-8g**  | 8x H100 80GB  | 640GB | $88.49   | us-central1 region        |
| **a3-highgpu-8g**  | 8x H100 80GB  | 640GB | ~$85     | Varies by region          |
| **a2-ultragpu-8g** | 8x A100 80GB  | 640GB | ~$60     | Contact sales for pricing |
| **a2-ultragpu-4g** | 4x A100 80GB  | 320GB | ~$30     | Ultra memory variant      |
| **a2-ultragpu-2g** | 2x A100 80GB  | 160GB | ~$15     |                           |
| **a2-ultragpu-1g** | 1x A100 80GB  | 80GB  | ~$7.50   |                           |
| **a2-megagpu-16g** | 16x A100 40GB | 640GB | ~$55     | Mega configuration        |
| **a2-highgpu-8g**  | 8x A100 40GB  | 320GB | ~$27     | High performance          |
| **a2-highgpu-4g**  | 4x A100 40GB  | 160GB | ~$14     |                           |
| **a2-highgpu-2g**  | 2x A100 40GB  | 80GB  | ~$7      |                           |
| **a2-highgpu-1g**  | 1x A100 40GB  | 40GB  | ~$3.67   | Entry A100                |
| **g2-standard-48** | 4x L4         | 96GB  | ~$5      | L4 optimized              |
| **g2-standard-24** | 2x L4         | 48GB  | ~$2.50   |                           |
| **g2-standard-12** | 1x L4         | 24GB  | ~$1.25   | Cost-effective inference  |
| **g2-standard-4**  | 1x L4         | 24GB  | ~$1.00   | Entry L4                  |

## N1 VMs with Attached GPUs

| GPU Type | VRAM | Price per GPU/hr | Max GPUs | Notes                 |
| -------- | ---- | ---------------- | -------- | --------------------- |
| **V100** | 16GB | $2.55            | 8        | Previous gen flagship |
| **T4**   | 16GB | $0.35            | 4        | Inference optimized   |
| **P100** | 16GB | $1.46            | 4        | Legacy HPC            |
| **P4**   | 8GB  | $0.60            | 4        | Legacy inference      |

## Machine Types

**A3 Series**

- H100/H200 GPUs
- NVSwitch interconnect
- Best for large-scale training

**A2 Series**

- A100 GPUs (40GB or 80GB)
- Standard: 40GB variants
- Ultra: 80GB variants

**G2 Series**

- L4 GPUs
- Optimized for inference
- Cost-effective AI workloads

**N1 + GPU**

- Flexible GPU attachment
- Mix and match configurations
- Legacy but versatile

## Pricing Options

**On-Demand**

- Pay per hour
- No commitment
- Prices shown above

**Spot VMs**

- 60-91% discount
- Preemptible workloads
- Prices change every 30 days

**Committed Use**

- 1-year: ~37% discount
- 3-year: ~57% discount
- Sustained use discounts auto-applied

## Regional Availability

Not all GPU types available in all regions. Major availability:

- us-central1: Most GPU types
- us-west1: A100, V100, T4
- europe-west4: A100, T4, L4
- asia-east1: Limited selection

## Notes

- GPU cost included in accelerator-optimized VMs
- N1 VMs charge separately for GPU attachment
- Preemptible GPUs available for fault-tolerant workloads
- Custom machine configurations supported
