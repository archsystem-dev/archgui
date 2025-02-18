def add_in_combo(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    new_item = interpreter.fsg.Combo(
        parameters["v"],
        auto_size_text=False,
        key=parameters["k"],
        pad=parameters["p"],
        disabled=parameters["d"],
        enable_events=True,
        change_submits=True,
        size=parameters["s"],
        font=parameters["f"],
        expand_x=parameters["xx"],
        expand_y=parameters["xy"],
        readonly=parameters["ro"],
        default_value=parameters["dv"]
    )

    return new_item, items_list