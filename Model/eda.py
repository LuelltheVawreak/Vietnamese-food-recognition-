import os
import matplotlib.pyplot as plt
from PIL import Image

def eda_show(dataset_dir='dataset_raw/Images'):
    #Quick dataset summary: class count and example images
    for split in ['Train', 'Validate']:
        directory = os.path.join(dataset_dir, split)
        if not os.path.exists(directory):
            print(f"{split} directory not found at {directory}")
            continue
        classes = sorted([d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))])
        counts = {c: len(os.listdir(os.path.join(directory, c))) for c in classes}
        total = sum(counts.values())
        print(f"{split}: {len(classes)} classes, {total} images")
        top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
        print("Top classes (count):", top)
        # show example images
        samp_imgs = []
        for c in classes[:6]:
            imgs = os.listdir(os.path.join(directory, c))
            if imgs:
                samp_imgs.append(os.path.join(directory, c, imgs[0]))
        fig, axs = plt.subplots(1, len(samp_imgs), figsize=(14,4))
        for ax, p in zip(axs, samp_imgs):
            ax.axis('off')
            ax.imshow(Image.open(p).convert("RGB").resize((224,224)))
        plt.show()
