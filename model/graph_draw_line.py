def graph_draw_line(model, graph: str, point_from: list, point_to: list, color: str, width: int):

    figure = None

    if graph in list(model.items_list.keys()):  # TODO: Créer erreur spécifique
        figure = model.window[graph].draw_line(
            point_from=point_from,
            point_to=point_to,
            color=color,
            width=width
        )

    if figure is None:
        return False
    else:
        return figure