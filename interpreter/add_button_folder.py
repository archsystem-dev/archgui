def add_button_folder(interpreter, item, items_list):

    items_list = items_list
    parameters = interpreter.create_parameters(item)

    if "t" in parameters:
        items_list[parameters["k"]] = {
            "type": parameters["t"]
        }

    new_item = interpreter.fsg.FolderBrowse(
        key=parameters["k"],
        target=parameters["tg"],
        pad=parameters["p"],
        size=parameters["s"],
        disabled=parameters["d"],
        font=parameters["f"],
        button_text=parameters["v"],
    )

    return new_item, items_list