from .errors import ConfigurationError

__all__ = [
    "parse_array",
    "parse_value",
    "parse_xml",
    "parse_name"
]

def parse_xml(data):
    if isinstance(data, dict):
        return parse_dict(data)
    elif isinstance(data, list):
        return parse_array(data)
    else:
        raise ConfigurationError("Invalid data type at the top level.")

def parse_dict(data):
    output = "begin\n"
    for name, value in data.items():
        output += f" {name} := {parse_value(value)};\n"
    output += "end"
    return output

def parse_comment(data):
    return "(*" + "\n".join(parse_value(item) for item in data) + "\n*)"

def parse_array(data):
    return "[ " + ", ".join(parse_value(item) for item in data) + " ]"

def parse_name(data):
    slovar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in data:
        if(not(i in slovar)):
            raise ConfigurationError(f"Invalid name symbol:{i}")
            return
    return "data"

def parse_value(value):
    if isinstance(value, list):
        return parse_array(value)
    elif isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        raise ConfigurationError(f"Invalid value type: {type(value)}")