from string import Template
import argparse
import json

parser = argparse.ArgumentParser(description="testdesc")
parser.add_argument("--var-file", required=True, type=str, help="Path to the .tfvars.json file for the environment you want to deploy.")
args = parser.parse_args()

var_file = args.var_file

with open(var_file, "r") as f:
    tfvars = json.load(f)

params = {
    "bucket_name": tfvars["state_bucket"],
    "state_key"  : f'{tfvars["env"]}.tfstate',
    "region"     : tfvars["region"],
    "aws_profile": tfvars["aws_profile"]
}

with open('provider.tf.tmpl', 'r') as tmplFile:
    src = Template(tmplFile.read())
    result = src.substitute(params)

with open('provider.tf', 'w') as providerFile:
    providerFile.write(result)
