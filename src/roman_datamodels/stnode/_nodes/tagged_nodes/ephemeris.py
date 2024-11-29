from roman_datamodels.stnode import _core

__all__ = ["Ephemeris"]


class Ephemeris(_core.TaggedNode):
    """
    Ephemeris information
    """

    @property
    def tag(self) -> str:
        return "asdf://stsci.edu/datamodels/roman/tags/ephemeris-1.0.0"

    @property
    def required(self) -> tuple[str]:
        return (
            "earth_angle",
            "moon_angle",
            "sun_angle",
            "type",
            "time",
            "ephemeris_reference_frame",
            "spatial_x",
            "spatial_y",
            "spatial_z",
            "velocity_x",
            "velocity_y",
            "velocity_z",
        )

    @property
    def earth_angle(self) -> float:
        if not self._has_node("earth_angle"):
            self.earth_angle = _core.NONUM
        return self._get_node("earth_angle")

    @property
    def moon_angle(self) -> float:
        if not self._has_node("moon_angle"):
            self.moon_angle = _core.NONUM
        return self._get_node("moon_angle")

    @property
    def sun_angle(self) -> float:
        if not self._has_node("sun_angle"):
            self.sun_angle = _core.NONUM
        return self._get_node("sun_angle")

    @property
    def ephemeris_reference_frame(self) -> str:
        if not self._has_node("ephemeris_reference_frame"):
            self.ephemeris_reference_frame = _core.NOSTR
        return self._get_node("ephemeris_reference_frame")

    @property
    def type(self) -> str:
        if not self._has_node("type"):
            self.type = "DEFINITIVE"
        return self._get_node("type")

    @property
    def time(self) -> float:
        if not self._has_node("time"):
            self.time = _core.NONUM
        return self._get_node("time")

    @property
    def spatial_x(self) -> float:
        if not self._has_node("spatial_x"):
            self.spatial_x = _core.NONUM
        return self._get_node("spatial_x")

    @property
    def spatial_y(self) -> float:
        if not self._has_node("spatial_y"):
            self.spatial_y = _core.NONUM
        return self._get_node("spatial_y")

    @property
    def spatial_z(self) -> float:
        if not self._has_node("spatial_z"):
            self.spatial_z = _core.NONUM
        return self._get_node("spatial_z")

    @property
    def velocity_x(self) -> float:
        if not self._has_node("velocity_x"):
            self.velocity_x = _core.NONUM
        return self._get_node("velocity_x")

    @property
    def velocity_y(self) -> float:
        if not self._has_node("velocity_y"):
            self.velocity_y = _core.NONUM
        return self._get_node("velocity_y")

    @property
    def velocity_z(self) -> float:
        if not self._has_node("velocity_z"):
            self.velocity_z = _core.NONUM
        return self._get_node("velocity_z")
