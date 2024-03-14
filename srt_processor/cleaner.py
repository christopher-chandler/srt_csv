# Standard
import re

# Pip
# None

# Custom
# None


def remove_quotation_characters_srt(
    incoming_file_name: str, outgoing_file_name: str
) -> None:
    """
    This function processes as srt (subtitle) file and creates a clean version of it.
    It removes the unwanted characters from the file and saves it as a new srt file.
    This is mostly meant for Japanese, but you can simply replace the chars to be replaced


    Args:
        incoming_file_name (str): The path name to the incoming file
        outgoing_file_name (str): The path name to the outgoing file
    """

    with open(
        incoming_file_name, mode="r", encoding="utf-8", newline=""
    ) as incoming_file:
        outgoing_file = open(outgoing_file_name, mode="w+", encoding="utf-8")
        for line in incoming_file:
            char_sub = re.sub("[➡＜＞＜≪《》♬～]", "", line)
            string = re.sub("\(.*?\)", "", char_sub)
            outgoing_file.write(string)

    return None
