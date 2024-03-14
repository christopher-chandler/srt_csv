# SRT to CSV Converter

This script converts subtitle files in SRT (SubRip Text) format to CSV (Comma-Separated Values) format.

## Installation

No installation is required. Just ensure you have Python installed on your system.

## Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/christopher-chandler/srt_csv.git
   ```

2. **Navigate to the Directory**

   ```bash
   cd srt-to-csv-converter
   ```

3. **Run the Script**

   Execute the script using Python with the following command:

   ```bash
   python convert.py --file <filename_without_extension>
   ```

   Replace `<filename_without_extension>` with the name of the SRT file you want to convert.

4. **Output**

   The converted CSV file will be generated in the `data/outgoing` directory.

## Example

To convert a file named `example.srt`, run:

```bash
python convert.py --file example
```

## Options

- `--file`: Specifies the name of the SRT file to be converted.

## Dependencies

- **Standard Library**
  - `argparse`: For parsing command-line arguments.

- **Custom**
  - `srt_processor.convertor`: Module containing the conversion function.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

# Credits
This is based on the code https://stackoverflow.com/questions/53585676/creating-a-csv-file-from-an-srt-file-friends-subtitles-in-python
