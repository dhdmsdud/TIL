-- 함수는 SELECT, WHERE 에 적용가능
-- LENGTH() : NUMBER -> 문자의 갯수를 반환하는 함수
-- 문자열 함수
-- CHAR(고정길이) -->    나머지 공간에 대해서는 공백으로 처리
-- VARCHAR2(가변길이)--> 나머지 공간에 대해서는 패키지 (왠만하면 해당 문자열을 사용것이 좋다)
-- 한글 1 문자 = 3 byte (예시) 엘지씨엔에스 18 byte
-- 20 - 18 = 2 
--           :
--     6  +  2 = 8 = LENGTH(CHARTYPE)
SELECT  CHARTYPE,
        LENGTH(CHARTYPE),
        VARCHARTYPE,
        LENGTH(VARCHARTYPE)        
FROM    COLUMN_LENGTH;


-- LPAD / RPAD : 문자열의 길이를 덧붙이는 함수
-- 정렬효과를 가져오기 위해서 사용
-- EMAIL 에 30 byte를 주고 비어있는 공간은 '.'로 채워준다
-- LPAD : 문자열을 오른쪽으로 정렬
SELECT  EMAIL,
        LPAD(EMAIL,30,'.')
FROM    EMPLOYEE;

-- RPAD : 문자열을 왼쪽으로 정렬
SELECT  EMAIL,
        RPAD(EMAIL,30,'.')
FROM    EMPLOYEE;

SELECT  EMAIL,
        RPAD(EMAIL,30,'.'),
        LPAD(EMAIL,30,''),
        LENGTH(LPAD(EMAIL,30,''))
FROM    EMPLOYEE;


-- TRIM: 문자를 제거할때 사용하는 함수
-- LTRIM : 문자열의 오른쪽을 제거 / RTRIM : 문자열의 왼쪽을 제거
SELECT  LTRIM('  TEST  '),
        LENGTH(LTRIM('  TEST  ')),
        LTRIM('123123TEST','123'),  -- 문자 한칸씩 1 또는 2 또는 3 값을 찾아 제거
        LTRIM('XYZYYTEST','XYZ'),   -- 문자 한칸씩 X 또는 Y 또는 Z 값을 찾아 제거
        TRIM(LEADING  '1'  FROM 'TEST1'),       -- LTRIM 기능과 동일 ,'1' 없기 때문에 삭제할 내용 X
        TRIM(TRAILING '1'  FROM '123TEST111')   -- RTRIM 기능과 동일 , 문자의 '1' 삭제
FROM    DUAL;


-- SUBSTR  : 문자, 날짜 추출
--python과 다르게 인덱스 번지가 1로 시작함
SELECT  SUBSTR('This.is.a.test', 6, 2),     -- 6번째 부터 시작하여 2개의 문자를 가져온다
        SUBSTR('This.is.a.test', 6),        -- 6번째 부터 문자의 전체를 가져온다
        SUBSTR('이것은.연습입니다', 3, 4),     
        SUBSTR('TechOnTheNet', 1, 4),
        SUBSTR('TechOnTheNet', -3, 3),      --python과 다르게 인덱스 번지가 1로 시작함
        SUBSTR('TechOnTheNet', -6, 3),
        SUBSTR('TechOnTheNet', -8, 2)
FROM    DUAL;


-- ROUND : 지정한 자릿수에서 반올림하는 함수
SELECT  ROUND(123.315),     
        ROUND(123.315, 0), 
        ROUND(123.315, 1),  
        ROUND(123.315, -1), 
        ROUND(123.315, 3),  
        ROUND(-123.315, 2)   
FROM    DUAL;


-- TRUNC : 지정한 자릿수에서 버림하는 함수
SELECT  TRUNC(123.315),    
        TRUNC(123.315, 0), 
        TRUNC(123.315, 1),   
        TRUNC(123.315, -1), 
        TRUNC(123.315, 3),  
        TRUNC(-123.315, -3) 
FROM    DUAL;


--날짜함수
SELECT  SYSDATE
FROM    DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        ADD_MONTHS(HIRE_DATE, 240)  -- 240개월 후의 값 출력
FROM    EMPLOYEE;

SELECT  MONTHS_BETWEEN (SYSDATE, '21/03/14'),
        MONTHS_BETWEEN (SYSDATE, '20/03/14'),
        MONTHS_BETWEEN (SYSDATE, '21/01/19'),
        MONTHS_BETWEEN (SYSDATE, '20/11/19')
FROM    DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        MONTHS_BETWEEN (SYSDATE, HIRE_DATE)/12 AS 근무년수
FROM    EMPLOYEE
WHERE   MONTHS_BETWEEN (SYSDATE, HIRE_DATE) > 120;


-- 문자열함수 INSTR(string, searchChar, [position, occurrence]) : 해당 문자의 인덱스번지를 리턴
-- EMAIL 컬럼 값의 '@vcc.com'문자열 중 . 앞의 문자 'c' 위치
SELECT  *
FROM    EMPLOYEE ;

