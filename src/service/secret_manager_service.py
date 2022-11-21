import base64
import json

import boto3


class SecretManagerService(object):

    def __init__(self, profile_name=None):
        self.__session = boto3.session.Session(profile_name=profile_name)
        self.sm_client = self.__session.client("secretsmanager")

    def get_secrets(self, name):
        response = self.sm_client.get_secret_value(SecretId=name)
        if "SecretString" in response:
            secret = response["SecretString"]
        else:
            secret = base64.b64decode(response["SecretBinary"])
        return json.loads(secret)



