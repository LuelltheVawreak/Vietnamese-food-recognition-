# Upload kaggle.json
from google.colab import files
files.upload()  # choose kaggle.json file from yours computer.

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d quandang/vietnamese-foods
!unzip vietnamese-foods.zip -d dataset_raw
