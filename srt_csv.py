import argparse
import csv
import re

my_parser = argparse.ArgumentParser(description="CSV to SRT")

my_parser.add_argument("--f", "--file", type=str, help="the path to the file that should be converted")

args = my_parser.parse_args()


def convert_file(file):
    with open(file, "r") as h:
        sub = h.readlines()

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

    # Merge results
    subs = {start_time: line for start_time, line in zip(start_times, lines)}
    episode_name = file.replace(".srt","")

    with open(f"{episode_name}.csv", mode="w+", encoding="utf-8") as save_file:
        csv_writer = csv.writer(save_file)
        csv_writer.writerow(("Time","Text","Show Information"))
        for key, value in subs.items():
            flat_value = " ".join(value).replace("\n","").replace("➡ ","")
            print(key, flat_value )
            csv_writer.writerow((key, flat_value,episode_name))


if __name__ == "__main__":
    convert_file(input("File name: "))