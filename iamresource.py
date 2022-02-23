import boto3


awsconsole = boto3.session.Session(profile_name="root")
iamconsole = awsconsole.resource(service_name='iam', region_name="us-east-1")

for each in iamconsole.users.all():
    print(each.name)
