--1-1 CUSTOMERS TABLE
--3 CUSTOMERS ���̺��� ������ �Է�
CREATE TABLE CUSTOMERS(
    CNO     NUMBER(5) PRIMARY KEY,
    CNAME   VARCHAR2(10) NOT NULL,
    ADDRESS VARCHAR2(50) NOT NULL,
    EMAIL   VARCHAR2(20) NOT NULL,
    PHONE   VARCHAR2(20) NOT NULL
);

INSERT INTO CUSTOMERS VALUES(101, '��ö��', '���� ������', 'cskim@naver.com', '899-6666');
INSERT INTO CUSTOMERS VALUES(102, '�̿���', '�λ� ����', 'yhlee@empal.com', '355-8882');
INSERT INTO CUSTOMERS VALUES(103, '������', '���� ������', 'jkchoi@gmail.com', '852-5764');
INSERT INTO CUSTOMERS VALUES(104, '����ȣ', '���� ȫ����', 'jhkang@hanmail.com', '559-7777');
INSERT INTO CUSTOMERS VALUES(105, '�κ���', '���� ���ε�', 'bgmin@hotmail.com', '559-8741');
INSERT INTO CUSTOMERS VALUES(106, '���μ�', '���� �ϱ�', 'msoh@microsoft.com', '542-9988' );

    
SELECT  *
FROM    CUSTOMERS;

DROP TABLE CUSTOMERS;
--1-2 ORDERS TABLE
CREATE TABLE ORDERS(
    ORDER_NO    NUMBER(10) PRIMARY KEY,
    ODER_DATE   DATE DEFAULT SYSDATE NOT NULL,
    ADDRESS     VARCHAR2(50) NOT NULL,
    PHONE       VARCHAR2(20) NOT NULL,
    STATUS      VARCHAR2(20) NOT NULL, CHECK(STATUS IN('�����Ϸ�', '�����', '��ۿϷ�')),
    CNO         NUMBER(5) NOT NULL REFERENCES CUSTOMERS(CNO)
);

SELECT  *
FROM    ORDERS;

DROP TABLE ORDERS;



--1-3 PRODUCTS
--2 PRODUCTS ���̺��� ������ �Է�
CREATE TABLE PRODUCTS(
    PNO     NUMBER(5) PRIMARY KEY,
    PNAME   VARCHAR2(20) NOT NULL,
    COST    NUMBER(8) DEFAULT 0 NOT NULL,
    STOCK   NUMBER(5) DEFAULT 0 NOT NULL
    );

INSERT INTO PRODUCTS VALUES(1001, '�����', 1000, 200 );
INSERT INTO PRODUCTS VALUES(1002, '�����', 1500, 500);
INSERT INTO PRODUCTS VALUES(1003, '������', 2000, 350);
INSERT INTO PRODUCTS VALUES(1004, '������', 2000, 700);
INSERT INTO PRODUCTS VALUES(1005, '��ī�ݶ�', 1800, 550);
INSERT INTO PRODUCTS VALUES(1006, 'ȯŸ', 1600, 300);
 
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

--4. ������ ���� �ֹ� ������ orders ���̺�� orderdetail ���̺� �Է��Ͻÿ�. 
--cno�� customers ���̺��� �˻��Ͽ� �Է��� ��. orders�� 1��, orderdetail�� 1���� �Է��Ѵ�.  
--����ö��(101)�� 3������ �����(1001)�� ���� 1000���� 50�� �ֹ��Ͽ���.�� 
INSERT INTO ORDERS VALUES(1, SYSDATE-3, '���� ������', '899-6666', '�����Ϸ�', 101);
INSERT INTO ORDER_DETAIL VALUES(1, 1001, 50, 1000);

--5. ���� ���� �ֹ� �������� �ش� ��ǰ(products)�� ���(stock)�� �����Ͻÿ�.  
--�������(1001)�� ��� 150(=200-50)���� �����Ѵ١�
UPDATE  PRODUCTS
SET     STOCK = 150
WHERE   PNAME = '�����';

