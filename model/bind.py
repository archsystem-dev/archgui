def bind(model, binds: dict):

    error = False

    for bind_updated in binds:

        if all(k in bind_updated for k in ("item", "bind_string", "bind_key")):  # TODO: Créer erreur spécifique

            item = bind_updated["item"]
            bind_string = bind_updated["bind_string"]
            bind_key = bind_updated["bind_key"]

            if item is None:
                model.window.bind(bind_string, bind_key)
            elif item in list(model.items_list.keys()):
                model.window[item].bind(bind_string, bind_key)

    if error:
        return False
    else:
        return True