def update(model, items):
    """
    :param items:
    :return:
    """

    error = False

    for item_updated in items:

        if all(k in item_updated for k in ("item", "mode")):

            key = item_updated["item"]
            mode = item_updated["mode"]

            if key in list(model.items_list.keys()):

                key_type = model.items_list[key]["type"]

                if mode in ["add", "replace", "clear", "show", "hide", "disabled"]:

                    if mode == "show":
                        model.window[item_updated["item"]].update(visible=True)

                    if mode == "hide":
                        model.window[item_updated["item"]].update(visible=False)

                    if mode == "disabled":
                        if "value" in item_updated:
                            value = item_updated["value"]

                            if value is True or value is False:
                                model.window[item_updated["item"]].update(disabled=value)

                    if key_type == "label":

                        if "value" in item_updated:
                            value = item_updated["value"]

                            if mode == "add":
                                model.window[item_updated["item"]].print(value)
                            elif mode == "replace":
                                model.window[item_updated["item"]].update(value)

                        if mode == "clear":
                            model.window[item_updated["item"]].update()

                    if key_type == "in_line":

                        if "value" in item_updated:
                            value = item_updated["value"]

                            if mode == "add":
                                value = model.window[item_updated["item"]].get() + value
                                model.window[item_updated["item"]].update(value)
                            elif mode == "replace":
                                model.window[item_updated["item"]].update(value)

                        if mode == "clear":
                            model.window[item_updated["item"]].update("")

                    if key_type == "in_lines":

                        if mode in ["add", "replace"]:

                            if mode == "replace":
                                model.window[key].update("")

                            if "value" in item_updated:
                                value = item_updated["value"]

                                truncate_height = model.items_list[key]["truncate_height"]

                                if truncate_height:
                                    truncate_width = True
                                else:
                                    truncate_width = model.items_list[key]["truncate_width"]

                                max_chars = model.window[item_updated["item"]].Size[0]
                                max_lines = model.window[item_updated["item"]].Size[1]

                                lines = ""
                                lines_list = model.window[key].get().split("\n")

                                if truncate_width:
                                    value = value[0:max_chars]

                                if truncate_height:
                                    if len(lines_list) >= max_lines:
                                        dec = (len(lines_list) - max_lines) + 1
                                        lines_list = lines_list[dec:max_lines]

                                for line in lines_list:
                                    if len(line) > 0:
                                        if truncate_height:
                                            lines += line[0: max_chars] + "\n"
                                        else:
                                            lines += line + "\n"

                                lines += value

                                model.window[key].update(lines)

                        elif mode == "clear":
                            model.window[key].update("")

                    if key_type == "button":
                        error = True

                    if key_type == "button_file":
                        error = True

                    if key_type == "button_files":
                        error = True

                    if key_type == "button_save":
                        error = True

                    if key_type == "button_folder":
                        error = True

                    if key_type == "button_calendar":
                        error = True

                    if key_type == "button_color":
                        if "default_color" in item_updated:

                            default_color = item_updated["default_color"]

                            if mode == "replace":
                                if isinstance(default_color, str) or isinstance(default_color, int):
                                    model.window[item_updated["item"]].update(default_color)
                                else:
                                    error = True

                    if key_type == "in_combo":

                        if all(k in item_updated for k in ("value", "default_value")):

                            value = item_updated["value"]
                            default_value = item_updated["default_value"]

                            if mode == "add":

                                if isinstance(value, str) and isinstance(default_value, str) or isinstance(
                                        default_value, int):
                                    value = model.window[item_updated["item"]].get().append(value)
                                    if default_value in value:
                                        model.window[item_updated["item"]].update(default_value, value)
                                    else:
                                        error = True
                                else:
                                    error = True

                            elif mode == "replace":
                                if isinstance(value, list) and isinstance(default_value, str) or isinstance(
                                        default_value, int):
                                    if default_value in value:
                                        model.window[item_updated["item"]].update(default_value, value)
                                    else:
                                        error = True
                                else:
                                    error = True

                        elif "default_value" in item_updated:

                            default_value = item_updated["default_value"]

                            if mode == "replace":
                                if isinstance(default_value, str) or isinstance(default_value, int):
                                    model.window[item_updated["item"]].update(default_value)
                                else:
                                    error = True

                        else:
                            if mode == "clear":
                                model.window[item_updated["item"]].update("", "")
                            else:
                                error = True

                    if key_type == "progress_bar":

                        if "value" in item_updated:

                            max_value = model.window[item_updated["item"]].MaxValue
                            value = item_updated["value"]

                            if isinstance(value, int):

                                if value <= max_value:

                                    if mode == "add":
                                        current_count = model.window[item_updated["item"]]
                                        current_count = current_count.TKProgressBar.TKProgressBarForReal['value']

                                        if current_count is None:
                                            current_count = 0

                                        value = current_count + value

                                        if value > max_value:
                                            value = max_value

                                        model.window[item_updated["item"]].update(value)

                                    elif mode == "replace":
                                        model.window[item_updated["item"]].update(value)

                                else:
                                    error = True

                            else:
                                error = True

                        else:
                            if mode == "clear":
                                model.window[item_updated["item"]].update(0)
                            else:
                                error = True

                else:
                    error = True

    if error:
        return False
    else:
        return True