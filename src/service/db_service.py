
from mysql.connector import connect

from src.service.secret_manager_service import SecretManagerService


class DBService:

    def __init__(self):
        self.schema = None
        self.port = None
        self.host = None
        self.username = None
        self.password = None
        self.database = None
        self.ssm = SecretManagerService(profile_name=None)

    def setup_credentials(self, secret):
        credentials = self.ssm.get_secrets(secret)
        print(credentials)
        self.port = credentials["port"]
        ''' use local host when connecting from local using bastion host'''
        self.host = "localhost"
        #self.host = credentials["host"]
        self.username = credentials["username"]
        self.password = credentials["password"]
        self.database = credentials["database"]

    def get_db_connection(self, secret=None):
        if secret is None:
            raise ValueError("Missing secret name")
        self.setup_credentials(secret)
        return connect(host=self.host,
                       database=self.database,
                       user=self.username,
                       password=self.password)





db = DBService()
conn = db.get_db_connection(secret="tpadmin")
print(conn)