# Выполнение дз №14: Учимся быстро разрабатывать готовые проекты для тестовых заданий.
## UI тесты на сайт https://www.saucedemo.com/ 
___
### Используемые технологии
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain-wordmark.svg" height="40" wigth="40"/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" wigth="40"/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" wigth="40"/><img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" height="40" wigth="40"/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg" height="40" wigth="40"/>
### Настройка проекта перед запуском
Перед запуском тестов необходимо создать файл `.env` в директории `tests`   
Для файла `.env` заполнить креды для доступа к selenoid.   
**Например:**
```
SELENOID_LOGIN=user1
SELENOID_PASS=1234
SELENOID_URL=selenoid.autotests.cloud
```

#### Команды для запуска тестов:

- Прогон всех тестов   
```
pytest tests
```
- Запуск конкретного теста
```
pytest tests/<test_file_name>
```
- Генерация allure отчета после выполнения тестов   
```
allure serve tests/allure-results
```
--- 
### Запуск job в [jenkins](https://jenkins.autotests.cloud/job/k_f_python_hw_number_14/) и получение уведомления в telegram


<img width="1097" height="574" alt="image" src="https://github.com/user-attachments/assets/445d56d1-cd46-4570-9aea-6c15943f31d2" />

### Отчет в allure после прохождения тестов
<img width="1115" height="573" alt="image" src="https://github.com/user-attachments/assets/6f9a1934-2ab6-4dd1-9bf4-ee4d03527d11" />

### Описание шагов теста с выводом скришота и скринкаста
<img width="1104" height="574" alt="image" src="https://github.com/user-attachments/assets/90204432-6c13-4b2c-91a4-d876b73b294d" />

### Настройка telegram бота для уведомлений о результатах прохождении тестов

<img width="768" height="356" alt="image" src="https://github.com/user-attachments/assets/c1d0ad1e-90a3-4d08-addf-18012c397849" />


          
