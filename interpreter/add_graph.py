def add_graph(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    new_item = interpreter.fsg.Graph(
        key=parameters["k"],
        pad=parameters["p"],
        canvas_size=parameters["s"],
        border_width=parameters["bw"],
        graph_bottom_left=(0, parameters["s"][1]),
        graph_top_right=(parameters["s"][0], 0),
        change_submits=True,
        motion_events=True,
        enable_events=True
    )

    if parameters["bgc"] is not None:
        new_item.BackgroundColor = parameters["bgc"]
    else:
        new_item.BackgroundColor = interpreter.fsg.theme_background_color()

    return new_item, items_list