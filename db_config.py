import mysql.connector

def get_database_connection():

    connection=mysql.connector.connect(

        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="hkSgPdokE3G72VQ.root",
        password="50DmdR6GU7zU1Wf1",
        database="student_task_manager",
        port=4000

    )

    return connection