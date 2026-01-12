-- 03-insert.sql
INSERT INTO members (name, email, age)
VALUES ('김김김', 'my@email.com', 30);

INSERT INTO members (email) VALUES ('a@a.com');

INSERT INTO members (name) VALUES ('박박박');

INSERT INTO members (name, email)
VALUES
('이이이', 'lee@lee.com'),
('최최최', 'choi@choi.com'),
('정정정', '정@정.com');

-- 테이블 모든 데이터 확인
SELECT * FROM members;




