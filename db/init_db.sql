CREATE TABLE IF NOT EXISTS grpc_data (
    PacketSeqNum BIGINT,
    RecordSeqNum BIGINT,
    PacketTimestamp BIGINT,
    Decimal1 DOUBLE PRECISION,
    Decimal2 DOUBLE PRECISION,
    Decimal3 DOUBLE PRECISION,
    Decimal4 DOUBLE PRECISION,
    RecordTimestamp BIGINT,
    PRIMARY KEY (PacketSeqNum, RecordSeqNum)
);
