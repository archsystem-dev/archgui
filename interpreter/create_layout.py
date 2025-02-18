def create_layout(interpreter, items):

    items_list = {}
    layout, items_list = interpreter.create_items(items, items_list)

    return layout, items_list