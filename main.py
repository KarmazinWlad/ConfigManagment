from src.utils.errors import ConfigurationError
from src.utils.generator import generate_output
from src.utils.parser import parse_xml

def type(data):
    if data:
        if ('@"' == data[:2] and '"' == data[-1]):
            return data[2:-1]
        elif ("({" == data[:2] and "})" == data[-2:]):
            data = data[2:-2]
            start = 0
            slovo = ""
            fold = []
            for g in data:

                if g == "(":
                    start += 1
                if not start and g == ",":
                    fold.append(slovo)
                    slovo = ""
                else:
                    slovo += g
                if g == ")":
                    start -= 1
            fold.append(slovo)
            a = []
            for newdata in fold:
                a.append(type(newdata))
            return a
        elif ('"' == data[0] and '"' == data[-1]):
            data = data.replace('"', "")
            if (data.isdigit()):
                return int(data)
        else:
            raise ConfigurationError(f"Invalid type variable:{data}")
        return

def load(s):
    slov = {}
    s = s.replace(", ", ",")
    s = s.strip("<configuration>").strip("</configuration>").replace("<variable","").replace("/>", "")
    s = s.replace(" ", "")
    arr = s.split('\n')
    for line in arr:
        if (line):
            elements = line.replace("\'","").split("value=")
            if(type(elements[1])):
                slov[elements[0].replace("name=", "").replace('"', "")] = type(elements[1])
    print(slov)
    return slov

def main():
    xml_file_path = input("Введите путь к XML-файлу: ")

    try:
        # Открываем файл по указанному пути
        with open(xml_file_path, 'r', encoding="UTF-8") as file:
            s = file.read()
            xml_data = load(s)

        if xml_data is None:
            raise ConfigurationError(f"Configuration error: Invalid value type: {type(xml_data)}")

        # Парсим XML и генерируем выходной формат
        parsed_data = parse_xml(xml_data)
        output = generate_output(parsed_data)
        print("Сконвертированный текст в учебном конфигурационном языке:")
        print(output)


    except FileNotFoundError:
        print(f"Error: File '{xml_file_path}' not found.")
    except ConfigurationError as e:
        print(f"Configuration error: {e}")


if __name__ == "__main__":
    main()
