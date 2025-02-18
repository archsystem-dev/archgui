
def add_button(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    new_item = interpreter.fsg.Button(
        parameters["v"],
        key=parameters["k"],
        pad=parameters["p"],
        size=parameters["s"],
        disabled=parameters["d"],
        font=parameters["f"]
    )

    return new_item, items_list