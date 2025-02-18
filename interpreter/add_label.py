def add_label(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    new_item = interpreter.fsg.Text(
        parameters["v"],
        key=parameters["k"],
        pad=parameters["p"],
        size=parameters["s"],
        font=parameters["f"],
        expand_x=parameters["xx"],
        expand_y=parameters["xy"]
    )

    return new_item, items_list