# PRCE Audio Examples

**Access the interactive examples:** https://rdoerfler.github.io/prce-examples/

Please consider listening with headphones.

**Note:** All audio examples are direct network outputs without post-processing. For easier comparison and better audibility, they have been normalized to 0dBFS on this webpage.

## Overview

This repository contains audio examples comparing Target sounds with HPN and PTR variants of the Procedural Engines Model (PRCE) across three datasets (C, B, A) from the Procedural Engine Sounds Dataset [1]. The datasets are presented in order of decreasing complexity to facilitate comparative assessment.

The main model development and research can be found at: https://github.com/rdoerfler/prce-model

## What You're Hearing

- **Target**: Ground truth engine sounds from the test/validation sets
- **HPN**: Harmonic-Plus-Noise model variant - produces smoother, more continuous sounds
- **PTR**: Pulse-Train-Resonator model variant - exhibits characteristic pulse-train resonator signatures

The examples include:
- **Best Predictions**: Curated examples from test set inference using the best-performing models
- **First Predictions**: Examples from validation set using first epoch models (baseline comparison, revealing each model's inherent acoustic biases)

All audio examples represent unseen data, ensuring unbiased model evaluation. The distinct sonic characteristics of each synthesizer architecture become particularly audible in the contrast between PTR's pulse-train resonator nature and HPN's smoother, more continuous approach.

## References

[1] Doerfler, R. (2025). Procedural Engine Sounds Dataset (Version 1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.16883336

<details>
<summary>BibTeX</summary>

```bibtex
@dataset{doerfler_2025_procedural_engine_sounds,
  author       = {Doerfler, Robin},
  title        = {Procedural Engine Sounds Dataset},
  month        = {August},
  year         = 2025,
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.16883336},
  url          = {https://doi.org/10.5281/zenodo.16883336}
}
```

</details>

## Model Performance

Best validation losses (lower is better):

| Dataset | HPN Harmonic | HPN STFT | HPN Total | PTR Harmonic | PTR STFT | PTR Total |
|---------|--------------|----------|-----------|--------------|----------|-----------|
| A       | 0.107        | 1.781    | 0.944     | **0.090**    | **1.649** | **0.872** |
| B       | 0.059        | 1.824    | 0.943     | **0.055**    | **1.754** | **0.907** |
| C       | 0.166        | 2.093    | 1.132     | **0.117**    | **2.017** | **1.069** |
| Mean    | 0.111        | 1.899    | 1.006     | 0.088        | 1.807     | 0.949     |

PTR models consistently outperform HPN across all datasets and loss components.

## Repository Structure

```
index.html
README.md
audiofiles/
├─ HPN/
│  ├─ A/
│  │  ├─ test_inference/targets/
│  │  ├─ test_inference/predictions/
│  │  ├─ epoch_001/targets/
│  │  └─ epoch_001/predictions/
│  ├─ B/
│  └─ C/
├─ PTR/
│  ├─ A/
│  ├─ B/
│  └─ C/
```