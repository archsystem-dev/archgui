def add_tab(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    items, items_list = interpreter.create_items(
        items=item[1],
        items_list=items_list)

    new_item = interpreter.fsg.Tab(
        parameters["v"],
        items,
        key=parameters["k"],
        pad=parameters["p"],
        disabled=parameters["d"],
        element_justification=parameters["ae"],
        expand_x=parameters["xx"],
        expand_y=parameters["xy"]
    )

    return new_item, items_list