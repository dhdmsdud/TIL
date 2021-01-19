--GROUP FUNCTION(�׷��Լ�, �����Լ�)
--�׷��Լ��� SELECT���� ���Ǹ� �ٸ� �÷��� ����X
--�׷��Լ��� NULL���� ������ �� ������ �ϹǷ� ����!
--GROUP BY [�����÷�]
SELECT  SUM(SALARY), 
        SUM(DISTINCT SALARY)
FROM    EMPLOYEE;

SELECT  AVG(BONUS_PCT),
        ROUND(AVG(NVL(BONUS_PCT, 0)), 2) --NULL���� 0���� �����ϰ� �Ҽ��� 3°�ڸ����� �ݿø� ��, 2°�ڸ����� ����
FROM    EMPLOYEE;

--MIN, MAX, COUNT --> ANY
SELECT  MIN(SALARY), MAX(SALARY),
        MIN(HIRE_DATE), MAX(HIRE_DATE),
        MIN(JOB_ID), MAX(JOB_ID)
FROM    EMPLOYEE;

SELECT  COUNT(*), 
        COUNT(JOB_ID), --NULL���� �� ��
        COUNT(DISTINCT JOB_ID) --NULL,�ߺ� ���� �� ��
FROM    EMPLOYEE;

--�μ��� �޿����
--�μ��� �޿������ 3000000�� �������
SELECT      DEPT_ID, 
            JOB_ID,
            ROUND(AVG(SALARY), -5) AS �޿����
FROM        EMPLOYEE
GROUP BY    ROLLUP(DEPT_ID, JOB_ID)
--HAVING  AVG (SALARY) > 3000000
ORDER BY    DEPT_ID;

--������ ���� �޿����
SELECT  DECODE(SUBSTR(EMP_NO, 8, 1), 
        '1', '����', '3', '����', '����'),
        AVG(SALARY)
FROM    EMPLOYEE
GROUP BY DECODE(SUBSTR(EMP_NO, 8, 1), 
        '1', '����', '3', '����', '����')
ORDER BY 2 DESC;

SELECT  CASE SUBSTR(EMP_NO,8,1) 
            WHEN '1' THEN '����'
            WHEN '3' THEN '����'
            ELSE '����'
        END,
        AVG(SALARY)
FROM    EMPLOYEE
GROUP BY  CASE SUBSTR(EMP_NO,8,1) 
            WHEN '1' THEN '����'
            WHEN '3' THEN '����'
            ELSE '����'
        END














