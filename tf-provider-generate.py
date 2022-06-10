from string import Template

params = {
    "bucket_name": "REDACTED",
    "state_key"  : "test.tfstate",
    "region"     : "us-east-1",
    "aws_profile": "chrisdev_admin"
}

with open('provider.tf.tmpl', 'r') as tmplFile:
    src = Template(tmplFile.read())
    result = src.substitute(params)

with open('provider.tf', 'w') as providerFile:
    providerFile.write(result)
