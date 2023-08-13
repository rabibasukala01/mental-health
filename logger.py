import logging
import os


logging_path = os.path.join(os.getcwd(), "logs")


LOG_FILE = "log.txt"
os.makedirs(logging_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logging_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("This is a test log message")
