from roman_datamodels.stnode import _core, _default

__all__ = ["Ephemeris"]


class Ephemeris(_core.TaggedObjectNode):
    """
    Ephemeris information
    """

    @classmethod
    def asdf_tag(cls) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/ephemeris-1.0.0"

    @property
    def earth_angle(self) -> float:
        return self._get_node("earth_angle", lambda: _default.NONUM)

    @property
    def moon_angle(self) -> float:
        return self._get_node("moon_angle", lambda: _default.NONUM)

    @property
    def sun_angle(self) -> float:
        return self._get_node("sun_angle", lambda: _default.NONUM)

    @property
    def ephemeris_reference_frame(self) -> str:
        return self._get_node("ephemeris_reference_frame", lambda: _default.NOSTR)

    @property
    def type(self) -> str:
        return self._get_node("type", lambda: "DEFINITIVE")

    @property
    def time(self) -> float:
        return self._get_node("time", lambda: _default.NONUM)

    @property
    def spatial_x(self) -> float:
        return self._get_node("spatial_x", lambda: _default.NONUM)

    @property
    def spatial_y(self) -> float:
        return self._get_node("spatial_y", lambda: _default.NONUM)

    @property
    def spatial_z(self) -> float:
        return self._get_node("spatial_z", lambda: _default.NONUM)

    @property
    def velocity_x(self) -> float:
        return self._get_node("velocity_x", lambda: _default.NONUM)

    @property
    def velocity_y(self) -> float:
        return self._get_node("velocity_y", lambda: _default.NONUM)

    @property
    def velocity_z(self) -> float:
        return self._get_node("velocity_z", lambda: _default.NONUM)
