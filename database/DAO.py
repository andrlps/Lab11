from database.DB_connect import DBConnect
from model.arco import Arco
from model.product import Product


class DAO():
    @staticmethod
    def getColori():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)

        query = ("""select distinct gp.Product_color 
                    from go_products gp""")

        cursor.execute(query)

        result = []

        for row in cursor:
            result.append(row["Product_color"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(c):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = ("""select *
                    from go_products gp
                    where gp.Product_color = %s""")

        cursor.execute(query, (c,))

        result = []

        for row in cursor:
            result.append(Product(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(idP, y,c):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = ("""select t1.Product_number as a, t2.Product_number as b, count(*) as n
                    from (select gds.Product_number, gds.Retailer_code, gds.`Date` 
                    from go_products gp, go_daily_sales gds 
                    where gp.Product_number = gds.Product_number 
                    and gp.Product_color =%s
                    and year(gds.`Date`)=%s) t1,
                    (select gds.Product_number, gds.Retailer_code, gds.`Date` 
                    from go_products gp, go_daily_sales gds 
                    where gp.Product_number = gds.Product_number 
                    and gp.Product_color =%s
                    and year(gds.`Date`)=%s) t2
                    where t1.Retailer_code = t2.Retailer_code
                    and t1.`Date` = t2.`Date` 
                    and t1.Product_number <> t2.Product_number
                    group by t1.Product_number, t1.Retailer_code, t2.Product_number, t2.Retailer_code""")

        cursor.execute(query, (c,y,c,y,))

        result = []

        for row in cursor:
            result.append(Arco(idP[row["a"]], idP[row["b"]], row["n"]))

        cursor.close()
        conn.close()
        return result

if __name__ == '__main__':
    print(DAO.getColori())
    print(DAO.getAllNodes("Brown"))