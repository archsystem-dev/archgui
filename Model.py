"""
Model.py
"""

import re
import json

from .model.bind import bind
from .model.graph_draw_image import graph_draw_image
from .model.graph_draw_line import graph_draw_line
from .model.activate import activate
from .model.set_location_x import set_location_x
from .model.set_location_y import set_location_y
from .model.set_size_height import set_size_height
from .model.set_size_width import set_size_width
from .model.update import update

from archgui.Interpreter import Interpreter


class Model:
    """
    Class Model
    """
    def __init__(self, script_dir, windows, model, specter):

        # -----------------------------------------------------------------

        self.script_dir = script_dir
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
        self.title = ""
        self.window = None

        # -----------------------------------------------------------------

        self.interpreter = Interpreter(self.script_dir, self.fsg, self.windows.config, self.window)

        # -----------------------------------------------------------------

        # Chargement des items depuis un fichier JSON.
        with open(script_dir + "/config/model.json", "r") as file:
            self.parameters = json.load(file)

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

    # -------------------------------------------------------------------------
    # / Converti une list en tuple
    # -------------------------------------------------------------------------

    def list_to_tuple(self, ll):
        return tuple(self.list_to_tuple(x) for x in ll) if type(ll) is list else ll

    # -------------------------------------------------------------------------
    # / Vérifier qu'un paramètre de Size ou Location n’est pas vide
    # / Retourne True ou False
    # -------------------------------------------------------------------------

    def pisnt_null(self, parameters):
        """
        :param parameters:
        :return:
        """
        not_null = True
        if parameters["uniqid"] is None:
            not_null = False

        if parameters["interpreter"] is not None:
            if parameters["wid"] is not None:
                not_null = True

        return not_null

    # ---------------------------------------------------------------------
    # / Définit la position de la fenêtre en X
    # ---------------------------------------------------------------------

    def set_location_x(self):
        return set_location_x(self)

    # ---------------------------------------------------------------------
    # / Définit la position de la fenêtre en Y
    # ---------------------------------------------------------------------

    def set_location_y(self):
        return set_location_y(self)

    # ---------------------------------------------------------------------
    # / Définit la largeur de la fenêtre
    # ---------------------------------------------------------------------

    def set_size_width(self):
        return set_size_width(self)

    # ---------------------------------------------------------------------
    # / Définit la hauteur de la fenêtre
    # ---------------------------------------------------------------------

    def set_size_height(self):
        return set_size_height(self)

    # ---------------------------------------------------------------------
    # / Affiche la Window de FreeSimpleGUI
    # ---------------------------------------------------------------------

    def activate(self, monitor, id, title, location=None, size=None, alpha_channel=None):
        return activate(self, monitor, id, title, location=location, size=size, alpha_channel=alpha_channel)

    # ---------------------------------------------------------------------
    # / Affiche une fenêtre
    # ---------------------------------------------------------------------

    def show(self):
        self.is_hide = False
        self.window.UnHide()

    # ---------------------------------------------------------------------
    # / Masque une fenêtre
    # ---------------------------------------------------------------------

    def hide(self):
        self.is_hide = True
        self.window.hide()

    # ---------------------------------------------------------------------
    # / Créer un Bind
    # ---------------------------------------------------------------------

    def bind(self, binds: dict):
        return bind(self, binds)

    # ---------------------------------------------------------------------
    # / Retourne la taille de la fenêtre
    # ---------------------------------------------------------------------

    def get_size(self):
        return self.window_size

    # ---------------------------------------------------------------------
    # / Retourne la position initiale de la fenêtre
    # ---------------------------------------------------------------------

    def get_location(self):
        return self.window_location

    # ---------------------------------------------------------------------
    # / Retourne un Item de la fenêtre
    # ---------------------------------------------------------------------

    def get_item(self, item: str):
        return self.window[item].get()

    # ---------------------------------------------------------------------
    # / Modifie un Item de la fenêtre
    # ---------------------------------------------------------------------

    def update(self, items):
        return update(self, items)

    # ---------------------------------------------------------------------
    # / Dessine une image sur le graphique
    # / Retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def graph_draw_image(self, graph: str, location: list, image=None):
        return graph_draw_image(self, graph=graph, location=location, image=image)

    # ---------------------------------------------------------------------
    # / Dessine une line sur le graphique
    # / Retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def graph_draw_line(self, graph: str, point_from: list, point_to: list, color: str, width: int):
        return graph_draw_line(self, graph=graph, point_from=point_from, point_to=point_to, color=color, width=width)

    # ---------------------------------------------------------------------
    # / Fait monter une figure sur l'axe Z
    # ---------------------------------------------------------------------

    def graph_bring_figure_to_front(self, graph: str, figure: int) -> bool:
        self.window[graph].bring_figure_to_front(figure)
        return True

    # ---------------------------------------------------------------------
    # / Fait descendre une figure sur l'axe Z
    # ---------------------------------------------------------------------

    def graph_send_figure_to_back(self, graph: str, figure: int) -> bool:
        self.window[graph].send_figure_to_back(figure)
        return True

    # ---------------------------------------------------------------------
    # / Supprime une figure
    # ---------------------------------------------------------------------

    def graph_delete_figure(self, graph: str, figure: int) -> bool:
        self.window[graph].delete_figure(figure)
        return True

    # ---------------------------------------------------------------------
    # / Supprime toutes les figures
    # ---------------------------------------------------------------------

    def graph_erase(self, graph: str):
        self.window[graph].erase()

    # ---------------------------------------------------------------------
    # / Ferme la fenêtre
    # ---------------------------------------------------------------------

    def deactivate(self):
        self.window.close()
