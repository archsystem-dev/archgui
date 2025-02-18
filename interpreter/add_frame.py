def add_frame(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    items, items_list = interpreter.create_items(
        items=item[1],
        items_list=items_list)

    new_item = interpreter.fsg.pin(interpreter.fsg.Frame(
        parameters["v"],
        items,
        key=parameters["k"],
        pad=parameters["p"],
        size=parameters["s"],
        vertical_alignment=parameters["av"],
        element_justification=parameters["ae"],
        font=parameters["f"],
        expand_x=parameters["xx"],
        expand_y=parameters["xy"]
    ), shrink=True)

    return new_item, items_list