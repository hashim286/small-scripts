from extract import Extract

extract = Extract()

extract.extraction()

class LectureMaker:

    def lectures(self):
        for i in extract.filtered_text:
            print(i)