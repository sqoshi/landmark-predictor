import logging
import os.path
import sys
from bz2 import BZ2File
from http.client import HTTPException
from pathlib import Path
from tarfile import CompressionError
from typing import Union
from urllib.error import HTTPError, URLError
from urllib.request import urlretrieve

from termcolor import colored

from .terminal_progressbar import TerminalProgressBar

logger = logging.getLogger(__name__)


def _unpack_bz2(filepath: Union[Path, str]) -> str:
    """Unpack downloaded bz2 file and returns path to content."""
    model_name = str(Path(filepath).name).replace(".bz2", ".dat")
    model_fp = os.path.join(Path(os.path.abspath(__file__)).parent.parent, model_name)
    with open(model_fp, "wb") as fw:
        fw.write(BZ2File(filepath).read())
    return model_fp


def _accepted_download(auto: bool) -> bool:
    """Ask for permission to download bundled model."""
    if auto:
        return True
    response = input(
        colored("Would you like to download ", "green")
        + colored("64 [MB]", "red")
        + colored(" model ?\n", "green")
    )
    return str(response).lower() in {"", "y", "yes"}


def download_predictor(
    url: str = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2",
    predictor_name: str = "shape_predictor_68_face_landmarks.bz2",
    auto: bool = False,
) -> str:
    """Downloads default dlib shape predictor (68-landmark)"""

    logger.warning("Shape predictor not passed directly.")
    if _accepted_download(auto):
        logger.warning("Downloading shape `shape_predictor_68_face_landmarks.bz2` ...")
        download_fp = Path(os.path.join("/tmp", predictor_name))
        try:
            urlretrieve(url, download_fp, TerminalProgressBar())
            return _unpack_bz2(download_fp)
        except URLError or HTTPError or HTTPException:
            logger.critical(
                "Error occurred during model download. "
                "Please download model manually and input filepath via arguments."
            )
            sys.exit()
        except FileNotFoundError or FileExistsError or CompressionError:
            logger.critical(
                "Error occurred during model decompression. "
                "Please input filepath to model via terminal arguments."
            )
            sys.exit()
        finally:
            if download_fp.exists() and download_fp.is_file():
                os.remove(download_fp)
    else:
        logger.critical("Shape predictor not provided. Detection interrupted.")
        sys.exit()
