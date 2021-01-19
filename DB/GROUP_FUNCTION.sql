--GROUP FUNCTION(그룹함수, 집계함수)
--그룹함수가 SELECT절에 사용되면 다른 컬럼은 정의X
--그룹함수는 NULL값을 제거한 후 연산을 하므로 주의!
--GROUP BY [기준컬럼]
SELECT  SUM(SALARY), 
        SUM(DISTINCT SALARY)
FROM    EMPLOYEE;

SELECT  AVG(BONUS_PCT),
        ROUND(AVG(NVL(BONUS_PCT, 0)), 2) --NULL값을 0으로 지정하고 소숫점 3째자리에서 반올림 후, 2째자리까지 리턴
FROM    EMPLOYEE;

--MIN, MAX, COUNT --> ANY
SELECT  MIN(SALARY), MAX(SALARY),
        MIN(HIRE_DATE), MAX(HIRE_DATE),
        MIN(JOB_ID), MAX(JOB_ID)
FROM    EMPLOYEE;

SELECT  COUNT(*), 
        COUNT(JOB_ID), --NULL값을 뺀 수
        COUNT(DISTINCT JOB_ID) --NULL,중복 값을 뺀 수
FROM    EMPLOYEE;

--부서별 급여평균
--부서별 급여평균이 3000000이 넘을경우
SELECT      DEPT_ID, 
            JOB_ID,
            ROUND(AVG(SALARY), -5) AS 급여평균
FROM        EMPLOYEE
GROUP BY    ROLLUP(DEPT_ID, JOB_ID)
--HAVING  AVG (SALARY) > 3000000
ORDER BY    DEPT_ID;

--성별에 따른 급여평균
SELECT  DECODE(SUBSTR(EMP_NO, 8, 1), 
        '1', '남자', '3', '남자', '여자'),
        AVG(SALARY)
FROM    EMPLOYEE
GROUP BY DECODE(SUBSTR(EMP_NO, 8, 1), 
        '1', '남자', '3', '남자', '여자')
ORDER BY 2 DESC;

SELECT  CASE SUBSTR(EMP_NO,8,1) 
            WHEN '1' THEN '남자'
            WHEN '3' THEN '남자'
            ELSE '여자'
        END,
        AVG(SALARY)
FROM    EMPLOYEE
GROUP BY  CASE SUBSTR(EMP_NO,8,1) 
            WHEN '1' THEN '남자'
            WHEN '3' THEN '남자'
            ELSE '여자'
        END














