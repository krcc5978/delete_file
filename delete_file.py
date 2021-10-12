import os
import re
import shutil
import argparse

parser = argparse.ArgumentParser(description='ファイル、ディレクトリ削除')
parser.add_argument('--target', help='対象ディレクトリ', required=True)
parser.add_argument('--delete_pattern', help='削除文字列', default='.*', type=str)
parser.add_argument('--not_delete_pattern', help='非削除文字列', default='', type=str)
parser.add_argument('--delete', help='削除フラグ', action='store_true')
parser.add_argument('--check', help='確認ファイル出力フラグ', action='store_true')
args = parser.parse_args()

file = open('delete_file_name.txt', 'w')


def delete_dir_list(path):
    files = os.listdir(path)
    files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
    for i in files_dir:
        if re.fullmatch(args.delete_pattern, i):
            print('\\'.join([path, i]))
            if args.check:
                file.write('\\'.join([path, i]) + '\n')
            if args.delete:
                shutil.rmtree('\\'.join([path, i]))
        elif re.fullmatch(args.not_delete_pattern, i):
            continue
        else:
            delete_dir_list('\\'.join([path, i]))


def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        delete_dir_list(path)
    else:
        print('no such file or dir')


if __name__ == '__main__':
    delete_file(args.target)
