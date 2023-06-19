'''Разработать БД «ЗАРПЛАТА», содержащую две таблицы Анкета и
Больничные листы. Установить связь между таблицами. Заполнить
таблицы произвольными данными (не менее 10 записей). Реализовать
SQL-запросы на выборку, обновление, удаление данных из БД.
Таблица "Анкета"
id (INT, PK) - уникальный идентификатор сотрудника
имя (VARCHAR)
фамилия (VARCHAR)
дата_рождения (DATE)
пол (VARCHAR)
дата_найма (DATE)
должность (VARCHAR)
отдел (VARCHAR)
базовая_ставка (DECIMAL)
Таблица "Больничные листы"
id (INT, PK) - уникальный идентификатор больничного листа
id_сотрудника (INT, FK) - идентификатор сотрудника, на которого выписан больничный
лист
дата_начала (DATE)
дата_окончания (DATE)
причина (VARCHAR)
диагноз (VARCHAR)
оплачен (BOOLEAN)
В данной структуре таблица "Больничные листы" связана с таблицей "Анкета" через
внешний ключ id_сотрудника. Это означает, что каждый больничный лист относится к
определенному сотруднику из таблицы "Анкета".'''
import sqlite3 as sq 
import data_sotr

with sq.connect('zarplata.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS anketa (
        id_sotrydnika INTEGER PRIMARY KEY,
        name VARCHAR,
        surname VARCHAR,
        date_rozdeniya DATE,
        sex VARCHAR,
        date_naim DATE,
        dolznost VARCHAR,
        otdel VARCHAR,
        basovaya_stavka DECIMAL
    )""")

with sq.connect('zarplata.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS bolnichnie_listi (
        id_lista INTEGER PRIMARY KEY,
        id_sotrydnika INTEGER,
        date_nachala DATE,
        date_okonch DATE,
        prichina VARCHAR,
        diagnoz VARCHAR,
        oplachen BOOLEAN,
        FOREIGN KEY (id_sotrydnika) REFERENCES anketa (id_sotrydnika)
    )""")

# with sq.connect("zarplata.db") as con:
#     cur = con.cursor()
#     cur.executemany("INSERT INTO anketa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", data_sotr.info_sotr)
#     cur.executemany("INSERT INTO bolnichnie_listi VALUES (?, ?, ?, ?, ?, ?, ?)", data_sotr.info_listi)

