--Run this in your MySQL workbench to create a db and a table

CREATE DATABASE dramas;
USE dramas;

CREATE TABLE k_dramas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    year_of_release YEAR NOT NULL,
    aired_date VARCHAR(255),
    aired_on VARCHAR(255),
    number_of_episodes INT,
    network VARCHAR(255),
    duration VARCHAR(50),
    content_rating VARCHAR(100),
    synopsis TEXT,
    cast TEXT,
    genre VARCHAR(255),
    tags TEXT,
    `rank` VARCHAR(10),  -- Enclosed in backticks to use the reserved word, rank
    rating DECIMAL(3, 1)
);

INSERT INTO k_dramas (name, year_of_release, aired_date, aired_on, number_of_episodes, network, duration, content_rating, synopsis, cast, genre, tags, `rank`, rating)
VALUES
('Crash Landing on You', 2019, 'Dec 14, 2019 - Feb 16, 2020', 'Sunday, Saturday', 16, 'Netflix, tvN', '1 hr. 25 min.', '15+ - Teens 15 or older',
'After getting into a paragliding accident, South Korean heiress Yoon Se Ri crash lands in North Korea. There, she meets North Korean army officer Ri Jung Hyuk, who agrees to help her return to South Korea. Despite the tension between their countries, the two of them start falling for one another.',
'Hyun Bin, Son Ye Jin, Seo Ji Hye, Kim Jung Hyun, Yang Kyung Won, Lee Shin Young', 'Military, Comedy, Romance, Political',
'North And South Korea, Strong Male Lead, Rich Female Lead, Fate, Nice Male Lead, Calm Male Lead, Strong Female Lead, Friendship, Smart Female Lead, Soulmates', '#15', 9.0),

('Alchemy of Souls Season 2', 2022, 'Dec 10, 2022 - Jan 8, 2023', 'Saturday, Sunday', 10, 'Netflix, tvN', '1 hr. 21 min.', '15+ - Teens 15 or older',
'Jang Uk returns from death, and three years later, the story of the mages unfolds anew. Jang Uk becomes a hunter of the soul-shifters when a young woman, a prisoner in her own home, seeks his help to reclaim her freedom.',
'Lee Jae Wook, Go Youn Jung, Hwang Min Hyun, Shin Seung Ho, Yoo Joon Sang, Oh Na Ra', 'Action, Historical, Romance, Fantasy',
'Magical Power, Strong Male Lead, Marriage Of Convenience, Fantasy World, Smart Male Lead, Birth Secret, Nice Male Lead, Transmigration, Supernatural, Antihero Male Lead', '#16', 9.0),

('Extraordinary Attorney Woo', 2022, 'Jun 29, 2022 - Aug 18, 2022', 'Wednesday, Thursday', 16, 'ENA, Netflix', '1 hr. 17 min.', '15+ - Teens 15 or older',
'Diagnosed with autism spectrum disorder, 27-year-old Woo Young Woo graduated at the top of her class from the prestigious Seoul National University for both college and law school due to her high IQ of 164, impressive memory, and creative thought process. Working as a lawyer, she finds herself struggling when it comes to social interactions.',
'Park Eun Bin, Kang Tae Oh, Kang Ki Young, Jeon Bae Soo, Baek Ji Won, Jin Kyung', 'Law, Romance, Life, Drama',
'Autistic Female Lead, Autism, Attorney Female Lead, Smart Female Lead, Workplace Setting, Nice Male Lead, Father-Daughter Relationship, Courtroom Setting, Single Mother/Father Supporting Character, Slow Burn Romance', '#17', 8.9),

