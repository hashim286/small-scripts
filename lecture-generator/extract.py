from text import RawText
import re as re

raw_text = RawText()


class Extract:
    def extraction(self):
        self.filtered_text = re.findall('[0-9]+\.\s.+', raw_text.text)









