Робота з фреймами у python selenium

### Опис

Написати на python selenium код який пройде по двох фреймах на початковiй сторiнцi, ввійде в кожний фрейм, введе правильний секретний текст, натисне кнопку “Перевiрити”, порівняє текст дiалогового вiкна для підтвердження успішності верифікації та закриє діалогове вікно

### Складнicть

Проста

### Початковi данi

- **Пiдготовка серверної частини**

Код початкової HTML-сторінки **`dz.html`** з двома фреймами

```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Сторінка з фреймами</title>
</head>
<body>
    <iframe id="frame1" src="dz_frame1.html" style="display: block;"></iframe>
    <iframe id="frame2" src="dz_frame2.html" style="display: block;"></iframe>
</body>
</html>
```

Код фрейму1 `dz_frame1.html`:

```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Фрейм 1</title>
</head>
<body>
    <br/>	
    <h3>Frame1</h3>	
    <input type="text" id="input1" placeholder="Введіть текст">
    <button onclick="verifyInput('input1')">Перевірити</button>

    <script>
        function verifyInput(inputId) {
            var inputValue = document.getElementById(inputId).value;
            if (inputValue === "Frame1_Secret") {
                alert("Верифікація пройшла успішно!");
            } else {
                alert("Введено неправильний текст!");
            }
        }
    </script>
</body>
</html>
```

Код фрейму2 `dz_frame2.html`:

```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Фрейм 2</title>
</head>
<body>
    <br/>	
    <h3>Frame2</h3>	
    <input type="text" id="input2" placeholder="Введіть текст">
    <button onclick="verifyInput('input2')">Перевірити</button>

    <script>
        function verifyInput(inputId) {
            var inputValue = document.getElementById(inputId).value;
            if (inputValue === "Frame2_Secret") {
                alert("Верифікація пройшла успішно!");
            } else {
                alert("Введено неправильний текст!");
            }
        }
    </script>
</body>
</html>
```

Щоб запустити цi сторінки локально за допомогою Python http.server, збережіть код першої сторiнки у файл **`dz.html`**  другу сторiнку як **`dz_frame1.html` ,** а третю як **`dz_frame2.html`**Потім ви можете запустити локальний сервер за допомогою командного рядка `python -m http.server 8000`  виконуючи команду  iї у тiй самiй директорiї де були збереженi `html` файли

Після цього основна веб-сторінка буде доступна за адресою `http://localhost:8000/dz.html`