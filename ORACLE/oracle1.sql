--1-1 CUSTOMERS TABLE
--3 CUSTOMERS 테이블의 데이터 입력
CREATE TABLE CUSTOMERS(
    CNO     NUMBER(5) PRIMARY KEY,
    CNAME   VARCHAR2(10) NOT NULL,
    ADDRESS VARCHAR2(50) NOT NULL,
    EMAIL   VARCHAR2(20) NOT NULL,
    PHONE   VARCHAR2(20) NOT NULL
);

INSERT INTO CUSTOMERS VALUES(101, '김철수', '서울 강남구', 'cskim@naver.com', '899-6666');
INSERT INTO CUSTOMERS VALUES(102, '이영희', '부산 서면', 'yhlee@empal.com', '355-8882');
INSERT INTO CUSTOMERS VALUES(103, '최진국', '제주 동광양', 'jkchoi@gmail.com', '852-5764');
INSERT INTO CUSTOMERS VALUES(104, '강준호', '강릉 홍제동', 'jhkang@hanmail.com', '559-7777');
INSERT INTO CUSTOMERS VALUES(105, '민병국', '대전 전민동', 'bgmin@hotmail.com', '559-8741');
INSERT INTO CUSTOMERS VALUES(106, '오민수', '광주 북구', 'msoh@microsoft.com', '542-9988' );

    
SELECT  *
FROM    CUSTOMERS;

DROP TABLE CUSTOMERS;
--1-2 ORDERS TABLE
CREATE TABLE ORDERS(
    ORDER_NO    NUMBER(10) PRIMARY KEY,
    ODER_DATE   DATE DEFAULT SYSDATE NOT NULL,
    ADDRESS     VARCHAR2(50) NOT NULL,
    PHONE       VARCHAR2(20) NOT NULL,
    STATUS      VARCHAR2(20) NOT NULL, CHECK(STATUS IN('결제완료', '배송중', '배송완료')),
    CNO         NUMBER(5) NOT NULL REFERENCES CUSTOMERS(CNO)
);

SELECT  *
FROM    ORDERS;

DROP TABLE ORDERS;



--1-3 PRODUCTS
--2 PRODUCTS 테이블의 데이터 입력
CREATE TABLE PRODUCTS(
    PNO     NUMBER(5) PRIMARY KEY,
    PNAME   VARCHAR2(20) NOT NULL,
    COST    NUMBER(8) DEFAULT 0 NOT NULL,
    STOCK   NUMBER(5) DEFAULT 0 NOT NULL
    );

INSERT INTO PRODUCTS VALUES(1001, '삼양라면', 1000, 200 );
INSERT INTO PRODUCTS VALUES(1002, '새우깡', 1500, 500);
INSERT INTO PRODUCTS VALUES(1003, '월드콘', 2000, 350);
INSERT INTO PRODUCTS VALUES(1004, '빼빼로', 2000, 700);
INSERT INTO PRODUCTS VALUES(1005, '코카콜라', 1800, 550);
INSERT INTO PRODUCTS VALUES(1006, '환타', 1600, 300);
 
SELECT  *
FROM    PRODUCTS;

DROP TABLE PRODUCTS;

--1-4. ORDER_DETAIL
CREATE TABLE ORDER_DETAIL(
    ORDER_NO    NUMBER(10) REFERENCES ORDERS(ORDER_NO),
    PNO         NUMBER(5)  REFERENCES PRODUCTS(PNO),
    QTY         NUMBER(5)  DEFAULT 0,
    COST        NUMBER(8)  DEFAULT 0,
    PRIMARY KEY(ORDER_NO, PNO)   
);

SELECT  *
FROM    ORDER_DETAIL;

DROP TABLE ORDER_DETAIL;

--4. 다음과 같은 주문 정보를 orders 테이블과 orderdetail 테이블에 입력하시오. 
--cno는 customers 테이블에서 검색하여 입력할 것. orders에 1건, orderdetail에 1건을 입력한다.  
--“김철수(101)가 3일전에 삼양라면(1001)을 개당 1000원에 50개 주문하였다.” 
INSERT INTO ORDERS VALUES(1, SYSDATE-3, '서울 강남구', '899-6666', '결제완료', 101);
INSERT INTO ORDER_DETAIL VALUES(1, 1001, 50, 1000);

--5. 위와 같은 주문 정보에서 해당 상품(products)의 재고(stock)을 수정하시오.  
--“삼양라면(1001)의 재고를 150(=200-50)개로 변경한다”
UPDATE  PRODUCTS
SET     STOCK = 150
WHERE   PNAME = '삼양라면';

--6. 다음과 같은 주문 정보를 orders 테이블과 orderdetail 테이블에 입력하시오. 
--cno는 customers 테이블에서 검색하여 입력할 것. orders에 1건, orderdetail에 2건을 입력한다.  
--“이영희(102)가 이틀전에 새우깡(1002)을 개당 1500원에 100개, 월드콘(1003)을 개당 2000원에 150개 주문하였다.” 
INSERT INTO ORDERS VALUES(2, SYSDATE-2, '부산 서면', '337-5000', '결제완료', 102);
INSERT INTO ORDER_DETAIL VALUES(2, 1002, 100, 1500);
INSERT INTO ORDER_DETAIL VALUES(2, 1003, 150, 2000);

--7. 위와 같은 주문 정보에서 해당 상품(products)의 재고(stock)을 수정하시오. 
--“새우깡(1002)의 재고를 400(=500-100)개로 변경한다”   
--“월드콘(1003)의 재고를 200(=350-150)개로 변경한다” 
UPDATE  PRODUCTS    
SET     STOCK = 400
WHERE   PNAME = '새우깡';

UPDATE  PRODUCTS
SET     STOCK = 200
WHERE   PNAME = '월드콘';

--8. 다음과 같은 주문 정보를 orders 테이블과 orderdetail 테이블에 입력하시오. 
--cno는 customers 테이블에서 검색하여 입력할 것. orders에 1건, orderdetail에 2건을 입력한다. 
--“오민수(106)가 어제 빼빼로(1004)를 개당 2000원에 100개, 코카콜라(1005)를 개당 1800원에 50개 주문하였다.”
INSERT INTO ORDERS VALUES(3, SYSDATE-1, '광주 북구', '542-9988', '결제완료', 106);
INSERT INTO ORDER_DETAIL VALUES(3,1004, 100, 2000);
INSERT INTO ORDER_DETAIL VALUES(3, 1005, 50, 1800);

--9. 위와 같은 주문 정보에서 해당 상품(products)의 재고(stock)을 수정하시오. 
--“빼빼로(1004)의 재고를 600(=700-100)개로 변경한다”   
--“코카콜라(1005)의 재고를 500(=550-50)개로 변경한다” 
UPDATE  PRODUCTS
SET     STOCK = 600
WHERE   PNAME = '빼빼로';

UPDATE  PRODUCTS
SET     STOCK = 500
WHERE   PNAME = '코카콜라';
