import sys
import json
from client import DaubechiesD4Wavelet

def main():
    dwt = DaubechiesD4Wavelet()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "forward":
            approx, detail = dwt.forward(params.get("signal", []))
            res = {"approximation": approx, "detail": detail}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
