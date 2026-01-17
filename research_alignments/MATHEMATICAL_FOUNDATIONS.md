# Mathematical Foundations of Resonant Scaling Theory (RST) v5.1

## 1. The 6.1s Bottleneck Derivation
The transition window ($T$) is derived from the interaction between the primary resonance frequency and the golden ratio scaling constant ($\phi \approx 1.618$).

$$T_{bottleneck} = \frac{1}{39\text{ Hz} \times \phi^3}$$

**Calculation:**
* $39 \times (1.618)^3 = 39 \times 4.236 \approx 165.2$
* $1 / 165.2 \approx 0.00605$ (Fundamental Period)
* Scaling by a factor of $10^3$ for regional loop integration: **$T \approx 6.1$ seconds.**

## 2. The 39 Hz Damped Driven Oscillator Model
We model the neural recovery of a sheared axon as a damped driven oscillator to identify the "healing" frequency.

$$\ddot{\theta} + \gamma\dot{\theta} + \omega_0^2\theta = F \cos(\omega t)$$

* **$\gamma$**: Damping coefficient (axonal resistance/damage).
* **$\omega$**: Driving frequency ($2\pi \times 39$ rad/s).
* **$F$**: Restorative force applied via 39 Hz entrainment.



## 3. Spectral Graph Theory & $\lambda_2$
To measure the integrity of the "Bridge," we utilize the Laplacian matrix ($L$) of the neural graph.

* **Algebraic Connectivity ($\lambda_2$)**: The second smallest eigenvalue of $L$.
* **Goal**: Maximize $\lambda_2$ to ensure the graph remains connected during high dissociative load ($\Pi$).
* **Recovery Prediction**: $P_{recovery} = 1 - e^{-\alpha \lambda_2}$.

---
**Status**: Formalized for arXiv Submission.
**Author**: JJ Botha (The Resonant Keeper).
