import json


class JSONTool:

    def format_json(self, text):
        try:
            data = json.loads(text)

            print("\n===== FORMATTED JSON =====")
            print(json.dumps(data, indent=4))

        except json.JSONDecodeError as error:
            print("\nInvalid JSON ❌")
            print(f"Error: {error}")

    def validate_json(self, text):
        try:
            json.loads(text)
            print("\nJSON is valid ✅")
        except json.JSONDecodeError:
            print("\nJSON is invalid ❌")

    def load_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            print("\n===== JSON FILE =====")
            print(json.dumps(data, indent=4))

        except FileNotFoundError:
            print("File not found ❌")

        except json.JSONDecodeError:
            print("File contains invalid JSON ❌")