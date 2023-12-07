import sys
import time

def loading_animation(duration=1):
    chars = "/—\\|"
    interval = 0.1  # Adjust the interval as needed
    iterations = int(duration / (len(chars) * interval))

    for _ in range(iterations):
        for char in chars:
            sys.stdout.write(f"\r[*] Opening tool {char}")
            sys.stdout.flush()
            time.sleep(interval)

# Example usage
# loading_animation(1)
# print("\nLoading complete!")
