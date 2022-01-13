CREATE TABLE `messages` (
	`message_id` VARCHAR(100) NOT NULL,
	`content` VARCHAR(1000) NOT NULL,
	`channel_id` VARCHAR(100) NOT NULL,
	PRIMARY KEY (`message_id`),
	FOREIGN KEY (channel_id) REFERENCES channels(channel_id)
);