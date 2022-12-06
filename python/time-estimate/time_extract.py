import re as re


class Extraction:

    def __init__(self):
        self.times = []
        self.total = 0
        with open("text.txt") as file:
            self.text = file.read()

    def extract_times(self):
        # \\d pulls out digits in the text self.input, the + is meant to specify more than one digit if any exist, 
        # repeat this for the other side of the colon in timestamps
        self.times = re.findall('\\d+:\\d+', self.text)

    def separate_mins_from_seconds(self):
        for item in self.times:
            times_separated = item.split(':')
            seconds = int(times_separated[1])/60
            minutes = float(times_separated[0])
            self.total += round(seconds + minutes, 2)

    def convert_to_hours_and_minutes(self):
        convert = int(self.total)
        hours = int(convert/60)
        minutes = convert % 60
        print(f"This section should take {hours} hour(s) and {minutes} minute(s) to finish")
