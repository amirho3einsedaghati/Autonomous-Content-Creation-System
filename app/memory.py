from typing import Dict, Any
from pydantic import BaseModel


class ContentState(BaseModel):
    url: str = ""            # Provided by user (used as a query string; no network calls)
    content_type: str = ""   # "blog" | "newsletter" | "linkedin"
    final_content: str = ""  # Final generated content
    metadata: Dict[str, Any] = {}
