import json
from typing import Dict, List

# GPU specifications (corrected values, using non-sparse TFLOPS)
GPU_SPECS = {
    # Blackwell Generation
    "RTX PRO 6000 Blackwell": {
        "vram_gb": 96,
        "bandwidth_gb_s": 1792,
        "fp16_tflops": 126,
    },
    "RTX 5090": {"vram_gb": 32, "bandwidth_gb_s": 1792, "fp16_tflops": 209.5},
    # Hopper Generation
    "H200 SXM": {"vram_gb": 141, "bandwidth_gb_s": 4800, "fp16_tflops": 989},
    "H100 SXM": {
        "vram_gb": 80,
        "bandwidth_gb_s": 3350,
        "fp16_tflops": 989,
    },  # Corrected bandwidth
    "H100 NVL": {"vram_gb": 94, "bandwidth_gb_s": 3900, "fp16_tflops": 989},
    "H100 PCIe": {"vram_gb": 80, "bandwidth_gb_s": 2000, "fp16_tflops": 756},
    # Ada Lovelace Generation
    "RTX 6000 Ada": {"vram_gb": 48, "bandwidth_gb_s": 960, "fp16_tflops": 91.1},
    "RTX 4090": {"vram_gb": 24, "bandwidth_gb_s": 1000, "fp16_tflops": 82.6},
    "RTX 4000 Ada": {"vram_gb": 20, "bandwidth_gb_s": 320, "fp16_tflops": 26.5},
    "RTX 2000 Ada": {"vram_gb": 16, "bandwidth_gb_s": 288, "fp16_tflops": 12},
    "L40S": {"vram_gb": 48, "bandwidth_gb_s": 864, "fp16_tflops": 91.6},
    "L40": {"vram_gb": 48, "bandwidth_gb_s": 864, "fp16_tflops": 90.5},
    "L4": {"vram_gb": 24, "bandwidth_gb_s": 300, "fp16_tflops": 30.3},
    # Ampere Generation
    "A100 SXM": {"vram_gb": 80, "bandwidth_gb_s": 2000, "fp16_tflops": 312},
    "A100 PCIe 80GB": {"vram_gb": 80, "bandwidth_gb_s": 2000, "fp16_tflops": 312},
    "A100 PCIe 40GB": {"vram_gb": 40, "bandwidth_gb_s": 1600, "fp16_tflops": 312},
    "A40": {"vram_gb": 48, "bandwidth_gb_s": 696, "fp16_tflops": 37.4},
    "RTX A6000": {"vram_gb": 48, "bandwidth_gb_s": 768, "fp16_tflops": 38.7},
    "RTX A5000": {"vram_gb": 24, "bandwidth_gb_s": 768, "fp16_tflops": 27.7},
    "RTX A4500": {"vram_gb": 20, "bandwidth_gb_s": 640, "fp16_tflops": 23.7},
    "RTX A4000": {"vram_gb": 16, "bandwidth_gb_s": 448, "fp16_tflops": 19.2},
    "RTX 3090": {"vram_gb": 24, "bandwidth_gb_s": 936, "fp16_tflops": 35.6},
    "RTX 3090 Ti": {"vram_gb": 24, "bandwidth_gb_s": 1008, "fp16_tflops": 40},
    "RTX 3080": {"vram_gb": 10, "bandwidth_gb_s": 760, "fp16_tflops": 29.8},
    # Older Generation
    "V100": {"vram_gb": 16, "bandwidth_gb_s": 900, "fp16_tflops": 31.4},
    "T4": {"vram_gb": 16, "bandwidth_gb_s": 320, "fp16_tflops": 65},
    "A10G": {"vram_gb": 24, "bandwidth_gb_s": 600, "fp16_tflops": 31.2},
}

