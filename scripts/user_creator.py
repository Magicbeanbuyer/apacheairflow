from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
user = PasswordUser(models.User())
user.username = 'airflow'
# user.email = 'email'
user.password = 'airflow'
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()