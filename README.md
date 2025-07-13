# GPU Specs

> No longer do you need to go google a bunch of nvidia datasheets to figure compare performance.

If any of the numbers look sus, just submit a PR.

For cost data on specific major providers, look in `costs/`, where there's a summary comparing providers, and then you can check out individual ones in their respective markdown files.

---

## Specs Table

| GPU                        | Gen          | VRAM  | Bandwidth | FP64 | FP32/TF32 | FP16/BF16 | FP8   | INT8  | FP4   |
| -------------------------- | ------------ | ----- | --------- | ---- | --------- | --------- | ----- | ----- | ----- |
| **B200**                   | Blackwell    | 192GB | 8.0 TB/s  | 30   | 1,125     | 2,250     | 4,500 | 4,500 | 9,000 |
| **RTX PRO 6000 Blackwell** | Blackwell    | 96GB  | 1.8 TB/s  | 1.97 | 126       | 126       | 252   | 504   | 1,008 |
| **RTX 5090**               | Blackwell    | 32GB  | 1.8 TB/s  | 1.64 | 104.8     | 209.5     | 419   | 419   | 838   |
| **H200 SXM**               | Hopper       | 141GB | 4.8 TB/s  | 67   | 989       | 989       | 1,979 | 3,958 | -     |
| **H100 SXM**               | Hopper       | 80GB  | 3.35 TB/s | 67   | 989       | 989       | 1,979 | 3,958 | -     |
| **H100 PCIe**              | Hopper       | 80GB  | 2.0 TB/s  | 51   | 756       | 756       | 1,513 | 3,026 | -     |
| **H100 NVL**               | Hopper       | 94GB  | 3.9 TB/s  | 67   | 989       | 989       | 1,979 | 3,958 | -     |
| **RTX 6000 Ada**           | Ada Lovelace | 48GB  | 960 GB/s  | -    | 91.1      | 91.1      | 182   | 364   | -     |
| **RTX 4090**               | Ada Lovelace | 24GB  | 1.0 TB/s  | -    | 82.6      | 82.6      | 165   | 330   | -     |
| **RTX 4000 Ada**           | Ada Lovelace | 20GB  | 320 GB/s  | -    | 26.5      | 26.5      | 53    | 106   | -     |
| **RTX 2000 Ada**           | Ada Lovelace | 16GB  | 288 GB/s  | -    | 12        | 12        | 24    | 48    | -     |
| **L40S**                   | Ada Lovelace | 48GB  | 864 GB/s  | -    | 91.6      | 91.6      | 183   | 366   | -     |
| **L40**                    | Ada Lovelace | 48GB  | 864 GB/s  | -    | 90.5      | 90.5      | 181   | 362   | -     |
| **L4**                     | Ada Lovelace | 24GB  | 300 GB/s  | -    | 30.3      | 30.3      | 60.6  | 121   | -     |
| **A100 80GB**              | Ampere       | 80GB  | 2.0 TB/s  | 9.7  | 156       | 312       | -     | 624   | -     |
| **A100 40GB**              | Ampere       | 40GB  | 1.6 TB/s  | 9.7  | 156       | 312       | -     | 624   | -     |
| **A40**                    | Ampere       | 48GB  | 696 GB/s  | -    | 37.4      | 37.4      | -     | 74.8  | -     |
| **RTX A6000**              | Ampere       | 48GB  | 768 GB/s  | -    | 38.7      | 38.7      | -     | 77.4  | -     |
| **RTX A5000**              | Ampere       | 24GB  | 768 GB/s  | -    | 27.7      | 27.7      | -     | 55.4  | -     |
| **RTX A4500**              | Ampere       | 20GB  | 640 GB/s  | -    | 23.7      | 23.7      | -     | 47.4  | -     |
| **RTX A4000**              | Ampere       | 16GB  | 448 GB/s  | -    | 19.2      | 19.2      | -     | 38.4  | -     |
| **RTX 3090**               | Ampere       | 24GB  | 936 GB/s  | -    | 35.6      | 35.6      | -     | 71.2  | -     |
| **RTX 3090 Ti**            | Ampere       | 24GB  | 1.0 TB/s  | -    | 40        | 40        | -     | 80    | -     |
| **RTX 3080**               | Ampere       | 10GB  | 760 GB/s  | -    | 29.8      | 29.8      | -     | 59.6  | -     |
| **V100**                   | Volta        | 16GB  | 900 GB/s  | 7.8  | 15.7      | 31.4      | -     | -     | -     |
| **T4**                     | Turing       | 16GB  | 320 GB/s  | -    | 8.1       | 65        | -     | 130   | -     |
| **A10G**                   | Ampere       | 24GB  | 600 GB/s  | -    | 31.2      | 31.2      | -     | 62.4  | -     |

## Notes

- All TFLOPS values are theoretical maximum performance (non-sparse unless specified)
- Dash (-) means not supported by that architecture
- FP16/BF16 values shown are for Tensor Core performance where available
- RTX 5090 specifications based on Blackwell architecture with 5th gen Tensor Cores
- H100 SXM uses HBM3 memory with 3.35 TB/s bandwidth (not 3.0 TB/s)
- RTX PRO 6000 Blackwell features 96GB GDDR7 and targets professional workstations
- Consumer Blackwell GPUs (RTX 50 series) support FP4 precision
- Professional Ada GPUs (RTX 6000 Ada, L40S, etc.) use standard FP16 without sparsity
- Ampere A100 introduced support for structured sparsity (2:4) in Tensor Core operations
