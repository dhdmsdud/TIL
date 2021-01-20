--1. 학생이름과 주소지를 표시하시오. 
--단, 출력 헤더는 "학생 이름", "주소지"로 하고, 정렬은 이름으로 오름차순 표시
SELECT  STUDENT_NAME AS "학생 이름", 
        STUDENT_ADDRESS AS 주소지
FROM    TB_STUDENT
ORDER BY STUDENT_NAME;

--2.  휴학중인 학생들의 이름과 주민번호를 나이가 적은 순서로 화면에 출력하시오.
SELECT  STUDENT_NAME,
        STUDENT_SSN
FROM    TB_STUDENT
WHERE   ABSENCE_YN = 'Y'
ORDER BY 2 DESC;

--3. 주소지가 강원도나 경기도인 학생들 중 1900년대 학번을 가진 학생들의 이름과 학번, 주소를 이름의 오름차순으로 화면에 출력하시오.
--단, 출력헤더에는 "학생이름","학번", "거주지 주소" 가 출력되도록 한다.
SELECT  STUDENT_NAME AS 학생이름, 
        STUDENT_NO AS 학번, 
        STUDENT_ADDRESS AS "거주지 주소"
FROM    TB_STUDENT
WHERE   STUDENT_ADDRESS LIKE '경기도%' AND STUDENT_NO LIKE '9%'
ORDER BY STUDENT_NAME ASC;

--4. 현재 법학과 교수 중 가장 나이가 많은 사람부터 이름을 확인할 수 있는 SQL 문장을 작성하시오. 
--(법학과의 '학과코드'는 학과 테이블(TB_DEPARTMENT)을 조회해서 찾아 내도록 하자) / 005
SELECT  PROFESSOR_NAME, PROFESSOR_SSN
FROM    TB_PROFESSOR
WHERE   DEPARTMENT_NO = 005
ORDER BY PROFESSOR_SSN ASC;

--5. 2004 년2학기에 'C3118100' 과목을 수강한 학생들의 학점을 조회하려고 한다. 
--학점이 높은 학생부터 표시하고, 학점이 같으면 학번이 낮은 학생부터 표시하는 구문을 작성해보시오.
SELECT  STUDENT_NO, POINT
FROM    TB_GRADE
WHERE   CLASS_NO ='C3118100' AND TERM_NO=200402
ORDER BY POINT DESC, STUDENT_NO;

--6. 학생 번호, 학생 이름, 학과 이름을 학생 이름으로 오름차순 정렬하여 출력하는 SQL 문을 작성하시오. 
SELECT  STUDENT_NO, STUDENT_NAME, DEPARTMENT_NAME
FROM    TB_STUDENT
JOIN    TB_DEPARTMENT USING(DEPARTMENT_NO)
ORDER BY 2 ASC ;

--7. 기술대학교의 과목 이름과 과목의 학과 이름을 출력하는 SQL 문장을 작성하시오.
SELECT  CLASS_NAME, DEPARTMENT_NAME
FROM    TB_CLASS
JOIN    TB_DEPARTMENT USING(DEPARTMENT_NO);

--8. 과목별 교수 이름을 찾으려고 한다. 과목 이름과 교수 이름을 출력하는 SQL 문을 작성하시오. 
SELECT  C.CLASS_NAME, P.PROFESSOR_NAME
FROM    TB_CLASS C
JOIN    TB_CLASS_PROFESSOR CP USING(CLASS_NO)
JOIN    TB_PROFESSOR P USING(PROFESSOR_NO)
ORDER BY 1 ASC;

--9. 8번의 결과 중 ‘인문사회’ 계열에 속한 과목의 교수 이름을 찾으려고 한다. 
--이에 해당하는 과목 이름과 교수 이름을 출력하는 SQL 문을 작성하시오. 
SELECT  C.CLASS_NAME, P.PROFESSOR_NAME
FROM    TB_CLASS C
JOIN    TB_CLASS_PROFESSOR CP USING(CLASS_NO)
JOIN    TB_PROFESSOR P USING(PROFESSOR_NO)
JOIN    TB_DEPARTMENT D ON(D.DEPARTMENT_NO=P.DEPARTMENT_NO)
WHERE   CATEGORY IN '인문사회'
ORDER BY 1 ASC;

--10. ‘음악학과’ 학생들의 평점을 구하려고 한다. 
--음악학과 학생들의 "학번", "학생 이름", "전체 평점"을 출력하는 SQL 문장을 작성하시오. 
--(단, 평점은 소수점 1 자리까지 반올림하여 표시한다.) /059 
SELECT STUDENT_NO AS 학번,
       STUDENT_NAME AS "학생 이름",
       ROUND(AVG(POINT),1) AS "전체평점"
FROM   TB_STUDENT
JOIN   TB_GRADE USING(STUDENT_NO)
WHERE  DEPARTMENT_NO=059
GROUP BY ROLLUP(STUDENT_NO, STUDENT_NAME);

--11. 학번이 A313047인 학생이 학교에 나오고 있지 않다.
--지도 교수에게 내용을 전달하기 위한 학과 이름, 학생 이름과 지도 교수 이름이 필요하다. 
--이때 사용할 SQL 문을 작성하시오.  단, 출력헤더는 ?학과이름?, ?학생이름?, ?지도교수이름?으로 출력되도록 한다.
SELECT  DEPARTMENT_NAME AS 학과이름,
        STUDENT_NAME AS 학생이름,
        PROFESSOR_NAME AS 지도교수이름
FROM    TB_DEPARTMENT D
JOIN    TB_STUDENT S ON (S.DEPARTMENT_NO=D.DEPARTMENT_NO)
JOIN    TB_PROFESSOR P ON (P.DEPARTMENT_NO=S.DEPARTMENT_NO)
WHERE   DEPARTMENT_NAME = '경제학과' AND STUDENT_NO = 'A313047';

--12. 2007 년도에 '인간관계론' 과목을 수강한 학생을 찾아 학생이름과 수강학기를 표시하는 SQL 문장을 작성하시오.
SELECT  STUDENT_NAME, TERM_NO
FROM    TB_STUDENT S
JOIN    TB_GRADE G USING(STUDENT_NO)
JOIN    TB_CLASS C USING(CLASS_NO)
WHERE   CLASS_NAME='인간관계론' AND TERM_NO LIKE '2007%';

--13. 예체능 계열 과목 중 과목 담당교수를 한 명도 배정받지 못한 과목을 찾아 
--그 과목 이름과 학과 이름을 출력하는 SQL 문장을 작성하시오.
SELECT  CLASS_NAME, DEPARTMENT_NAME
FROM    TB_DEPARTMENT D
JOIN    TB_CLASS C ON (C.DEPARTMENT_NO=D.DEPARTMENT_NO)
JOIN    TB_STUDENT S ON(S.DEPARTMENT_NO=D.DEPARTMENT_NO)
WHERE   CATEGORY = '예체능' 
