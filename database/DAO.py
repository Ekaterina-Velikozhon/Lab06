from database.DB_connect import DBConnect
from model.sale import Sale


class DAO():
    @staticmethod
    def getYear() -> list[tuple[int]] | None:
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """SELECT DISTINCT YEAR(gds.Date)
        FROM go_daily_sales gds"""
        cursor.execute(query)

        res = cursor.fetchall()

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """SELECT DISTINCT gp.Product_brand
        FROM go_products gp"""
        cursor.execute(query)

        res = cursor.fetchall()

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getRetailer():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """SELECT DISTINCT gr.Retailer_name 
        FROM go_retailers gr """
        cursor.execute(query)

        res = cursor.fetchall()

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getTopSales(anno, brand, retailer_code):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT gds.*, gds.Unit_sale_price*gds.Quantity AS Ricavo
                FROM go_daily_sales gds, go_retailers gr, go_products gp 
                WHERE gds.Retailer_code  = gr.Retailer_code  
                AND gds.Product_number = gp.Product_number 
                AND (YEAR(gds.Date)=COALESCE(%s,YEAR(gds.Date)))
                AND (gp.Product_brand =COALESCE(%s,gp.Product_brand))
                AND (gr.Retailer_name =COALESCE(%s,gr.Retailer_name))
                ORDER BY Ricavo DESC"""
        cursor.execute(query, (anno, brand, retailer_code,))

        res = []

        for row in cursor:
            res.append(Sale(row["Date"], row["Quantity"], row["Unit_price"], row["Unit_sale_price"], row["Retailer_code"], row["Product_number"], row["Order_method_code"]))

        cursor.close()
        cnx.close()
        return res

if __name__ == '__main__':
    print(DAO.getTopSales(2016, None, None))

