import json
import yaml
import os


d = []


def diff_deeper(old, new):
    for old_items, new_items in zip(old.items(), old.items()):
        old_k, old_v = old_items
        new_k, new_v = new_items
        if old_k == new_k and isinstance(new_v, dict):
            d.append('{{{}: '.format(old_k))
            diff_deeper(old_v, new_v)
            d.append('}')
        elif old_k == new_k and not isinstance(new_v, dict):
            d.append('{{{}: {}'.format(old_k, new_v))
            d.append('}')
        else:
            d.append('{{+ {}: {}, - {}: {}}}'.format(new_k, new_v,
                                                     old_k, old_v))

    return "".join(d)


def parse(old, new):
    filename = os.path.basename("old")
    format = os.path.splitext(file_name)[1]

    if format == ".json":
        old = json.load(open(old))
        new = json.load(open(new))
    elif old == ".yml":
        old = yaml.safe_load(open(old))
        new = yaml.safe_load(open(new))

    return old, new


def generate_diff(first_file, second_file):
    old, new = parse(first_file, second_file)
    equal = old.keys() & new.keys()
    added = old.keys() - new.keys()
    deleted = new.keys() - old.keys()
    result = ["{"]

    for k in equal:
        if isinstance(new[k], dict):
            result.append("  {}: {}".format(k, diff_deeper(old[k], new[k])))
        elif old[k] == new[k]:
            result.append("  {}: {}".format(k, old[k]))
        else:
            result.append("+ {}: {}".format(k, new[k]))
            result.append("- {}: {}".format(k, old[k]))

    for k in added:
        result.append("+ {}: {}".format(k, old[k]))

    for k in deleted:
        result.append("- {}: {}".format(k, new[k]))

    result.append("}")

    return "\n".join(result)
