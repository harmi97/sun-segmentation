import glob
import zipfile
from datetime import datetime
from tqdm import tqdm
from pathlib import Path

import astropy.units as u
import numpy as np
import sunpy
from PIL import Image, ImageDraw

from prep_utils import (convert_jp2_to_png, create_labels_img,
                            create_limb_mask, crop_limb)
from sunpy.coordinates.sun import angular_radius
from sunpy.net.helioviewer import HelioviewerClient
