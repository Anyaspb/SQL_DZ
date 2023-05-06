INSERT INTO genres (name) 
VALUES('pop'),('rock'),('rap'),('jazz'),('electronic');

INSERT INTO artists (name) 
VALUES('30 seconds to mars'),('billie eilish'),('ed sheeran'),('u2'),('eminem'),('weekend'),('linkin park'),('david guetta');

INSERT INTO albums (name,year) 
VALUES('30 seconds to mars','2002'),('A beautiful lie','2005'),('This is war','2009'),('Love lust faith + dreams','2013'),('America','2018'),('Starboy','2016'),('After hours', '2020'),('Dawn FM', '2022');

INSERT INTO tracks (name,lenth,album_id) 
VALUES('Was It a Dream','259','2'),('A beautiful lie','249','2'),('From Yesterday','252','2'),
('Up in the Air','276','4'),('City of Angels','302','4'),
('Hurricane','372','3'),('Closer to the Edge', '274','3'),
('Save Your Tears', '215','7'),('Blinding lights','220','7'),('I Feel It Coming','269','7'),
('Take My Breath"','339','8'),('Gasoline', '274','8'),
('Rescue Me', '217','5'),('Dangerous Night','199','5'),('Walk on Water"','185','5');

INSERT INTO mixalbums (name,year) 
VALUES('top 40 ver 25','2022'),('top 40 ver 24','2021'),('top 40 ver 23','2020'),('top 40 ver 22','2019'),('top 40 ver 21','2018'),('top 40 ver 20','2017'),('top 40 ver 19','2016'),('top 40 ver 2','2002');

INSERT INTO artist_genre (artist_id,genre_id) 
VALUES('1','2'),('2','1'),('3','1'),('4','2'),('5','3'),('6','1'),('7','2'),('8','1'),('8','5'),('1','1');

INSERT INTO artist_album (artist_id,album_id) 
VALUES('1','1'),('1','2'),('1','3'),('1','4'),('1','5'),('6','6'),('6','7'),('6','8');

INSERT INTO track_mixalbum (track_id,mixalbum_id) 
VALUES('3','8'),('12','1'),('11','1'),('9','3'),('8','3');


