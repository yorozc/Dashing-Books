from database.db import user_coll
from models.user import User, UserWithID, UserUpdate
from bson import ObjectId
from fastapi import HTTPException
from bson import ObjectId
from pymongo import ReturnDocument
 
 # TODO: add error stuff
class UserService():
    def __init__():
        pass

    def create_user(user: User):
        result = user_coll.insert_one(user.model_dump(exclude_none=True))
        user_response = UserWithID(id=str(result.inserted_id), **user.model_dump())
        return user_response

    def get_user(user_id: str) -> UserWithID:
        result = user_coll.find_one({"_id": ObjectId(user_id)})
        result["id"] = str(result["_id"])
        del result["_id"]
        return UserWithID(**result)

    def edit_user(user_id: str, user: UserUpdate):
        updated_data = user.model_dump(exclude_unset=True)
        updated_result = user_coll.find_one_and_update({"_id": ObjectId(user_id)}, 
                                                       {"$set": updated_data},
                                                       return_document=ReturnDocument.AFTER)
        return User(**updated_result)

    def delete_user(user_id: str):
        return user_coll.find_one_and_delete({"_id": ObjectId(user_id)})