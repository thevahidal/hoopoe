import json


def generate_telegram_message(organization, context):
    return f"""
{context.get('timestamp')}

{context.get('message')}
{json.dumps(context.get('extra'), indent=4, sort_keys=True, ensure_ascii=False)}
"""
