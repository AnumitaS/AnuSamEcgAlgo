# ==============================================================================
# COPYRIGHT (C) 2026 BY [YOUR LLC NAME]. ALL RIGHTS RESERVED.
# Licensed under the Apache License, Version 2.0 (the "License");
# 
# DISCLAIMER OF WARRANTY: THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER 
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY 
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE of THIS SOFTWARE.
# ==============================================================================

import numpy as np


def adaptive_cluster_extreme_fast_new(arr, indices, fs):
    abs_arr = np.abs(arr)
    diffs = np.diff(indices)
    x = int(0.2 * fs)
    breaks = np.flatnonzero(diffs > x) + 1
    raw_r = []
    start = 0
    for b in np.append(breaks, len(indices)):
        c = indices[start:b]
        if c.size:
            r_point = c[np.argmax(abs_arr[c])]
            raw_r.append(r_point)
        start = b
    raw_r = np.array(raw_r)
    return np.array(raw_r, dtype=int)


def AnuSamEcgAlgo(ecg, fs):
    """ Proposed Adaptive R-Peak Detector. """
    abs_diffs = np.abs(np.diff(ecg))
    abs_diffs = np.append(abs_diffs, 0)
    mean_val, std_val = np.mean(abs_diffs), np.std(abs_diffs)
    thresh = mean_val + 2.3 * std_val
    indices = np.flatnonzero(abs_diffs > thresh) + 1
    return adaptive_cluster_extreme_fast_new(ecg, indices, fs)
