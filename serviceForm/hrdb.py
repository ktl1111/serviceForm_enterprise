from django.db import connections

def User():

    rs = []

    cursor = connections['hrm7_cyhc'].cursor()
    cursor.execute("SELECT EMPID FROM db.HRUSER WHERE EMPID = '010107';")
    zones = cursor.fetchall()

    for v in zones[::]:
        rs.append(v)



# select * from dbo.HRUSER_DEPT_BAS where DEP_NAME LIKE '%醫用技術部%'