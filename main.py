import psutil
import argparse
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("monitor_resources.log"),
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
        help="Threshold (in percentage) for alerts. Default is 90%."
    )
    return parser.parse_args()

def monitor_resources(interval, threshold):
    """
    Monitor system resources and log them periodically.
    """
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=interval)
            memory_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage('/').percent

            logging.info(f"CPU Usage: {cpu_usage}%")
            logging.info(f"Memory Usage: {memory_usage}%")
            logging.info(f"Disk Usage: {disk_usage}%")

            if cpu_usage > threshold:
                logging.warning(f"CPU usage exceeds threshold: {cpu_usage}%")
            if memory_usage > threshold:
                logging.warning(f"Memory usage exceeds threshold: {memory_usage}%")
            if disk_usage > threshold:
                logging.warning(f"Disk usage exceeds threshold: {disk_usage}%")
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
    monitor_resources(args.interval, args.threshold)

if __name__ == "__main__":
    main()