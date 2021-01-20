--1. �л��̸��� �ּ����� ǥ���Ͻÿ�. 
--��, ��� ����� "�л� �̸�", "�ּ���"�� �ϰ�, ������ �̸����� �������� ǥ��
SELECT  STUDENT_NAME AS "�л� �̸�", 
        STUDENT_ADDRESS AS �ּ���
FROM    TB_STUDENT
ORDER BY STUDENT_NAME;

--2.  �������� �л����� �̸��� �ֹι�ȣ�� ���̰� ���� ������ ȭ�鿡 ����Ͻÿ�.
SELECT  STUDENT_NAME,
        STUDENT_SSN
FROM    TB_STUDENT
WHERE   ABSENCE_YN = 'Y'
ORDER BY 2 DESC;

--3. �ּ����� �������� ��⵵�� �л��� �� 1900��� �й��� ���� �л����� �̸��� �й�, �ּҸ� �̸��� ������������ ȭ�鿡 ����Ͻÿ�.
--��, ���������� "�л��̸�","�й�", "������ �ּ�" �� ��µǵ��� �Ѵ�.
SELECT  STUDENT_NAME AS �л��̸�, 
        STUDENT_NO AS �й�, 
        STUDENT_ADDRESS AS "������ �ּ�"
FROM    TB_STUDENT
WHERE   STUDENT_ADDRESS LIKE '��⵵%' AND STUDENT_NO LIKE '9%'
ORDER BY STUDENT_NAME ASC;

--4. ���� ���а� ���� �� ���� ���̰� ���� ������� �̸��� Ȯ���� �� �ִ� SQL ������ �ۼ��Ͻÿ�. 
--(���а��� '�а��ڵ�'�� �а� ���̺�(TB_DEPARTMENT)�� ��ȸ�ؼ� ã�� ������ ����) / 005
SELECT  PROFESSOR_NAME, PROFESSOR_SSN
FROM    TB_PROFESSOR
WHERE   DEPARTMENT_NO = 005
ORDER BY PROFESSOR_SSN ASC;

--5. 2004 ��2�б⿡ 'C3118100' ������ ������ �л����� ������ ��ȸ�Ϸ��� �Ѵ�. 
--������ ���� �л����� ǥ���ϰ�, ������ ������ �й��� ���� �л����� ǥ���ϴ� ������ �ۼ��غ��ÿ�.
SELECT  STUDENT_NO, POINT
FROM    TB_GRADE
WHERE   CLASS_NO ='C3118100' AND TERM_NO=200402
ORDER BY POINT DESC, STUDENT_NO;

--6. �л� ��ȣ, �л� �̸�, �а� �̸��� �л� �̸����� �������� �����Ͽ� ����ϴ� SQL ���� �ۼ��Ͻÿ�. 
SELECT  STUDENT_NO, STUDENT_NAME, DEPARTMENT_NAME
FROM    TB_STUDENT
JOIN    TB_DEPARTMENT USING(DEPARTMENT_NO)
ORDER BY 2 ASC ;

--7. ������б��� ���� �̸��� ������ �а� �̸��� ����ϴ� SQL ������ �ۼ��Ͻÿ�.
SELECT  CLASS_NAME, DEPARTMENT_NAME
FROM    TB_CLASS
JOIN    TB_DEPARTMENT USING(DEPARTMENT_NO);

--8. ���� ���� �̸��� ã������ �Ѵ�. ���� �̸��� ���� �̸��� ����ϴ� SQL ���� �ۼ��Ͻÿ�. 
SELECT  C.CLASS_NAME, P.PROFESSOR_NAME
FROM    TB_CLASS C
JOIN    TB_CLASS_PROFESSOR CP USING(CLASS_NO)
JOIN    TB_PROFESSOR P USING(PROFESSOR_NO)
ORDER BY 1 ASC;

--9. 8���� ��� �� ���ι���ȸ�� �迭�� ���� ������ ���� �̸��� ã������ �Ѵ�. 
--�̿� �ش��ϴ� ���� �̸��� ���� �̸��� ����ϴ� SQL ���� �ۼ��Ͻÿ�. 
SELECT  C.CLASS_NAME, P.PROFESSOR_NAME
FROM    TB_CLASS C
JOIN    TB_CLASS_PROFESSOR CP USING(CLASS_NO)
JOIN    TB_PROFESSOR P USING(PROFESSOR_NO)
JOIN    TB_DEPARTMENT D ON(D.DEPARTMENT_NO=P.DEPARTMENT_NO)
WHERE   CATEGORY IN '�ι���ȸ'
ORDER BY 1 ASC;

--10. �������а��� �л����� ������ ���Ϸ��� �Ѵ�. 
--�����а� �л����� "�й�", "�л� �̸�", "��ü ����"�� ����ϴ� SQL ������ �ۼ��Ͻÿ�. 
--(��, ������ �Ҽ��� 1 �ڸ����� �ݿø��Ͽ� ǥ���Ѵ�.) /059 
SELECT STUDENT_NO AS �й�,
       STUDENT_NAME AS "�л� �̸�",
       ROUND(AVG(POINT),1) AS "��ü����"
FROM   TB_STUDENT
JOIN   TB_GRADE USING(STUDENT_NO)
WHERE  DEPARTMENT_NO=059
GROUP BY ROLLUP(STUDENT_NO, STUDENT_NAME);

--11. �й��� A313047�� �л��� �б��� ������ ���� �ʴ�.
--���� �������� ������ �����ϱ� ���� �а� �̸�, �л� �̸��� ���� ���� �̸��� �ʿ��ϴ�. 
--�̶� ����� SQL ���� �ۼ��Ͻÿ�.  ��, �������� ?�а��̸�?, ?�л��̸�?, ?���������̸�?���� ��µǵ��� �Ѵ�.
SELECT  DEPARTMENT_NAME AS �а��̸�,
        STUDENT_NAME AS �л��̸�,
        PROFESSOR_NAME AS ���������̸�
FROM    TB_DEPARTMENT D
JOIN    TB_STUDENT S ON (S.DEPARTMENT_NO=D.DEPARTMENT_NO)
JOIN    TB_PROFESSOR P ON (P.DEPARTMENT_NO=S.DEPARTMENT_NO)
WHERE   DEPARTMENT_NAME = '�����а�' AND STUDENT_NO = 'A313047';

--12. 2007 �⵵�� '�ΰ������' ������ ������ �л��� ã�� �л��̸��� �����б⸦ ǥ���ϴ� SQL ������ �ۼ��Ͻÿ�.
SELECT  STUDENT_NAME, TERM_NO
FROM    TB_STUDENT S
JOIN    TB_GRADE G USING(STUDENT_NO)
JOIN    TB_CLASS C USING(CLASS_NO)
WHERE   CLASS_NAME='�ΰ������' AND TERM_NO LIKE '2007%';

--13. ��ü�� �迭 ���� �� ���� ��米���� �� �� �������� ���� ������ ã�� 
--�� ���� �̸��� �а� �̸��� ����ϴ� SQL ������ �ۼ��Ͻÿ�.
SELECT  CLASS_NAME, DEPARTMENT_NAME
FROM    TB_CLASS C
FULL JOIN    TB_DEPARTMENT D ON(D.DEPARTMENT_NO=C.DEPARTMENT_NO)
FULL JOIN    TB_PROFESSOR P ON(P.DEPARTMENT_NO=D.DEPARTMENT_NO)
WHERE   CATEGORY='��ü��' AND PROFESSOR_NO IS NULL
