--���ڿ� INSERT(STRING, CHAR, [POSITION, OCCURRENCE]) : �ش� ������ �ε����� ������
--EMAIL�� '@VVC.COM' ���ڿ� �� ���� ���� 'C'�� ��ġ��
SELECT  EMAIL,
        INSTR(EMAIL, 'c', -1, 2) AS ��ġ,
        INSTR(EMAIL, 'c', INSTR(EMAIL, '.')-1)
FROM    EMPLOYEE;

--���� ǥ������
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
        TO_CHAR(HIRE_DATE, 'YYYY"��"MM"��"DD"��"') AS �Ի�����
FROM    EMPLOYEE;


