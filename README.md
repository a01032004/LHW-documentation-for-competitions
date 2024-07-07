# LHW-documentation-for-competitions
В данном ДДЗ необходимо реализовать создание протоколов (стартового, итогого личного и итогого по командам) для облегчения рутинной работы сотрудников кафедры КФП.

## Запуск
Чтобы запустить приложение из консоли необходимо перейти в директорию, куда был склонирован проект и прописать команду: `python3 -m Interactive-window.window`

Далее вводим название команд, тип соревнований, при добавлении участника вводим его данные. Начинаем соревнования и заполняем необходимые данные. Все протоколы будут распологаться в папке "Interactive-window" файл "start.xlsx"

## Функционал

1) На вход получем список команд и участников 
 В командах поле имя (номер, тип! группы соревнований). Считаем что соревнования проводятся для конкретной группы участников (1-постоянный М и Ж, 2-переменный М, 3-переменный Ж)
 В участнимках (ФИО, звание, возраст, пол, стартовый номер)
    Генерируется массив команд, каждый элемент этого массива - это массив с участниками команды 
    
    Далее имеем кнопку "сгененрировать порядок команд". Здесь случайным образом генерируется стартовый порядок команд 
    (Например есть команды "Й", "Ц", "У". Значит сначала стартует один участник из команды "Й", потом один из команды "Ц", потом один из команды "У", потом один из команды "Й" и т.д. пока не закончатся участники)
    Так же при нажатии на кнопку "сгененрировать порядок команд" необходимор каждому участнику присвоить стартовое время (от 00:00:00). Время старта следующей партии участников расчитывается как: время предыдущей партии + (30 сек * кол-во команд (Делаем по умолчанию 30 сек. Если что исправим))
    Необходимо уведомить пользователя о том, что сгенерировалась последовательность старта команд (какое-то окно). (////Или же ввод команд вручную????////)

2) Внизу есть кнопка "начать соревнования". При нажатии на неё происходит формирование стартового протокола в формате таблицы в exel, который находится в папке ""Interactive-window". 
Так же появляется новое окно в котором есть болшьшой массив участников (участника определям по стартовому номеру) и есть поля у каждого участника "время финиша", и снятие с соревнований за: "неспортивное поведение", "нарушение правил прохождения маршрута"
Пользователь заполняет время финиша и при необходимости ставит галки за снятие. При вводе время финиша участники отсортироваанны по стартовцым номерам, т.е. участника определяем по стартовому номеру. В данный момент на окне только стартовый номер и заполняем время финиша

3) Далее внизу есть кнопка "подвести итоги". При нажатии на неё происхлодит сортировка участников для личного и командного зачёта (формирование суммы баллов учитывая возратсные коэффициенты. Быллы участников команды - это места, занятые участниками в личном зачёте).
Получаются 2 отсортированных массива (личный и командный зачёт), из которых формируюся итоговые протоколы exel личного и командного зачёта. 
Так после формированиия необходимор уведомить пользователя о том, что "Ура! Соревнования завершились! Протоколы в папке "Interactive-window". 

