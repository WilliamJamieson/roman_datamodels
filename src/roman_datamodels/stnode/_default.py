from astropy import coordinates
from astropy import units as u
from astropy.modeling import models
from gwcs import WCS, coordinate_frames

__all__ = ["NOFN", "NONUM", "NOSTR", "Wcs"]


NOFN = "none"
NOSTR = "?"
NONUM = -999999


def Wcs():
    pixelshift = models.Shift(-500) & models.Shift(-500)
    pixelscale = models.Scale(0.1 / 3600.0) & models.Scale(0.1 / 3600.0)  # 0.1 arcsec/pixel
    tangent_projection = models.Pix2Sky_TAN()
    celestial_rotation = models.RotateNative2Celestial(30.0, 45.0, 180.0)

    det2sky = pixelshift | pixelscale | tangent_projection | celestial_rotation

    detector_frame = coordinate_frames.Frame2D(name="detector", axes_names=("x", "y"), unit=(u.pix, u.pix))
    sky_frame = coordinate_frames.CelestialFrame(reference_frame=coordinates.ICRS(), name="icrs", unit=(u.deg, u.deg))
    return WCS(
        [
            (detector_frame, det2sky),
            (sky_frame, None),
        ]
    )
