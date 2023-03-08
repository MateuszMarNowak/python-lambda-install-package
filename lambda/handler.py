import json
import subprocess
import sys
import importlib

def load_event(event):
    package = json.loads(event["body"])
    return dict(
        name = package["name"],
        version = package["version"]
    )

def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', name])

def lambda_handler(event, context):
    package = load_event(event)
    name = package["name"]
    try:
        install(name)
        safe_name = name.replace("-", "_")
        # sys.path.insert(0, '/var/lang/lib/python3.9/site-packages/{}'.format(safe_name))
        package_name = importlib.import_module(safe_name).__name__
        return {
            "statusCode": 200,
            "body": json.dumps({
                "statusCode": 200,
                "body": package_name
            })
        }
    except:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "statusCode": 500,
                "body": "Install Failed"
            })
        }



