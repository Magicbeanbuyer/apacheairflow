from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
import os

user = PasswordUser(models.User())
user.username = os.environ['AA_USERNAME']
user.email = os.environ['AA_EMAIL']
user.password = os.environ['AA_PASSWORD']
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()