def add_tab_group(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    items, items_list = interpreter.create_items(
        items=item[1],
        items_list=items_list)

    new_item = interpreter.fsg.TabGroup(
        items,
        key=parameters["k"],
        pad=parameters["p"],
        size=parameters["s"],
        font=parameters["f"],
        enable_events=True,
        change_submits=True,
        tab_location=parameters["tl"],
        expand_x=parameters["xx"],
        expand_y=parameters["xy"]
    )

    return new_item, items_list