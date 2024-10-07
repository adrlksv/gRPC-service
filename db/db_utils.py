import psycopg2
import os


def connect_to_db():
    conn = psycopg2.connect(
        host="postgres",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    return conn


def insert_data(request):
    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            for i, data in enumerate(request.PacketData):
                cursor.execute(
                    """INSERT INTO grpc_data ("PacketSeqNum", "RecordSeqNum", "PacketTimestamp",
                    "Decimal1", "Decimal2", "Decimal3", "Decimal4", "RecordTimestamp") VALUES (%s, %s, %s, %s,
                    %s, %s, %s, %s)""",
                    (request.PacketSeqNum, i, request.PacketTimestamp, data.Decimal1, 
                    data.Decimal2, data.Decimal3, data.Decimal4, data.Timestamp)
                )

            conn.commit()
