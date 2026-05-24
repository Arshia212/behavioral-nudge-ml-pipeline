# HelloAlfred — AI-Powered Behavioral Nudging for Atrial Fibrillation Care

A machine learning pipeline that classifies patients into behavioral archetype clusters and generates personalized behavioral nudges to improve medication adherence and self-management in Atrial Fibrillation (AF) care.

---

## Overview

Patients with AF vary widely in their motivation, health literacy, clinical risk, and engagement with care. HelloAlfred addresses this by:

1. **Clustering** patients into 10 behavioral archetypes (C1–C10) based on clinical, behavioral, and engagement features
2. **Classifying** new patients into their archetype using a trained Random Forest model
3. **Selecting nudges** personalized to each patient's barriers using the COM-B framework and MINDSPACE/EAST behavioral science principles

---

## Repository Structure

| File | Description |
|------|-------------|
| `HelloAlfredModel.ipynb` | Main modeling notebook — preprocessing, Random Forest + Logistic Regression training, evaluation, SHAP analysis |
| `RandomForestModel.ipynb` | Standalone Random Forest implementation |
| `HelloAlfredPseudocode.py` | End-to-end system pseudocode: data ingestion → behavioral assessment → nudge selection → delivery → feedback loop |
| `synth_AF_clusters_100k.csv.zip` | Synthetic dataset of 100,000 AF patients with clinical, behavioral, and engagement features |
| `All_58_Subcluster_Distributions.csv` | Distribution summary across all 58 patient subclusters |
| `Implementing Behavioral Nudges in Atrial Fibrillation Care.docx` | Research paper on the nudge framework |
| `Cluster and Subcluster distribution (visual).docx` | Visual documentation of cluster and subcluster distributions |
| `7-Thota-FA25.pdf` | Research report |
| `HelloAlfredAI_Nudge_Classifiers.pptx` | Presentation: AI nudge classifier overview |
| `Arshia_Thota_LightningTalk-2.pptx` | Lightning talk slides |

---

## Model

**Task:** Multi-class classification — predict a patient's macro cluster (C1–C10)

**Models trained:**
- Random Forest Classifier (primary) — 100 trees, unconstrained depth
- Logistic Regression (baseline) — multinomial, L-BFGS solver

**Data:** 100,000 synthetic AF patients with 50+ features including demographics, comorbidities, medication type, behavioral readiness scores, and engagement metrics

**Train/Val split:** 80/20 stratified by cluster label

### Top Features (Random Forest)

| Feature | Importance |
|---------|------------|
| oac_drug_Warfarin | 0.1932 |
| ckd | 0.1355 |
| portal_active | 0.1181 |
| autonomy | 0.0719 |
| has_bled | 0.0705 |
| literacy_conf | 0.0566 |
| low_literacy_proxy | 0.0523 |
| reply_rate2 | 0.0397 |
| BRI | 0.0260 |
| open_rate2 | 0.0245 |

SHAP values are used alongside feature importances for per-class interpretability.

---

## Nudge Pipeline

The system pipeline (detailed in `HelloAlfredPseudocode.py`) follows these steps:

1. **Ingest** patient data from app or EHR
2. **Assess** behavioral readiness (Capability / Opportunity / Motivation via COM-B)
3. **Identify** the key barrier to the target behavior
4. **Select** a nudge strategy based on MINDSPACE and EAST principles
5. **Personalize** message content to patient characteristics
6. **Schedule** delivery using Just-In-Time Adaptive (JITAI) logic
7. **Deploy** via preferred channel (SMS, in-app, email)
8. **Record** feedback and update the patient's behavioral profile

---

## Behavioral Clusters (C1–C10)

Each cluster represents a distinct patient archetype defined by a combination of clinical risk, behavioral readiness, and engagement patterns. Subclusters (58 total) further stratify patients by TTM stage and care pathway (e.g., `C10-SafetyFirst-PC/R`).

---

## Tech Stack

- Python, scikit-learn, pandas, NumPy
- SHAP for model interpretability
- Jupyter Notebooks

---

## Context

Developed during an internship at **HelloAlfred** as part of a research initiative to apply behavioral science and ML to chronic disease self-management.