SELECT  EMAIL,
        INSTR(EMAIL , 'c'),
        INSTR(EMAIL , 'c', -1, 2),
        INSTR(EMAIL , 'c', INSTR(EMAIL , '.')-1)
FROM    EMPLOYEE ;
--문자열 INSERT(STRING, CHAR, [POSITION, OCCURRENCE]) : 해당 문자의 인덱스를 리턴함
--EMAIL의 '@VVC.COM' 문자열 중 앞의 문자 'C'의 위치를
SELECT  EMAIL,
        INSTR(EMAIL, 'c', -1, 2) AS 위치,
        INSTR(EMAIL, 'c', INSTR(EMAIL, '.')-1)
FROM    EMPLOYEE;

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
        TO_CHAR(HIRE_DATE, 'YYYY"년"MM"월"DD"일"') AS 입사일자,
        SUBSTR(HIRE_DATE, 1, 2) || '년' ||
        SUBSTR(HIRE_DATE, 4, 2) || '월' ||
        SUBSTR(HIRE_DATE, 7, 2) || '일' AS 입사일자
FROM    EMPLOYEE;

--TO_DATE
SELECT  TO_DATE('20210119', 'YYYYMMDD')
FROM    DUAL;

SELECT  TO_CHAR(TO_DATE('20210119', 'YYYYMMDD'), 'YYYY, MON')
FROM    DUAL;

SELECT TO_DATE('210119 132000', 'YYMMDD HH24MISS')
FROM    DUAL;

SELECT TO_CHAR(TO_DATE('210119 132000', 'YYMMDD HH24MISS'), 'DD-MON-YY HH:MI:SS PM')
FROM    DUAL;

SELECT TO_DATE('210119', 'YYMMDD')
FROM    DUAL;

SELECT TO_CHAR(TO_DATE('210119', 'YYMMDD'), 'YYYY.MM.DD')
FROM    DUAL;

SELECT  HIRE_DATE
FROM    EMPLOYEE
WHERE   HIRE_DATE = TO_DATE('900401 133030', 'YYMMDD HH24MISS') --연,월,일 이외의 시,분,초가 있는걸 알때 사용

SELECT  HIRE_DATE
FROM    EMPLOYEE
WHERE   TO_CHAR(HIRE_DATE, 'YYMMDD') = '900401'; --시,분,초가 들어있는 경우를 모를때 사용

--YYYY(현재세기를 기준) / RRRR(세기를 구분)
SELECT  EMP_NAME,
        HIRE_DATE,
        TO_CHAR(HIRE_DATE, 'YYYY/MM/DD')
FROM    EMPLOYEE
WHERE   EMP_NAME = '한선기';

SELECT  EMP_NAME,
        HIRE_DATE,
        TO_CHAR (TO_DATE(HIRE_DATE, 'RR/MM/DD'), 'RRRR')
FROM    EMPLOYEE
WHERE   EMP_NAME = '한선기';

--TO_NUMBER : CHAR 형식을  NUMBER타입으로 변환
SELECT  EMP_NO,
        SUBSTR(EMP_NO, 1, 6),
        SUBSTR(EMP_NO, 8),
        TO_NUMBER(SUBSTR(EMP_NO, 1, 6) + SUBSTR(EMP_NO, 8))
FROM    EMPLOYEE;

--NVL : NULL을 지정한 값으로 변환하는 함수
SELECT  EMP_NAME, SALARY, NVL(BONUS_PCT, 0)
FROM    EMPLOYEE   
WHERE   SALARY > 350000;

SELECT EMP_NAME,
       (SALARY*12) + ((SALARY*12)*NVL(BONUS_PCT, 0))
FROM    EMPLOYEE
WHERE SALARY > 3500000;

--DECODE : SELECT 구문으로 IF-ELSE 논리를 제한적으로 구현한 함수
SELECT  EMP_NO,
        DECODE(SUBSTR(EMP_NO, 8, 1), '1', '남자', '3', '남자', '여자') AS GENDER
FROM    EMPLOYEE;

SELECT  EMP_ID,
        EMP_NAME,
        DECODE(MGR_ID, NULL, 'ADMIN', MGR_ID) AS MANAGER
FROM    EMPLOYEE
WHERE   JOB_ID = 'J4';

--직원의 직급별 인상급여 확인
--J7:20% J6:15%
SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        DECODE(JOB_ID, 'J7', SALARY * 1.2, 'J6', SALARY * 1.15, SALARY) AS "인상 급여"
FROM    EMPLOYEE;

--CASE
SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        CASE JOB_ID
            WHEN 'J7' THEN SALARY*1.2
            WHEN 'J6' THEN SALARY*1.15
            ELSE SALARY
        END AS "인상 급여"
FROM    EMPLOYEE;

SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        CASE WHEN JOB_ID = 'J7' THEN SALARY*1.2
             WHEN JOB_ID = 'J6' THEN SALARY*1.15
             ELSE SALARY
        END AS "인상 급여"
FROM    EMPLOYEE;

