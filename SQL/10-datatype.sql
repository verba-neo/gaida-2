-- 09-datatype.sql

CREATE TABLE dt_demo (
    id            INT           GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name          VARCHAR(20)   NOT NULL,
    nickname      VARCHAR(20),
    birth         DATE,             -- YYYY-MM-DD
    score         FLOAT,            -- 소수점 포함 저장 가능. 정확도 100% 아님
    salary        DECIMAL(20, 3),   -- 전체 20자리, 소수점 이하 3자리. 정확도 100%
    description   TEXT,             -- 길이제한 없는 문자열
    is_active     BOOL          DEFAULT TRUE,  -- 참/거짓
    created_at    TIMESTAMP     DEFAULT CURRENT_TIMESTAMP  -- 날짜 + 시간
);