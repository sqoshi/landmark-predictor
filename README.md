# landmark-predictor

## Table Of Contents

- [landmark-predictor](#landmark-predictor)
  - [Table Of Contents](#table-of-contents)
  - [General](#general)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Automatic download](#automatic-download)
  - [Code Example](#code-example)

## General

Python wrapper for the dlib model with automated model download and predict functionalities.

Package has been created to allow automatic dlib's predictor handling ( download, get, find ,
store)

## Installation

```shell
pip install git+https://github.com/sqoshi/landmark-predictor.git
```

## Usage

```python
from landmarks_predictor import LandmarksPredictor

landmarks_predictor = LandmarksPredictor(
        predictor_fp=None, show_samples=True,
        face_detection=True, auto_download=True
)

images = os.listdir(path/to/images) # absolute paths

landmarks_predictor.detect(images)
```

## Automatic download

```console
[22:48:43][INFO] - Looking for shape predictor in '/home/Documents/bsc-thesis/mask-imposer/venv/lib/python3.8/site-packages'
[22:48:43][INFO] - Looking for shape predictor in '/home/Documents/bsc-thesis/mask-imposer'
[22:48:43][WARNING] - Shape predictor not found.
Would you like to download 64 [MB] model ?
y
[22:48:45][WARNING] - Downloading shape `shape_predictor_68_face_landmarks.bz2` ...
100% |#############################################################################################################################################|
[22:53:45][INFO] - Predictor downloaded.
```

## Code Example

```python
    def detect(self, images_list: List[Union[str, tuple]], create_map: bool) -> None:
        """Creates landmark collection.

        During creation may optionally display samples with drawn landmarks.
        May detect face boxes, but it is preferred to pass images as stated in readme.
        """
        for img_path in images_list:
            image = Image(img_path)
            try:
                rect = self._detect_face_rect(image)  # detect rectangles with faces

                shape = self._predictor(image.get_gray_img(), rect)  # detect landmarks

                self._landmarks_collection[str(image)] = _shape_to_dict(shape)

                if create_map:
                    self.fake_map[str(image)] = image.img

                if self._should_display_samples:
                    self._display_sample(image, rect, shape)

            except NotImplementedError:  # must be changed
                logger.warning(f"Landmarks not detected on {image}.")
                continue
        self._check_fails(images_list)
        logger.info("Detection finished.")
```
