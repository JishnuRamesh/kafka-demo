class KafkaError(Exception):
    pass


class KafkaDeserializationError(KafkaError):
    def __init__(self, error_msg, raw_message, topic):
        self.error_msg = error_msg
        self.raw_message = raw_message
        self.topic = topic


class KafkaMessageError(KafkaError):
    pass


class KafkaMsgProcessorError(KafkaError):
    def __init__(self, error_msg, deserialized_msg, topic, schema_id, schema_name):
        self.error_msg = error_msg
        self.deserialized_msg = deserialized_msg
        self.topic = (topic,)
        self.schema_id = (schema_id,)
        self.schema_name = schema_name


class KafkaEncodeMsgError(KafkaError):
    def __init__(self, error_msg, raw_msg, topic):
        self.error_msg = error_msg
        self.raw_msg = raw_msg
        self.topic = topic


class KafkaProduceError(KafkaError):
    def __init__(self, error_msg, raw_msg, msg_key, encoded_msg, topic):
        self.error_msg = error_msg
        self.raw_msg = raw_msg
        self.msg_key = msg_key
        self.encoded_msg = encoded_msg
        self.topic = topic