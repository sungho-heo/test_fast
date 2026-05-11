from sqlalchemy import (
    Column, 
    String, 
    Enum,
    Text,
    DateTime
)
from datetime import datetime
import uuid
from db.base import Base
from status_enum import DocumentStatus 

class Document(Base):
    
    __tablename__ = "documents"
    # uuid id값 들어감.
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    filename = Column(String)
    stored_path = Column(String)
    file_type = Column(String)
    status = Column(Enum(DocumentStatus), default=DocumentStatus.uploaded)
    
    summary = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)