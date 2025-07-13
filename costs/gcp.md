# Google Cloud Platform GPU Pricing

> Accelerator-optimized VMs with integrated GPU pricing.

Prices shown are on-demand hourly rates. Spot instances offer 60-91% discounts.

---

## GPU Performance Metrics

| GPU       | Instance/Config         | Price/hr | VRAM/$ | BW/$   | FP16 TFLOPS/$ |
| --------- | ----------------------- | -------- | ------ | ------ | ------------- |
| H100 SXM  | a3-megagpu-8g (per GPU) | $12.29   | 6.51   | 272.58 | 80.47         |
| A100 80GB | a2-ultragpu-1g          | $3.67    | 21.80  | 544.96 | 85.01         |
| A100 40GB | a2-highgpu-1g           | $1.89    | 21.16  | 846.56 | 165.08        |
| L4        | g2-standard-4           | $0.81    | 29.63  | 370.37 | 37.41         |
| V100      | N1 + GPU                | $2.48    | 6.45   | 362.90 | 12.66         |
| T4        | N1 + GPU                | $0.35    | 45.71  | 914.29 | 185.71        |

## Performance Scores

| GPU       | Balanced | VRAM-Focused | Compute-Focused | Bandwidth-Focused |
| --------- | -------- | ------------ | --------------- | ----------------- |
| T4        | 91.91    | 91.79        | 92.14           | 91.79             |
| A100 40GB | 69.97    | 62.96        | 73.02           | 73.54             |
| A100 80GB | 46.82    | 46.05        | 45.78           | 48.77             |
| L4        | 38.14    | 43.56        | 33.43           | 38.01             |
| H100 SXM  | 26.97    | 23.38        | 30.19           | 26.94             |
| V100      | 18.39    | 17.11        | 15.46           | 22.95             |

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

## Best Value Options

- **T4**: Exceptional inference value at $0.35/hr
- **A100 40GB**: Best training performance/price at $1.89/hr
- **L4**: Modern architecture for AI workloads at $0.81/hr

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
