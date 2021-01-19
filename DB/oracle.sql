--select����
--SELECT   [Ư���÷� | *(��ü�÷�) | ǥ���� | DISTINCT | AS �÷���Ī]
--FROM     ���̺��̸�;
--WHERE    ���ǽ�(���� ����)
--GROUP BY �����÷�
--HAVING   ���ǽ�
--ORDER BY �����÷�; -->��Ī, ��������� ���� ����

--��ü�÷�EMPLOYEE
SELECT *
FROM employee;

--Ư���÷�
SELECT EMP_NAME, 
       EMP_NO
FROM   EMPLOYEE;

--��Ī : �ݵ�� ���ڷ� �����ؾ���(���ڷ� ����X), ���� Ư����ȣ,������ ����""�ٿ�����
--AS�� ������ ������
SELECT EMP_NAME AS "�� ��", 
       EMP_NO AS �ֹι�ȣ, 
       SALARY AS "�޿�(��)", 
       DEPT_ID �μ���ȣ
FROM   EMPLOYEE;


--DISTINCT : ���� �ߺ��� ����
SELECT DISTINCT JOB_ID
FROM EMPLOYEE;

--ǥ���� : �÷����� ���� ������ ������ �ۼ�����
SELECT EMP_NAME AS �����,
       SALARY AS �޿�,
       (SALARY+(SALARY*BONUS_PCT))*12 AS ����
FROM   EMPLOYEE;

--�����÷�
--'������' / "Ű����"
SELECT EMP_ID, 
       EMP_NAME,
       '����' AS �ٹ�����
FROM   EMPLOYEE;

--�μ���ȣ�� 90���� ����� ������ ������
--WHERE : ���� ����
--���������� ���� ��밡�� = �����
SELECT *
FROM   EMPLOYEE
WHERE  dept_id=90;

--�μ��ڵ尡 90���̰� �޿��� 20000000���� ���� �޴� ����� �̸�, �μ��ڵ�, �޿���ȸ
--AND, OR
SELECT DEPT_ID, 
       EMP_NAME, 
       SALARY
FROM   EMPLOYEE
WHERE dept_id=90 AND salary>2000000;
--�μ��ڵ尡 90�̰ų� 20���� ����� �̸�, �ڵ�, �޿�
SELECT EMP_NAME,
       DEPT_ID,
       SALARY
FROM   EMPLOYEE
WHERE  DEPT_ID=90 OR DEPT_ID=20;

--"~���� ������ �� �Դϴ�."
-- || : ���Ῥ����
--�÷�||�÷� / �÷�||"���ڿ�" 
SELECT EMP_ID||'�� ������'||SALARY||'�� �Դϴ�.'
FROM   EMPLOYEE;

--OPERATER : =,<,>,<=,>=,!=
--BETWEEN AND : Ư�� ������ ���ԵǴ��� ��
--LIKE / NOT LIKE : ���������� ��
--IS NULL / IS NOT NULL : NULL�� ���κ�

--�޿��� 3500000���� ���� �ް� 5500000���� ���Թ޴� �����޿�
SELECT EMP_NAME,
       SALARY
FROM   EMPLOYEE
WHERE  SALARY BETWEEN 3500000 AND 5500000;

SELECT EMP_NAME,
       SALARY
FROM   EMPLOYEE
WHERE  SALARY >= 3500000
AND    SALARY <= 5500000;

--�达 ���� ���� ���� �̸��� �޿���ȸ
SELECT EMP_NAME,
       SALARY
FROM EMPLOYEE
WHERE EMP_NAME LIKE '��%';

--9000���� 4�ڸ� ������ ��ȭ��ȣ�� ����ϴ� ���� ��ȭ��ȣ ��ȸ
SELECT EMP_NAME,
       PHONE
FROM   EMPLOYEE
WHERE  PHONE LIKE '___9%';

--�̸��� �ּ��� ����� ���ڸ��� 3�ڶ��� ���� ��ȸ
SELECT EMP_NAME,
       EMAIL
FROM   EMPLOYEE
WHERE  EMAIL LIKE'___@_%'ESCAPE'@'; --_�� ���ڿ��� �����ϰڽ��ϴ�.

--�达 ���� �ƴ� ������ �̸��� �޿��� ��ȸ
SELECT EMP_NAME,
       SALARY
FROM   EMPLOYEE
WHERE  EMP_NAME NOT LIKE '��%';

--�μ��� ���µ��� �ұ��ϰ� ���ʽ��� �޴� ������ �̸�, �μ�, ���ʽ��� ��ȸ
--IS NULL / IS NOT NULL
SELECT EMP_NAME,
       BONUS_PCT,
       DEPT_ID
FROM EMPLOYEE
WHERE DEPT_ID IS NULL AND BONUS_PCT IS NOT NULL;

--IN : OR�� ����
--�μ��ڵ尡 90���̰� �޿��� 20000000���� ���� �޴� ����� �̸�, �μ��ڵ�, �޿���ȸ
SELECT EMP_NAME,
       DEPT_ID,
       SALARY
FROM   EMPLOYEE
WHERE  DEPT_ID IN('90','20');

--�μ���ȣ�� 20 �Ǵ� 90�� ����� �޿��� 3000000�ʰ��� ������ �̸�, �޿�, �μ��ڵ� ��ȸ
SELECT EMP_NAME,
       DEPT_ID,
       SALARY
FROM EMPLOYEE
WHERE DEPT_ID IN('20','90') AND SALARY > 3000000;

--�μ���ȣ�� 50�̰ų� �������� �ʴ� ����� �̸�, �޿� ��ȸ
--���� �޿������� ������ ORDER BY [�����÷�][ASC|DESC]
SELECT  EMP_NAME,
        SALARY
FROM    EMPLOYEE
WHERE   DEPT_ID = '50' OR DEPT_ID IS NULL
ORDER BY    SALARY DESC;

--�Ի����� 03/01/01�� ���� �Ի��ڵ��� �̸�, �Ի���, �μ���ȣ ��ȸ
--�μ���ȣ�� ���������� ����, ���ٸ� �Ի����� ���������� ����, ���ٸ� �̸��� ���������� ����
SELECT  EMP_NAME, HIRE_DATE, DEPT_ID
FROM    EMPLOYEE
WHERE   HIRE_DATE > TO_DATE('03/01/01', 'RR/MM/DD')
ORDER BY DEPT_ID DESC NULLS LAST, HIRE_DATE, EMP_NAME; --NULLS LAST : NULL���� �� �ڷ� ����









       

