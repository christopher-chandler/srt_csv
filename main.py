# Standard
import argparse

# Pip
# None

# Custom
from srt_processor.convertor import convert_file

my_parser = argparse.ArgumentParser(description="Convert SRT to CSV>")

my_parser.add_argument(
    "--f", "--file", type=str, help="the name of the file that should be converted."
)

args = my_parser.parse_args()


if __name__ == "__main__":
    convert_file(args.f)
