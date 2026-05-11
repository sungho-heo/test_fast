import enum

class DocumentStatus(str, enum.Enum):
    uploaded = "uploaded"
    parsing = "parsing"
    summarizing = "summarizing"
    done = "done"
    failed = "failed"