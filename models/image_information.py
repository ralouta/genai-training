from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional

class ImageInformation(BaseModel):
    """Information about an image."""

    title: str = Field(description="Title of the PDF document")
    image_description: str = Field(description="a short description of the image")
    point_measurements: list[int] = Field(description="list of the numbers of measurements in the map or graph or table")
    location_point_measurements: list[str] = Field(description="list of the locations of the measurements in the map or graph or table")
    point_measurements_description: str = Field(description="explaination of the point measurements")
    average_measurements: float = Field(description="average measurement of data in the image")
    average_measurements_description: str = Field(description="explaination of the average measurement calculation")
    country: Optional[str] = Field("", description="country where the picture was taken")
    main_objects: list[str] = Field(
        description="list of the main objects on the picture"
    )
