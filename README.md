# Solar corona structures segmentation by deep learning

This repository was created to demonstrate results of my diploma thesis. Thesis in Slovak language is available at 
following [link](https://opac.crzp.sk/?fn=detailBiblioForm&sid=14E8631BC0ED910BF5FAA533AA8B).

We trained two segmentation models with modified U-Net [[1]](#1) architecture. We named our model SCSS-Net - Solar Corona Structures Segmentation. 
The first model was trained for coronal hole segmentation, and the second model was trained for the segmentation of active regions.

## Data

The training data were images of the sun ([SDO AIA](https://sdo.gsfc.nasa.gov/)) and a corresponding binary mask of 
a specific region 
(a coronal hole or active region).


![sun-image](imgs/2018_06_30__03_46_16_84__SDO_AIA_AIA_193_img.png "sun-image") 
![binary-mask](imgs/2018_06_30__03_46_16_84__SDO_AIA_AIA_193_mask.png "binary-mask")

For data augmentations we used [Albumentations](https://github.com/albumentations-team/albumentations) together with 
[ImageDataAugmentor](https://github.com/mjkvaak/ImageDataAugmentor).

### Data sources
You can download images with [HEK API](https://www.lmsal.com/hek/api.html) or with 
[SunPy module](https://docs.sunpy.org/en/stable/guide/acquiring_data/hek.html). Additional data sources can be found below.

#### Images

- https://sdo.gsfc.nasa.gov/data/
- https://suntoday.lmsal.com/suntoday/
- http://jsoc.stanford.edu/

#### Annotations
- [CHIMERA](https://solarmonitor.org/data/)
- [Region Growth](https://github.com/observethesun/coronal_holes/tree/mnras2018/data)
- [SPoCA](https://www.lmsal.com/hek/api.html)

## Model
![model-architecture](imgs/U-Net.png "SCCS-Net")

## Videos (External)
Clicking on image opens video uploaded on YouTube.

[![AR](imgs/video-AR.png)](https://youtu.be/Sp3VLSgxK3w "AR - YouTube video")
[![CH](imgs/video-CH.png)](https://youtu.be/OX6s8WnC1ho "CH - YouTube video")

## References
<a id="1">[1]</a> 
Olaf Ronneberger, Philipp Fischer, & Thomas Brox. (2015). 
U-Net: Convolutional Networks for Biomedical Image Segmentation.

<a id="1">[2]</a>
Illarionov, E., & Tlatov, A. (2018). 
Segmentation of coronal holes in solar disc images with a convolutional neural network.
Monthly Notices of the Royal Astronomical Society, 481(4), 5014–5021.

<a id="1">[3]</a> 
Tlatov, A., Tavastsherna, K., & Vasil’eva, V. (2014). 
Coronal Holes in Solar Cycles 21 to 23.
Solar Physics, 289.

<a id="1">[4]</a> 
Tukiainen, M.. (2019). 
ImageDataAugmentor.

<a id="1">[5]</a>
Buslaev, A., Iglovikov, V., Khvedchenya, E., Parinov, A., Druzhinin, M., & Kalinin, A. (2020). 
Albumentations: Fast and Flexible Image Augmentations.
Information, 11(2).

<a id="1">[6]</a>
Verbeeck, C., Delouille, V., Mampaey, B., & De Visscher, R. (2014). 
The SPoCA-suite: Software for extraction, characterization, and tracking of active regions and coronal holes on EUV images.
A&A, 561, A29.

<a id="1">[7]</a>
Garton, T., Gallagher, P., & Murray, S. (2018). 
Automated coronal hole identification via multi-thermal intensity segmentation.
Journal of Space Weather and Space Climate, 8, A02.

<a id="1">[8]</a>
Lemen, J., et al.. (2011). 
The Atmospheric Imaging Assembly (AIA) on the Solar Dynamics Observatory (SDO).
Solar Physics, 275, 17-40.



