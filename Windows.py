"""
Windows.py
"""

import sys
import copy
import uuid
import threading
import logging

from pynput.keyboard import Key, Controller


class Windows:
    """
    Class Windows
    """
    def __init__(self, platform, fsg, workarea):

        self.modules = {}

        self.platform = platform
        self.fsg = fsg
        self.wageo = workarea.geometry()

        # -----------------------------------------------------------------

        self.lock = threading.Lock()

        # -----------------------------------------------------------------

        self.keyboard = Controller()
        self.key = Key

        # -----------------------------------------------------------------

        self.script_dir = None
        self.config = None
        self.window_main = None

        # -----------------------------------------------------------------

        self.models_window = {
            "sys": {},
            "usr": {}
        }
        self.models_event = {
            "sys": {},
            "usr": {}
        }

        # -----------------------------------------------------------------

        self.wds_simplegui = {}
        self.wds_windows = {}
        self.wds_uniqid = {}
        self.wds_events = {}
        self.wds_graphs = {}

    # ---------------------------------------------------------------------
    # / Chargement de la configuration de FreeSimpleGUI
    # ---------------------------------------------------------------------

    def load_config(self, script_dir, config):
        self.script_dir = script_dir
        self.config = config
        self.fsg.theme(self.config["general"]["theme"])

    # ---------------------------------------------------------------------
    # / Chargement des models et events
    # ---------------------------------------------------------------------

    def load_models(self, models_window, models_event):
        self.models_window = models_window
        self.models_event = models_event

    # ---------------------------------------------------------------------
    # / Chargement des modules de l’utilisateur
    # ---------------------------------------------------------------------

    def define_modules(self, modules) -> bool:
        self.modules = modules
        return True

    # ---------------------------------------------------------------------
    # / Définition de la fenêtre principale
    # ---------------------------------------------------------------------

    def define_main(self, uniqid: str) -> bool:
        if uniqid in self.wds_uniqid:
            self.window_main = uniqid
            return True
        else:
            return False

    # ---------------------------------------------------------------------
    # / Retourne l’UNIQID d’une fenêtre à partir du interpreter + wid
    # ---------------------------------------------------------------------

    def uniqid(self, model: str, id: int):
        uniqid = None
        if model in self.wds_windows:
            if id in self.wds_windows[model]:
                uniqid = self.wds_windows[model][id].uniqid

        if uniqid is not None:
            return uniqid
        else:
            return False

    # ---------------------------------------------------------------------
    # / Retourne l’UNIQID d’une fenêtre à partir du interpreter + wid
    # ---------------------------------------------------------------------

    def window(self, uniqid: str) -> bool:
        if uniqid in self.wds_uniqid:
            return self.wds_uniqid[uniqid]
        else:
            return False

    # ---------------------------------------------------------------------
    # / Retourne True ou False si la fenêtre existe ou non
    # ---------------------------------------------------------------------

    def exist(self, uniqid: str) -> bool:
        if uniqid in self.wds_uniqid:
            return True
        else:
            return False

    # ---------------------------------------------------------------------
    # / Ouvre une nouvelle fenêtre
    # / Retourne l'UNIQID si la fenêtre n’existe pas deja
    # / Retourne False si la fenêtre existe déjà
    # ---------------------------------------------------------------------

    def activate(self, model: str, monitor: str, id: str, title: str,
                 uniqid=None, location=None, size=None, alpha_channel=None):

        with self.lock:

            try:

                if monitor is None:
                    monitor = "primary"

                if id is None:
                    id = "0"

                if not isinstance(self.wds_windows, dict):
                    self.wds_windows = {}
                    self.wds_events = {}

                if model not in self.wds_windows:
                    self.wds_windows[model] = {}
                    self.wds_events[model] = {}

                if id not in self.wds_windows[model]:
                    self.wds_windows[model][id] = copy.copy(self.models_window[model])
                    self.wds_events[model][id] = copy.copy(self.models_event[model])

                    simplegui = self.wds_windows[model][id].activate(
                        monitor=monitor,
                        id=id,
                        title=title,
                        location=location,
                        size=size,
                        alpha_channel=alpha_channel
                    )

                    if uniqid is None:
                        uniqid = uuid.uuid4()

                    self.wds_simplegui[uniqid] = simplegui
                    self.wds_uniqid[uniqid] = self.wds_windows[model][id]
                    self.wds_graphs[uniqid] = {}

                    self.wds_windows[model][id].uniqid = uniqid
                    self.wds_events[model][id].uniqid = uniqid
                    self.wds_events[model][id].id = id

                    self.wds_events[model][id].windows = self
                    self.wds_events[model][id].window = simplegui
                    self.wds_events[model][id].model = self.wds_windows[model][id]

                    return uniqid

                else:
                    return False

            except Exception as e:
                logging.exception(e)
                return False

    # ---------------------------------------------------------------------
    # / Si la fenêtre est hide, la fenêtre est unhide et retourne True
    # / Si la fenêtre n’est pas hide, retourne False
    # ---------------------------------------------------------------------

    def show(self, uniqid: str) -> bool:
        if uniqid is not None and uniqid in self.wds_uniqid:
            if self.wds_uniqid[uniqid].is_hide:
                self.wds_uniqid[uniqid].show()
                return True
            else:
                return False

    # ---------------------------------------------------------------------
    # / Si la fenêtre n’est pas hide, la fenêtre est hide et retourne True
    # / Si la fenêtre est hide, retourne False
    # ---------------------------------------------------------------------

    def hide(self, uniqid: str):
        if uniqid is not None and uniqid in self.wds_uniqid:
            if self.wds_uniqid[uniqid].is_hide:
                return False
            else:
                self.wds_uniqid[uniqid].hide()
                return True

    # ---------------------------------------------------------------------
    # / Créer un Bind
    # ---------------------------------------------------------------------

    def bind(self, uniqid: str, binds: list) -> bool:
        if uniqid is not None and uniqid in self.wds_uniqid:
            if self.wds_uniqid[uniqid].bind(binds):
                return True
            else:
                return False

    # ---------------------------------------------------------------------
    # / Retourne la valeur de l'item
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def get_item(self, item: str, uniqid=None):
        if uniqid is None:
            uniqid = self.window_main

        if uniqid is not None and uniqid in self.wds_uniqid:
            return self.wds_uniqid[uniqid].get_item(item)
        else:
            return False

    # ---------------------------------------------------------------------
    # / Modifie un item de la fenêtre ciblée et retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def update(self, items: list, uniqid=None) -> bool:
        if uniqid is None:
            uniqid = self.window_main

        if uniqid is not None and uniqid in self.wds_uniqid:
            if self.wds_uniqid[uniqid].update(items):
                return True
            else:
                return False

    # ---------------------------------------------------------------------
    # / Dessine une image sur le graphique
    # / Retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def graph_draw_image(self, graph: str, location: list, uniqid=None, image=None) -> bool:
        if uniqid is None:
            uniqid = self.window_main

        if uniqid is not None and uniqid in self.wds_uniqid:
            return self.wds_uniqid[uniqid].graph_draw_image(graph, location, image)

    # ---------------------------------------------------------------------
    # / Dessine une line sur le graphique
    # / Retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def graph_draw_line(self, graph: str, point_from: list, point_to: list, color="white", width=1, uniqid=None) -> bool:
        if uniqid is None:
            uniqid = self.window_main

        if uniqid is not None and uniqid in self.wds_uniqid:
            return self.wds_uniqid[uniqid].graph_draw_line(graph, point_from, point_to, color, width)

    # ---------------------------------------------------------------------
    # / Fait monter une figure sur l'axe Z
    # / Retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def graph_bring_figure_to_front(self, graph: str, figure: int, uniqid=None) -> bool:
        if uniqid is None:
            uniqid = self.window_main

        if uniqid is not None and uniqid in self.wds_uniqid:
            if self.wds_uniqid[uniqid].graph_bring_figure_to_front(graph, figure):
                return True
            else:
                return False

    # ---------------------------------------------------------------------
    # / Fait descendre une figure sur l'axe Z
    # / Retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def graph_send_figure_to_back(self, graph: str, figure: int, uniqid=None) -> bool:
        if uniqid is None:
            uniqid = self.window_main

        if uniqid is not None and uniqid in self.wds_uniqid:
            if self.wds_uniqid[uniqid].graph_send_figure_to_back(graph, figure):
                return True
            else:
                return False

    # ---------------------------------------------------------------------
    # / Supprimer une figure
    # / Retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def graph_delete_figure(self, graph: str, figure: int, uniqid=None) -> bool:
        if uniqid is None:
            uniqid = self.window_main

        if uniqid is not None and uniqid in self.wds_uniqid:
            if self.wds_uniqid[uniqid].graph_delete_figure(graph, figure):
                return True
            else:
                return False

    # ---------------------------------------------------------------------
    # / Ferme une fenêtre
    # ---------------------------------------------------------------------

    def deactivate(self, uniqid: str):
        if uniqid in self.wds_simplegui:
            self.deactivate_and_purge(self.wds_simplegui[uniqid])

    # ---------------------------------------------------------------------
    # / Purge les données lors da la fermeture d’une fenêtre
    # ---------------------------------------------------------------------

    def deactivate_and_purge(self, window):
        """
        :param window:
        """
        wds_deleted = {}

        for uniqid in self.wds_simplegui:
            if self.wds_simplegui[uniqid] == window:
                wds_deleted[uniqid] = {
                    "interpreter": self.wds_uniqid[uniqid].model,
                    "id": self.wds_uniqid[uniqid].id
                }

        for uniqid in wds_deleted:

            del self.wds_graphs[uniqid]
            del self.wds_simplegui[uniqid]
            del self.wds_uniqid[uniqid]

            model = wds_deleted[uniqid]["interpreter"]
            id = wds_deleted[uniqid]["id"]

            del self.wds_windows[model][id]
            del self.wds_events[model][id]

            if len(self.wds_windows[model]) == 0:
                del self.wds_windows[model]
                del self.wds_events[model]

            if len(self.wds_windows) == 0:
                del self.wds_windows
                del self.wds_events

        window.close()

    # ---------------------------------------------------------------------
    # / Boucle d'écoute des Events
    # ---------------------------------------------------------------------

    def stop(self):
        uniqids = self.wds_uniqid.copy()
        for uniqid in uniqids:
            if uniqid != self.window_main:
                self.deactivate_and_purge(self.wds_simplegui[uniqid])
        self.deactivate_and_purge(self.wds_simplegui[self.window_main])

    # ---------------------------------------------------------------------
    # / Boucle d'écoute des Events
    # ---------------------------------------------------------------------

    def events_run(self):

        while True:

            stop = False
            window, event, values = self.fsg.read_all_windows()

            if event == self.fsg.WIN_CLOSED or event == 'Exit':

                if self.window_main is not None:
                    if self.window_main in self.wds_uniqid:
                        if window == self.wds_uniqid[self.window_main].window:
                            for module in self.modules:
                                if module != "archgui":
                                    self.modules[module].stop()

                            stop = True

                if window is not None:
                    self.deactivate_and_purge(window)

            else:

                with self.lock:
                    wds_simplegui_cp = copy.copy(self.wds_simplegui)

                for uniqid in wds_simplegui_cp:
                    if uniqid in self.wds_simplegui:
                        if self.wds_simplegui[uniqid] == window:
                            model = self.wds_uniqid[uniqid].model
                            id = self.wds_uniqid[uniqid].id
                            self.wds_events[model][id].events(event, self.modules, values)

                del wds_simplegui_cp

            if stop:
                break

        sys.exit(0)
