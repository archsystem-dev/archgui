def add_in_radio(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    new_item = interpreter.fsg.Radio(
        parameters["v"],
        parameters["g"],
        key=parameters["k"],
        pad=parameters["p"],
        size=parameters["s"],
        expand_x=parameters["xx"],
        expand_y=parameters["xy"],
        group_id=parameters["g"]
    )

    return new_item, items_list