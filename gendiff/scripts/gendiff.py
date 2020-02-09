import argparse


parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument("-f","--function", metavar="FORMAT", help='see format of output')


def main():
    parser.print_help()


if __name__ == '__main__':
    main()
