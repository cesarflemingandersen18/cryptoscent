import matplotlib.pyplot as plt

def plot_activity(hourly_data, weekday_data):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    hourly_data.sort_index().plot(kind='bar')
    plt.title("Hourly Activity Pattern")
    plt.xlabel("Hour of Day")
    plt.ylabel("Tx Count")

    plt.subplot(1, 2, 2)
    weekday_data.sort_index().plot(kind='bar', color='orange')
    plt.title("Weekday Activity Pattern")
    plt.xlabel("Day of Week (0=Mon)")
    plt.ylabel("Tx Count")

    plt.tight_layout()
    plt.show()
