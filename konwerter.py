import sys
import json


def parse_arguments():
    if len(sys.argv) != 3:
        print("Sposób użycia: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if input_file.endswith(".json"):
        input_format = "json"
    elif input_file.endswith(".yml") or input_file.endswith(".yaml"):
        input_format = "yaml"
    elif input_file.endswith(".xml"):
        input_format = "xml"
    else:
        print("Nieobsługiwany format pliku wejściowego.")
        sys.exit(1)

    if output_file.endswith(".json"):
        output_format = "json"
    elif output_file.endswith(".yml") or output_file.endswith(".yaml"):
        output_format = "yaml"
    elif output_file.endswith(".xml"):
        output_format = "xml"
    else:
        print("Nieobsługiwany format pliku wyjściowego.")
        sys.exit(1)

    return input_file, output_file, input_format, output_format


def load_json(input_file):
    try:
        with open(input_file, "r") as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print("Błąd w składni pliku JSON:", str(e))
        sys.exit(1)
    except FileNotFoundError:
        print("Plik", input_file, "nie istnieje.")
        sys.exit(1)
