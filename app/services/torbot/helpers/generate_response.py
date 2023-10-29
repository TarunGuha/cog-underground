def categorize_message(data):
    if bool(data.message):
        return "main"

    else:
        choice = data.callback_query.get("data").split("_")[0]
        return choice


def generate_response(auth, data):
    category = categorize_message(data)