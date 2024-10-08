import fitz  # PyMuPDF
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import JsonOutputParser
from models.pdf_information import PDFInformation


class PDFExtractChain:

    def __init__(self, model, pdf_path, output_model=PDFInformation):
        self.model = model
        self.output_model = output_model
        self.parser = JsonOutputParser(pydantic_object=output_model)
        self.pdf_text = self.extract_text_from_pdf(pdf_path)

        self.vision_prompt = """
        Given the following text extracted from a PDF, provide the following information in English:
        - Title of the PDF document
        - Author of the PDF document
        - Number of pages in the PDF document
        - Creation date of the PDF document
        - Last modification date of the PDF document
        - A short summary of the PDF document
        - List of the main topics covered in the PDF document
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
                        "type": "text",
                        "text": self.pdf_text,
                    },
                ]
            )
        ]

    def extract_text_from_pdf(self, pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        return text

    def extract_from_pdf(self):
        response = self.chain.invoke(self.prompt_messages)
        return self.output_model(**response)

    def format_for_attachment(self, pdf_information):
        prompt = """
        Given a JSON object that describes a PDF, summarize the information in English. 
        Do not mention the JSON object or its keys in your summary.
        Do not refer to the JSON object at all in your summary.
        Do not provide any other commentary or information.
        """
        messages = [
            ("system", prompt),
            (
                "human",
                f"Please summarize this JSON object: {pdf_information.json()}",
            ),
        ]

        response = self.model.invoke(messages)

        return response.content
