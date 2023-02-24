CREATE TABLE users
(
	user_id INT NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(75) NOT NULL,
	last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE book
(
	book_id INT NOT NULL AUTO_INCREMENT,
	book_name VARCHAR(200) NOT NULL,
	details VARCHAR(500) NULL,
	author VARCHAR(200) NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE wishlist
(
	wishlist_id INT NOT NULL AUTO_INCREMENT,
	user_id INT NOT NULL,
	book_id INT NOT NULL,
	PRIMARY KEY(wishlist_id),
    FOREIGN KEY(user_id)
		REFERENCES users(user_id),
    FOREIGN KEY(book_id)
		REFERENCES book(book_id)
);

CREATE TABLE store
(
	store_id INT NOT NULL,
	locale VARCHAR(500) NOT NULL,
    PRIMARY KEY(store_id)
);