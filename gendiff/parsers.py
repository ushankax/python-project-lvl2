import argparse
from gendiff.engine import generate_diff


def parser():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", metavar="FORMAT",
                        help='see format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


def parse(before, after):
    file_name = os.path.basename("{}".format(before))
    file_format = os.path.splitext(file_name)[1]

    if file_format == ".json":
        old = json.load(open(before))
        new = json.load(open(after))
    elif file_format == ".yml":
        old = yaml.safe_load(open(before))
        new = yaml.safe_load(open(after))

    return old, new