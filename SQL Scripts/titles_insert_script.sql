TRUNCATE TABLE titles;

INSERT INTO titles (id, name, type, duration, description, country, release_year, cast, director)
Select s.title_id, s.title, n.type, n.duration, n.description, n.country, n.release_year, n.cast, n.director
From streaming s
JOIN netflix n ON n.title = s.title
Group By s.title_id, s.title;

INSERT INTO titles (id, name, type, duration, description, country, release_year, cast, director)
Select s.title_id, s.title, p.type, p.duration, p.description, p.country, p.release_year, p.cast, p.director
From streaming s
Left Join titles t ON t.id = s.title_id
Join prime p ON p.title = s.title
Where t.id IS NULL
Group By s.title_id, s.title;

INSERT INTO titles (id, name, type, duration, description, country, release_year, cast, director)
Select s.title_id, s.title, p.type, p.duration, p.description, p.country, p.release_year, p.cast, p.director
From streaming s
Left Join titles t ON t.id = s.title_id
Join hulu p ON p.title = s.title
Where t.id IS NULL
Group By s.title_id, s.title;

INSERT INTO titles (id, name, type, duration, description, country, release_year, cast, director)
Select s.title_id, s.title, p.type, p.duration, p.description, p.country, p.release_year, p.cast, p.director
From streaming s
Left Join titles t ON t.id = s.title_id
Join disney p ON p.title = s.title
Where t.id IS NULL
Group By s.title_id, s.title;