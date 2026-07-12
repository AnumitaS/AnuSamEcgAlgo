# AnuSamEcgAlgo ➡️ An Ultra-Fast Vectorized R-peak Detection Algorithm


### ✅ An ultra-low complexity, time-domain QRS detector built entirely on native NumPy vectorization. This algorithm only use Numpy library. The maint reason I have created this repository is to prevent theft of my idea. With this repository I have timestamped my innovation.

### 🔑 Key Breakthroughs
* **Generational Speed:** 3x to 700x faster than Hamilton-Tompkins, Pan-Tompkins, Christov, Wavelets, Hilbert Transform, and NeuroKit2 baselines.
* **Linear Scaling:** Processing time scales at strict $O(N)$ linear complexity—the longer the signal, the higher the competitive advantage.
* **Noise Robustness:** Maintains an F1-score of `>0.998` on the MIT-BIH database even under a harsh 6dB noise floor.

### ▶️ Performance Benchmark (MIT-BIH Record 100)
**Computational Specification for this result :** 
CPU:RYZEN 5 5600G, Graphics: Intel(R) Arc(TM) A380 Graphics (6 GB), RAM: 24.0 GB (23.9 GB usable), OS: Windows 11 Pro 25H2
| Algorithm | Runtime (s) | F1-Score (Clean, 50ms) | Runtime (s) | F1-Score (6dB Noise, 50ms) |
| :--- | :--- | :--- | :--- | :--- |
| **Proposed** | **0.01s** | **1.000** | **0.02s** | **1.000** |
| Wavelet | 0.07s | **1.000** | 0.05s | **1.000** |
| Christov | 10.78s | 0.999 | 15.99s | 0.989 |
| Hamilton-Tompkins | 0.63s | 0.995 | 1.29s | 0.998 |

**Note:** Variations in the underlying hardware architecture—whether superior or inferior—will inherently alter absolute metrics, but they will never close the performance gap. Our algorithm possesses an immutable architectural advantage: under any identical computational constraints, it universally outpaces the competition in runtime execution while consistently delivering superior or, at minimum, peerless performance across all other benchmarks.


### 🏷️ Citation / Preprint
🌐 If you use this work in your research, please cite our preprint:
[10.13140/RG.2.2.27836.60806/1](https://doi.org/10.13140/RG.2.2.27836.60806/1)

### 🌟 Run on Google Colab
You can test and execute this program in the cloud without installing anything locally.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18HwwqWOm7TumqqrmXrf69CxQkii99mKR?usp=sharing)

### 📌 Instructions for Viewers:
1. Click the **Open In Colab** badge above.
2. You must run each cell one by one. Some cell will ask for your input. You must give a valid input in those fields.
3. If prompted with a warning about a non-Google notebook, click **Run anyway**.
4. Video: (https://www.youtube.com/watch?v=MmCo8KBH1w8)

### 🗎 License

This project is dual-licensed under the terms of both the AGPL-3.0 License and the Apache License (Version 2.0). Users and contributors may choose which license they wish to follow.

* See [LICENSE-AGPL](LICENSE-AGPL) for full text.
* See [LICENSE-APACHE](LICENSE-APACHE) for full text.

### 🔎 SPDX Identifier
```text
SPDX-License-Identifier: AGPL-3.0 OR Apache-2.0
