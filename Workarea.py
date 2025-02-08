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
        window = self.fsg.Window(
            '',
            [[]],
            alpha_channel=0,
            finalize=True,
            auto_close=True
        )

        window.TKroot.update_idletasks()
        window.set_size((100, 100))
        window.TKroot.update_idletasks()

        offset_y = int(window.TKroot.geometry().rsplit('+', 1)[-1])
        titlebar_height = window.TKroot.winfo_rooty() - offset_y
        window.close()

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
                x_max = x_min + info["width"]
                y_min = info["y"]
                y_max = y_min + info["height"]

                calib_siz = {"width": 0, "height": 0}
                calib_pos = [
                    ["tl", {"x": x_min, "y": y_min}],
                    ["br", {"x": x_max - calib_siz["width"], "y": y_max - calib_siz["height"]}],
                ]

                calib_res = {}
                for pos in calib_pos:
                    window = self.fsg.Window(
                        '',
                        [[]],
                        alpha_channel=0,
                        size=(calib_siz["width"], calib_siz["height"]),
                        location=(int(pos[1]["x"]), int(pos[1]["y"])),
                        finalize=True,
                        auto_close=True
                    )

                    calib_res[pos[0]] = {"x": window.TKroot.winfo_x(), "y": window.TKroot.winfo_y()}
                    window.close()

                geometry = {
                    "primary": primary,
                    "screen_width": info["width"],
                    "screen_height": info["height"],
                    "screen_x_min": x_min,
                    "screen_y_min": y_min,
                    "x_min": calib_res["tl"]["x"],
                    "y_min": calib_res["tl"]["y"] - titlebar_height,
                    "x_max": calib_res["br"]["x"] + calib_siz["width"] + 1,
                    "y_max": calib_res["br"]["y"] + calib_siz["height"] + 1,
                    "width": (calib_res["br"]["x"] + calib_siz["width"] + 1),
                    "height": (calib_res["br"]["y"] + calib_siz["height"] + 1),
                    "titlebar_height": titlebar_height
                }

                workarea_geometry[str(nm)] = geometry
                nm += 1

            workarea_geometry["primary"] = workarea_geometry[str(primary_monitor)]

        # -----------------------------------------------------------------
        # Utilisation de win32api pour Windows
        # -----------------------------------------------------------------

        # elif self.platform == "win32":
        #
        #     from win32api import GetMonitorInfo, MonitorFromPoint, GetSystemMetrics
        #
        #     monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
        #     work_area = monitor_info.get("Work")
        #
        #     workarea_raw = {
        #         "x": int(work_area[0]),
        #         "y": int(work_area[1]),
        #         "width": int(work_area[2]),
        #         "height": int(work_area[3])
        #     }

        return workarea_geometry
