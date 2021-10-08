import os
import shutil
import argparse

parser = argparse.ArgumentParser(description='ファイル、ディレクトリ削除')

parser.add_argument('--d', '--delete', help='削除パス', required=True)
args = parser.parse_args()


def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        print('no such file or dir')


if __name__ == '__main__':
    delete_file(args.d)
