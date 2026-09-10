from client import DaubechiesD4Wavelet

def main():
    print("=== Testing Daubechies D4 Wavelet Transform ===")
    dwt = DaubechiesD4Wavelet()
    sig = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    approx, detail = dwt.forward(sig)
    print("Approximation subband:", [round(a, 3) for a in approx])
    print("Detail subband:", [round(d, 3) for d in detail])

    assert len(approx) == 4 and len(detail) == 4
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
