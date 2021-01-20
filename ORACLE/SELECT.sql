--select구문
--SELECT   [특정컬럼 | *(전체컬럼) | 표현식 | DISTINCT | AS 컬럼명칭]
--FROM     테이블이름;
--WHERE    조건식(행의 제한)
--GROUP BY 기준컬럼
--HAVING   조건식
--ORDER BY 기준컬럼; -->별칭, 기술순서로 변경 가능

--전체컬럼EMPLOYEE
SELECT *
FROM employee;

--특정컬럼
SELECT EMP_NAME, 
       EMP_NO
FROM   EMPLOYEE;

--별칭 : 반드시 문자로 시작해야함(숫자로 시작X), 만약 특수부호,공백이 들어가면""붙여야함
--AS는 생략이 가능함
SELECT EMP_NAME AS "이 름", 
       EMP_NO AS 주민번호, 
       SALARY AS "급여(원)", 
       DEPT_ID 부서번호
FROM   EMPLOYEE;


--DISTINCT : 값의 중복을 제거
SELECT DISTINCT JOB_ID
FROM EMPLOYEE;

--표현식 : 컬럼값에 대한 연산을 식으로 작성가능
SELECT EMP_NAME AS 사원명,
       SALARY AS 급여,
       (SALARY+(SALARY*BONUS_PCT))*12 AS 연봉
FROM   EMPLOYEE;

--더미컬럼
--'데이터' / "키워드"
SELECT EMP_ID, 
       EMP_NAME,
       '재직' AS 근무여부
FROM   EMPLOYEE;

--부서번호가 90번인 사원들 정보만 가져옴
--WHERE : 행의 제한
--조건절에서 연산 사용가능 = 동등비교
SELECT *
FROM   EMPLOYEE
WHERE  dept_id=90;

--부서코드가 90번이고 급여를 20000000보다 많이 받는 사원의 이름, 부서코드, 급여조회
--AND, OR
SELECT DEPT_ID, 
       EMP_NAME, 
       SALARY
FROM   EMPLOYEE
WHERE dept_id=90 AND salary>2000000;
--부서코드가 90이거나 20번인 사원의 이름, 코드, 급여
SELECT EMP_NAME,
       DEPT_ID,
       SALARY
FROM   EMPLOYEE
WHERE  DEPT_ID=90 OR DEPT_ID=20;

--"~님의 월급은 원 입니다."
-- || : 연결연산자
--컬럼||컬럼 / 컬럼||"문자열" 
SELECT EMP_ID||'의 월급은'||SALARY||'원 입니다.'
FROM   EMPLOYEE;

--OPERATER : =,<,>,<=,>=,!=
--BETWEEN AND : 특정 범위에 포함되는지 비교
--LIKE / NOT LIKE : 문자패턴을 비교
--IS NULL / IS NOT NULL : NULL의 여부비교

--급여를 3500000보다 많이 받고 5500000보다 적게받는 직원급여
SELECT EMP_NAME,
       SALARY
FROM   EMPLOYEE
WHERE  SALARY BETWEEN 3500000 AND 5500000;

SELECT EMP_NAME,
       SALARY
FROM   EMPLOYEE
WHERE  SALARY >= 3500000
AND    SALARY <= 5500000;

--김씨 성을 가진 직원 이름과 급여조회
SELECT EMP_NAME,
       SALARY
FROM EMPLOYEE
WHERE EMP_NAME LIKE '김%';

--9000번대 4자리 국번의 전화번호를 사용하는 직원 전화번호 조회
SELECT EMP_NAME,
       PHONE
FROM   EMPLOYEE
WHERE  PHONE LIKE '___9%';

--이메일 주소의 언더바 앞자리가 3자라인 직원 조회
SELECT EMP_NAME,
       EMAIL
FROM   EMPLOYEE
WHERE  EMAIL LIKE'___@_%'ESCAPE'@'; --_를 문자열로 지정하겠습니다.

--김씨 성이 아닌 직원의 이름과 급여를 조회
SELECT EMP_NAME,
       SALARY
FROM   EMPLOYEE
WHERE  EMP_NAME NOT LIKE '김%';

--부서가 없는데도 불구하고 보너스를 받는 직원의 이름, 부서, 보너스를 조회
--IS NULL / IS NOT NULL
SELECT EMP_NAME,
       BONUS_PCT,
       DEPT_ID
FROM EMPLOYEE
WHERE DEPT_ID IS NULL AND BONUS_PCT IS NOT NULL;

--IN : OR와 동일
--부서코드가 90번이고 급여를 20000000보다 많이 받는 사원의 이름, 부서코드, 급여조회
SELECT EMP_NAME,
       DEPT_ID,
       SALARY
FROM   EMPLOYEE
WHERE  DEPT_ID IN('90','20');

--부서번호가 20 또는 90인 사원중 급여가 3000000초과인 직원의 이름, 급여, 부서코드 조회
SELECT EMP_NAME,
       DEPT_ID,
       SALARY
FROM EMPLOYEE
WHERE DEPT_ID IN('20','90') AND SALARY > 3000000;

--부서번호가 50이거나 존재하지 않는 사원의 이름, 급여 조회
--높은 급여순으로 보려면 ORDER BY [기준컬럼][ASC|DESC]
SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
WHERE   DEPT_ID = '50' OR DEPT_ID IS NULL
ORDER BY    SALARY DESC;

--입사일이 03/01/01일 이후 입사자들의 이름, 입사일, 부서번호 조회
--부서번호가 높은순으로 정렬, 같다면 입사일이 빠른순으로 정렬, 같다면 이름이 빠른순으로 정렬
SELECT  EMP_NAME, HIRE_DATE, DEPT_ID
FROM    EMPLOYEE
WHERE   HIRE_DATE > TO_DATE('03/01/01', 'RR/MM/DD')
ORDER BY DEPT_ID DESC NULLS LAST, HIRE_DATE, EMP_NAME; --NULLS LAST : NULL값을 맨 뒤로 정렬









       

