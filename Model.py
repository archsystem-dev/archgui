"""
Model.py
"""

import re
import logging

from io import BytesIO

from archgui.Interpreter import Interpreter


# -------------------------------------------------------------------------
# / Converti une List en Tuple
# -------------------------------------------------------------------------


def list_to_tuple(ll):
    """
    :param ll:
    :return:
    """
    return tuple(list_to_tuple(x) for x in ll) if type(ll) is list else ll


# -------------------------------------------------------------------------
# / Vérifier qu'un paramètre de Size ou Location n’est pas vide
# / Retourne True ou False
# -------------------------------------------------------------------------


def pisnt_null(parameters):
    """
    :param parameters:
    :return:
    """
    not_null = True
    if parameters["uniqid"] is None:
        not_null = False

    if parameters["model"] is not None:
        if parameters["wid"] is not None:
            not_null = True

    return not_null


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
#
#    Classe étant la surcouche de la Window de FreeSimpleGUI.
#    Elle génère le Layout de la Window et transmet les interactions issues
#    de la classe Windows à FreeSimpleGUI.
#
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------


class Model:
    """
    Class Model
    """
    def __init__(self, windows, model, specter):

        # -----------------------------------------------------------------

        self.windows = windows
        self.fsg = windows.fsg

        # -----------------------------------------------------------------

        self.is_hide = False
        self.reperc = re.compile(r"\d{2}%", re.IGNORECASE)

        # -----------------------------------------------------------------

        self.model = model
        self.monitor = None
        self.id = None
        self.uniqid = None

        # -----------------------------------------------------------------

        self.wageo = None

        # -----------------------------------------------------------------

        self.title = ""

        # -----------------------------------------------------------------

        self.window = None

        # -----------------------------------------------------------------

        self.interpreter = Interpreter(self.fsg, self.windows.config, self.window)

        # -----------------------------------------------------------------

        self.parameters = {
                "full-screen": False,
                "location_x": None,
                "location_y": None,
                "width": None,
                "height": None,
                "location_x_relative": {
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "location_y_relative": {
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "location_x_equal": {
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "location_y_equal": {
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "width_equal": {
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "height_equal": {
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "width_until": {
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "height_until": {
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "scrollable": False
            }

        # -----------------------------------------------------------------

        self.specter = specter
        self.items = self.specter["items"]

        # -----------------------------------------------------------------

        if len(self.specter["parameters"]) > 0:
            for parameter in self.specter["parameters"]:
                if isinstance(self.specter["parameters"][parameter], dict):
                    for sub_param in self.specter["parameters"][parameter]:
                        self.parameters[parameter][sub_param] = self.specter["parameters"][parameter][sub_param]
                else:
                    self.parameters[parameter] = self.specter["parameters"][parameter]

        # -----------------------------------------------------------------

        self.layout = None
        self.items_list = None

        # -----------------------------------------------------------------

        self.window_location = []
        self.window_size = []
        self.window_dpi = 80

    # ---------------------------------------------------------------------
    # / Définit la position de la fenêtre en X
    # ---------------------------------------------------------------------

    def set_location_x(self):
        """
        :return:
        """
        if pisnt_null(self.parameters["location_x_relative"]):

            if not isinstance(self.window_location[0], int):
                self.window_location[0] = self.wageo["x_min"]

            try:
                rel = self.parameters["location_x_relative"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    size = self.windows.wds_uniqid[rel["uniqid"]].get_size()
                    location = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    size = self.windows.wds_windows[rel["model"]][rel["wid"]].get_size()
                    location = self.windows.wds_windows[rel["model"]][rel["wid"]].get_location()
            except Exception as e:
                logging.exception(e)
                return False

            self.window_location[0] += size[0] + location[0]

        elif pisnt_null(self.parameters["location_x_equal"]):

            try:
                rel = self.parameters["location_x_equal"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    location = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    location = self.windows.wds_windows[rel["model"]][rel["wid"]].get_location()
            except Exception as e:
                logging.exception(e)
                return False

            self.window_location[0] = location[0]

        elif self.parameters["location_x"] == 0 or self.parameters["location_x"] is None:
            self.window_location[0] = self.wageo["x_min"]

        elif isinstance(self.parameters["location_x"], int):
            self.window_location[0] = self.wageo["x_min"] + self.parameters["location_x"]

        elif self.reperc.match(str(self.parameters["location_x"])) and isinstance(self.parameters["width"], int):
            percent = int(self.parameters["location_x"].split("%")[0])
            self.window_location[0] = self.wageo["x_min"]
            self.window_location[0] += int((self.wageo["width"] / 100) * percent)
            self.window_location[0] -= int(self.parameters["width"] / 2)

        else:
            self.window_location[0] = 0

        return True

    # ---------------------------------------------------------------------
    # / Définit la position de la fenêtre en Y
    # ---------------------------------------------------------------------

    def set_location_y(self):
        """

        :return:
        """
        if pisnt_null(self.parameters["location_y_relative"]):

            if not isinstance(self.window_location[1], int):
                self.window_location[1] = self.wageo["y_min"]

            try:
                rel = self.parameters["location_y_relative"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    size = self.windows.wds_uniqid[rel["uniqid"]].get_size()
                    location = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    size = self.windows.wds_windows[rel["model"]][rel["wid"]].get_size()
                    location = self.windows.wds_windows[rel["model"]][rel["wid"]].get_location()
            except Exception as e:
                logging.exception(e)
                return False

            self.window_location[1] += size[1] + location[1]
            self.window_location[1] += self.wageo["titlebar_height"] + 1

        elif pisnt_null(self.parameters["location_y_equal"]):

            try:
                rel = self.parameters["location_y_equal"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    location = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    location = self.windows.wds_windows[rel["model"]][rel["wid"]].get_location()
            except Exception as e:
                logging.exception(e)
                return False

            self.window_location[1] = location[1]

        elif self.parameters["location_y"] == 0 or self.parameters["location_y"] is None:
            self.window_location[1] = self.wageo["y_min"]

        elif isinstance(self.parameters["location_y"], int):
            self.window_location[1] = self.wageo["y_min"] + self.parameters["location_y"]

        elif self.reperc.match(str(self.parameters["location_y"])) and isinstance(self.parameters["height"], int):
            percent = int(self.parameters["location_y"].split("%")[0])
            self.window_location[1] = self.wageo["y_min"]
            self.window_location[1] += int((self.wageo["height"] / 100) * percent)
            self.window_location[1] -= int(self.parameters["height"] / 2)

        else:
            self.window_location[1] = 0

        return True

    # ---------------------------------------------------------------------
    # / Définit la largeur de la fenêtre
    # ---------------------------------------------------------------------

    def set_size_width(self):
        """

        :return:
        """
        if pisnt_null(self.parameters["width_equal"]):

            try:
                rel = self.parameters["width_equal"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    size = self.windows.wds_uniqid[rel["uniqid"]].get_size()
                else:
                    size = self.windows.wds_windows[rel["model"]][rel["wid"]].get_size()
            except Exception as e:
                logging.exception(e)
                return False

            self.window_size[0] = size[0]

        elif pisnt_null(self.parameters["width_until"]):

            try:
                rel = self.parameters["width_until"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    size = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    size = self.windows.wds_windows[rel["model"]][rel["wid"]].get_location()
            except Exception as e:
                logging.exception(e)
                return False

            self.window_size[0] = size[0]

        elif self.parameters["width"] is None:
            if self.parameters["height"] is None and not pisnt_null(self.parameters["height_equal"]):
                self.window_size[0] = None

        elif self.parameters["width"] == 0 or self.parameters["width"] == "100%":
            self.window_size[0] = self.wageo["width"]
            self.window_size[0] -= self.window_location[0]

        elif isinstance(self.parameters["width"], int):
            self.window_size[0] = self.parameters["width"]

        elif self.reperc.match(str(self.parameters["width"])):
            percent = int(self.parameters["width"].split("%")[0])
            self.window_size[0] = int((self.wageo["width"] / 100) * percent)

        else:
            self.window_size[0] = 0

        if self.window_size[0] is not None:
            self.window_size[0] = int(self.window_size[0])

        return True

    # ---------------------------------------------------------------------
    # / Définit la hauteur de la fenêtre
    # ---------------------------------------------------------------------

    def set_size_height(self):
        """

        :return:
        """
        if pisnt_null(self.parameters["height_equal"]):

            try:
                rel = self.parameters["height_equal"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    size = self.windows.wds_uniqid[rel["uniqid"]].get_size()
                else:
                    size = self.windows.wds_windows[rel["model"]][rel["wid"]].get_size()
            except Exception as e:
                logging.exception(e)
                return False

            self.window_size[1] = size[1]

        elif pisnt_null(self.parameters["height_until"]):

            try:
                rel = self.parameters["height_until"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    height_size = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    height_size = self.windows.wds_windows[rel["model"]][rel["wid"]].get_location()
            except Exception as e:
                logging.exception(e)
                return False

            self.window_size[1] = height_size[1] - (2 * self.wageo["titlebar_height"]) + 4

        elif self.parameters["height"] is None:
            if self.parameters["width"] is None and not pisnt_null(self.parameters["width_equal"]):
                self.window_size[1] = None

        elif self.parameters["height"] == 0 or self.parameters["height"] == "100%":
            self.window_size[1] = self.wageo["height"]
            self.window_size[1] -= self.window_location[1]
            self.window_size[1] -= 5

        elif isinstance(self.parameters["height"], int):
            self.window_size[1] = self.parameters["height"]

        elif self.reperc.match(str(self.parameters["height"])):
            percent = int(self.parameters["height"].split("%")[0])
            self.window_size[1] = (self.wageo["height"] / 100) * percent

        else:
            self.window_size[1] = 0

        if self.window_size[1] is not None:
            self.window_size[1] = int(self.window_size[1])

        return True

    # ---------------------------------------------------------------------
    # / Affiche la Window de FreeSimpleGUI
    # ---------------------------------------------------------------------

    def open(self, monitor, id, title, location=None, size=None, alpha_channel=None, force_toplevel=None):
        """
        :param monitor:
        :param id:
        :param title:
        :param location:
        :param size:
        :param alpha_channel:
        :param force_toplevel:
        :return:
        """
        self.monitor = monitor
        self.id = id
        self.title = title

        # -----------------------------------------------------------------

        self.wageo = self.windows.wageo[self.monitor]

        # -----------------------------------------------------------------

        self.window_location = [0, 0]

        # -----------------------------------------------------------------

        self.window_size = [0, 0]

        # -----------------------------------------------------------------

        if self.parameters["full-screen"]:

            no_titlebar = True
            keep_on_top = True

            self.window_location = [
                self.wageo["screen_x_min"],
                self.wageo["screen_x_min"]
            ]

            self.window_size = [
                self.wageo["screen_width"],
                self.wageo["screen_height"]
            ]

        else:

            no_titlebar = False
            keep_on_top = False

            location_loaded = False
            if location is not None:
                if isinstance(location, list) and len(location) == 2:
                    if isinstance(location[0], int) and isinstance(location[1], int):
                        self.window_location = [int(location[0]), int(location[1])]
                        location_loaded = True

            if not location_loaded:
                if not self.set_location_x():
                    return False
                if not self.set_location_y():
                    return False

            size_loaded = False
            if size is not None:
                if isinstance(size, list) and len(size) == 2:
                    if isinstance(size[0], int) and isinstance(size[1], int):
                        self.window_size = [int(size[0]), int(size[1])]
                        size_loaded = True

            if not size_loaded:
                if not self.set_size_width():
                    return False
                if not self.set_size_height():
                    return False

        # -----------------------------------------------------------------

        self.layout, self.items_list = self.interpreter.create_layout(self.items)

        # -----------------------------------------------------------------

        self.window = self.fsg.Window(self.title, self.layout,
                                      location=list_to_tuple(self.window_location),
                                      size=list_to_tuple(self.window_size),
                                      margins=(0, 0),
                                      element_padding=(0, 0),
                                      no_titlebar=no_titlebar,
                                      keep_on_top=keep_on_top,
                                      alpha_channel=alpha_channel,
                                      force_toplevel=force_toplevel,
                                      enable_close_attempted_event=True)

        self.window.finalize()

        self.window_size = self.window.current_size_accurate()

        relocation = False
        if self.reperc.match(str(self.parameters["location_x"])) and not isinstance(self.parameters["width"], int):
            percent = int(self.parameters["location_x"].split("%")[0])
            self.window_location[0] = self.wageo["x_min"]
            self.window_location[0] += int((self.wageo["width"] / 100) * percent)
            self.window_location[0] -= int(self.window_size[0] / 2)
            relocation = True

        if self.reperc.match(str(self.parameters["location_y"])) and not isinstance(self.parameters["height"], int):
            percent = int(self.parameters["location_y"].split("%")[0])
            self.window_location[1] = self.wageo["y_min"]
            self.window_location[1] += int((self.wageo["height"] / 100) * percent)
            self.window_location[1] -= int(self.window_size[1] / 2)
            relocation = True

        if relocation:
            geometry = str(self.window_size[0]) + "x"
            geometry += str(self.window_size[1]) + "+"
            geometry += str(self.window_location[0]) + "+"
            geometry += str(self.window_location[1])

            self.window.TKroot.wm_geometry(newGeometry=geometry)
            self.window.TKroot.update()

        self.window_dpi = self.window.TKroot.winfo_fpixels('1i')

        # -----------------------------------------------------------------

        return self.window

    # ---------------------------------------------------------------------
    # / Affiche une fenêtre précédemment masquée
    # ---------------------------------------------------------------------

    def show(self):
        """
        test.py
        """
        self.is_hide = False
        self.window.UnHide()

    # ---------------------------------------------------------------------
    # / Masque une fenêtre
    # ---------------------------------------------------------------------

    def hide(self):
        """
        test.py
        """
        self.is_hide = True
        self.window.hide()

    # ---------------------------------------------------------------------
    # / Créer un Bind
    # ---------------------------------------------------------------------

    def bind(self, binds: dict):
        """
        :param binds:
        :return:
        """
        error = False

        for bind_updated in binds:

            if all(k in bind_updated for k in ("item", "bind_string", "bind_key")):  # TODO: Créer erreur spécifique

                item = bind_updated["item"]
                bind_string = bind_updated["bind_string"]
                bind_key = bind_updated["bind_key"]

                if item is None:
                    self.window.bind(bind_string, bind_key)
                elif item in list(self.items_list.keys()):
                    self.window[item].bind(bind_string, bind_key)

        if error:
            return False
        else:
            return True

    # ---------------------------------------------------------------------
    # / Retourne la taille de la fenêtre
    # ---------------------------------------------------------------------

    def get_size(self):
        """
        :return:
        """
        return self.window_size

    # ---------------------------------------------------------------------
    # / Retourne la position initiale de la fenêtre
    # ---------------------------------------------------------------------

    def get_location(self):
        """
        :return:
        """
        return self.window_location

    # ---------------------------------------------------------------------
    # / Retourne le DPI de l'écran sur lequel est affiché la fenêtre
    # ---------------------------------------------------------------------

    def get_dpi(self):
        """
        :return:
        """
        return self.window_dpi

    # ---------------------------------------------------------------------
    # / Retourne un Item de la fenêtre
    # ---------------------------------------------------------------------

    def get_item(self, item: str):
        """
        :param item:
        :return:
        """
        return self.window[item].get()

    # ---------------------------------------------------------------------
    # / Modifie un Item de la fenêtre
    # ---------------------------------------------------------------------

    def update(self, items):
        """
        :param items:
        :return:
        """

        # TODO: try/except pour virer le error = False

        error = False

        for item_updated in items:

            if all(k in item_updated for k in ("item", "mode")):  # TODO: Créer erreur spécifique

                key = item_updated["item"]
                mode = item_updated["mode"]

                if key in list(self.items_list.keys()):  # TODO: Créer erreur spécifique

                    key_type = self.items_list[key]["type"]

                    if mode in ["add", "replace", "clear", "show", "hide", "disabled"]:

                        if mode == "show":
                            self.window[item_updated["item"]].update(visible=True)

                        if mode == "hide":
                            self.window[item_updated["item"]].update(visible=False)

                        if mode == "disabled":
                            if "value" in item_updated:
                                value = item_updated["value"]

                                if value is True or value is False:
                                    self.window[item_updated["item"]].update(disabled=value)

                        if key_type == "label":

                            if "value" in item_updated:
                                value = item_updated["value"]

                                if mode == "add":
                                    self.window[item_updated["item"]].print(value)
                                elif mode == "replace":
                                    self.window[item_updated["item"]].update(value)

                            if mode == "clear":
                                self.window[item_updated["item"]].update()

                        if key_type == "in_line":

                            if "value" in item_updated:
                                value = item_updated["value"]

                                if mode == "add":
                                    value = self.window[item_updated["item"]].get() + value
                                    self.window[item_updated["item"]].update(value)
                                elif mode == "replace":
                                    self.window[item_updated["item"]].update(value)

                            if mode == "clear":
                                self.window[item_updated["item"]].update("")

                        if key_type == "in_lines":

                            if mode in ["add", "replace"]:

                                if mode == "replace":
                                    self.window[key].update("")

                                if "value" in item_updated:
                                    value = item_updated["value"]

                                    truncate_height = self.items_list[key]["truncate_height"]

                                    if truncate_height:
                                        truncate_width = True
                                    else:
                                        truncate_width = self.items_list[key]["truncate_width"]

                                    max_chars = self.window[item_updated["item"]].Size[0]
                                    max_lines = self.window[item_updated["item"]].Size[1]

                                    lines = ""
                                    lines_list = self.window[key].get().split("\n")

                                    if truncate_width:
                                        value = value[0:max_chars]

                                    if truncate_height:
                                        if len(lines_list) >= max_lines:
                                            dec = (len(lines_list) - max_lines) + 1
                                            lines_list = lines_list[dec:max_lines]

                                    for line in lines_list:
                                        if len(line) > 0:
                                            if truncate_height:
                                                lines += line[0: max_chars] + "\n"
                                            else:
                                                lines += line + "\n"

                                    lines += value

                                    self.window[key].update(lines)

                            elif mode == "clear":
                                self.window[key].update("")

                        if key_type == "button":
                            error = True

                        if key_type == "button_file":
                            error = True

                        if key_type == "button_files":
                            error = True

                        if key_type == "button_save":
                            error = True

                        if key_type == "button_folder":
                            error = True

                        if key_type == "button_calendar":
                            error = True

                        if key_type == "button_color":
                            if "default_color" in item_updated:

                                default_color = item_updated["default_color"]

                                if mode == "replace":
                                    if isinstance(default_color, str) or isinstance(default_color, int):
                                        self.window[item_updated["item"]].update(default_color)
                                    else:
                                        error = True

                        if key_type == "in_combo":

                            if all(k in item_updated for k in ("value", "default_value")):

                                value = item_updated["value"]
                                default_value = item_updated["default_value"]

                                if mode == "add":

                                    if isinstance(value, str) and isinstance(default_value, str) or isinstance(default_value, int):
                                        value = self.window[item_updated["item"]].get().append(value)
                                        if default_value in value:
                                            self.window[item_updated["item"]].update(default_value, value)
                                        else:
                                            error = True
                                    else:
                                        error = True

                                elif mode == "replace":
                                    if isinstance(value, list) and isinstance(default_value, str) or isinstance(default_value, int):
                                        if default_value in value:
                                            self.window[item_updated["item"]].update(default_value, value)
                                        else:
                                            error = True
                                    else:
                                        error = True

                            elif "default_value" in item_updated:

                                default_value = item_updated["default_value"]

                                if mode == "replace":
                                    if isinstance(default_value, str) or isinstance(default_value, int):
                                        self.window[item_updated["item"]].update(default_value)
                                    else:
                                        error = True

                            else:
                                if mode == "clear":
                                    self.window[item_updated["item"]].update("", "")
                                else:
                                    error = True

                        if key_type == "progress_bar":

                            if "value" in item_updated:

                                max_value = self.window[item_updated["item"]].MaxValue
                                value = item_updated["value"]

                                if isinstance(value, int):

                                    if value <= max_value:

                                        if mode == "add":
                                            current_count = self.window[item_updated["item"]]
                                            current_count = current_count.TKProgressBar.TKProgressBarForReal['value']

                                            if current_count is None:
                                                current_count = 0

                                            value = current_count + value

                                            if value > max_value:
                                                value = max_value

                                            self.window[item_updated["item"]].update(value)

                                        elif mode == "replace":
                                            self.window[item_updated["item"]].update(value)

                                    else:
                                        error = True

                                else:
                                    error = True

                            else:
                                if mode == "clear":
                                    self.window[item_updated["item"]].update(0)
                                else:
                                    error = True

                    else:
                        error = True

        if error:
            return False
        else:
            # self.windows.wds_simplegui[self.uniqid].refresh()
            return True

    # ---------------------------------------------------------------------
    # / Dessine une image sur le graphique
    # / Retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def graph_draw_image(self, graph: str, location: list, image=None):
        """
        :param graph:
        :param location:
        :param image:
        :return:
        """
        figure = None

        if graph in list(self.items_list.keys()):  # TODO: Créer erreur spécifique

            # TODO: Try/except

            with BytesIO() as output:
                image.save(output, format="PNG")
                image_data = output.getvalue()

            figure = self.window[graph].draw_image(data=image_data, location=location)

        if figure is None:
            return False
        else:
            return figure

    # ---------------------------------------------------------------------
    # / Dessine une line sur le graphique
    # / Retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def graph_draw_line(self, graph: str, point_from: list, point_to: list, color: str, width: int):
        """
        :param graph:
        :param point_from:
        :param point_to:
        :param color:
        :param width:
        :return:
        """
        figure = None

        if graph in list(self.items_list.keys()):  # TODO: Créer erreur spécifique
            figure = self.window[graph].draw_line(
                point_from=point_from,
                point_to=point_to,
                color=color,
                width=width
            )

        if figure is None:
            return False
        else:
            return figure

    # ---------------------------------------------------------------------
    # / Fait monter une figure sur l'axe Z
    # ---------------------------------------------------------------------

    def graph_bring_figure_to_front(self, graph: str, figure: int) -> bool:
        """
        :param graph:
        :param figure:
        :return:
        """
        try:
            self.window[graph].bring_figure_to_front(figure)
            return True
        except Exception as e:
            logging.exception(e)
            return False

    # ---------------------------------------------------------------------
    # / Fait descendre une figure sur l'axe Z
    # ---------------------------------------------------------------------

    def graph_send_figure_to_back(self, graph: str, figure: int) -> bool:
        """
        :param graph:
        :param figure:
        :return:
        """
        try:
            self.window[graph].send_figure_to_back(figure)
            return True
        except Exception as e:
            logging.exception(e)
            return False

    # ---------------------------------------------------------------------
    # / Supprime une figure
    # ---------------------------------------------------------------------

    def graph_delete_figure(self, graph: str, figure: int) -> bool:
        """
        :param graph:
        :param figure:
        :return:
        """
        try:
            self.window[graph].delete_figure(figure)
            return True
        except Exception as e:
            logging.exception(e)
            return False

    # ---------------------------------------------------------------------
    # / Supprime toutes les figures
    # ---------------------------------------------------------------------

    def graph_erase(self, graph: str):
        """
        :param graph:
        """
        self.window[graph].erase()

    # ---------------------------------------------------------------------
    # / Ferme la fenêtre
    # ---------------------------------------------------------------------

    def close(self):
        """
        :return:
        """
        self.window.close()
        return True
