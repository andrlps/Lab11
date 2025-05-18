from database import DB_connect
from database.DB_connect import DBConnect
from model.edge import Edge
from model.product import Product


class DAO():
    @staticmethod
    def getColors():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct gp.Product_color
                    from go_products gp 
                    order by gp.Product_color asc"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row["Product_color"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getAllProducts(color):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                    from go_products gp 
                    where gp.Product_color = %s"""
        cursor.execute(query, (color,))
        result = []
        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def getAllEdges(color, year, ids):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select t.p1 as p1, t.p2 as p2, count(*) as weight
                    FROM 
                    (select distinct t1.Product_number as p1, t2.Product_number as p2, t1.`Date`
                    from
                    (select gds.Retailer_code, gds.Product_number, gds.`Date`
                    from go_daily_sales gds, go_products gp
                    where gds.Product_number = gp.Product_number
                    and gp.Product_color = %s
                    and YEAR(gds.`Date`) = %s) t1,
                    (select gds1.Retailer_code, gds1.Product_number, gds1.`Date`
                    from go_daily_sales gds1, go_products gp1
                    where gds1.Product_number = gp1.Product_number
                    and gp1.Product_color = %s
                    and YEAR(gds1.`Date`) = %s) t2
                    where t1.`Date` = t2.`Date`
                    and t1.Product_number < t2.Product_number
                    and t1.Retailer_code = t2.Retailer_code) t
                    group by t.p1,t.p2
                    order by weight desc"""
        cursor.execute(query, (color,year, color, year,))
        result = []
        for row in cursor:
            result.append(Edge(ids[row["p1"]], ids[row["p2"]], row["weight"]))
        cursor.close()
        cnx.close()
        return result

if __name__ == '__main__':
    print(DAO.getAllProducts("White"))

