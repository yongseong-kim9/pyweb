create table t_espanse( 
exp_seq number not null,
exp_item varchar2(50) not null,
exp_price number not null,
exp_shop varchar2(30) not null,
exp_category varchar2(20) not null,
exp_methode char(1) not null,
exp_date varchar2(30) not null,
user_id varchar2(20) not null
)

SELECT * from T_ESPANSE

insert into t_espanse(
EXP_SEQ,
EXP_ITEM,
EXP_PRICE,
EXP_SHOP,
EXP_CATEGORY,
EXP_METHODE,
EXP_DATE,
USER_ID
) 
VALUES(
1,
'test',
5300,
'커피빈코리아합정',
'a',
'c',
'2020-05-02',
'user_ud01'
)
DROP TABLE t_expense


DELETE FROM t_expense WHERE EXP_SEQ = 1


SELECT *
FROM NLS_SESSION_PARAMETERS;
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD';

SELECT TO_DATE(EXP_DATE,'YYYY-MM-DD') FROM T_ESPANSE;


CREATE TABLE t_expense
(
    exp_seq         NUMBER(18, 0)    , 
    exp_item        VARCHAR2(50)     NOT NULL, 
    exp_price       NUMBER(18, 0)    NOT NULL, 
    exp_shop        VARCHAR2(30)     NOT NULL, 
    exp_category    VARCHAR2(20)     NOT NULL, 
    exp_methode     CHAR(1)          NOT NULL, 
    exp_date        VARCHAR2(20)     NOT NULL, 
    user_id         VARCHAR2(20)     NOT NULL, 
    PRIMARY KEY (exp_seq)
)


CREATE SEQUENCE t_expense_SEQ
START WITH 1
INCREMENT BY 1;


CREATE OR REPLACE TRIGGER t_expense_AI_TRG
BEFORE INSERT ON t_expense 
REFERENCING NEW AS NEW FOR EACH ROW 
BEGIN 
    SELECT t_expense_SEQ.NEXTVAL
    INTO :NEW.exp_seq
    FROM DUAL;
END;

select * from t_expense

INSERT INTO t_expense (exp_item, exp_price, exp_shop, exp_category, exp_methode, exp_date, user_id) VALUES ('exp_item1', 1, 'exp_shop1', 'exp_category1', 'N', '2020-05-20', 'user_id1');