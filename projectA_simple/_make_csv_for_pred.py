import os
import glob
import csv
import yaml


def do(target_dir):
    d = []
    out_csv = target_dir + '/pred.csv'
    for file in glob.glob(target_dir + '/*.yml'):
        file_name = os.path.basename(file)
        it_name = file_name.split('_')[0]
        y = yaml.safe_load(open(file, 'r'))
        score = y['pred']
        it = [it_name, score]
        d.append(it)
    w = csv.writer(open(out_csv, 'w', newline=''))
    w.writerows(d)


if __name__ == '__main__':
    target_dir = 'test_out_eu'
    do(target_dir)
