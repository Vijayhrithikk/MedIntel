from enum import Enum


class DocumentStatus(str, Enum):

    INDEXING = "INDEXING"

    READY = "READY"

    FAILED = "FAILED"