import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ml-validation-service")

def main():
    logger.info("Service ml-validation-service starting...")
    while True:
        logger.info("Service ml-validation-service is running...")
        time.sleep(60)

if __name__ == "__main__":
    main()