--6. ������ ���� �ֹ� ������ orders ���̺�� orderdetail ���̺� �Է��Ͻÿ�. 
--cno�� customers ���̺��� �˻��Ͽ� �Է��� ��. orders�� 1��, orderdetail�� 2���� �Է��Ѵ�.  
--���̿���(102)�� ��Ʋ���� �����(1002)�� ���� 1500���� 100��, ������(1003)�� ���� 2000���� 150�� �ֹ��Ͽ���.�� 
INSERT INTO ORDERS VALUES(2, SYSDATE-2, '�λ� ����', '337-5000', '�����Ϸ�', 102);
INSERT INTO ORDER_DETAIL VALUES(2, 1002, 100, 1500);
INSERT INTO ORDER_DETAIL VALUES(2, 1003, 150, 2000);

--7. ���� ���� �ֹ� �������� �ش� ��ǰ(products)�� ���(stock)�� �����Ͻÿ�. 
--�������(1002)�� ��� 400(=500-100)���� �����Ѵ١�   
--��������(1003)�� ��� 200(=350-150)���� �����Ѵ١� 
UPDATE  PRODUCTS    
SET     STOCK = 400
WHERE   PNAME = '�����';

UPDATE  PRODUCTS
SET     STOCK = 200
WHERE   PNAME = '������';

--8. ������ ���� �ֹ� ������ orders ���̺�� orderdetail ���̺� �Է��Ͻÿ�. 
--cno�� customers ���̺��� �˻��Ͽ� �Է��� ��. orders�� 1��, orderdetail�� 2���� �Է��Ѵ�. 
--�����μ�(106)�� ���� ������(1004)�� ���� 2000���� 100��, ��ī�ݶ�(1005)�� ���� 1800���� 50�� �ֹ��Ͽ���.��
INSERT INTO ORDERS VALUES(3, SYSDATE-1, '���� �ϱ�', '542-9988', '�����Ϸ�', 106);
INSERT INTO ORDER_DETAIL VALUES(3,1004, 100, 2000);
INSERT INTO ORDER_DETAIL VALUES(3, 1005, 50, 1800);

--9. ���� ���� �ֹ� �������� �ش� ��ǰ(products)�� ���(stock)�� �����Ͻÿ�. 
--��������(1004)�� ��� 600(=700-100)���� �����Ѵ١�   
--����ī�ݶ�(1005)�� ��� 500(=550-50)���� �����Ѵ١� 
UPDATE  PRODUCTS
SET     STOCK = 600
WHERE   PNAME = '������';

UPDATE  PRODUCTS
SET     STOCK = 500
WHERE   PNAME = '��ī�ݶ�';

--10. ������ ���� ��ü �ֹ� ����� ����ϴ� ������ �ۼ��Ͻÿ�.
SELECT  ORDER_DATE, CNAME, ADDRESS, PHONE, STATUS, PNAME, COST, QTY, COST*QTY
FROM    CUSTOMERS 
JOIN    ORDERS USING(CNO)
JOIN    ORDER_DETAIL USING(ORDER_NO)
JOIN    PRODUCTS USING(PNO);

--11. ������ ���� �Ϻ� ���� ����� ����ϴ� ������ �ۼ��Ͻÿ�. 
SELECT  ORDER_DATE, SUM(COST*QTY)
FROM    ORDERS
JOIN    ORDER_DETAIL USING(ORDER_NO)
GROUP BY    ORDER_DATE;

--12. ������ ���� �ű� ��ǰ ������ products ���̺� �Է��Ͻÿ�. 
--����ǰ��ȣ�� 1007, ��ǰ���� ��ĵ��, �ܰ��� 3000��, ���� 500���̴�.�� 
INSERT INTO PRODUCTS VALUES(1007, '��ĵ��', 300, 500);
UPDATE  PRODUCTS
SET     COST = 3000
WHERE   PNAME = '��ĵ��'
--13. ������ ���� 4�� �ֹ� ������ �Է��ϰ�, ��� ������ �����Ͻÿ�. 
--�ֹ� ������ �Է��ϰ�, 10�� �������� �ۼ��� �������� �˻��ϸ� ������ ����.  
--��������(103)�� ���� ��ĵ��(1007)�� ���� 3000���� 200�� �ֹ��Ͽ�����, 
--������� �ּҴ� ���� �������̸�, ����ó�� 352-4657�̰�, ������ �Ϸ�� �����̴�.�� 
INSERT INTO ORDERS VALUES(4, SYSDATE, '���� ������', '352-4657', '�����Ϸ�', 103);
INSERT INTO ORDER_DETAIL VALUES(4, 1007, 200, 3000);

UPDATE  PRODUCTS
SET     STOCK = 300
WHERE   PNAME = '��ĵ��';
