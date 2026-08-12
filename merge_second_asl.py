from pathlib import Path
import random
import shutil
import string

SECOND = Path("data/asl_second_raw/dataset")
DEST = Path("data/asl")

CLASSES = [
    c for c in string.ascii_uppercase
    if c not in ["J", "Z"]
]

random.seed(123)

extensions = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

for label in CLASSES:

    folder = SECOND / f"{label}-samples"

    images = [
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in extensions
    ]

    random.shuffle(images)

    split = int(len(images) * 0.8)

    train_images = images[:split]
    val_images = images[split:]

    for i, image in enumerate(train_images):
        destination = (
            DEST
            / "train"
            / label
            / f"second_{label}_{i:04d}{image.suffix.lower()}"
        )
        shutil.copy2(image, destination)

    for i, image in enumerate(val_images):
        destination = (
            DEST
            / "val"
            / label
            / f"second_{label}_{i:04d}{image.suffix.lower()}"
        )
        shutil.copy2(image, destination)

    print(
        label,
        "train added:", len(train_images),
        "val added:", len(val_images)
    )

print("MERGE COMPLETE")
