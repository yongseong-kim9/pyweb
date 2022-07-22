SELECT * from T_USER

DROP TABLE T_USER

CREATE TABLE t_user
(
    user_id          VARCHAR2(50)    NOT NULL, 
    user_pw          VARCHAR2(50)    NOT NULL, 
    user_name        VARCHAR2(50)    NOT NULL, 
    user_joindate    DATE            DEFAULT SYSDATE NOT NULL, 
    PRIMARY KEY (user_id)
)

INSERT INTO T_USER(user_id,user_pw,user_name) VALUES('test','test','test')