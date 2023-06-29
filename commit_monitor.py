import time
from monitor import monitor

def read_poll_interval():
    # Read the polling interval from the conf/poll_interval_min file
    with open('conf/poll_interval_min', 'r') as file:
        interval = file.read().strip()
    interval = int(interval)
    if interval = None or interval < 1:
        interval = 5
    return interval

def main():
    # Read the polling interval
    poll_interval_min = read_poll_interval()

    # Loop indefinitely and run the monitoring process
    while True:
        # Call the monitor function
        monitor.monitor_repositories()

        # Wait for the specified polling interval
        time.sleep(poll_interval_min * 60)  # Convert minutes to seconds

if __name__ == '__main__':
    main()
