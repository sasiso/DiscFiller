import argparse

if __name__ == '__main__':
    argument_Parser = argparse.ArgumentParser(description='Disc Filler')
    argument_Parser.add_argument('num_files', help='num_files')
    argument_Parser.add_argument('size_of_file', help='size_of_file')
    args = argument_Parser.parse_args()
    num_files = 0
    size_of_file = 0

    num_files = int(args.num_files)
    size_of_file = int(args.size_of_file)

    for i in range(num_files):
        name = 'f-' + str(i)
        with open('f-' + str(i), "wb") as f:
            f.seek(size_of_file - 1)
            f.write("\0")
            f.close()
            import os
            os.stat(name).st_size
