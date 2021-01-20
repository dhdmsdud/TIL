-- �Լ��� SELECT, WHERE �� ���밡��
-- LENGTH() : NUMBER -> ������ ������ ��ȯ�ϴ� �Լ�
-- ���ڿ� �Լ�
-- CHAR(��������) -->    ������ ������ ���ؼ��� �������� ó��
-- VARCHAR2(��������)--> ������ ������ ���ؼ��� ��Ű�� (�ظ��ϸ� �ش� ���ڿ��� ������ ����)
-- �ѱ� 1 ���� = 3 byte (����) ������������ 18 byte
-- 20 - 18 = 2 
--           :
--     6  +  2 = 8 = LENGTH(CHARTYPE)
SELECT  CHARTYPE,
        LENGTH(CHARTYPE),
        VARCHARTYPE,
        LENGTH(VARCHARTYPE)        
FROM    COLUMN_LENGTH;


-- LPAD / RPAD : ���ڿ��� ���̸� �����̴� �Լ�
-- ����ȿ���� �������� ���ؼ� ���
-- EMAIL �� 30 byte�� �ְ� ����ִ� ������ '.'�� ä���ش�
-- LPAD : ���ڿ��� ���������� ����
SELECT  EMAIL,
        LPAD(EMAIL,30,'.')
FROM    EMPLOYEE;

-- RPAD : ���ڿ��� �������� ����
SELECT  EMAIL,
        RPAD(EMAIL,30,'.')
FROM    EMPLOYEE;

SELECT  EMAIL,
        RPAD(EMAIL,30,'.'),
        LPAD(EMAIL,30,''),
        LENGTH(LPAD(EMAIL,30,''))
FROM    EMPLOYEE;


-- TRIM: ���ڸ� �����Ҷ� ����ϴ� �Լ�
-- LTRIM : ���ڿ��� �������� ���� / RTRIM : ���ڿ��� ������ ����
SELECT  LTRIM('  TEST  '),
        LENGTH(LTRIM('  TEST  ')),
        LTRIM('123123TEST','123'),  -- ���� ��ĭ�� 1 �Ǵ� 2 �Ǵ� 3 ���� ã�� ����
        LTRIM('XYZYYTEST','XYZ'),   -- ���� ��ĭ�� X �Ǵ� Y �Ǵ� Z ���� ã�� ����
        TRIM(LEADING  '1'  FROM 'TEST1'),       -- LTRIM ��ɰ� ���� ,'1' ���� ������ ������ ���� X
        TRIM(TRAILING '1'  FROM '123TEST111')   -- RTRIM ��ɰ� ���� , ������ '1' ����
FROM    DUAL;


-- SUBSTR  : ����, ��¥ ����
--python�� �ٸ��� �ε��� ������ 1�� ������
SELECT  SUBSTR('This.is.a.test', 6, 2),     -- 6��° ���� �����Ͽ� 2���� ���ڸ� �����´�
        SUBSTR('This.is.a.test', 6),        -- 6��° ���� ������ ��ü�� �����´�
        SUBSTR('�̰���.�����Դϴ�', 3, 4),     
        SUBSTR('TechOnTheNet', 1, 4),
        SUBSTR('TechOnTheNet', -3, 3),      --python�� �ٸ��� �ε��� ������ 1�� ������
        SUBSTR('TechOnTheNet', -6, 3),
        SUBSTR('TechOnTheNet', -8, 2)
FROM    DUAL;


-- ROUND : ������ �ڸ������� �ݿø��ϴ� �Լ�
SELECT  ROUND(123.315),     
        ROUND(123.315, 0), 
        ROUND(123.315, 1),  
        ROUND(123.315, -1), 
        ROUND(123.315, 3),  
        ROUND(-123.315, 2)   
FROM    DUAL;


-- TRUNC : ������ �ڸ������� �����ϴ� �Լ�
SELECT  TRUNC(123.315),    
        TRUNC(123.315, 0), 
        TRUNC(123.315, 1),   
        TRUNC(123.315, -1), 
        TRUNC(123.315, 3),  
        TRUNC(-123.315, -3) 
FROM    DUAL;


--��¥�Լ�
SELECT  SYSDATE
FROM    DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        ADD_MONTHS(HIRE_DATE, 240)  -- 240���� ���� �� ���
FROM    EMPLOYEE;

SELECT  MONTHS_BETWEEN (SYSDATE, '21/03/14'),
        MONTHS_BETWEEN (SYSDATE, '20/03/14'),
        MONTHS_BETWEEN (SYSDATE, '21/01/19'),
        MONTHS_BETWEEN (SYSDATE, '20/11/19')
FROM    DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        MONTHS_BETWEEN (SYSDATE, HIRE_DATE)/12 AS �ٹ����
FROM    EMPLOYEE
WHERE   MONTHS_BETWEEN (SYSDATE, HIRE_DATE) > 120;


-- ���ڿ��Լ� INSTR(string, searchChar, [position, occurrence]) : �ش� ������ �ε��������� ����
-- EMAIL �÷� ���� '@vcc.com'���ڿ� �� . ���� ���� 'c' ��ġ
SELECT  *
FROM    EMPLOYEE ;

