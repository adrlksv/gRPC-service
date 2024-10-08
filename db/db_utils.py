import psycopg2
import os


def connect_to_db():
    conn = psycopg2.connect(
        host=os.getenv("DATABASE_HOST", "localhost"),
        database=os.getenv("DATABASE_NAME", "grpc_data"),
        user=os.getenv("DATABASE_USER", "postgres"),
        password=os.getenv("DATABASE_PASSWORD", "postgres")
    )
    return conn


def insert_data(request):
    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            for i, data in enumerate(request.PacketData):
                cursor.execute(
                    """INSERT INTO grpc_data (packetseqnum, recordseqnum, packettimestamp,
                    decimal1, decimal2, decimal3, decimal4, recordTimestamp) VALUES (%s, %s, %s, %s,
                    %s, %s, %s, %s)""",
                    (request.PacketSeqNum, i, request.PacketTimestamp, data.Decimal1, 
                    data.Decimal2, data.Decimal3, data.Decimal4, data.Timestamp)
                )

            conn.commit()
