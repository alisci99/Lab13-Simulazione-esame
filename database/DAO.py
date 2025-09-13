from database.DB_connect import DBConnect
from model.driver import Driver


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def get_years():
        cnx = DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        result=[]
        query="""select distinct year
                    from seasons
                    order by year asc"""

        cursor.execute(query)
        for row in cursor:
            result.append(row['year'])

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_nodes(anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        result = []
        query = """select distinct d.driverId as driverID , d.forename as name , d.surname as surname
                    from races ry, drivers d, results re
                    where  ry.`year` =%s
                    and ry.raceId = re.raceId
                    and re.driverId =d.driverId
                    and re.`position` is not null"""

        cursor.execute(query,(anno,))
        for row in cursor:
            result.append(Driver(**row))

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getDriverYearResults(anno,_idMapPiloti):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)
        result = []
        query ="""select r1.driverId as d1, r2.driverId as d2, count(*) as cnt
				from results as r1, results as r2, races
				where r1.raceId = r2.raceId
				and races.raceId = r1.raceId
				and races.year = %s
				and r1.position is not null
				and r2.position is not null 
				and r1.position < r2.position 
				group by d1, d2"""

        cursor.execute(query, (anno,))
        for row in cursor:
            result.append((_idMapPiloti[row["d1"]],_idMapPiloti[row["d2"]],row["cnt"]))

        cursor.close()
        cnx.close()
        return result

