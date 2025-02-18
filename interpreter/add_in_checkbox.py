def add_in_checkbox(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    new_item = interpreter.fsg.Checkbox(
        parameters["v"],
        key=parameters["k"],
        pad=parameters["p"],
        disabled=parameters["d"],
        size=parameters["s"],
        expand_x=parameters["xx"],
        expand_y=parameters["xy"]
    )

    return new_item, items_list