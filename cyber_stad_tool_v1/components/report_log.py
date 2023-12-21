import psutil
import time

def print_background_processes(duration=30):
    end_time = time.time() + duration

    print("PID  |  Process Name  |  Status  |  CPU Usage (%)  |  Memory Usage (MB)")
    print("-" * 70)

    while time.time() < end_time:
        for process in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_info']):
            try:
                pid = process.info['pid']
                name = process.info['name']
                status = process.info['status']
                cpu_percent = process.info['cpu_percent']
                memory_info = process.info['memory_info']

                print(f"{pid:5} | {name:15} | {status:7} | {cpu_percent:15.2f} | {memory_info.rss / (1024 ** 2):15.2f}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        time.sleep(1)  # Sleep for 1 second between iterations

def start_log():
    print_background_processes(duration=10)
