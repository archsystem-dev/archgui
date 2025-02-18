"""
Interpreter.py
"""

import json

# Importation des modules nécessaires pour gérer les différents éléments du modèle.
from .interpreter.add_button import add_button
from .interpreter.add_button_calendar import add_button_calendar
from .interpreter.add_button_color import add_button_color
from .interpreter.add_button_file import add_button_file
from .interpreter.add_button_files import add_button_files
from .interpreter.add_button_folder import add_button_folder
from .interpreter.add_button_save import add_button_save
from .interpreter.add_canvas import add_canvas
from .interpreter.add_column import add_column
from .interpreter.add_frame import add_frame
from .interpreter.add_graph import add_graph
from .interpreter.add_in_checkbox import add_in_checkbox
from .interpreter.add_in_combo import add_in_combo
from .interpreter.add_in_line import add_in_line
from .interpreter.add_in_lines import add_in_lines
from .interpreter.add_label import add_label
from .interpreter.add_progress_bar import add_progress_bar
from .interpreter.add_tab import add_tab
from .interpreter.add_in_radio import add_in_radio
from .interpreter.add_tab_group import add_tab_group
from .interpreter.create_items import create_items
from .interpreter.create_layout import create_layout
from .interpreter.create_parameters import create_parameters


class Interpreter:
    """
    Classe `Interpreter` :
    Cette classe agit comme un interpréteur pour initialiser le modèle
    avec des éléments, configurations, et pour permettre la création
    de layouts dynamiques.
    """

    def __init__(self, script_dir, fsg, config, window):
        """
        Constructeur de la classe Interpreter.

        :param script_dir: Répertoire contenant les scripts de configuration.
        :param fsg: Instance ou gestionnaire (non défini précisément ici).
        :param config: Configuration globale sous forme de dictionnaire.
        :param window: Fenêtre ou contexte associé à l'interface graphique.
        """

        # Initialisation des attributs principaux.
        self.script_dir = script_dir
        self.fsg = fsg
        self.window = window
        self.config = config

        # Chargement des paramètres par défaut depuis un fichier JSON.
        with open(script_dir + "/config/parameters.json", "r") as file:
            self.config["parameters"] = json.load(file)

        # Chargement des items depuis un fichier JSON.
        with open(script_dir + "/config/items.json", "r") as file:
            self.config["items"] = json.load(file)

        # Création d'un sous-dictionnaire contenant les items qui peuvent
        # être "déclencheurs" dans des événements.
        self.config["trigger_items"] = {
            "in_line": self.config["items"]["in_line"],
            "in_lines": self.config["items"]["in_lines"],
            "in_radio": self.config["items"]["in_radio"],
            "in_checkbox": self.config["items"]["in_checkbox"],
            "in_combo": self.config["items"]["in_combo"],
            "button": self.config["items"]["button"],
            "button_file": self.config["items"]["button_file"],
            "button_files": self.config["items"]["button_files"],
            "button_save": self.config["items"]["button_save"],
            "button_folder": self.config["items"]["button_folder"],
            "button_calendar": self.config["items"]["button_calendar"],
            "button_color": self.config["items"]["button_color"]
        }

    def list_to_tuple(self, ll):
        return tuple(self.list_to_tuple(x) for x in ll) if type(ll) is list else ll

    # ---------------------------------------------------------------------
    # Methodes principales pour la gestion des paramètres et du layout.
    # ---------------------------------------------------------------------

    def create_parameters(self, item):
        """
        Agrège les paramètres par défaut et les paramètres spécifiés
        pour un item donné.

        :param item: Élément pour lequel les paramètres doivent être générés.
        :return: Résultat de l'appel à `create_parameters`.
        """
        return create_parameters(self, item)

    def create_layout(self, items):
        """
        Crée le layout basé sur les items fournis.

        :param items: Liste des items à organiser dans le layout.
        :return: Résultat de l'appel à `create_layout`.
        """
        return create_layout(self, items)

    # ---------------------------------------------------------------------
    # Accesseurs pour les items et les "trigger items".
    # ---------------------------------------------------------------------

    def items(self):
        """
        Retourne la liste complète des items issus de la configuration actuelle.

        :return: Dictionnaire des items.
        """
        return self.config["items"]

    def trigger_items(self):
        """
        Retourne la liste des items pouvant être déclenchés par un événement.

        :return: Dictionnaire des items "déclencheurs".
        """
        return self.config["trigger_items"]

    # ---------------------------------------------------------------------
    # Gestion de la création des items pour les layouts.
    # ---------------------------------------------------------------------

    def create_items(self, items=None, items_list=None):
        """
        Crée les items pour le layout. Les items et items_list représentent
        les éléments à intégrer dans l'interface graphique.

        :param items: Liste des items définis.
        :param items_list: Autre liste optionnelle d'items.
        :return: Résultat de l'appel à `create_items`.
        """
        return create_items(self, items=items, items_list=items_list)

    # ---------------------------------------------------------------------
    # Méthodes pour gérer les différents types d'éléments du modèle.
    # Ces méthodes appellent les modules correspondants pour chaque type.
    # ---------------------------------------------------------------------

    def add_column(self, item, items_list):
        return add_column(self, item, items_list)

    def add_tab_group(self, item, items_list):
        return add_tab_group(self, item, items_list)

    def add_tab(self, item, items_list):
        return add_tab(self, item, items_list)

    def add_frame(self, item, items_list):
        return add_frame(self, item, items_list)

    def add_canvas(self, item, items_list):
        return add_canvas(self, item, items_list)

    def add_graph(self, item, items_list):
        return add_graph(self, item, items_list)

    def add_label(self, item, items_list):
        return add_label(self, item, items_list)

    def add_progress_bar(self, item, items_list):
        return add_progress_bar(self, item, items_list)

    def add_in_line(self, item, items_list):
        return add_in_line(self, item, items_list)

    def add_in_lines(self, item, items_list):
        return add_in_lines(self, item, items_list)

    def add_in_radio(self, item, items_list):
        return add_in_radio(self, item, items_list)

    def add_in_checkbox(self, item, items_list):
        return add_in_checkbox(self, item, items_list)

    def add_in_combo(self, item, items_list):
        return add_in_combo(self, item, items_list)

    def add_button(self, item, items_list):
        return add_button(self, item, items_list)

    def add_button_file(self, item, items_list):
        return add_button_file(self, item, items_list)

    def add_button_files(self, item, items_list):
        return add_button_files(self, item, items_list)

    def add_button_save(self, item, items_list):
        return add_button_save(self, item, items_list)

    def add_button_folder(self, item, items_list):
        return add_button_folder(self, item, items_list)

    def add_button_calendar(self, item, items_list):
        return add_button_calendar(self, item, items_list)

    def add_button_color(self, item, items_list):
        return add_button_color(self, item, items_list)
