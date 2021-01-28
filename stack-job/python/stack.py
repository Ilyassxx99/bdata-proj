import boto3
import sys

def create_cloudformation_stack(stack,file,cloudformation):
    cf_template = open(file).read()
    response = cloudformation.create_stack(
        StackName=stack,
        TemplateBody=cf_template,
        Capabilities=[
            "CAPABILITY_NAMED_IAM",
        ],
        OnFailure="DO_NOTHING",
    )
    waiter = cloudformation.get_waiter("stack_create_complete")
    waiter.wait(StackName=stack, WaiterConfig={"Delay": 15, "MaxAttempts": 300})

def cloudformation_stack_exists(stack,cloudformation):
    exists = False
    response = cloudformation.list_stacks(
    StackStatusFilter=[
            'CREATE_COMPLETE',
            'CREATE_IN_PROGRESS',
            'CREATE_FAILED'
        ]
    )
    stacks =[]
    for i in range(len(response["StackSummaries"])):
        stacks.append(response["StackSummaries"][i]["StackName"])
    if stack in stacks:
        exists = True
    else:
        exists = False
    return exists

def delete_cloudformation_stack(ec2,client,stack,cloudformation):
    controllerReserv = client.describe_instances(
        Filters=[
        {
            'Name': 'tag:Type',
            'Values': [
                'Controller',
            ]
        },
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
        ],
    )
    if (len(controllerReserv['Reservations']) > 0):
        controllers = controllerReserv['Reservations'][0]['Instances']
        # Disable Api Termination for each controller
        if (len(controllers) > 0):
            for controller in controllers:
                ec2.Instance(controller["InstanceId"]).modify_attribute(
                DisableApiTermination={
                'Value': False
                })
    response = cloudformation.delete_stack(
        StackName=stack,
    )
    waiter = cloudformation.get_waiter("stack_delete_complete")
    waiter.wait(StackName=stack, WaiterConfig={"Delay": 15, "MaxAttempts": 300})
