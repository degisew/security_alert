import json
import avro


avro_schema = {
  "type": "record",
  "name": "userInfo",
  "fields": [
    {"name": "userIP", "type": "string"},
    { "name": 'uid', "type": 'string' },
    {"name": "timestamp", "type": "string"},
    {"name": "email", "type": "string"},
    {
      "name": "location",
      "type":{
        "name": "Location",
        "type": "record",
        "fields": [
          {"name": "city", "type": "string"},
          {"name": "country", "type": "string"}
        ],
      }
    },
    {
      "name": "deviceInfo",
      "type": {
        "type": "record",
        "name": "DeviceInfo",
        "fields": [
          {"name": "browser", "type": "string"},
          {"name": "browserVersion", "type": "string"},
          {"name": "OS", "type": "string"},
          {"name": "platform", "type": "string"},
          {"name": "source", "type": "string"}
        ]
      }
    }
  ]
}

parsed_schema = avro.schema.parse(json.dumps(avro_schema))
# print("############", parsed_schema, type(parsed_schema))
