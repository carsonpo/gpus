# Google Cloud Platform GPU Pricing

> Accelerator-optimized VMs with integrated GPU pricing.

Prices shown are on-demand hourly rates. Spot instances offer 60-91% discounts.

---

## GPU Performance Metrics

| GPU       | Instance/Config         | VRAM | Price/hr | VRAM/$ | BW/$   | FP16 TFLOPS/$ |
| --------- | ----------------------- | ---- | -------- | ------ | ------ | ------------- |
| H100 SXM  | a3-highgpu-8g (per GPU) | 80GB | $11.06   | 7.23   | 271.22 | 89.41         |
| A100 80GB | a2-ultragpu-1g          | 80GB | $7.50    | 10.67  | 266.67 | 41.60         |
| A100 40GB | a2-highgpu-1g           | 40GB | $3.67    | 10.90  | 435.97 | 85.01         |
| L4        | g2-standard-4           | 24GB | $1.00    | 24.00  | 300.00 | 60.00         |
| V100      | N1 + GPU                | 16GB | $2.55    | 6.27   | 352.94 | 49.02         |
| T4        | N1 + GPU                | 16GB | $0.35    | 45.71  | 914.29 | 185.71        |

## Performance Scores

| GPU       | VRAM-Focused | Compute-Focused | Bandwidth-Focused |
| --------- | ------------ | --------------- | ----------------- |
| H100 SXM  | 35.54        | 41.92           | 36.42             |
| A100 80GB | 24.31        | 23.70           | 25.49             |
| A100 40GB | 40.81        | 44.15           | 44.20             |
| L4        | 37.44        | 34.21           | 34.76             |
| V100      | 26.28        | 27.45           | 30.39             |
| T4        | 100.00       | 100.00          | 100.00            |

## Machine Types

### A3 Series (H100/H200)

- NVSwitch interconnect
- Best for large-scale training
- 8 GPU configurations standard

### A2 Series (A100)

- Standard: 40GB variants
- Ultra: 80GB variants
- 1-16 GPU configurations

### G2 Series (L4)

- Optimized for inference
- Cost-effective AI workloads
- 1-4 GPU configurations

### N1 + GPU Attachment

- Flexible GPU attachment
- V100, T4, P100, P4 available
- Mix and match configurations

## Pricing Options

- **On-Demand**: Pay per hour, no commitment
- **Spot VMs**: 60-91% discount, preemptible
- **Committed Use**: 1-year ~37%, 3-year ~57% discount
- **Sustained Use**: Auto-applied discounts

## Notes

- GPU cost included in accelerator-optimized VMs
- N1 VMs charge separately for GPU attachment
- Not all GPU types available in all regions
- Custom machine configurations supported
