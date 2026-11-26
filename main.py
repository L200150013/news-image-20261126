# news-image-20261126 entrypoint: ship the pre-rendered image, byte-identical.
import os
import shutil

_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
_OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(_OUT), exist_ok=True)
shutil.copyfile(_SRC, _OUT)
