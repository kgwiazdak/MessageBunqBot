tools = [
    {
        "type": "function",
        "function": {
            "name": "get_last_transactions",
            "description": "Fetches the user's most recent bank transactions",
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer",
                        "description": "Number of transactions to return",
                        "default": 5
                    }
                },
                "required": ["limit"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "pay",
            "description": "Send an instant payment to a specific alias with amount and optional description.",
            "parameters": {
                "type": "object",
                "properties": {
                    "receiver_alias_name": {
                        "type": "string",
                        "description": "The type of alias, e.g., 'PHONE_NUMBER' or 'EMAIL'."
                    },
                    "receiver_alias_value": {
                        "type": "string",
                        "description": "The value of the alias, e.g., '+31613127783' or 'user@example.com'."
                    },
                    "amount": {
                        "type": "number",
                        "description": "The amount of money to send in EUR."
                    },
                    "description": {
                        "type": "string",
                        "description": "The payment description.",
                        "default": "Payment"
                    }
                },
                "required": ["receiver_alias_name", "receiver_alias_value", "amount"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "request_payment",
            "description": "Send an payment request to a specific alias with amount and optional description.",
            "parameters": {
                "type": "object",
                "properties": {
                    "receiver_alias_name": {
                        "type": "string",
                        "description": "The type of alias, e.g., 'PHONE_NUMBER' or 'EMAIL'."
                    },
                    "receiver_alias_value": {
                        "type": "string",
                        "description": "The value of the alias, e.g., '+31613127783' or 'user@example.com'."
                    },
                    "amount": {
                        "type": "number",
                        "description": "The amount of money to ask for in EUR."
                    },
                    "description": {
                        "type": "string",
                        "description": "The payment description.",
                        "default": "Payment request"
                    }
                },
                "required": ["receiver_alias_name", "receiver_alias_value", "amount"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "request_mult_payments",
            "description": "Send multiple payment request based on a dictionary",
            "parameters": {
                "type": "object",
                "properties": {
                    "payment_details": {
                        "type": "dictionary",
                        "description": "Details of payment requests."
                    }
                },
                "required": ["payment_details"]
            }
        }
    }

]
