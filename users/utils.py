def jwt_payload_handler(user):
    return dict(uuid=str(user.uuid))


def get_username_from_payload_handler(payload):
    return payload.get('uuid')
