#!/usr/bin/env python3
import urllib.request, pathlib, os, sys

img_dir = pathlib.Path("/Users/pranav/Documents/hermes/health/img")
img_dir.mkdir(parents=True, exist_ok=True)

images = {
    "bench-press": "https://v3b.fal.media/files/b/0aa2bb02/VY9cv4eu-YFo8akgdMpkM_8HJyWIJA.png",
    "seated-row": "https://v3b.fal.media/files/b/0aa2bb03/qPgApP9lBfrg6pMQzPadW_cotkcLnE.png",
    "shoulder-press": "https://v3b.fal.media/files/b/0aa2bb04/i3fvdklLIvaf0DjzOjtUu_i1s9iPWN.png",
    "plank": "https://v3b.fal.media/files/b/0aa2bb04/H5Uy8Q_qHQuP6aMQner2T_PI8YLf1X.png",
    "dead-bug": "https://v3b.fal.media/files/b/0aa2bb05/u2V02qPetgVHTiAGLoIJd_XgfLmBr5.png",
    "squat": "https://v3b.fal.media/files/b/0aa2bb05/tt6-S4zjLxAGuhbxqalgQ_PoTEGbQX.png",
    "deadlift": "https://v3b.fal.media/files/b/0aa2bb06/znQcgLXQzu7IKWx3-az-C_AjaL2Zap.png",
    "glute-bridge": "https://v3b.fal.media/files/b/0aa2bb06/qSYb_-6Ya9IGFOVHWF_Ba_3SOcKjEE.png",
    "thoracic-rotation": "https://v3b.fal.media/files/b/0aa2bb07/c7UFNuwfwKNbP8Xa7vyE4_fGUiAgZd.png",
}

for name, url in images.items():
    path = img_dir / f"{name}.png"
    if path.exists():
        print(f"EXISTS {name}.png ({path.stat().st_size/1024:.0f} KB)")
        continue
    urllib.request.urlretrieve(url, path)
    sz = path.stat().st_size
    print(f"OK {name}.png ({sz/1024:.0f} KB)")

print(f"\nTotal: {len(list(img_dir.glob('*.png')))} images, {sum(f.stat().st_size for f in img_dir.glob('*.png'))/1024:.0f} KB")
