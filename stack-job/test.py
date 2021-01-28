import paramiko
import boto3
from botocore.config import Config


ACCESS_KEY = "AKIATJB6EADHVJQCUVFJ"
SECRET_KEY = "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"
REGION = "eu-west-3"

my_config = Config(
    region_name = REGION,
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

ssm = boto3.client('ssm',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=my_config
    )

response = ssm.put_parameter(
    Name='AMI-ID',
    Value='sdqzdqxw<c',
    Type='String',
    Overwrite=True,
)

amiId = ssm.get_parameter(
    Name='AMI-ID',
)

print(result["Parameter"]["Value"])

deleteAmi = ssm.delete_parameter(
    Name='AMI-ID'
)
