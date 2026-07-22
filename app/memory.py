from typing import Dict, Any
from pydantic import BaseModel


class ContentState(BaseModel):
    # User Inputs
    url: str = ""            # used as a query string
    content_type: str = ""   # "blog" | "newsletter" | "linkedin"
    
    # Final generated content
    final_content: str = ""  

    metadata: Dict[str, Any] = {}
