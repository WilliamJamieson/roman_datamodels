from asdf_pydantic import AsdfPydanticModel as Model
from astropy.time import Time


class Basic(Model):
    _tag = "asdf://stsci.edu/datamodels/roman/tags/basic-1.0.0"
    calibration_software_version: str
    filename: str
    file_date: Time
