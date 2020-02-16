import json


def generate_diff(first_file, second_file):
    first_file = json.load(open('gendiff/files/before.json'))
    second_file =json.load(open('gendiff/files/after.json'))
    d = {}

    for item in first_file.keys():
        if item in second_file.keys():
            if first_file[item] == second_file[item]:
                d["{}".format(item)] = first_file[item]
            else:
                d["+ {}".format(item)] = first_file[item]
                d["- {}".format(item)] = second_file[item]
        elif item not in second_file.keys():
            d["+ {}".format(item)] = first_file[item]
    
    da = json.dumps(d, indent=4)

    return da
