import paramiko
import boto3
from botocore.config import Config




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
