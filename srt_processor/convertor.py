# Standard
import csv
import os
import re

# Pip
# None

# Custom
# None


def convert_file(file: str):
    """
    Convert subtitle file (.srt) to CSV format.

    :param file: Name of the subtitle file (without extension).
    """
    # Path to the input subtitle file
    incoming = os.path.join(os.getcwd(), "data", "incoming", f"{file}.srt")

    # Read lines from the subtitle file
    with open(incoming, "r") as h:
        sub = h.readlines()

    # Regular expression pattern to match time stamps
    re_pattern = r"[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3} -->"
    regex = re.compile(re_pattern)

    # Get start times
    start_times = list(filter(regex.search, sub))
    start_times = [time.split(" ")[0] for time in start_times]

    # Get lines
    lines = [[]]
    for sentence in sub:
        if re.match(re_pattern, sentence):
            lines[-1].pop()
            lines.append([])
        else:
            lines[-1].append(sentence)
    lines = lines[1:]

    # Merge start times and lines into a dictionary
    subs = {start_time: line for start_time, line in zip(start_times, lines)}

    # Extract episode name from the file name
    episode_name = file.replace(".srt", "")

    # Path to the output CSV file
    outgoing = os.path.join(os.getcwd(), "data", "outgoing", f"{episode_name}.csv")

    # Write subtitles to the CSV file
    with open(outgoing, mode="w+", encoding="utf-8") as save_file:
        csv_writer = csv.writer(save_file)
        csv_writer.writerow(("Time", "Text", "Show Information"))  # Write header row
        for key, value in subs.items():
            flat_value = (
                " ".join(value).replace("\n", "").replace("➡ ", "")
            )  # Flatten lines
            csv_writer.writerow((key, flat_value, episode_name))  # Write data row


if __name__ == "__main__":
    pass
