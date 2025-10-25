# Upload kaggle.json
from google.colab import files
files.upload()  # Chọn tệp kaggle.json từ máy bạn

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d quandang/vietnamese-foods
!unzip vietnamese-foods.zip -d dataset_raw
