/* 오늘은 내가 좋아하는 SQL을! 
날짜: 2022년 5월 2일 월요일
문제지문: https://programmers.co.kr/learn/challenges with filters (language == sql) */

/* first question: 우유와 요거트가 담긴 장바구니
link: https://programmers.co.kr/learn/courses/30/lessons/62284 */

SELECT CART_ID 
FROM CART_PRODUCTS
WHERE NAME = "Milk"
AND CART_ID IN
(SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME = "Yogurt")
    
/* second question: 입양시각 구하기
link: https://programmers.co.kr/learn/courses/30/lessons/59413 */

WITH RECURSIVE CAH AS (SELECT 0 AS HOUR
                   UNION ALL
                   SELECT HOUR+1
                   FROM CAH
                   WHERE HOUR < 23)
                   
SELECT CAH.HOUR, COUNT(HOUR(AO.DATETIME)) AS COUNT
FROM CAH
LEFT JOIN ANIMAL_OUTS AS AO
ON CAH.HOUR = HOUR(AO.DATETIME)
GROUP BY CAH.HOUR
ORDER BY CAH.HOUR;


/* third question: 보호소에서 중성화된 동물
link: https://programmers.co.kr/learn/courses/30/lessons/59045 */

SELECT a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
FROM ANIMAL_INS a
JOIN ANIMAL_OUTS b
ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE a.SEX_UPON_INTAKE LIKE "%Intact%" AND b.SEX_UPON_OUTCOME NOT LIKE "%Intact%"
