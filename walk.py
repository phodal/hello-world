# -*- coding: utf-8 -*-
import json
import os
import os.path


def generate_json(dir_name, files_name):
    data = []
    index = 0
    for file in files_name:
        language_info = {'language': file, 'id': index}
        data.append(language_info)
        index += 1

    with open('data/' + dir_name + '.json', 'w') as outfile:
        json.dump(data, outfile)

for directory in ['lv1', 'lv2', 'lv3', 'lv4']:
    for root, dirs, files in os.walk(directory):
        generate_json(directory, files)