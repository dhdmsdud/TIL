--1. ������а�(�а��ڵ� 002) �л����� �й��� �̸�, ���� �⵵�� ���� �⵵�� ���� ������ ǥ���ϴ� SQL ������ �ۼ��Ͻÿ�.
--( ��, ����� "�й�", "�̸�", "���г⵵" �� ǥ�õǵ��� �Ѵ�.) 
SELECT  STUDENT_NO AS �й�,
        STUDENT_NAME AS �̸�,
        ENTRANCE_DATE AS ���г⵵
FROM    TB_STUDENT
ORDER BY ENTRANCE_DATE;

--2. ������б��� ���� �� �̸��� �� ���ڰ� �ƴ� ������ �� �� �ִٰ� �Ѵ�. 
--�� ������ �̸��� �ֹι�ȣ�� ȭ�鿡 ����ϴ� SQL ������ �ۼ��� ����. 
--(* �̶� �ùٸ��� �ۼ��� SQL ������ ��� ���� ����� �ٸ��� ���� �� �ִ�. ������ �������� �����غ� ��) 
SELECT  PROFESSOR_NAME,
        PROFESSOR_SSN
FROM    TB_PROFESSOR
WHERE   PROFESSOR_NAME NOT LIKE '___';
--3. ������б��� ���� �������� �̸��� ���̸� ����ϴ� SQL ������ �ۼ��Ͻÿ�. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
--�� �̶� ���̰� ���� ������� ���� ��� ������ ȭ�鿡 ��µǵ��� ����ÿ�. 
--(��, ���� �� 2000�� ���� ����ڴ� ������ ��� ����� "�����̸�", "����"�� �Ѵ�. ���̴� ���������� ����Ѵ�.) 
SELECT  PROFESSOR_NAME �����̸�,
        TO_DATE(SYSDATA, 'YYYY') - TO_DATE(SUBSTR(PROFESSOR_SSN, 1, 2), 'YYYY') AS ����
FROM    TB_PROFESSOR;  

--4. �������� �̸� �� ���� ������ �̸��� ����ϴ� SQL ������ �ۼ��Ͻÿ�. 
--��� ����� ?�̸�? �� �������� �Ѵ�. 
--(���� 2 ���� ���� ������ ���ٰ� �����Ͻÿ�.)
SELECT  SUBSTR(PROFESSOR_NAME,2,3) AS �̸�
FROM    TB_PROFESSOR;

--5. ������б��� ����� �����ڸ� ���Ϸ��� �Ѵ�.
--�̶�, 19�쿡 �����ϸ� ����� ���� ���� ������ �����Ѵ�.
SELECT  STUDENT_NAME,
        TO_CHAR(TO_DATE(SUBSTR(STUDENT_SSN,1,6), 'RRMMDD'), 'YYYY/MM/DD') AS �����,
        TO_CHAR(ENTRANCE_DATE, 'RRRR/MM/DD') AS ������,
        TRUNC(MONTHS_BETWEEN(ENTRANCE_DATE, TO_DATE(SUBSTR(STUDENT_SSN,1,6), 'RRMMDD')) /12) AS ����
FROM    TB_STUDENT
WHERE   TRUNC(MONTHS_BETWEEN(ENTRANCE_DATE, TO_DATE(SUBSTR(STUDENT_SSN,1,6),'RRMMDD')) /12) > 19;

--6. 2020 �� ũ���������� ���� �����ΰ�?
SELECT  TO_CHAR(TO_DATE('20201225', 'YYYYMMDD'), 'DAY')
FROM    DUAL;

--7. TO_DATE('99/10/11','YY/MM/DD'), TO_DATE('49/10/11','YY/MM/DD')  �� ���� �� �� �� �� �� ���� �ǹ� 
--�� TO_DATE('99/10/11','RR/MM/DD'), TO_DATE('49/10/11','RR/MM/DD') �� ���� �� �� �� �� �� ���� �ǹ�
SELECT  TO_CHAR(TO_DATE('99/10/11','YY/MM/DD'), 'YYYY-MM-DD'),
        TO_CHAR(TO_DATE('49/10/11','YY/MM/DD'), 'YYYY-MM-DD')
FROM    DUAL;

