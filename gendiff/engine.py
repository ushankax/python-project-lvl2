import json


d = []


def diff_deeper(first_file, second_file):
    for first, second in zip(first_file.items(), first_file.items()):
        k1, v1 = first
        k2, v2 = second
        if k1 == k2 and isinstance(v1, dict) and isinstance(v2, dict):
            d.append('{{{}: '.format(k1))
            diff_deeper(v1, v2)
            d.append('}')
        else:
            d.append('{{+ {}: {}, - {}: {}}}'.format(k2, v2, k1, v1))

    return "".join(d)


def generate_diff(first_file, second_file):
    first_file = json.load(open('gendiff/files/before.json'))
    second_file = json.load(open('gendiff/files/after.json'))
    equal = first_file.keys() & second_file.keys()
    added = first_file.keys() - second_file.keys()
    deleted = second_file.keys() - first_file.keys()
    result = []

    result.append("{")

    for item in equal:
        if isinstance(first_file[item], dict) and isinstance(second_file[item], dict):
            result.append("  {}: {}".format(item, diff_deeper(first_file[item], second_file[item])))
        elif first_file[item] == second_file[item]:
            result.append("  {}: {}".format(item, first_file[item]))
        else:
            result.append("+ {}: {}".format(item, second_file[item]))
            result.append("- {}: {}".format(item, first_file[item]))

    for item in added:
        result.append("+ {}: {}".format(item, first_file[item]))

    for item in deleted:
        result.append("- {}: {}".format(item, second_file[item]))

    result.append("}")

    return "\n".join(result)
