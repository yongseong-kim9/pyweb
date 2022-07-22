DROP TABLE T_ESPANSE


create table t_espanse( 
exp_seq number not null,
exp_item varchar2(50) not null,
exp_price number not null,
exp_shop varchar2(30) not null,
exp_category varchar2(20) not null,
exp_methode char(1) not null,
exp_date date not null,
user_id varchar2(20) not null
)

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

SELECT *
FROM NLS_SESSION_PARAMETERS;
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD';


SELECT * from T_ESPANSE