('Vincenzo', 2021, 'Feb 20, 2021 - May 2, 2021', 'Saturday, Sunday', 20, 'Netflix, tvN', '1 hr. 25 min.', '15+ - Teens 15 or older',
'At the age of eight, Park Joo Hyeong left for Italy after being adopted. Now an adult, he is known as Vincenzo Cassano and employed by a Mafia family as a consigliere. Due to warring Mafia factions, he flies to South Korea where he gets involved with lawyer Hong Cha Young. She is the type of attorney who will do anything to win a case. Now back in his motherland, he gives an unrivalled conglomerate a taste of his own medicine—with a side of his own version of justice.',
'Song Joong Ki, Jeon Yeo Been, Ok Taec Yeon, Kim Yeo Jin, Jo Han Chul, Kwak Dong Yeon', 'Comedy, Law, Crime, Drama',
'Mafia, Revenge, Slight Romance, Eccentric Female Lead, Smart Male Lead, Injustice, Black Comedy, Corrupt Legal System, Badass Male Lead, Skilled Killer', '#18', 8.9),

('Navillera', 2021, 'Mar 22, 2021 - Apr 27, 2021', 'Monday, Tuesday', 12, 'Netflix, tvN', '1 hr. 5 min.', '15+ - Teens 15 or older',
'A 70-year-old with a dream and a 23-year-old with a gift lift each other out of harsh realities and rise to the challenge of becoming ballerinos.',
'Park In Hwan, Song Kang, Na Moon Hee, Hong Seung Hee, Kim Tae Hoon, Yoon Ji Hye', 'Life, Drama',
'Ballet, Life Lesson, Unusual Friendship, Adapted From A Webtoon, Second Chance, Father-Son Relationship, Character Development, Grandpa-Granddaughter Relationship, Bromance, Kind Male Lead', '#19', 8.9),

('It\'s Okay to Not Be Okay', 2020, 'Jun 20, 2020 - Aug 9, 2020', 'Saturday, Sunday', 16, 'Netflix, tvN', '1 hr. 15 min.', '15+ - Teens 15 or older',
'Moon Gang Tae is a community health worker at a psychiatric ward who was blessed with everything including a great body, smarts, ability to sympathize with others, patience, ability to react quickly, stamina, and more. Meanwhile, Ko Moon Young is a popular writer of children\'s literature who, due to suffering from an antisocial personality disorder, seems extremely selfish, arrogant, and rude.',
'Kim Soo Hyun, Seo Yea Ji, Oh Jung Se, Park Gyu Young, Jang Young Nam, Kim Chang Wan', 'Psychological, Comedy, Romance, Drama',
'Possessive Female Lead, Independent Female Lead, Successful Female Lead, Melodrama, Healing, Selfless Male Lead, Badass Female Lead, Psychiatry, Childhood Connection, Trauma', '#20', 8.9),

('Signal', 2016, 'Jan 22, 2016 - Mar 12, 2016', 'Friday, Saturday', 16, 'tvN', '1 hr. 15 min.', '15+ - Teens 15 or older',
'Fifteen years ago, a young girl was kidnapped on the way from school, and Park Hae Yeong, who was an elementary school student at that time, witnessed the crime. A few days later, the girl was found dead, and the police were not able to find the culprit. As time went by, Hae Yeong started distrusting the police.',
'Lee Je Hoon, Kim Hye Soo, Jo Jin Woong, Kim Won Hae, Lee Yoo Joon, Jang Hyun Sung', 'Thriller, Mystery, Sci-Fi',
'Different Timelines, Butterfly Effect, Murder, Hwaseong Serial Murders, Suspense, Investigation, Death, Tragic Past, Corruption, Time Altering', '#21', 8.9),

('The Glory', 2022, 'Dec 30, 2022', 'Friday', 8, 'Netflix', '50 min.', '18+ Restricted (violence & profanity)',
'A high school student dreams of becoming an architect. However, she had to drop out of school after suffering from brutal school violence. Years later, the perpetrator gets married and has a kid. Once the kid is in elementary school, the former victim becomes her homeroom teacher and starts her thorough revenge towards the perpetrators and bystanders of her bullying days.',
'Song Hye Kyo, Lee Do Hyun, Im Ji Yeon, Yeom Hye Ran, Park Sung Hoon, Jung Sung Il', 'Thriller, Drama, Melodrama',
'Revenge, School Bullying, School Violence, Strong Female Lead, Social Issues, Sexual Content, Antiheroine Female Lead, Doctor Male Lead, Teacher Female Lead, Time Skip', '#22', 8.9);



