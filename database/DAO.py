from database.DB_connect import DBConnect
from model.artista import Artista


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getGenere():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select g.name
                from genre g """

        cursor.execute(query)

        for row in cursor:
            result.append(row["name"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArtistiGenere(genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(a.Name),a.ArtistId 
                from track t , genre g ,artist a 
                where t.GenreId =%s and t.Composer =a.Name"""

        cursor.execute(query,(genere,))

        for row in cursor:
            result.append(Artista(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct a2.ArtistId as Id1,a3.ArtistId as Id2
        from invoice i ,invoiceline il ,track t ,album a ,artist a2,invoice i2 ,invoiceline il2 ,track t2 ,album a4 ,artist a3 
        where i.InvoiceId =il.InvoiceId and il.TrackId =t.TrackId and t.AlbumId =a.AlbumId and a.ArtistId =a2.ArtistId 
		and i2.InvoiceId =il2.InvoiceId and il2.TrackId =t2.TrackId and t2.AlbumId =a4.AlbumId and a4.ArtistId =a3.ArtistId
	    and a2.ArtistId>a3.ArtistId"""
        cursor.execute(query)

        for row in cursor:
            result.append((row["Id1"], row["Id2"]))

        cursor.close()
        conn.close()
        return result
    #hfjsdk


