import os
import yaml
from jinja2 import Environment, FileSystemLoader

with open("input.txt") as file:
    # list comprehension to add lines into the list called "lines" if the line, when stripped, does not have a length of
    # 0, this was meant to remove '' entries in the list
    lines = [line.strip() for line in file if len(line.strip()) != 0]
    words = []
    # split line of text by single space
    for line in lines:
        words.append(line.split(" "))

    cleaned_words = []
    # cleans up "words" list by taking out '' characters
    for word_list in words:
        temp_list = []
        for item in word_list:
            if len(item) != 0:
                temp_list.append(item.lower())

        cleaned_words.append(temp_list)

# Defines basic structure of dictionary
template_info = {
    "records": [

    ]
}

# adds each list item in the cleaned_words list as a dictionary item in the template_info["records"] list
for list in cleaned_words:
    record_type = list[0]
    fqdn = list[1]
    ip = list[2]
    template_info["records"].append(
        {
            "fqdn": fqdn,
            "ip": ip,
            "record_type": record_type
        })

# dumps dictionary made above into a yaml file
with open("output.yaml", "w") as file:
    yaml.dump(template_info, file)
    # sets jinja parameters for input file, template file, and output file
    yaml_file = "output.yaml"
    template_file = "dns_removal.j2"
    output_file = "output.txt"

    with open(f"{yaml_file}") as file:
        file = yaml.load(file, Loader=yaml.Loader)

    env = Environment(loader=FileSystemLoader(""))
    template = env.get_template(template_file)

    content = template.render(file)

    with open(f"{output_file}", "w") as output:
        output.write(content)

os.startfile("output.txt")