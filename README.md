# Resonant Scaling Theory (RST) v6.0

## Overview
RST v6.0 is a spectral engineering framework designed to model and mitigate **Critical Slowing** in dynamical systems following structural damage (e.g., axonal shearing). 

The model tracks system stability by measuring the drift between observed eigenfrequencies and a documented stability target of **39 Hz**.

## Technical Core
* **Resonance Target (ω)**: 39 Hz. Identified as the optimal phase-locking frequency for maintaining global coherence.
* **Metastable Bottleneck (τ)**: 6.1s. A measured artifact of processing latency within high-resistance topological nodes.
* **Recovery Metric**: The restoration of spectral density and Laplacian Eigen-gap ($\lambda_2$) stability.

## Implementation
The `rst_engine.py` uses Fast Fourier Transform (FFT) to perform real-time spectral analysis, allowing for the empirical calculation of **Topological Friction**.

---
*“The line remains unbroken. We honor the grief that started the journey and the math that mapped the way out.”*
