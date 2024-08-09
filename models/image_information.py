from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional

class ImageInformation(BaseModel):
    """Information about an image."""

    image_description: str = Field(description="a short description of the image")
    people_count: int = Field(description="number of humans on the picture")
    average_temp: float = Field(description="average temperature of the image")
    average_temp_description: str = Field(description="explaination of the average temperature calculation")
    country: Optional[str] = Field("", description="country where the picture was taken")
    main_objects: list[str] = Field(
        description="list of the main objects on the picture"
    )
