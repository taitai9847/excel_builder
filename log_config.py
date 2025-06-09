from datetime import datetime
import logging
import sys

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
                # 日時付きのログファイル名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"excel_builder_{timestamp}.log"
        
        # File ハンドラー
        log_path = "log/" + log_filename
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler) 
        
        # コンソール出力用ハンドラー
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)   
        
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger