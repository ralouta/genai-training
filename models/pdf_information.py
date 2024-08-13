from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional, List, Dict

class GraphAttributes(BaseModel):
    """Attributes of a graph in the PDF document."""
    title: str = Field(description="Title of the graph")
    page_number: int = Field(description="Page number where the graph is located")
    description: Optional[str] = Field("", description="Description of the graph")

class PDFInformation(BaseModel):
    """Information about a PDF document."""

    title: str = Field(description="Title of the PDF document")
    author: Optional[str] = Field("", description="Author of the PDF document")
    number_of_pages: int = Field(description="Number of pages in the PDF document")
    number_of_graphs: int = Field(description="Number of graphs in the PDF document")
    graphs: Dict[str, GraphAttributes] = Field(description="Graphs in the PDF document")
    creation_date: Optional[str] = Field("", description="Creation date of the PDF document")
    modification_date: Optional[str] = Field("", description="Last modification date of the PDF document")
    keywords: List[str] = Field(description="List of keywords associated with the PDF document")
    summary: str = Field(description="A short summary of the PDF document")
    main_topics: List[str] = Field(description="List of the main topics covered in the PDF document")