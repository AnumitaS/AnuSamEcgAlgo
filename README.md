# AnuSamEcgAlgo
# Ultra-Fast Vectorized QRS Detector

An ultra-low complexity, time-domain QRS detector built entirely on native NumPy vectorization. This algorithm only use Numpy library.

## Key Breakthroughs
* **Generational Speed:** 3x to 700x faster than Wavelets, Hilbert Transform, and NeuroKit2 baselines.
* **Linear Scaling:** Processing time scales at strict $O(N)$ linear complexity—the longer the signal, the higher the competitive advantage.
* **Noise Robustness:** Maintains an F1-score of `>0.998` on the MIT-BIH database even under a harsh 6dB noise floor.

## Performance Benchmark (MIT-BIH Record 100)
| Method | Runtime (s) | F1-Score (Clean) | Runtime (s) | F1-Score (6dB Noise) |
| :--- | :--- | :--- | :--- | :--- |
| **Proposed** | **0.01s** | **1.000** | **0.02s** | **1.000** |
| Wavelet | 0.07s | 1.000 | 0.05s | 1.000 |
| Christov | 10.78s | 0.999 | 15.99s | 0.989 |
| HTompkins | 0.63s | 0.995 | 1.29s | 0.998 |


## Citation / Preprint
If you use this work in your research, please cite our preprint:
[10.13140/RG.2.2.27836.60806/1](https://doi.org/10.13140/RG.2.2.27836.60806/1)
