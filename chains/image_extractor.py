import json
import base64
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import JsonOutputParser
from models.image_information import ImageInformation


class ImageExtractChain:

    def __init__(self, model, image_path, output_model=ImageInformation):
        self.model = model
        self.output_model = output_model
        self.parser = JsonOutputParser(pydantic_object=self.output_model)
        self.local_image = self.load_image(image_path)
        self.image_content_type = self.get_image_file_type(image_path)

        self.vision_prompt = """
        Given the image, provide the following information:
        - A count of how many people are in the image
        - A list of the main objects present in the image
        - A description of the image
        """

        self.prompt_messages = self.collect_messages()

        self.chain = self.model | self.parser

    def collect_messages(self):
        return [
            HumanMessage(
                content=[
                    {"type": "text", "text": self.vision_prompt},
                    {
                        "type": "text",
                        "text": self.parser.get_format_instructions(),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/{self.image_content_type};base64,{self.local_image}"
                        },
                    },
                ]
            )
        ]

    def get_image_file_type(self, image_path):
        return image_path.split(".")[-1]

    def load_image(self, image_path) -> dict:
        """Load image from file and encode it as base64."""

        def encode_image(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")

        image_base64 = encode_image(image_path)

        return image_base64

    def extract_from_image(self):
        response = self.chain.invoke(self.prompt_messages)
        return self.output_model(**response)

    def format_for_attachment(self, image_information):
        prompt = """
        Given a JSON object that describes an image, summarize the information in English. 
        Do not mention the JSON object or its keys in your summary.
        Do not refer to the JSON object at all in your summary.
        Do not provide any other commentary or information.
        """
        messages = [
            ("system", prompt),
            (
                "human",
                f"Please summarize this JSON object: {image_information.json()}",
            ),
        ]

        response = self.model.invoke(messages)

        return response.content
