import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", 5000))


class Header(Enum):
    X_GRD_SIGNATURE = "X-Grd-Signature"
    IS_LOCAL_TEST = "Is-Local-Test"
    X_GRD_REASON = "X-Grd-Reason"
