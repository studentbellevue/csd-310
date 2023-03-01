INSERT INTO store(store_id, locale)
VALUES (000001,
'446 Wilson Ave, Beaver PA 15009');

INSERT INTO book(book_name,details,author)
VALUES('llama llama I Love YOU', 'Anna Dewdneys famous adaption into the world of cybertronics', 'Anna Dewdney'), ('workshop help', 'how to handle yourself in a workshop', 'Dale Bilster'), 
('The little Indian', 'A story about a young mans growth into adulthood', 'Chief Strongbow'), ('The littlest mermaid', 'A tail as old as time', 'Queen Ariel'), 
('Crossbow country', 'A wounded Vet returns to hunting wild hog', 'Captain Price'), ('Engine Trouble', 'How to fix any engine in 2 minutes', 'Richard Earnhert'), 
('Tickle fight', 'The untold story of how the British almost lost WW2', 'Jeremy baker'), ('Tiny time', 'An instructional book on watch repair', 'Father Time'), 
('Compute this', 'The story of an IT student and his struggles with SQL', 'Devon Lohrmann');

INSERT INTO users(first_name, last_name)
Values('Tim', 'Armstrong'), ('David', 'Fangerton'), ('Rebecca', 'DeMoriam');

INSERT INTO wishlist(user_id, book_id)
	VALUES(
    (SELECT user_id FROM users WHERE first_name = 'Tim'),
    (SELECT book_id FROM book WHERE book_name = 'Crossbow country'));
    
INSERT INTO wishlist(user_id, book_id)
	VALUES(
    (SELECT user_id FROM users WHERE first_name = 'David'),
    (SELECT book_id FROM book WHERE book_name = 'llama llama I Love YOU'));
    
INSERT INTO wishlist(user_id, book_id)
	VALUES(
    (SELECT user_id FROM users WHERE first_name = 'Rebecca'),
    (SELECT book_id FROM book WHERE book_name = 'Compute this'));

