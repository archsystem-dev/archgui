"""
Workarea.py
"""


class Workarea:
    """
    Class Workarea
    """

    def __init__(self, platform, fsg):

        self.platform = platform
        self.fsg = fsg

    # ---------------------------------------------------------------------
    # / Retourne la géométrie interne de la workarea
    # ---------------------------------------------------------------------

    def geometry(self):
        """
        geometry()
        """

        workarea_geometry = {}

        # -----------------------------------------------------------------
        # Utilisation de screeninfo pour Linux
        # -----------------------------------------------------------------

        if self.platform == "linux" or self.platform == "linux2":

            from screeninfo import get_monitors

            workarea_geometry = {}

            primary_monitor = 0

            nm = 0
            for monitor in get_monitors():

                primary = False
                if monitor.is_primary:
                    primary_monitor = str(nm)
                    primary = True

                info = {
                    "x": int(monitor.x),
                    "y": int(monitor.y),
                    "width": int(monitor.width),
                    "height": int(monitor.height)
                }

                x_min = info["x"]
                y_min = info["y"]

                geometry = {
                    "primary": primary,
                    "width": info["width"],
                    "height": info["height"],
                    "x_min": x_min,
                    "y_min": y_min
                }

                workarea_geometry[str(nm)] = geometry
                nm += 1

            workarea_geometry["primary"] = workarea_geometry[str(primary_monitor)]

        return workarea_geometry
