import sys
import json
import yaml
import xml.etree.ElementTree as ET


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
        print(f"Błąd w składni pliku JSON: {str(e)}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Plik {input_file} nie istnieje.")
        sys.exit(1)


def save_json(output_file, data):
    try:
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Błąd podczas zapisu pliku JSON: {e}")
        sys.exit(1)


def load_yaml(input_file):
    try:
        with open(input_file, "r") as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError as e:
        print(f"Błąd w składni pliku YAML: {str(e)}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Plik {input_file} nie istnieje.")
        sys.exit(1)


def save_yaml(output_file, data):
    try:
        with open(output_file, "w") as file:
            yaml.dump(data, file, default_flow_style=False)
    except Exception as e:
        print(f"Błąd podczas zapisu pliku YAML: {e}")
        sys.exit(1)


def load_xml(input_file):
    try:
        tree = ET.parse(input_file)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Błąd w składni pliku XML: {str(e)}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Plik {input_file} nie istnieje.")
        sys.exit(1)


def save_xml(output_file, root):
    try:
        tree = ET.ElementTree(root)
        tree.write(output_file, encoding="utf-8", xml_declaration=True)
    except Exception as e:
        print(f"Błąd podczas zapisu pliku XML: {e}")
        sys.exit(1)


def main():
    input_file, output_file, input_format, output_format = parse_arguments()

    if input_format == "json":
        data = load_json(input_file)
    elif input_format == "yaml":
        data = load_yaml(input_file)
    elif input_format == "xml":
        root = load_xml(input_file)
    else:
        print("Nieobsługiwany format pliku wejściowego.")
        sys.exit(1)

    if output_format == "json":
        save_json(output_file, data)
    elif output_format == "yaml":
        save_yaml(output_file, data)
    elif output_format == "xml":
        save_xml(output_file, root)
    else:
        print("Nieobsługiwany format pliku wyjściowego.")
        sys.exit(1)


if __name__ == "__main__":
    main()
