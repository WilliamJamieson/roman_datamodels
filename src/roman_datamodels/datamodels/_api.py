from ._asdf import AsdfFileMixin

__all__ = ["StpipeAPIMixin"]


class StpipeAPIMixin(AsdfFileMixin):
    @property
    def crds_observatory(self) -> str:
        """The observatory for CRDS."""
        return "roman"

    def get_crds_parameters(self) -> dict[str, str | int | float | complex | bool]:
        """
        Get parameters used by CRDS to select references for this model.

        This will only return items under ``roman.meta``.

        Returns
        -------
        dict
        """
        return {
            f"roman.meta.{key}": val
            for key, val in self.meta.to_flat_dict(include_arrays=False, recursive=True).items()
            if isinstance(val, str | int | float | complex | bool)
        }
