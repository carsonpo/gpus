import json
from typing import Dict, List

# GPU specifications (constant across providers)
GPU_SPECS = {
    "H200 SXM": {"vram_gb": 141, "bandwidth_gb_s": 4800, "fp16_tflops": 989},
    "H100 SXM": {"vram_gb": 80, "bandwidth_gb_s": 3000, "fp16_tflops": 989},
    "H100 NVL": {"vram_gb": 94, "bandwidth_gb_s": 3900, "fp16_tflops": 989},
    "H100 PCIe": {"vram_gb": 80, "bandwidth_gb_s": 2000, "fp16_tflops": 756},
    "A100 SXM": {"vram_gb": 80, "bandwidth_gb_s": 2000, "fp16_tflops": 312},
    "A100 PCIe 80GB": {"vram_gb": 80, "bandwidth_gb_s": 2000, "fp16_tflops": 312},
    "A100 PCIe 40GB": {"vram_gb": 40, "bandwidth_gb_s": 1600, "fp16_tflops": 312},
    "RTX 6000 Ada": {"vram_gb": 48, "bandwidth_gb_s": 960, "fp16_tflops": 330},
    "RTX 5090": {"vram_gb": 32, "bandwidth_gb_s": 1500, "fp16_tflops": 387},
    "RTX 4090": {"vram_gb": 24, "bandwidth_gb_s": 1000, "fp16_tflops": 330},
    "RTX 4000 Ada": {"vram_gb": 20, "bandwidth_gb_s": 320, "fp16_tflops": 153.4},
    "RTX 2000 Ada": {"vram_gb": 16, "bandwidth_gb_s": 288, "fp16_tflops": 95.95},
    "L40S": {"vram_gb": 48, "bandwidth_gb_s": 864, "fp16_tflops": 362},
    "L40": {"vram_gb": 48, "bandwidth_gb_s": 864, "fp16_tflops": 181},
    "L4": {"vram_gb": 24, "bandwidth_gb_s": 300, "fp16_tflops": 60},
    "A40": {"vram_gb": 48, "bandwidth_gb_s": 696, "fp16_tflops": 149.7},
    "RTX A6000": {"vram_gb": 48, "bandwidth_gb_s": 768, "fp16_tflops": 154.8},
    "RTX A5000": {"vram_gb": 24, "bandwidth_gb_s": 768, "fp16_tflops": 100},
    "RTX A4500": {"vram_gb": 20, "bandwidth_gb_s": 640, "fp16_tflops": 75},
    "RTX A4000": {"vram_gb": 16, "bandwidth_gb_s": 448, "fp16_tflops": 50},
    "RTX 3090": {"vram_gb": 24, "bandwidth_gb_s": 936, "fp16_tflops": 142},
    "RTX 3090 Ti": {"vram_gb": 24, "bandwidth_gb_s": 1008, "fp16_tflops": 160},
    "RTX 3080": {"vram_gb": 10, "bandwidth_gb_s": 760, "fp16_tflops": 119},
    "V100": {"vram_gb": 16, "bandwidth_gb_s": 900, "fp16_tflops": 125},
    "T4": {"vram_gb": 16, "bandwidth_gb_s": 320, "fp16_tflops": 65},
    "A10G": {"vram_gb": 24, "bandwidth_gb_s": 600, "fp16_tflops": 125},
}

