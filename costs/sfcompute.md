# SFCompute GPU Pricing

> Marketplace for large-scale GPU clusters with InfiniBand interconnect.

Market-based pricing with ability to buy and sell contracts. No long-term lock-in.

---

## Available GPUs

| GPU Type       | Interconnect       | Price Range  | Notes                |
| -------------- | ------------------ | ------------ | -------------------- |
| **H100 80GB**  | 3.2Tb/s InfiniBand | ~$2.30/hr    | Market pricing       |
| **H200 141GB** | 3.2Tb/s InfiniBand | Market-based | Limited availability |

## Deployment Options

**Kubernetes Clusters**

- Full InfiniBand fabric included
- 3.2Tb/s interconnect
- Ideal for distributed training

**Virtual Machines**

- No InfiniBand support yet
- More flexible configurations
- Quick deployment

**Bare Metal**

- Contact for custom configs
- Full hardware control
- Enterprise support

## Pricing Model

**Market-Based**

- Buy at your max price
- Sell unused capacity
- No fixed rates

**Example CLI Usage**

```bash
# Buy 256 H100s for 3 days at max $2.30/GPU/hr
$ sf buy -n 256 -d 3d -p 2.3

# Sell part of contract for $2.10/GPU/hr
$ sf sell -c <contract> -s tomorrow -d 1d -p 2.1
```
