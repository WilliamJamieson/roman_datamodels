from astropy.coordinates import ICRS
from astropy.modeling.models import Pix2Sky_TAN, RotateNative2Celestial, Scale, Shift
from astropy.units import deg, pix
from gwcs import WCS, coordinate_frames

__all__ = [
    "NOFN",
    "NOINT",
    "NONUM",
    "NOSTR",
    "Wcs",
]


NOFN = "none"
NOSTR = "?"
NONUM = -999999.0
NOINT = int(NONUM)


def Wcs() -> WCS:
    pixelshift = Shift(-500) & Shift(-500)
    pixelscale = Scale(0.1 / 3600.0) & Scale(0.1 / 3600.0)  # 0.1 arcsec/pixel
    tangent_projection = Pix2Sky_TAN()
    celestial_rotation = RotateNative2Celestial(30.0, 45.0, 180.0)

    det2sky = pixelshift | pixelscale | tangent_projection | celestial_rotation

    detector_frame = coordinate_frames.Frame2D(name="detector", axes_names=("x", "y"), unit=(pix, pix))
    sky_frame = coordinate_frames.CelestialFrame(reference_frame=ICRS(), name="icrs", unit=(deg, deg))
    return WCS(
        [
            (detector_frame, det2sky),
            (sky_frame, None),
        ]
    )