# Provider pricing data
PROVIDERS = {
    "runpod": {
        "name": "RunPod",
        "pricing": {
            "secure": {
                "H200 SXM": 3.99,
                "H100 SXM": 2.99,
                "H100 NVL": 2.79,
                "H100 PCIe": 2.39,
                "A100 SXM": 1.89,
                "A100 PCIe 80GB": 1.64,
                "L40S": 0.86,
                "L40": 0.99,
                "RTX 6000 Ada": 0.77,
                "RTX A6000": 0.49,
                "A40": 0.40,
                "RTX 5090": 0.89,
                "RTX 4090": 0.69,
                "L4": 0.43,
                "RTX A5000": 0.26,
                "RTX 3090": 0.43,
                "RTX A4500": 0.34,
                "RTX 4000 Ada": 0.34,
                "RTX A4000": 0.29,
                "RTX 2000 Ada": 0.28,
            },
            "community": {
                "H200 SXM": 3.59,
                "H100 SXM": 2.69,
                "H100 NVL": 2.59,
                "H100 PCIe": 1.99,
                "A100 PCIe 80GB": 1.19,
                "L40S": 0.79,
                "L40": 0.69,
                "RTX 6000 Ada": 0.74,
                "RTX A6000": 0.33,
                "RTX 5090": 0.69,
                "RTX 4090": 0.34,
                "RTX A5000": 0.16,
                "RTX 3090": 0.22,
                "RTX 3090 Ti": 0.27,
                "RTX A4500": 0.19,
                "RTX 4000 Ada": 0.20,
                "RTX A4000": 0.17,
                "V100": 0.19,
                "RTX 3080": 0.17,
            },
        },
    },
    "aws": {
        "name": "AWS",
        "pricing": {
            "ondemand": {
                # P-series - divide by GPU count
                "H100 SXM": 98.32 / 8,  # p5.48xlarge
                "H200 SXM": 120.0 / 8,  # p5e.48xlarge estimate
                "A100 PCIe 40GB": 22.0 / 8,  # p4d.24xlarge
                "A100 PCIe 80GB": 27.0 / 8,  # p4de.24xlarge
                "V100": 24.48 / 8,  # p3.16xlarge
                # G-series - single GPU
                "L40S": 1.50,  # g6e.xlarge
                "L4": 0.80,  # g6.xlarge
                "A10G": 1.00,  # g5.xlarge
                "T4": 0.53,  # g4dn.xlarge
            }
        },
    },
    "gcp": {
        "name": "Google Cloud",
        "pricing": {
            "ondemand": {
                "H100 SXM": 88.49 / 8,  # a3-megagpu-8g
                "A100 PCIe 80GB": 7.50,  # a2-ultragpu-1g
                "A100 PCIe 40GB": 3.67,  # a2-highgpu-1g
                "L4": 1.00,  # g2-standard-4
                "V100": 2.55,  # n1 + gpu
                "T4": 0.35,  # n1 + gpu
            }
        },
    },
    "sfcompute": {
        "name": "SFCompute",
        "pricing": {
            "market": {
                "H100 SXM": 2.30,
                "H200 SXM": 2.50,  # estimate
            }
        },
    },
    "novita": {
        "name": "Novita AI",
        "pricing": {
            "ondemand": {
                "H100 SXM": 2.99,
                "A100 PCIe 80GB": 0.35,
                "RTX 4090": 0.50,  # estimate
            }
        },
    },
    "fluidstack": {
        "name": "FluidStack",
        "pricing": {
            "ondemand": {
                "H200 SXM": 2.20,  # estimate
                "H100 SXM": 1.99,
                "A100 PCIe 80GB": 1.40,
                "A100 PCIe 40GB": 1.20,  # estimate
            }
        },
    },
}


def calculate_metrics(gpu_name: str, price_per_hour: float) -> Dict:
    """Calculate per-dollar metrics for a GPU"""
    if gpu_name not in GPU_SPECS:
        return None

    specs = GPU_SPECS[gpu_name]

    return {
        "gpu": gpu_name,
        "price_per_hour": price_per_hour,
        "vram_per_dollar": specs["vram_gb"] / price_per_hour,
        "bandwidth_per_dollar": specs["bandwidth_gb_s"] / price_per_hour,
        "tflops_per_dollar": specs["fp16_tflops"] / price_per_hour,
    }


def normalize_scores(scores: List[float]) -> List[float]:
    """Normalize scores to 0-100 scale"""
    if not scores or max(scores) == 0:
        return scores
    max_score = max(scores)
    return [100 * s / max_score for s in scores]


def calculate_weighted_scores(
    metrics_list: List[Dict], weights: Dict[str, float]
) -> List[float]:
    """Calculate weighted scores based on metrics"""
    scores = []

    for m in metrics_list:
        if m is None:
            scores.append(0)
            continue

        score = (
            weights["vram"]
            * m["vram_per_dollar"]
            / 100  # Normalize by dividing by rough scale
            + weights["bandwidth"] * m["bandwidth_per_dollar"] / 1000
            + weights["tflops"] * m["tflops_per_dollar"] / 100
        )
        scores.append(score)

    return normalize_scores(scores)


def process_provider(provider_key: str, provider_data: Dict) -> Dict:
    """Process all GPUs for a provider"""
    result = {"name": provider_data["name"], "tiers": {}}

    weight_profiles = {
        "vram_focused": {"vram": 0.5, "bandwidth": 0.25, "tflops": 0.25},
        "compute_focused": {"vram": 0.25, "bandwidth": 0.25, "tflops": 0.5},
        "bandwidth_focused": {"vram": 0.25, "bandwidth": 0.5, "tflops": 0.25},
    }

    for tier_name, pricing in provider_data["pricing"].items():
        tier_data = {"gpus": [], "scores": {}}

        # Calculate metrics for each GPU
        for gpu_name, price in pricing.items():
            metrics = calculate_metrics(gpu_name, price)
            if metrics:
                tier_data["gpus"].append(metrics)

        # Calculate scores for each weight profile
        for profile_name, weights in weight_profiles.items():
            scores = calculate_weighted_scores(tier_data["gpus"], weights)
            tier_data["scores"][profile_name] = [
                {"gpu": tier_data["gpus"][i]["gpu"], "score": scores[i]}
                for i in range(len(scores))
            ]

        result["tiers"][tier_name] = tier_data

    return result


def main():
    results = {}

    for provider_key, provider_data in PROVIDERS.items():
        results[provider_key] = process_provider(provider_key, provider_data)

    # Pretty print JSON
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
