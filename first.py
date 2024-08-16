# Создание HTML
html_content = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ваша очередь решать загадки</title>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head>
<body>
    <div>
        <input type="text" id="answer" placeholder="Введите слово">
        <span>охотник желает знать, где сидит фазан</span>
    </div>
    <button id="submit-button">ответить</button>

    <py-script output="console">
        from js import console, window

        def check_answer(event):
            input_value = Element("answer").element.value.lower()
            if input_value == "каждый":
                window.location.href = "https://raz00m-team.github.io/2/second"
            else:
                console.log("Неправильный ответ. Попробуйте снова.")

        Element("submit-button").element.onclick = check_answer
    </py-script>
</body>
</html>
"""

# Запись в HTML-файл
with open("first.html", "w", encoding="utf-8") as file:
    file.write(html_content)
