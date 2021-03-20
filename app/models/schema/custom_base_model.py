from pydantic import BaseModel


class CamelCaseBaseModel(BaseModel):

	class Config:
		allow_population_by_field_name = True

		@classmethod
		def alias_generator(cls, string: str) -> str:
			return ''.join(
				word.capitalize() if i else word
				for i, word in enumerate(string.split('_'))
			)
