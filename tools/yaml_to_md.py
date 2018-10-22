import sys
from utils import read_feeds
from jinja2 import Environment, FileSystemLoader

if len(sys.argv)== 3:
    data_dir = sys.argv[1]
    output_file = sys.argv[2]

    entries=read_feeds(data_dir)

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('entry.md')
    output = template.render(entries = entries)

    with open(output_file, 'w') as f:
        f.write(output)
else:
    print("Usage:", sys.argv[0], "data-dir output-file")

