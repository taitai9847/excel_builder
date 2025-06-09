import sys
import config
from create_file_from_template import create_file_from_template
from create_input import create_input
from excel_builder import write_values_from_input
from log_config import setup_logger

logger = setup_logger("excel_builder")

def main():
    logger.info("excel_builder の処理を開始します")
            
    if len(sys.argv) == 2 and sys.argv[1] == 'template':
        try:
            logger.info(f"{config.INPUT_FILE} の作成を開始します")
            create_input()
            logger.info(f"{config.INPUT_FILE} が正常に作成されました")
            logger.info("excel_builder の処理を終了します")
        except Exception as e:
            logger.error(f"{config.INPUT_FILE} の作成処理中にエラーが発生しました: {e}")
            raise ValueError(e)
        return
    
    if len(sys.argv) == 2 and sys.argv[1] == 'file':
        try:
            logger.info("ファイルの作成処理を開始します")
            create_file_from_template()
            logger.info("ファイルの作成処理を終了します")
            logger.info("excel_builder の処理を終了します")
        except Exception as e:
            logger.error(f"ファイルの作成処理中にエラーが発生しました: {e}")
            raise ValueError(e)
        return
    
    if len(sys.argv) == 1:
        try:
            logger.info("対象ファイルに値の入力処理を開始します")
            write_values_from_input()
            logger.info("対象ファイルに値の入力処理を終了します")
            logger.info("excel_builder の処理を終了します")
        except Exception as e:
            logger.error(f"対象ファイルに値の入力処理中にエラーが発生しました: {e}")
            raise ValueError(e)
        return

    logger.error("Error: Invalid argument(s).")
    logger.info("excel_builder の処理を終了します")
    sys.exit(1)

if __name__ == '__main__':
    main()