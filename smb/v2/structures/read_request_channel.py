from enum import IntEnum


class ReadRequestChannel(IntEnum):
    SMB2_CHANNEL_NONE = 0x00000000
    SMB2_CHANNEL_RDMA_V1 = 0x00000001
    SMB2_CHANNEL_RDMA_V1_INVALIDATE = 0x00000002