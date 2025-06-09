import csv
import logging
import shutil
import config

logger = logging.getLogger("excel_builder")

def create_file_from_template():
    with open(config.INPUT_FILE, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        created_files = set()
        for v in reader:
            file_name = v[0]
            if file_name in created_files:
                continue
            output_path = "output/" + file_name
            shutil.copy(config.BASE_EXCEL_FILE, output_path)
            created_files.add(file_name)
            logger.info(f"{file_name} が正常に作成されました")
    return