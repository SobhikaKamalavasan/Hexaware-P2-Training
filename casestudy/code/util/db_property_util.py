
import os

class DBPropertyUtil:
    @staticmethod
    def get_property_string(file_path="config.properties"):
        props = {}
        with open(file_path, 'r') as file:
            for line in file:
                if "=" in line and not line.startswith("#"):
                    key, value = line.strip().split("=")
                    props[key.strip()] = value.strip()

        return {
            "host": props.get("hostname"),
            "port": int(props.get("port", 3306)),
            "user": props.get("username"),
            "password": props.get("password"),
            "database": props.get("dbname")
        }
