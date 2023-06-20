INSERT INTO person (name, tg_name, tg_user_id, tg_chat_id)
VALUES
    ('Alice', 'alicetg', '1111', 'chat1'),
    ('Bob', 'bobtg', '2222', 'chat2'),
    ('Charlie', 'charlietg', '3333', 'chat3'),
    ('David', 'davidtg', '4444', 'chat4'),
    ('Emily', 'emilytg', '5555', 'chat5'),
    ('Frank', 'franktg', '6666', 'chat6'),
    ('Grace', 'gracetg', '7777', 'chat7'),
    ('Henry', 'henrytg', '8888', 'chat8'),
    ('Isabella', 'isabellatg', '9999', 'chat9'),
    ('Jack', 'jacktg', '1010', 'chat10');


INSERT INTO meetup (
  title, organizer, description, start_date, 
  end_date
) 
SELECT 
  'PyCon 2023' as title, 
  id as organizer, 
  'Join us for PyCon 2023, the annual gathering of Python enthusiasts. This event will feature keynote speeches, technical sessions, workshops, and networking opportunities' as description, 
  TIMESTAMP '2023-05-30 10:00:00' as start_date, 
  TIMESTAMP '2023-05-31 19:00:00' as end_date 
FROM 
  person 
LIMIT 
  1;


INSERT INTO talk (title, meetup, speaker, description, start_date, end_date)
SELECT
  CASE
    WHEN ROW_NUMBER() OVER () = 1 THEN 'Introduction to Python'
    WHEN ROW_NUMBER() OVER () = 2 THEN 'Advanced Python Techniques'
    WHEN ROW_NUMBER() OVER () = 3 THEN 'Python for Data Science'
    WHEN ROW_NUMBER() OVER () = 4 THEN 'Python Web Development'
    WHEN ROW_NUMBER() OVER () = 5 THEN 'Python Machine Learning'
  END AS title,
  meetup.id AS meetup,
  person.id AS speaker,
  CASE
    WHEN ROW_NUMBER() OVER () = 1 THEN 'Introduction to Python: This talk provides an introductory overview of the Python programming language, covering its syntax, data types, control flow, and basic concepts. It is aimed at beginners who want to learn the fundamentals of Python and understand its versatility and ease of use.'
    WHEN ROW_NUMBER() OVER () = 2 THEN 'Advanced Python Techniques: This talk explores advanced techniques and features in Python, including topics such as metaprogramming, decorators, generators, context managers, and concurrency. It is intended for experienced Python developers who want to deepen their understanding and learn more sophisticated programming techniques.'
    WHEN ROW_NUMBER() OVER () = 3 THEN 'Python for Data Science: This talk focuses on using Python for data analysis, manipulation, and visualization. It covers popular data science libraries such as NumPy, Pandas, Matplotlib, and scikit-learn, showcasing how Python can be used to explore and derive insights from data.'
    WHEN ROW_NUMBER() OVER () = 4 THEN 'Python Web Development: This talk highlights the use of Python in web development, covering frameworks like Django or Flask, database integration, and building RESTful APIs. It demonstrates how Python can be leveraged to create dynamic, scalable, and interactive web applications.'
    WHEN ROW_NUMBER() OVER () = 5 THEN 'Python Machine Learning: This talk explores the field of machine learning using Python, showcasing libraries like TensorFlow, Keras, or scikit-learn. It covers topics such as supervised and unsupervised learning, model training and evaluation, and applying machine learning algorithms to real-world problems.'
  END AS description,
  CASE
    WHEN ROW_NUMBER() OVER () = 1 THEN TIMESTAMP '2023-05-30 10:00:00'
    WHEN ROW_NUMBER() OVER () = 2 THEN TIMESTAMP '2023-05-30 11:00:00'
    WHEN ROW_NUMBER() OVER () = 3 THEN TIMESTAMP '2023-05-30 12:00:00'
    WHEN ROW_NUMBER() OVER () = 4 THEN TIMESTAMP '2023-05-30 13:00:00'
    WHEN ROW_NUMBER() OVER () = 5 THEN TIMESTAMP '2023-05-30 14:00:00'
  END AS start_date,
  CASE
    WHEN ROW_NUMBER() OVER () = 1 THEN TIMESTAMP '2023-05-30 10:50:00'
    WHEN ROW_NUMBER() OVER () = 2 THEN TIMESTAMP '2023-05-30 11:50:00'
    WHEN ROW_NUMBER() OVER () = 3 THEN TIMESTAMP '2023-05-30 12:50:00'
    WHEN ROW_NUMBER() OVER () = 4 THEN TIMESTAMP '2023-05-30 13:50:00'
    WHEN ROW_NUMBER() OVER () = 5 THEN TIMESTAMP '2023-05-30 14:50:00'
  END AS end_date
FROM
  meetup
INNER JOIN
  person ON TRUE
LIMIT 5;

INSERT INTO profile (person, bio, website)
select 
  person.id as person,
  CASE
    WHEN ROW_NUMBER() OVER () = 1 THEN 'Passionate about technology and coding. Love to explore new programming languages and frameworks.'
    WHEN ROW_NUMBER() OVER () = 2 THEN 'Enthusiastic Python developer with a keen interest in web development and machine learning.'
    WHEN ROW_NUMBER() OVER () = 3 THEN 'Experienced software engineer specializing in backend development and database management.'
    WHEN ROW_NUMBER() OVER () = 4 THEN 'Full-stack developer with expertise in building scalable and performant web applications.'
    WHEN ROW_NUMBER() OVER () = 5 THEN 'Data science enthusiast with a strong background in statistical analysis and machine learning algorithms.'
  END AS bio,
   CASE
    WHEN ROW_NUMBER() OVER () = 1 THEN 'https://www.facebook.com/Passionate'
    WHEN ROW_NUMBER() OVER () = 2 THEN 'https://www.facebook.com/Enthusiastic'
    WHEN ROW_NUMBER() OVER () = 3 THEN 'https://www.facebook.com/Experienced'
    WHEN ROW_NUMBER() OVER () = 4 THEN 'https://www.facebook.com/Fullstack'
    WHEN ROW_NUMBER() OVER () = 5 THEN 'https://www.facebook.com/Datascience'
  END AS website
from 
  person 
limit 
  5;
