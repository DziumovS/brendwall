# brendwall test-app

A small Django application consisting of two parts:

1) API for working with products (list creation and retrieval).
2) An HTML page using JavaScript to send data to the API and display products.

API (Django):  
`POST`-request creates a product (accepts JSON with data: name, description, price).  
`GET`-request gets a list of all products in JSON format.  
When creating a product, simple checks are performed (price is greater than zero, title is not empty).

Frontend (HTML + JavaScript):  
`HTML`-page with a form for adding a product (name, description, price) and a “Submit” button.  
`JavaScript` for logic: sends form data to an API using AJAX (Fetch API).

When a product is successfully added, the list of products on the page is updated:  
make a `GET`-request to the API to get all products,  
display them in table form



<details>
Небольшое Django-приложение, состоящее из двух частей:

1) API для работы с продуктами (создание и получение списка).
2) Страница на HTML с использованием JavaScript для отправки данных на API и отображения продуктов.

API (Django):  
`POST`-запрос создает продукт (принимает JSON с данными: название, описание, цена).  
`GET`-запрос получает список всех продуктов в формате JSON.  
При создании продукта выполняются простые проверки (цена больше нуля, название не пустым).

Фронтенд (HTML + JavaScript):  
`HTML`-страница с формой для добавления продукта (название, описание, цена) и кнопка "Отправить".
`JavaScript` для логики: отправляет данные формы на API с использованием AJAX (Fetch API).

После успешного добавления продукта обновляется список продуктов на странице:  
делаем `GET`-запрос к API для получения всех продуктов,  
отображаем их в виде таблицы
</details>