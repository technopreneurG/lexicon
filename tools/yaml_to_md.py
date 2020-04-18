import sys
from utils.feed import *
from jinja2 import Environment, FileSystemLoader
import argparse
import yaml
import os.path

parser = argparse.ArgumentParser()

# Usage: yaml_to_md.py -d data-dir -o output -m true/false -t readme/mkdocs
#  data-dir: is where the yaml files with lexicons are placed
#  output-file: the markdown file in which to write the contents

parser.add_argument("-d", "--data_dir", help="process the yaml files from data dir", required=True)
parser.add_argument("-o", "--output", help="output file OR dir if multi is enabled", required=True)
parser.add_argument("-m", "--multi", help="generate multiple or single files, default: False", type=bool, default=False, choices=[True, False])
parser.add_argument("-t", "--output_type", help="output type [readme, mkdocs]", default="mkdocs")

args = parser.parse_args()
if not args.data_dir:
  raise Exception("data directory is needed")
if not args.output:
  raise Exception("output file/dir is needed")

data_dir = args.data_dir
output = args.output
output_type= args.output_type
multi = args.multi


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


if multi:
  #TODO
  print('TODO')
else:
  lexicon=False
  if os.path.isfile(data_dir+"_lexicon.yaml"):
    lexicon = yaml.load(open(data_dir+"_lexicon.yaml", 'r'), Loader=yaml.FullLoader)
    print(lexicon)

  entries=read_feeds(data_dir)
  template = env.get_template('entry.md')
  content = template.render(entries = entries, lexicon=lexicon, output_type=output_type)
  output_file = output

  with open(output_file, 'w') as f:
    f.write(content)

