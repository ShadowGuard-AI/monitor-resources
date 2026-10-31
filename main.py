import psutil
import argparse
import logging
import sys
from logging.handlers import RotatingFileHandler

LOG_MAX_BYTES = 1024 * 1024
LOG_BACKUP_COUNT = 3

# Configure console logging only. The log file handler is created when
# monitoring starts, so importing this module or running --help creates
# no log file.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

def setup_argparse():
    """
    Set up command-line argument parsing.
    """
    parser = argparse.ArgumentParser(
        description="Monitor system resources (CPU, memory, disk) and log usage details."
    )
    parser.add_argument(
        '--interval', type=int, default=5,
        help="Time interval (in seconds) between resource checks. Default is 5 seconds."
    )
    parser.add_argument(
        '--threshold', type=int, default=90,
        help="Threshold (in percentage) for alerts. Default is 90 percent."
    )
    return parser.parse_args()

def monitor_resources(interval, threshold):
    """
    Monitor system resources and log them periodically.
    """
    file_handler = RotatingFileHandler(
        "monitor_resources.log", maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT
    )
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(file_handler)
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=interval)
            memory_usage = psutil.virtual_memory().percent

            logging.info(f"CPU Usage: {cpu_usage}%")
            logging.info(f"Memory Usage: {memory_usage}%")

            if cpu_usage > threshold:
                logging.warning(f"CPU usage exceeds threshold: {cpu_usage}%")
            if memory_usage > threshold:
                logging.warning(f"Memory usage exceeds threshold: {memory_usage}%")
            for partition in psutil.disk_partitions():
                disk_usage = psutil.disk_usage(partition.mountpoint).percent
                logging.info(f"Disk Usage ({partition.mountpoint}): {disk_usage}%")
                if disk_usage > threshold:
                    logging.warning(f"Disk usage on {partition.mountpoint} exceeds threshold: {disk_usage}%")
    except KeyboardInterrupt:
        logging.info("Resource monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to initialize and run the resource monitoring tool.
    """
    args = setup_argparse()
    if args.interval <= 0:
        logging.error("Interval must be a positive number of seconds.")
        sys.exit(1)
    if args.threshold < 0 or args.threshold > 100:
        logging.error("Threshold must be between 0 and 100.")
        sys.exit(1)
    monitor_resources(args.interval, args.threshold)

if __name__ == "__main__":
    main()