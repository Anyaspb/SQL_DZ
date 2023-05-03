
--Название и год выхода альбомов, вышедших в 2018 году.
SELECT name,year FROM albums 
WHERE year = 2018;

--Название и продолжительность самого длительного трека.
SELECT name,lenth FROM tracks
WHERE lenth = (SELECT MAX(lenth) FROM tracks);

--Название треков, продолжительность которых не менее 3,5 минут.
SELECT name FROM tracks
WHERE lenth > 210;

--Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT name FROM mixalbums
WHERE year IN (2018,2019,2020)

--Исполнители, чьё имя состоит из одного слова.
SELECT name FROM artists
WHERE name NOT LIKE '% %'

--Название треков, которые содержат слово «мой» или «my»
SELECT name FROM artists
WHERE name LIKE '%мой%' OR name LIKE '%my%'

	
