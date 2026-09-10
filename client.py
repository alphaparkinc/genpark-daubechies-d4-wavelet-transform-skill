import math

class DaubechiesD4Wavelet:
    """
    Daubechies D4 Discrete Wavelet Transform (DWT) Engine.
    Uses 4-tap scaling and wavelet coefficients for orthogonal decomposition.
    """
    def __init__(self):
        h0 = (1.0 + math.sqrt(3.0)) / (4.0 * math.sqrt(2.0))
        h1 = (3.0 + math.sqrt(3.0)) / (4.0 * math.sqrt(2.0))
        h2 = (3.0 - math.sqrt(3.0)) / (4.0 * math.sqrt(2.0))
        h3 = (1.0 - math.sqrt(3.0)) / (4.0 * math.sqrt(2.0))
        self.h = [h0, h1, h2, h3]
        self.g = [h3, -h2, h1, -h0]

    def forward(self, x):
        n = len(x)
        approx = []
        detail = []
        for i in range(0, n, 2):
            a = 0.0
            d = 0.0
            for j in range(4):
                idx = (i + j) % n
                a += self.h[j] * x[idx]
                d += self.g[j] * x[idx]
            approx.append(a)
            detail.append(d)
        return approx, detail
