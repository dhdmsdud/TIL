--문자열 INSERT(STRING, CHAR, [POSITION, OCCURRENCE]) : 해당 문자의 인덱스를 리턴함
--EMAIL의 '@VVC.COM' 문자열 중 앞의 문자 'C'의 위치를
SELECT  EMAIL,
        INSTR(EMAIL, 'c', -1, 2) AS 위치,
        INSTR(EMAIL, 'c', INSTR(EMAIL, '.')-1)
FROM    EMPLOYEE;

--숫자 표현형식
--TO_CHAR(날짜 | 숫자, '표현형식') --> CHAR형식으로 리턴
SELECT  TO_CHAR(1234, '99999') --자릿수 지정
FROM    DUAL;

SELECT  TO_CHAR(1234, '09999') --남는 자릿수는 0으로 지정
FROM    DUAL;

SELECT  TO_CHAR(1234, 'L99999') --통화기호 표시
FROM    DUAL;

SELECT  TO_CHAR(1234, '99,999')
FROM    DUAL;

SELECT  TO_CHAR(1234, '999') --자릿수가 맞지 않으면 오류
FROM    DUAL;

SELECT  SYSDATE,
        TO_CHAR(SYSDATE, 'YYYY-MM-DD DAY AM HH:MI:SS')
FROM    DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        TO_CHAR(HIRE_DATE, 'YYYY"년"MM"월"DD"일"') AS 입사일자
FROM    EMPLOYEE;


