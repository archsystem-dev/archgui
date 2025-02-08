"""
__init__.py
"""

import FreeSimpleGUI as fsg

import os
import io
import json
import importlib

from sys import platform

from .Windows import Windows
from .Model import Model
from .Workarea import Workarea

script_dir = os.path.dirname(__file__)
parent_dir = script_dir.replace("/archgui", "")

workarea = Workarea(platform, fsg)
windows = Windows(platform, fsg, workarea)

models_event = {}
specters = {}

if os.path.isdir(parent_dir + "/archgui_events"):

    for file in os.listdir(parent_dir + "/archgui_events"):
        file_split = os.path.splitext(file)

        if file_split[1] == ".py":
            my_module = importlib.import_module("archgui_events." + file_split[0])
            models_event[file_split[0]] = my_module.Events()
else:

    print("Le dossier 'archgui_events' est introuvable.")
    exit(0)


if os.path.isdir(parent_dir + "/archgui_windows"):

    for file in os.listdir(parent_dir + "/archgui_windows"):
        file_split = os.path.splitext(file)

        if file_split[1] == ".json":
            specters[file_split[0]] = json.load(io.open(parent_dir + "/archgui_windows/" + file))
else:

    print("Le dossier 'archgui_events' est introuvable.")
    exit(0)


config = json.load(io.open(script_dir + "/config/default.json"))

windows.load_config(config)
models_window = {}

for model in models_event:
    models_window[model] = Model(windows, model, specters[model])

windows.load_models(models_window, models_event)


def define_modules(modules):
    """
    :param modules:
    :return:
    """
    global windows

    if windows.define_modules(modules):
        return True
    else:
        return False


def define_main(uniqid: str):
    """
    :param uniqid:
    :return:
    """
    global windows

    if windows.define_main(uniqid=uniqid):
        return True
    else:
        return False


def open(model: str, monitor=None, id=None, title=None, uniqid=None, location=None, size=None, alpha_channel=1, force_toplevel=False):
    """
    :param model:
    :param monitor:
    :param id:
    :param title:
    :param uniqid:
    :param location:
    :param size:
    :param alpha_channel:
    :param force_toplevel:
    :return:
    """
    global windows

    uniqid = windows.open(
        model=model,
        monitor=monitor,
        id=id,
        title=title,
        uniqid=uniqid,
        location=location,
        size=size,
        alpha_channel=alpha_channel,
        force_toplevel=force_toplevel)

    if uniqid:
        return uniqid
    else:
        return False


def bind(uniqid: str, binds: list):
    """
    :param uniqid:
    :param binds:
    :return:
    """
    global windows

    if windows.bind(
            uniqid=uniqid,
            binds=binds):
        return True
    else:
        return False


def get_item(item: str, uniqid=None):
    """
    :param uniqid:
    :param item:
    :return:
    """
    global windows

    return windows.get_item(
        uniqid=uniqid,
        item=item)


def update(items: list, uniqid=None):
    """
    :param uniqid:
    :param items:
    :return:
    """
    global windows

    if windows.update(
            uniqid=uniqid,
            items=items):
        return True
    else:
        return False


def close(uniqid: str):
    """
    :param uniqid:
    :return:
    """
    global windows

    if windows.close(uniqid=uniqid):
        return True
    else:
        return False


def graph_draw_image(graph: str, location: list, uniqid=None, image=None):
    """
    :param uniqid:
    :param graph:
    :param location:
    :param image:
    :return:
    """
    global windows

    result = windows.graph_draw_image(
        uniqid=uniqid,
        graph=graph,
        location=location,
        image=image)
    return result


def graph_draw_line(graph: str, point_from: list, point_to: list, color="white", width=1, uniqid=None):
    """
    :param graph:
    :param point_from:
    :param point_to:
    :param color:
    :param width:
    :param uniqid:
    :return:
    """
    global windows

    result = windows.graph_draw_line(
        uniqid=uniqid,
        graph=graph,
        point_from=point_from,
        point_to=point_to,
        color=color,
        width=width,
    )
    return result


def graph_bring_figure_to_front(graph: str, figure: int, uniqid=None):
    """
    :param uniqid:
    :param graph:
    :param figure:
    :return:
    """
    global windows

    if windows.graph_bring_figure_to_front(
            uniqid=uniqid,
            graph=graph,
            figure=figure):
        return True
    else:
        return False


def graph_send_figure_to_back(graph: str, figure: int, uniqid=None):
    """
    :param uniqid:
    :param graph:
    :param figure:
    :return:
    """
    global windows

    if windows.graph_send_figure_to_back(
            uniqid=uniqid,
            graph=graph,
            figure=figure):
        return True
    else:
        return False


def graph_delete_figure(graph: str, figure: int, uniqid=None):
    """
    :param uniqid:
    :param graph:
    :param figure:
    :return:
    """
    global windows

    if windows.graph_delete_figure(
            uniqid=uniqid,
            graph=graph,
            figure=figure):
        return True
    else:
        return False


def stop():
    """
    run()
    """
    global windows

    windows.stop()


def run():
    """
    run()
    """
    global windows

    windows.events_run()
