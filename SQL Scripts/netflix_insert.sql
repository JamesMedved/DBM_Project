START TRANSACTION;

Truncate table streaming;

INSERT INTO streaming (Provider, DateAdded, ListedIn, title)
Select 'Netflix', n.date_added, n.listed_in, n.title
From netflix n;

Select * From Streaming;

ROLLBACK;