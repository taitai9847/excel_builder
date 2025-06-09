import csv
import re
import config
import logging

logger = logging.getLogger("excel_builder")

def replace_placeholders(template_rows, value_map):
    replaced = []
    for row in template_rows:
        def replacer(match):
            key = match.group(1)
            return value_map.get(key, match.group(0))
        new_row = re.sub(r'\$\{(\w+)\}', replacer, row)
        replaced.append(new_row)
    return replaced

def load_template(row, input_template):
    replaced = []
    with open(input_template, encoding='utf-8') as f:
        input_template_rows = csv.reader(f)
        next(input_template_rows)
        for v in input_template_rows:
            new_row = replace_placeholders(v, row)
            replaced.append(new_row)
    return replaced

def get_input_template_header(input_template):
    header = []
    with open(input_template, encoding='utf-8') as f:
        input_template_rows = csv.reader(f)
        header = next(input_template_rows)
    return header

def write_to_csv(rows, header, input_csv):
    with open(input_csv, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

def create_input():
    res = []
    try:
        with open(config.INPUT_TEMPLATE_VALUE_FILE, encoding='utf-8') as f:
            reader = csv.reader(f)
            keys = next(reader)
            for row in reader:
                row = dict(zip(keys,row))
                row_list = load_template(row, config.INPUT_TEMPLATE_FILE)
                res.extend(row_list)
    except Exception as e:
        logger.error("処理中にエラーが発生しました")
        raise ValueError(e)
    
    header = get_input_template_header(config.INPUT_TEMPLATE_FILE)
    write_to_csv(res, header, config.INPUT_FILE)
    return