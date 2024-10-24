from ._tagged import TaggedObjectNode


class Guidewindow(TaggedObjectNode): ...


class Ramp(TaggedObjectNode): ...


class RampFitOutput(TaggedObjectNode): ...


class WfiScienceRaw(TaggedObjectNode): ...


class WfiImage(TaggedObjectNode): ...


class WfiMosaic(TaggedObjectNode): ...


class WfiMode(TaggedObjectNode):
    # Every optical element is a grating or a filter
    #   There are less gratings than filters so its easier to list out the
    #   gratings.
    _GRATING_OPTICAL_ELEMENTS = {"GRISM", "PRISM"}

    @property
    def filter(self):
        """
        Returns the filter if it is one, otherwise None
        """
        if self.optical_element in self._GRATING_OPTICAL_ELEMENTS:
            return None
        else:
            return self.optical_element

    @property
    def grating(self):
        """
        Returns the grating if it is one, otherwise None
        """
        if self.optical_element in self._GRATING_OPTICAL_ELEMENTS:
            return self.optical_element
        else:
            return None


class Exposure(TaggedObjectNode): ...


class Program(TaggedObjectNode): ...


class Observation(TaggedObjectNode): ...


class Ephemeris(TaggedObjectNode): ...


class Visit(TaggedObjectNode): ...


class Photometry(TaggedObjectNode): ...


class SourceDetection(TaggedObjectNode): ...


class Coordinates(TaggedObjectNode): ...


class Aperture(TaggedObjectNode): ...


class Pointing(TaggedObjectNode): ...


class Target(TaggedObjectNode): ...


class VelocityAberration(TaggedObjectNode): ...


class Wcsinfo(TaggedObjectNode): ...


class Guidestar(TaggedObjectNode): ...


class L2CalStep(TaggedObjectNode): ...


class L3CalStep(TaggedObjectNode): ...


class OutlierDetection(TaggedObjectNode): ...


class SkyBackground(TaggedObjectNode): ...


class Resample(TaggedObjectNode): ...


class IndividualImageMeta(TaggedObjectNode): ...


class MosaicBasic(TaggedObjectNode): ...


class MosaicAssociations(TaggedObjectNode): ...


class MosaicWcsinfo(TaggedObjectNode): ...


class AbvegaoffsetRef(TaggedObjectNode): ...


class ApcorrRef(TaggedObjectNode): ...


class DarkRef(TaggedObjectNode): ...


class DistortionRef(TaggedObjectNode): ...


class EpsfRef(TaggedObjectNode): ...


class FlatRef(TaggedObjectNode): ...


class GainRef(TaggedObjectNode): ...


class InverselinearityRef(TaggedObjectNode): ...


class IpcRef(TaggedObjectNode): ...


class LinearityRef(TaggedObjectNode): ...


class MaskRef(TaggedObjectNode): ...


class PixelareaRef(TaggedObjectNode): ...


class ReadnoiseRef(TaggedObjectNode): ...


class RefpixRef(TaggedObjectNode): ...


class SaturationRef(TaggedObjectNode): ...


class SuperbiasRef(TaggedObjectNode): ...


class WfiImgPhotomRef(TaggedObjectNode): ...


class Associations(TaggedObjectNode): ...


class RefFile(TaggedObjectNode): ...


class SourceCatalog(TaggedObjectNode): ...


class SegmentationMap(TaggedObjectNode): ...


class MosaicSourceCatalog(TaggedObjectNode): ...


class MosaicSegmentationMap(TaggedObjectNode): ...


class Fps(TaggedObjectNode): ...


class FpsCalStep(TaggedObjectNode): ...


class FpsExposure(TaggedObjectNode): ...


class FpsGroundtest(TaggedObjectNode): ...


class FpsGuidestar(TaggedObjectNode): ...


class FpsStatistics(TaggedObjectNode): ...


class FpsRefFile(TaggedObjectNode): ...


class FpsWfiMode(TaggedObjectNode): ...


class Tvac(TaggedObjectNode): ...


class TvacCalStep(TaggedObjectNode): ...


class TvacExposure(TaggedObjectNode): ...


class TvacGroundtest(TaggedObjectNode): ...


class TvacGuidestar(TaggedObjectNode): ...


class TvacStatistics(TaggedObjectNode): ...


class TvacRefFile(TaggedObjectNode): ...


class TvacWfiMode(TaggedObjectNode): ...


class MsosStack(TaggedObjectNode): ...
