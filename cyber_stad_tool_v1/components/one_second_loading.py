import sys
import time

def loading_animation_for_reconnaissance_feature(duration=1, content=None):
    chars = "/—\\|"
    interval = 0.1  # Adjust the interval as needed
    iterations = int(duration / (len(chars) * interval))

    for _ in range(iterations):
        for char in chars:
            sys.stdout.write(f"\r[*] {content} {char}")
            sys.stdout.flush()
            time.sleep(interval)
    print("\n\n")

# Example usage
# loading_animation(1)
# print("\nLoading complete!")
