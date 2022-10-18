START TRANSACTION;

Truncate table streaming;

# Inserting Netflix
INSERT INTO streaming (Provider, DateAdded, ListedIn, title)
Select 'Netflix', n.date_added, n.listed_in, n.title
From netflix n;

# Inserting Disney
INSERT INTO streaming (Title_ID, Provider, title, DateAdded, ListedIn)
Select s.Title_ID, 'Disney',  d.title, d.date_added, d.Listed_in
From disney d
Join streaming s ON s.title = d.title;

INSERT INTO streaming (Provider, DateAdded, ListedIn, title)
Select 'Disney', d.date_added, d.Listed_in, d.title
From disney d
LEFT JOIN streaming s ON d.title = s.title
Where s.title IS NULL;

# Inserting Hulu
INSERT INTO streaming (Title_ID, Provider, title, DateAdded, ListedIn)
Select Distinct s.Title_ID, 'Hulu',  h.title, h.date_added, h.Listed_in
From hulu h
Join streaming s ON s.title = h.title;

INSERT INTO streaming (Provider, DateAdded, ListedIn, title)
Select 'Hulu', h.date_added, h.Listed_in, h.title
From hulu h
LEFT JOIN streaming s ON h.title = s.title
Where s.title IS NULL;

# Inserting Prime
INSERT INTO streaming (Title_ID, Provider, title, DateAdded, ListedIn)
Select Distinct s.Title_ID, 'Prime',  p.title, p.date_added, p.Listed_in
From prime p
Join streaming s ON s.title = p.title;

INSERT INTO streaming (Provider, DateAdded, ListedIn, title)
Select 'Prime', p.date_added, p.Listed_in, p.title
From prime p
LEFT JOIN streaming s ON p.title = s.title
Where s.title IS NULL;

ROLLBACK;