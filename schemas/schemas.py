post_users = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        }
    },
    "required": [
        "name",
        "job",
        "id",
        "createdAt"
    ]
}

list_users = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "page": {
            "type": "integer"
        },
        "per_page": {
            "type": "integer"
        },
        "total": {
            "type": "integer"
        },
        "total_pages": {
            "type": "integer"
        },
        "data": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "avatar": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "email",
                        "first_name",
                        "last_name",
                        "avatar"
                    ]
                }
            ]
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                }
            },
            "required": [
                "url",
                "text"
            ]
        }
    },
    "required": [
        "page",
        "per_page",
        "total",
        "total_pages",
        "data",
        "support"
    ]
}

update_users = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "job": {
      "type": "string"
    },
    "updatedAt": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "job",
    "updatedAt"
  ]
}

error_register = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  },
  "required": [
    "error"
  ]
}

successful_registr = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "token": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "token"
  ]
}