SELECT  EMAIL,
        INSTR(EMAIL , 'c'),
        INSTR(EMAIL , 'c', -1, 2),
        INSTR(EMAIL , 'c', INSTR(EMAIL , '.')-1)
FROM    EMPLOYEE ;
--���ڿ� INSERT(STRING, CHAR, [POSITION, OCCURRENCE]) : �ش� ������ �ε����� ������
--EMAIL�� '@VVC.COM' ���ڿ� �� ���� ���� 'C'�� ��ġ��
SELECT  EMAIL,
        INSTR(EMAIL, 'c', -1, 2) AS ��ġ,
        INSTR(EMAIL, 'c', INSTR(EMAIL, '.')-1)
FROM    EMPLOYEE;

--TO_CHAR(��¥ | ����, 'ǥ������') --> CHAR�������� ����
SELECT  TO_CHAR(1234, '99999') --�ڸ��� ����
FROM    DUAL;

SELECT  TO_CHAR(1234, '09999') --���� �ڸ����� 0���� ����
FROM    DUAL;

SELECT  TO_CHAR(1234, 'L99999') --��ȭ��ȣ ǥ��
FROM    DUAL;

SELECT  TO_CHAR(1234, '99,999')
FROM    DUAL;

SELECT  TO_CHAR(1234, '999') --�ڸ����� ���� ������ ����
FROM    DUAL;

SELECT  SYSDATE,
        TO_CHAR(SYSDATE, 'YYYY-MM-DD DAY AM HH:MI:SS')
FROM    DUAL;

SELECT  EMP_NAME,
        HIRE_DATE,
        TO_CHAR(HIRE_DATE, 'YYYY"��"MM"��"DD"��"') AS �Ի�����,
        SUBSTR(HIRE_DATE, 1, 2) || '��' ||
        SUBSTR(HIRE_DATE, 4, 2) || '��' ||
        SUBSTR(HIRE_DATE, 7, 2) || '��' AS �Ի�����
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
WHERE   HIRE_DATE = TO_DATE('900401 133030', 'YYMMDD HH24MISS') --��,��,�� �̿��� ��,��,�ʰ� �ִ°� �˶� ���

SELECT  HIRE_DATE
FROM    EMPLOYEE
WHERE   TO_CHAR(HIRE_DATE, 'YYMMDD') = '900401'; --��,��,�ʰ� ����ִ� ��츦 �𸦶� ���

--YYYY(���缼�⸦ ����) / RRRR(���⸦ ����)
SELECT  EMP_NAME,
        HIRE_DATE,
        TO_CHAR(HIRE_DATE, 'YYYY/MM/DD')
FROM    EMPLOYEE
WHERE   EMP_NAME = '�Ѽ���';

SELECT  EMP_NAME,
        HIRE_DATE,
        TO_CHAR (TO_DATE(HIRE_DATE, 'RR/MM/DD'), 'RRRR')
FROM    EMPLOYEE
WHERE   EMP_NAME = '�Ѽ���';

--TO_NUMBER : CHAR ������  NUMBERŸ������ ��ȯ
SELECT  EMP_NO,
        SUBSTR(EMP_NO, 1, 6),
        SUBSTR(EMP_NO, 8),
        TO_NUMBER(SUBSTR(EMP_NO, 1, 6) + SUBSTR(EMP_NO, 8))
FROM    EMPLOYEE;

--NVL : NULL�� ������ ������ ��ȯ�ϴ� �Լ�
SELECT  EMP_NAME, SALARY, NVL(BONUS_PCT, 0)
FROM    EMPLOYEE   
WHERE   SALARY > 350000;

SELECT EMP_NAME,
       (SALARY*12) + ((SALARY*12)*NVL(BONUS_PCT, 0))
FROM    EMPLOYEE
WHERE SALARY > 3500000;

--DECODE : SELECT �������� IF-ELSE ���� ���������� ������ �Լ�
SELECT  EMP_NO,
        DECODE(SUBSTR(EMP_NO, 8, 1), '1', '����', '3', '����', '����') AS GENDER
FROM    EMPLOYEE;

SELECT  EMP_ID,
        EMP_NAME,
        DECODE(MGR_ID, NULL, 'ADMIN', MGR_ID) AS MANAGER
FROM    EMPLOYEE
WHERE   JOB_ID = 'J4';

--������ ���޺� �λ�޿� Ȯ��
--J7:20% J6:15%
SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        DECODE(JOB_ID, 'J7', SALARY * 1.2, 'J6', SALARY * 1.15, SALARY) AS "�λ� �޿�"
FROM    EMPLOYEE;

--CASE
SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        CASE JOB_ID
            WHEN 'J7' THEN SALARY*1.2
            WHEN 'J6' THEN SALARY*1.15
            ELSE SALARY
        END AS "�λ� �޿�"
FROM    EMPLOYEE;

SELECT  EMP_NAME,
        JOB_ID,
        SALARY,
        CASE WHEN JOB_ID = 'J7' THEN SALARY*1.2
             WHEN JOB_ID = 'J6' THEN SALARY*1.15
             ELSE SALARY
        END AS "�λ� �޿�"
FROM    EMPLOYEE;

