def add_canvas(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    new_item = interpreter.fsg.Canvas(
        key=parameters["k"],
        pad=parameters["p"],
        size=parameters["s"],
        expand_x=parameters["xx"],
        expand_y=parameters["xy"]
    )

    new_item.BackgroundColor = interpreter.fsg.theme_background_color()

    return new_item, items_list