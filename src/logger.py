import os
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%H-%M-%S-%d-%m-%Y')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format='[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has been set up.")