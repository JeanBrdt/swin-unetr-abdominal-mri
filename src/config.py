"""Constantes partagées : chemins, découpage des examens, étiquettes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "chaos-data"
OUTPUT_DIR = ROOT / "outputs"

TRAIN_IDS = [1, 2, 3, 5, 8, 10]   # apprentissage pendant les expériences
VAL_IDS = [13, 19]                # validation (mis de côté)
TEST_IDS = [21, 22, 32, 39]       # évaluation finale uniquement

LABELS = {0: "fond", 1: "foie", 2: "rein droit", 3: "rein gauche", 4: "rate"}
NUM_CLASSES = len(LABELS)


def image_path(exam_id: int) -> Path:
    return DATA_DIR / f"{exam_id:02d}-T2SPIR-src.nii.gz"


def mask_path(exam_id: int) -> Path:
    return DATA_DIR / f"{exam_id:02d}-T2SPIR-mask.nii.gz"