# Provider pricing data (updated with correct Novita prices)
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
    "novita": {
        "name": "Novita AI",
        "pricing": {
            "ondemand": {
                "RTX 5090": 0.50,
                "L40S": 0.55,
                "RTX 4090": 0.35,
                "RTX 4090 HF": 0.69,  # High frequency variant
                "RTX 3090": 0.21,
                "RTX 6000 Ada": 0.70,
                "A100 SXM": 1.60,
                "H100 SXM": 2.56,
                "H200 SXM": 3.25,
            }
        },
    },
    "aws": {
        "name": "AWS",
        "pricing": {
            "ondemand": {
                # P-series - divide by GPU count
                "H100 SXM": 98.32 / 8,  # p5.48xlarge
                "H200 SXM": 120.0 / 8,  # p5e.48xlarge estimate
                "A100 PCIe 40GB": 32.77 / 8,  # p4d.24xlarge
                "A100 PCIe 80GB": 40.77 / 8,  # p4de.24xlarge
                "V100": 24.48 / 8,  # p3.16xlarge
                # G-series - single GPU
                "L40S": 7.22,  # g6e.xlarge
                "L4": 0.99,  # g6.xlarge
                "A10G": 1.01,  # g5.xlarge
                "T4": 0.53,  # g4dn.xlarge
            }
        },
    },
    "gcp": {
        "name": "Google Cloud",
        "pricing": {
            "ondemand": {
                "H100 SXM": 98.32 / 8,  # a3-megagpu-8g
                "A100 PCIe 80GB": 3.67,  # a2-ultragpu-1g
                "A100 PCIe 40GB": 1.89,  # a2-highgpu-1g
                "L4": 0.81,  # g2-standard-4
                "V100": 2.48,  # n1 + gpu
                "T4": 0.35,  # n1 + gpu
            }
        },
    },
    "sfcompute": {
        "name": "SFCompute",
        "pricing": {
            "market": {
                "H100 SXM": 2.30,
                "H200 SXM": 2.50,
            }
        },
    },
    "fluidstack": {
        "name": "FluidStack",
        "pricing": {
            "ondemand": {
                "H200 SXM": 2.20,
                "H100 SXM": 1.99,
                "A100 PCIe 80GB": 1.40,
                "A100 PCIe 40GB": 1.20,
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


def calculate_value_score(metrics: Dict, weights: Dict[str, float]) -> float:
    """Calculate a weighted value score for a GPU offering"""
    if metrics is None:
        return 0

    # Create normalized scores based on typical ranges
    # These ranges represent "good" values for each metric
    vram_score = min(metrics["vram_per_dollar"] / 50, 2.0)  # 50 GB/$ is excellent
    bandwidth_score = min(
        metrics["bandwidth_per_dollar"] / 1000, 2.0
    )  # 1000 GB/s/$ is excellent
    tflops_score = min(
        metrics["tflops_per_dollar"] / 200, 2.0
    )  # 200 TFLOPS/$ is excellent

    # Apply weights and sum
    weighted_score = (
        weights["vram"] * vram_score
        + weights["bandwidth"] * bandwidth_score
        + weights["tflops"] * tflops_score
    )

    return weighted_score * 100  # Scale to 0-100 range


def process_provider(provider_key: str, provider_data: Dict) -> Dict:
    """Process all GPUs for a provider"""
    result = {"name": provider_data["name"], "tiers": {}}

    weight_profiles = {
        "balanced": {"vram": 0.33, "bandwidth": 0.33, "tflops": 0.34},
        "vram_focused": {"vram": 0.5, "bandwidth": 0.25, "tflops": 0.25},
        "compute_focused": {"vram": 0.25, "bandwidth": 0.25, "tflops": 0.5},
        "bandwidth_focused": {"vram": 0.25, "bandwidth": 0.5, "tflops": 0.25},
    }

    for tier_name, pricing in provider_data["pricing"].items():
        tier_data = {"gpus": [], "scores": {}}

        # Calculate metrics for each GPU
        gpu_metrics = []
        for gpu_name, price in pricing.items():
            metrics = calculate_metrics(gpu_name, price)
            if metrics:
                gpu_metrics.append(metrics)

        tier_data["gpus"] = gpu_metrics

        # Calculate scores for each weight profile
        for profile_name, weights in weight_profiles.items():
            scores = []
            for metrics in gpu_metrics:
                score = calculate_value_score(metrics, weights)
                scores.append(
                    {
                        "gpu": metrics["gpu"],
                        "score": round(score, 2),
                        "price": metrics["price_per_hour"],
                    }
                )

            # Sort by score descending
            tier_data["scores"][profile_name] = sorted(
                scores, key=lambda x: x["score"], reverse=True
            )

        result["tiers"][tier_name] = tier_data

    return result


def find_best_overall(all_results: Dict) -> Dict:
    """Find the best GPUs across all providers"""
    weight_profiles = {
        "balanced": {"vram": 0.33, "bandwidth": 0.33, "tflops": 0.34},
        "vram_focused": {"vram": 0.5, "bandwidth": 0.25, "tflops": 0.25},
        "compute_focused": {"vram": 0.25, "bandwidth": 0.25, "tflops": 0.5},
        "bandwidth_focused": {"vram": 0.25, "bandwidth": 0.5, "tflops": 0.25},
    }

    best_overall = {}

    for profile_name, weights in weight_profiles.items():
        all_scores = []

        for provider_key, provider_data in all_results.items():
            for tier_name, tier_data in provider_data["tiers"].items():
                for gpu_data in tier_data["gpus"]:
                    score = calculate_value_score(gpu_data, weights)
                    all_scores.append(
                        {
                            "provider": provider_data["name"],
                            "tier": tier_name,
                            "gpu": gpu_data["gpu"],
                            "score": round(score, 2),
                            "price": gpu_data["price_per_hour"],
                            "vram_per_dollar": round(gpu_data["vram_per_dollar"], 2),
                            "bandwidth_per_dollar": round(
                                gpu_data["bandwidth_per_dollar"], 0
                            ),
                            "tflops_per_dollar": round(
                                gpu_data["tflops_per_dollar"], 2
                            ),
                        }
                    )

        # Sort by score and take top 10
        best_overall[profile_name] = sorted(
            all_scores, key=lambda x: x["score"], reverse=True
        )[:10]

    return best_overall


def main():
    results = {}

    # Process each provider
    for provider_key, provider_data in PROVIDERS.items():
        results[provider_key] = process_provider(provider_key, provider_data)

    # Find best overall offerings
    best_overall = find_best_overall(results)

    # Create output structure
    output = {"providers": results, "best_overall": best_overall}

    # Pretty print JSON
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
