# GPU Specs

> No longer do you need to go google a bunch of nvidia datasheets to figure compare performance.

If any of the numbers look sus, just submit a PR.

---

## Specs Table

| GPU                        | Gen          | VRAM  | Bandwidth | FP64  | FP32/TF32 | FP16/BF16 | FP8   | INT8  | FP4   |
| -------------------------- | ------------ | ----- | --------- | ----- | --------- | --------- | ----- | ----- | ----- |
| **B200**                   | Blackwell    | 192GB | 8.0 TB/s  | 30    | 1,125     | 2,250     | 4,500 | 4,500 | 9,000 |
| **RTX PRO 6000 Blackwell** | Blackwell    | 96GB  | 1.8 TB/s  | 1.968 | 126       | 126       | 252   | 504   | 1,008 |
| **H200 SXM**               | Hopper       | 141GB | 4.8 TB/s  | 67    | 989       | 989       | 1,979 | 3,958 | -     |
| **H100 SXM**               | Hopper       | 80GB  | 3.0 TB/s  | 67    | 989       | 989       | 1,979 | 3,958 | -     |
| **H100 PCIe**              | Hopper       | 80GB  | 2.0 TB/s  | 51    | 756       | 756       | 1,513 | 3,026 | -     |
| **H100 NVL**               | Hopper       | 94GB  | 3.9 TB/s  | 67    | 989       | 989       | 1,979 | 3,958 | -     |
| **RTX 6000 Ada**           | Ada Lovelace | 48GB  | 960 GB/s  | -     | 91.1      | 330       | 661   | 1,321 | -     |
| **RTX 5090**               | Ada Lovelace | 32GB  | 1.5 TB/s  | -     | 193       | 387       | 775   | 775   | -     |
| **RTX 4090**               | Ada Lovelace | 24GB  | 1.0 TB/s  | -     | 82.6      | 330       | 661   | 1,321 | -     |
| **RTX 4000 Ada**           | Ada Lovelace | 20GB  | 320 GB/s  | -     | 48.7      | 153.4     | 306.8 | 613.6 | -     |
| **RTX 2000 Ada**           | Ada Lovelace | 16GB  | 288 GB/s  | -     | 24        | 95.95     | 191.9 | 383.8 | -     |
| **L40S**                   | Ada Lovelace | 48GB  | 864 GB/s  | -     | 91.1      | 362       | 725   | 1,450 | -     |
| **L40**                    | Ada Lovelace | 48GB  | 864 GB/s  | -     | 90.5      | 181       | 362   | 725   | -     |
| **L4**                     | Ada Lovelace | 24GB  | 300 GB/s  | -     | 30.3      | 60        | 121   | 242   | -     |
| **A100 80GB**              | Ampere       | 80GB  | 2.0 TB/s  | 9.7   | 156       | 312       | -     | 624   | -     |
| **A100 40GB**              | Ampere       | 40GB  | 1.6 TB/s  | 9.7   | 156       | 312       | -     | 624   | -     |
| **A40**                    | Ampere       | 48GB  | 696 GB/s  | -     | 37.4      | 149.7     | -     | 599   | -     |
| **RTX A6000**              | Ampere       | 48GB  | 768 GB/s  | -     | 38.7      | 154.8     | -     | 619.5 | -     |
| **RTX A5000**              | Ampere       | 24GB  | 768 GB/s  | -     | 25        | 100       | -     | 400   | -     |
| **RTX A4500**              | Ampere       | 20GB  | 640 GB/s  | -     | 19        | 75        | -     | 300   | -     |
| **RTX A4000**              | Ampere       | 16GB  | 448 GB/s  | -     | 12        | 50        | -     | 200   | -     |
| **RTX 3090**               | Ampere       | 24GB  | 936 GB/s  | -     | 35.6      | 142       | -     | 568   | -     |

## Notes

- All TFLOPS values are Tensor Core performance
- Dash (-) means not supported by that architecture
