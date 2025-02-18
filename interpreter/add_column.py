def add_column(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    items, items_list = interpreter.create_items(
        items=item[1],
        items_list=items_list)

    new_item = interpreter.fsg.pin(interpreter.fsg.Column(
        items,
        key=parameters["k"],
        pad=parameters["p"],
        size=parameters["s"],
        scrollable=parameters["sc"],
        vertical_scroll_only=parameters["scvo"],
        vertical_alignment=parameters["av"],
        element_justification=parameters["ae"],
        expand_x=parameters["xx"],
        expand_y=parameters["xy"],
        visible=parameters["vbl"],
        background_color=parameters["bgc"]
    ), shrink=True)

    if parameters["bgc"] is not None:
        new_item.BackgroundColor = parameters["bgc"]
    else:
        new_item.BackgroundColor = interpreter.fsg.theme_background_color()

    return new_item, items_list