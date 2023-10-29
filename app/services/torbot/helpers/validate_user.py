import os
from supabase import create_client, Client
from app.core.config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def validate_user(user_details):
    response = (
        supabase.table("users")
        .select("*")
        .eq("user_id", user_details.get("id"))
        .execute()
    )

    if bool(len(response.data)):
        return response.data[0].get("auth")
    else:
        onboard_user(user_details)
        return False


def onboard_user(user_details):
    del user_details["language_code"]
    del user_details["is_bot"]
    user_details["user_id"] = user_details.pop("id")
    supabase.table("users").insert(user_details).execute()
