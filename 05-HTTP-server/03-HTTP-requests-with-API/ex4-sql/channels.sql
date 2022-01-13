CREATE TABLE `channels` (
	`channel_id` VARCHAR(100) NOT NULL,
	`display_name` VARCHAR(100) NOT NULL,
	`team_id` VARCHAR(100) NOT NULL,
	PRIMARY KEY (`channel_id`),
	FOREIGN KEY (`team_id`) REFERENCES `teams`(`team_id`)
);