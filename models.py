from tortoise.contrib.pydantic import pydantic_model_creator
import db_models

User_Pydantic = pydantic_model_creator(db_models.User, name="User")
UserIn_Pydantic = pydantic_model_creator(db_models.User, name="UserIn", exclude_readonly=True)