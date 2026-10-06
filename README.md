# Deterministic Gravitational Wave Closed-Loop Inversion Suite

[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--3627--6997-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0004-3627-6997)
[![Zenodo Master DOI](https://img.shields.io/badge/Zenodo_Master_DOI-10.5281%2Fzenodo.23180574-blue?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.23180574)
[![Foundational Monograph Suite](https://img.shields.io/badge/Foundational_Theory-10.5281%2Fzenodo.23117791-green?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.23117791)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Research_Preprint-blue?style=flat-square)

> **"Sub-Second Deterministic Inversion, Relativistic Conservation Closure, and Double Residual Null Verification Across GWTC-1 Benchmarks"**  
> An open-science computational astrophysics suite providing an autonomous, deterministic closed-loop pipeline (v5.5) for binary black hole (BBH) parameter extraction. Bypasses the heavy computational latency of stochastic Markov Chain Monte Carlo (MCMC) and Nested Sampling frameworks by unifying frequency-domain Wiener matched filtering with exact general relativistic numerical relativity conservation laws, Wigner-Smith Lyapunov boundary regularization, and coherent beamforming.

---

## Repository Structure & File Inventory

The repository is structured into two open-access research manuscripts at the root, five standalone execution modules in `scripts/`, and all raw detector strains, intermediate binary tensors, and audit outputs centralized in `data/`:

```text
├── LICENSE
├── README.md
├── Deterministic_GW_Pipeline_Report.pdf
├── Theoretical_Foundations_Companion.pdf
├── scripts/
│   ├── pipeline_runner.py
│   ├── stage1_blind_extractor.py
│   ├── stage2_gr_engine.py
│   ├── stage3_report_compiler.py
│   └── extract_kerr_spin.py
└── data/
    ├── H1_GW150914_4kHz.hdf5
    ├── L1_GW150914_4kHz.hdf5
    ├── GW170814_H1.hdf5
    ├── GW170814_L1.hdf5
    ├── GW170104_H1.hdf5
    ├── GW170104_L1.hdf5
    ├── GW170823_H1.hdf5
    ├── GW170823_L1.hdf5
    ├── stage1_output/
    ├── stage2_output/
    ├── spin_analysis_summary.csv
    ├── spin_analysis_summary.json
    └── deterministic_imr_blind_audit_report_v3.pdf
