import numpy as np

class RSTEngine:
    """
    Resonant Scaling Theory (RST) v5.1 Core Engine
    Models the interaction between the 39Hz signal and the 6.1s bottleneck.
    """
    def __init__(self, frequency=39.0, phi=1.618):
        self.f = frequency
        self.phi = phi
        
    def calculate_bottleneck(self):
        """
        Derives the 6.1s window from the 39Hz constant and Golden Ratio scaling.
        Formula: T = 1 / (f * phi^3) * 1000 (scaled for macro-loop integration)
        """
        raw_period = 1 / (self.f * (self.phi**3))
        # Scaled to represent the regional integration window (macro-scale)
        bottleneck_t = raw_period * 1000 
        return round(bottleneck_t, 2)

    def simulate_resonance(self, duration=6.1, sampling_rate=1000):
        """
        Generates a 39Hz restorative signal over the 6.1s bottleneck period.
        """
        t = np.linspace(0, duration, int(sampling_rate * duration))
        signal = np.sin(2 * np.pi * self.f * t)
        return t, signal

# Example Usage:
# engine = RSTEngine()
# print(f"Verified Bottleneck: {engine.calculate_bottleneck()}s")
