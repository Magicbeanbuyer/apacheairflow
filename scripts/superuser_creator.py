from airflow import models, settings

session = settings.Session()
users = session.query(models.User).all()  # [admin, regular_user]

# users[1].superuser  # False

admin = users[0]
admin.superuser = True
session.add(admin)
session.commit()