SELECT  TO_CHAR(TO_DATE('99/10/11','RR/MM/DD'), 'RRRR-MM-DD'),
        TO_CHAR(TO_DATE('49/10/11','RR/MM/DD'), 'RRRR-MM-DD')
FROM    DUAL;

--8. ������б��� 2000�⵵ ���� �����ڵ��� �й��� A �� �����ϰ� �Ǿ��ִ�.
--2000�⵵ ���� �й��� ���� �л����� �й��� �̸��� �����ִ� SQL ������ �ۼ��Ͻÿ�. 
SELECT  STUDENT_NO,
        STUDENT_NAME,
        ENTRANCE_DATE
FROM    TB_STUDENT
WHERE   ENTRANCE_DATE < TO_DATE('00/01/01', 'YY/MM/DD');
--9. �й��� A517178 �� �ѾƸ� �л��� ���� �� ������ ���ϴ� SQL ���� �ۼ��Ͻÿ�. 
--��, �̶� ��� ȭ���� ����� "����" �̶�� ������ �ϰ�, ������ �ݿø��Ͽ� �Ҽ��� ���� �� �ڸ����� ǥ���Ѵ�. 
SELECT  ROUND(AVG(POINT), 1) AS ����
FROM    TB_GRADE
WHERE   STUDENT_NO = 'A517178';

--10. �а��� �л����� ���Ͽ� "�а���ȣ", "�л���(��)" �� ���·� ����� ����� ������� ��µǵ��� �Ͻÿ�.
SELECT  DEPARTMENT_NO AS "�а���ȣ",
        COUNT(*) AS "�л���(��)"
FROM    TB_STUDENT
GROUP BY DEPARTMENT_NO
ORDER BY 1 ;

--11. ���� ������ �������� ���� �л��� ���� �� �� ���� �Ǵ� �˾Ƴ��� SQL ���� �ۼ��Ͻÿ�.
SELECT  COUNT(*) - COUNT(COACH_PROFESSOR_NO)
FROM    TB_STUDENT;

--12. �й��� 'A112113'�� ���� �л��� �⵵ �� ������ ���ϴ� SQL ���� �ۼ��Ͻÿ�.
--��, �̶� ��� ȭ���� ����� "�⵵", "�⵵ �� ����" �̶�� ������ �ϰ�, ������ �ݿø��Ͽ� �Ҽ��� ���� �� �ڸ����� ǥ��.
SELECT  SUBSTR(TERM_NO, 1, 4) AS �⵵,
        ROUND(AVG(POINT),1) AS "�⵵ �� ����"
FROM    TB_GRADE
WHERE   STUDENT_NO='A112113'
GROUP BY SUBSTR(TERM_NO, 1, 4);

--13. �а� �� ���л� ���� �ľ��ϰ��� �Ѵ�. 
--�а� ��ȣ�� ���л� ���� ǥ���ϴ� SQL ������ �ۼ��Ͻÿ�. 
SELECT  DEPARTMENT_NO AS �а��ڵ��,
        SUM(CASE WHEN ABSENCE_YN='Y' THEN 1 ELSE 0 END) AS ���л�
FROM    TB_STUDENT
GROUP BY DEPARTMENT_NO;

--14. ���б��� �ٴϴ� ��������(��٣���) �л����� �̸��� ã���� �Ѵ�.
SELECT  STUDENT_NAME,
        COUNT(STUDENT_NAME)-1
FROM    TB_STUDENT
GROUP BY STUDENT_NAME;

--15. �й��� 'A112113' �� ���� �л��� �⵵, �б� �� ������ �⵵ �� ���� ���� , �� ������ ���ϴ� SQL ���� �ۼ��Ͻÿ�. 
--(��, ������ �Ҽ��� 1 �ڸ����� �ݿø��Ͽ� ǥ��)
SELECT  SUBSTR(TERM_NO, 1, 4) AS �⵵,
        NVL(SUBSTR(TERM_NO, 5, 6), ' ') AS �б�,
        ROUND(AVG(POINT),1) AS "�⵵ �� ����"
FROM    TB_GRADE
WHERE   STUDENT_NO='A112113'
GROUP BY ROLLUP(SUBSTR(TERM_NO, 1, 4), SUBSTR(TERM_NO, 5, 6));
