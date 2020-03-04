import json
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
        else:
            d.append('{{+ {}: {}, - {}: {}}}'.format(new_k, new_v, old_k, old_v))

    return "".join(d)


def generate_diff(old, new):
    os.chdir("gendiff/tests/fixtures/")
    old = json.load(open(old))
    new = json.load(open(new))
    equal = old.keys() & new.keys()
    added = old.keys() - new.keys()
    deleted = new.keys() - old.keys()
    result = []

    result.append("{")

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
