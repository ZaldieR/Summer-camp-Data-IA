CREATE TABLE `replies` (
	`replie_id` VARCHAR(100) NOT NULL,
	`content` VARCHAR(1000) NOT NULL,
	`message_id` VARCHAR(100) NOT NULL,
	PRIMARY KEY (`replie_id`),
	FOREIGN KEY (message_id) REFERENCES messages(message_id)
);