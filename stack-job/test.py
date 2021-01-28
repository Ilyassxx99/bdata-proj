import paramiko
import boto3
from botocore.config import Config




my_config = Config(
    region_name = "eu-west-3",
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)



response = cfd.list_stacks(
StackStatusFilter=[
        'CREATE_COMPLETE',
        'CREATE_IN_PROGRESS'
    ]
)
stacks =[]
print(response)
for i in range(len(response["StackSummaries"])):
    stacks.append(response["StackSummaries"][i]["StackName"])
print(stacks)
print(len(response["StackSummaries"]))
if len(response["StackSummaries"]) == 0:
    print("Empty")
else:
    print("Not Empty")

print(not True)
