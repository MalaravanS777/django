from django.db import models,connection

# Create your models here.
class credentials(models.Model):
    email=models.EmailField(max_length=50,unique=True)
    passw=models.CharField(max_length=50)

    class meta:
        db_table='Credentials'
class create_table:
    @staticmethod
    def create(tb):
        class Meta:
            db_table=tb
        fields={'task':models.CharField(max_length=200)}
        attrs={'__module__':__name__,'Meta':Meta}
        attrs.update(fields)
        user_task=type(tb,(models.Model,),attrs)
        with connection.schema_editor() as se:
            se.create_model(user_task)
        return
def fetch_rows(tb): 
    with connection.cursor() as cursor:
        cursor.execute(f"select * from {tb}")
        row=cursor.fetchall()
        return row
def insert_task(tb,values):
    with connection.cursor() as cursor:
        cursor.execute(f"select count(*) from {tb} where task=%s",[values])
        if cursor.fetchone()[0]==0:
            cursor.execute(f"insert into {tb} (task) values(%s)",[values])
    return
def delete_task(tb,id):
    with connection.cursor() as cursor:
        cursor.execute(f"delete from {tb} where id=%s",[id])
    return

def update_task(tb,id,task):
    with connection.cursor() as cursor:
        cursor.execute(f"update {tb} set task=%s where id=%s",[task,id])
    return