with sq.connect("zarplata.db") as con:
    cur = con.cursor()
 #Запросы на выборку данных
    #1.Вывести список всех сотрудников и их должностей
    #cur.execute("SELECT name, surname, dolznost FROM anketa")
    #2.Вывести список всех сотрудников и их базовых ставок
    #cur.execute("SELECT name, surname, basovaya_stavka FROM anketa")
    #3.Вывести список всех сотрудников, работающих в отделе "IT"
    #cur.execute("SELECT * FROM anketa WHERE otdel = 'Отдел IT'")
    #4.Вывести список всех сотрудников, принятых на работу после 1 января 2022 года
    #cur.execute("SELECT * FROM anketa WHERE data_naim < '2022.01.01'")
    #5.Вывести список всех больничных листов, выписанных сотруднику с id = 42
    #cur.execute("SELECT * FROM bolnichnie_listi WHERE id_sotrydnika = 42")
    #6.Вывести список всех больничных листов, оплаченных компанией
    #cur.execute("SELECT * FROM bolnichnie_listi WHERE oplachen = True") 
    #7.Вывести список всех сотрудников, имеющих больничные листы на текущий месяц
    #cur.execute("SELECT * FROM bolnichnie_listi WHERE date_nachala > '2023.04.01'")
    #8.Вывести среднюю базовую ставку всех сотрудников
    #cur.execute("SELECT avg(basovaya_stavka) FROM anketa")
    #9.Вывести список всех сотрудников, имеющих базовую ставку выше 100 000
    #cur.execute("SELECT * FROM anketa WHERE basovaya_stavka > 100000")
    #10.Вывести список всех сотрудников и общее количество дней, проведенных ими на больничном
    #cur.execute("SELECT anketa.name, anketa.surname," 
    #"SUM(julianday(bolnichnie_listi.date_okonch) - julianday(bolnichnie_listi.date_nachala))"
    #"FROM anketa INNER JOIN bolnichnie_listi ON anketa.id_sotrydnika = bolnichnie_listi.id_sotrydnika GROUP BY anketa.name, anketa.surname")
    #11.Вывести информацию о сотрудниках и их больничных листах за последний месяц(последний месяц действия листа-апрель)
    # cur.execute("SELECT anketa.name, anketa.surname, bolnichnie_listi.date_nachala, bolnichnie_listi.date_okonch, "
    # "bolnichnie_listi.prichina, bolnichnie_listi.diagnoz, bolnichnie_listi.oplachen FROM anketa "
    # "INNER JOIN bolnichnie_listi ON anketa.id_sotrydnika = bolnichnie_listi.id_sotrydnika WHERE "
    # "bolnichnie_listi.date_nachala >= DATE('now', '-3 month')")
    #12.Вывести среднюю продолжительность больничных листов сотрудников в каждом отделе
    # cur.execute("SELECT otdel, AVG(julianday(date_okonch) - julianday(date_nachala)) FROM anketa "
    # "INNER JOIN bolnichnie_listi ON anketa.id_sotrydnika = bolnichnie_listi.id_sotrydnika GROUP BY otdel")
    #13.Вывести список сотрудников и информацию о последнем больничном листе, который они оформляли
    # cur.execute("SELECT anketa.name, anketa.surname, bolnichnie_listi.date_nachala, bolnichnie_listi.date_okonch, "
    # "bolnichnie_listi.prichina, bolnichnie_listi.diagnoz, bolnichnie_listi.oplachen FROM anketa "
    # "INNER JOIN bolnichnie_listi ON anketa.id_sotrydnika = bolnichnie_listi.id_sotrydnika "
    # "WHERE bolnichnie_listi.date_nachala = (SELECT MAX(date_nachala) "
    # "FROM bolnichnie_listi WHERE bolnichnie_listi.id_sotrydnika = anketa.id_sotrydnika)")
    #14.Вывести список сотрудников и информацию о первом больничном листе, который они оформляли
    # cur.execute("SELECT anketa.name, anketa.surname, bolnichnie_listi.date_nachala, bolnichnie_listi.date_okonch, "
    # "bolnichnie_listi.prichina, bolnichnie_listi.diagnoz, bolnichnie_listi.oplachen FROM anketa "
    # "INNER JOIN bolnichnie_listi ON anketa.id_sotrydnika = bolnichnie_listi.id_sotrydnika "
    # "WHERE bolnichnie_listi.date_nachala = (SELECT MIN(date_nachala) "
    # "FROM bolnichnie_listi WHERE bolnichnie_listi.id_sotrydnika = anketa.id_sotrydnika)")
    #15.Вывести список сотрудников и суммарную продолжительность их больничных листов в текущем году
    # cur.execute("SELECT anketa.name, anketa.surname, SUM(julianday(date_okonch) - julianday(date_nachala)) AS summ  FROM anketa "
    # "INNER JOIN bolnichnie_listi ON anketa.id_sotrydnika = bolnichnie_listi.id_sotrydnika "
    # "WHERE strftime('%Y', date_nachala) = strftime('%Y', 'now') "
    # "GROUP BY anketa.name, anketa.surname ORDER BY summ")

 #Запросы на обновление данных
    #1.Обновить базовую ставку сотрудника на определенной должности
    #cur.execute("UPDATE anketa SET basovaya_stavka = 25000 WHERE dolznost = 'Уборщица'")
    #2.Обновить отдел для всех сотрудников в определенном диапазоне возраста
    #cur.execute("UPDATE anketa SET otdel = 'Отдел кадров' WHERE date_rozdeniya BETWEEN '1970-01-01' AND '1990-01-01'")
    #3.Обновить дату найма для сотрудника, получившего повышение.
    #cur.execute("UPDATE anketa SET date_naim = '2017-05-13' WHERE id_sotrydnika = 17")
    #4.Обновить причину больничного листа для сотрудника
    #cur.execute("UPDATE bolnichnie_listi SET prichina = 'болезнь' WHERE id_lista = 25")
    #5.Обновить базовую ставку сотрудника в таблице "Анкета" на определенный процент. При этом
    #необходимо исключить из обновления сотрудников, у которых были неоплаченные больничные листы.
    #cur.execute("UPDATE anketa SET basovaya_stavka = basovaya_stavka * 1.3 WHERE id_sotrydnika IN(SELECT id_sotrydnika FROM bolnichnie_listi WHERE oplachen = 1)")
    #6.Обновить дату начала больничного листа в таблице "Больничные листы" на определенную дату. При этом
    #необходимо исключить из обновления больничные листы с уже пройденной датой начала
    #cur.execute("UPDATE bolnichnie_listi SET date_nachala = '2014-10-10' WHERE date_nachala < '2013-08-20'")
    #7.Обновить причину больничного листа в таблице "Больничные листы" на определенное значение для всех сотрудников, работающих в отделе
    #"Бухгалтерия"(вместо бухгалтерии-отдел связи)
    # cur.execute("UPDATE bolnichnie_listi SET prichina = 'Обострение заболевания' WHERE id_sotrydnika IN (SELECT anketa.id_sotrydnika FROM anketa " 
    # "INNER JOIN bolnichnie_listi ON anketa.id_sotrydnika = bolnichnie_listi.id_sotrydnika WHERE otdel = 'Отдел связи')")


 #Запросы на удаление данных
    #1.Удалить все записи о больничных листах для сотрудника с именем "Иван"
    #cur.execute("DELETE FROM bolnichnie_listi WHERE id_sotrydnika IN(SELECT id_sotrydnika FROM anketa WHERE name = 'Иван')")
    #2.Удалить все записи о больничных листах для сотрудника с фамилией "Петров"
    #cur.execute("DELETE FROM bolnichnie_listi WHERE id_sotrydnika IN(SELECT id_sotrydnika FROM anketa WHERE surname = 'Петров')")
    #3.Удалить все записи о больничных листах для сотрудника с должностью "Менеджер"
    #cur.execute("DELETE FROM bolnichnie_listi WHERE id_sotrydnika IN(SELECT id_sotrydnika FROM anketa WHERE dolznost = 'Менеджер')")
    #4.Удалить все записи о больничных листах для сотрудника с отделом "Отдел продаж"
    #cur.execute("DELETE FROM bolnichnie_listi WHERE id_sotrydnika IN(SELECT id_sotrydnika FROM anketa WHERE otdel = 'Отдел продаж')")
    #5.Удалить все записи о больничных листах для сотрудника женского пола
    #cur.execute("DELETE FROM bolnichnie_listi WHERE id_sotrydnika IN(SELECT id_sotrydnika FROM anketa WHERE sex = 'Женский')")
    #6.Удалить все записи о больничных листах для сотрудников старше 50 лет
    #cur.execute("DELETE FROM bolnichnie_listi WHERE id_sotrydnika IN(SELECT id_sotrydnika FROM anketa WHERE date_rozdeniya < '1973-01-01')")
    #7.Удалить все записи о неоплаченных больничных листах
    #cur.execute("DELETE FROM bolnichnie_listi WHERE id_sotrydnika IN(SELECT id_sotrydnika FROM anketa WHERE oplachen = 0)")
    #8.Удалить все записи о больничных листах, дата окончания которых прошла
    #cur.execute("DELETE FROM bolnichnie_listi WHERE date_okonch < DATE('now')")
    #9.Удалить все записи о больничных листах, начиная с определенной даты
    #cur.execute("DELETE FROM bolnichnie_listi WHERE date_nachala >= DATE('2021-02-10')")
    #10.Удалить все записи о больничных листах, закончившихся до определенной даты
    #cur.execute("DELETE FROM bolnichnie_listi WHERE date_okonch <= DATE('2017-10-15')")
    #11.Удалить все больничные листы сотрудника с именем "Иван" из таблицы "Больничные листы"
    #cur.execute("DELETE FROM bolnichnie_listi WHERE id_sotrydnika IN(SELECT id_sotrydnika FROM anketa WHERE name = 'Иван')")
    #12.Удалить все больничные листы сотрудников, чьи фамилии начинаются на букву "С" из таблицы "Больничные листы"
    #cur.execute("DELETE FROM bolnichnie_listi WHERE id_sotrydnika IN (SELECT id_sotrydnika FROM anketa WHERE surname LIKE 'С%')")
    #13.Удалить все больничные листы, которые еще не были оплачены, у сотрудников с должностью "Менеджер" из таблицы "Больничные листы"
    #cur.execute(" DELETE FROM bolnichnie_listi WHERE oplachen=0 AND id_a IN (SELECT id_a FROM anketa WHERE dolznost='Менеджер')"
    #14.Удалить все больничные листы, выписанные сотрудникам отдела "IT" в период с 1 января 
    #cur.execute("DELETE FROM bolnichnie_listi WHERE id_sotrydnika IN (SELECT id_sotrydnika FROM anketa WHERE otdel='Отдел IT') AND start_date >= '2023-01-01'")
    #15.Удалить все больничные листы, связанные со сотрудниками старше 50 лет из таблицы "Больничные листы"
    #cur.execute("DELETE FROM bolnichnie_listi WHERE id_sotrydnika IN(SELECT id_sotrydnika FROM anketa WHERE date_rozdeniya < '1973-01-01')")
    
    result = cur.fetchall()
print(result)
