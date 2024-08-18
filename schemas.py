from pydantic import BaseModel

class TranslationRequestSchema(BaseModel):
    text: str
    languages: str

    class Config:
        schema_extra = {
            "example": {
                "text": "Hello, world!",
                "languages": "english, german, russian , spanish"
            }
        }