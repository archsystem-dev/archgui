def create_items(interpreter, items=None, items_list=None):

    layout = []

    row_c = 0
    for row in items:

        layout.append([])

        for item in row:

            if item[0]["t"] == "column":
                rl, items_list = interpreter.add_column(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "tab_group":
                rl, items_list = interpreter.add_tab_group(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "tab":
                rl, items_list = interpreter.add_tab(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "frame":
                rl, items_list = interpreter.add_frame(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "canvas":
                rl, items_list = interpreter.add_canvas(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "graph":
                rl, items_list = interpreter.add_graph(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "label":
                rl, items_list = interpreter.add_label(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "in_line":
                rl, items_list = interpreter.add_in_line(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "in_lines":
                rl, items_list = interpreter.add_in_lines(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "in_radio":
                rl, items_list = interpreter.add_in_radio(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "in_checkbox":
                rl, items_list = interpreter.add_in_checkbox(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "in_combo":
                rl, items_list = interpreter.add_in_combo(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "button":
                rl, items_list = interpreter.add_button(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "button_file":
                rl, items_list = interpreter.add_button_file(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "button_files":
                rl, items_list = interpreter.add_button_files(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "button_save":
                rl, items_list = interpreter.add_button_save(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "button_folder":
                rl, items_list = interpreter.add_button_folder(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "button_calendar":
                rl, items_list = interpreter.add_button_calendar(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "button_color":
                rl, items_list = interpreter.add_button_color(item, items_list)
                layout[row_c].append(rl)
            elif item[0]["t"] == "progress_bar":
                rl, items_list = interpreter.add_progress_bar(item, items_list)
                layout[row_c].append(rl)

        row_c += 1

    return layout, items_list