--Количество исполнителей в каждом жанре.
SELECT g.name, COUNT(a.name) FROM artists a
JOIN artist_genre ag ON a.artist_id = ag.artist_id
JOIN genres g ON g.genre_id = ag.genre_id
GROUP BY g.name
ORDER BY COUNT(a.name) DESC;

--Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT COUNT(t.name) FROM albums al
JOIN tracks t ON t.album_id = al.album_id
WHERE al.year IN (2019,2020);

--Средняя продолжительность треков по каждому альбому.
SELECT al.name,AVG(t.lenth) FROM albums al
JOIN tracks t ON t.album_id = al.album_id
GROUP BY al.name;

--Все исполнители, которые не выпустили альбомы в 2020 году.
SELECT DISTINCT a.name FROM artists a
LEFT JOIN artist_album aa ON a.artist_id = aa.artist_id
LEFT JOIN albums al ON al.album_id = aa.album_id;
WHERE al.year NOT IN (2020);

--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
SELECT DISTINCT m.name FROM mixalbums m 
JOIN track_mixalbum tm ON m.mixalbum_id = tm.mixalbum_id 
JOIN tracks t ON t.track_id = tm.track_id
JOIN albums al ON t.album_id = al.album_id
JOIN artist_album aa ON al.album_id = aa.album_id
JOIN artists a ON a.artist_id = aa.artist_id
WHERE a.name = 'weekend';

--Названия альбомов, в которых присутствуют исполнители более чем одного жанра.

SELECT al.name FROM artists a
JOIN artist_genre ag ON a.artist_id = ag.artist_id
JOIN genres g ON g.genre_id = ag.genre_id
JOIN artist_album aa ON a.artist_id = aa.artist_id
JOIN albums al ON al.album_id = aa.album_id
GROUP BY al.name
HAVING COUNT(g.name) > 1;

--Наименования треков, которые не входят в сборники.
SELECT t.name  FROM mixalbums m 
RIGHT JOIN track_mixalbum tm ON m.mixalbum_id = tm.mixalbum_id 
RIGHT JOIN tracks t ON t.track_id = tm.track_id
WHERE m.name IS NULL;

--Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.
SELECT a.name FROM albums al
JOIN tracks t ON t.album_id = al.album_id
JOIN artist_album aa ON al.album_id = aa.album_id
JOIN artists a ON a.artist_id = aa.artist_id
WHERE t.lenth = (SELECT MIN(lenth) FROM tracks);

--Названия альбомов, содержащих наименьшее количество треков.
SELECT al.name FROM albums al
JOIN tracks t ON t.album_id = al.album_id
GROUP BY al.name
HAVING COUNT(t.album_id) = (SELECT min(c) from (SELECT album_id, count(album_id) AS c FROM tracks GROUP BY album_id) AS x);




