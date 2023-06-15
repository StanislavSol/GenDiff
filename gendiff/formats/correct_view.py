def get_correct_view(data_tree):
    replacement_values = (('True', 'true'),
                          ('False', 'false'),
                          ('None', 'null'))
    for values in replacement_values:
        data_tree = data_tree.replace(*values)
    return data_tree
