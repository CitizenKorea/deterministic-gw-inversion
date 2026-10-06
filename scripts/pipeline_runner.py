#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PIPELINE RUNNER v3.0: Executes 3-Stage Coherent Blind Audit End-to-End
Stage 1: Coherent Beamforming & Adaptive Plunge Feature Extraction -> Saves NPZ
Stage 2: Deterministic Relativistic Closed-Loop Optimization -> Saves JSON & NPZ
Stage 3: Scientific Forensic Report PDF Compiler -> Generates Multi-Page PDF
"""

import os
import glob
import json
import numpy as np

import stage1_blind_extractor as s1
import stage2_gr_engine as s2
import stage3_report_compiler as s3

TARGET_EVENTS = [
    {'name': 'GW150914', 'gps': 1126259462.427},
    {'name': 'GW170814', 'gps': 1186741861.530},
    {'name': 'GW170104', 'gps': 1167559936.600},
    {'name': 'GW170823', 'gps': 1187529256.500}
]

def main():
    print("=" * 88)
    print("STARTING 3-STAGE DETERMINISTIC COHERENT BEAMFORMED BLIND AUDIT PIPELINE")
    print("=" * 88)

    # STAGE 1: Coherent Beamforming & Adaptive Plunge Feature Extraction
    os.makedirs("stage1_output", exist_ok=True)
    stage1_files = []
    for ev in TARGET_EVENTS:
        try:
            fpath = s1.process_event_stage1(ev['name'], ev['gps'], output_dir="stage1_output")
            stage1_files.append(fpath)
        except Exception as e:
            print(f"[!] Stage 1 error for {ev['name']}: {e}")

    # STAGE 2: Deterministic Relativistic Closed-Loop Optimization
    os.makedirs("stage2_output", exist_ok=True)
    all_metrics = []
    all_waveforms = {}

    for s1_fpath in stage1_files:
        try:
            metrics, arrays = s2.audit_event_stage2(s1_fpath)
            all_metrics.append(metrics)
            all_waveforms[metrics['name']] = arrays
        except Exception as e:
            print(f"[!] Stage 2 error for {s1_fpath}: {e}")

    # Save Stage 2 intermediate deliverables
    json_path = os.path.join("stage2_output", "audit_metrics.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_metrics, f, indent=2)

    npz_path = os.path.join("stage2_output", "waveforms.npz")
    npz_dict = {}
    for ev_name, wdict in all_waveforms.items():
        for k, v in wdict.items():
            npz_dict[f"{ev_name}__{k}"] = v
    np.savez_compressed(npz_path, **npz_dict)
    print(f"\n[+] Saved Stage 2 metrics to {json_path}")
    print(f"[+] Saved Stage 2 waveforms to {npz_path}")

    # STAGE 3: Scientific Audit Report PDF Compiler
    pdf_out = "deterministic_imr_blind_audit_report.pdf"
    s3.render_audit_report_pdf(all_metrics, all_waveforms, output_pdf=pdf_out)
    print(f"\n[+] Pipeline finished successfully! Deliverable: {pdf_out}")

if __name__ == '__main__':
    main()
