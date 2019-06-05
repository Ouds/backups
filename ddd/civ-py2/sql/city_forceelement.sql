--
-- PostgreSQL database dump
--

SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

--
-- Name: city_forceelement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('city_forceelement_id_seq', 15, true);


--
-- Data for Name: city_forceelement; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (15, '神机营', 'shen_ji_ying', 3, 12, 4, 1, 1, 1, 1, 11);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (14, '水师', 'shui_shi', 3, 11, 4, 1, 1, 1, 1, 11);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (13, '陌刀队', 'mo_dao_dui', 3, 10, 4, 1, 1, 1, 1, 11);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (12, '重甲兵', 'zhong_jia_bing', 3, 9, 4, 1, 1, 1, 1, 11);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (11, '诸葛弩', 'zhu_ge_nu', 3, 8, 4, 1, 1, 1, 1, 11);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (10, '布衣武士团', 'bu_yi_wu_shi_tuan', 3, 7, 4, 1, 1, 1, 1, 11);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (9, '工程兵', 'gong_cheng_bing', 3, 4, 4, 1, 1, 1, 1, 11);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (8, '弓箭兵', 'gong_jian_bing', 3, 6, 4, 1, 1, 1, 1, 11);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (7, '长枪兵', 'chang_qiang_bing', 3, 5, 4, 1, 1, 1, 1, 11);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (1, '狗', 'dog', 24, 3, 4, 1, 1, 1, 1, 11);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (2, '牛', 'cow', 24, 2, 10, 22, 22, 22, 22, 222);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (3, '马', 'horse', 24, 1, 4, 1, 1, 1, 1, 11);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (4, '大象', 'elephant', 24, 4, 4, 4, 4, 4, 4, 4);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (5, '海豚', 'dolphin', 24, 1, 22, 22, 22, 22, 22, 222);
INSERT INTO city_forceelement (id, name, code, building_element_id, level, speed, food, wood, ore, gold, "time") VALUES (6, '野兽', 'beast', 24, 5, 4, 4, 4, 4, 4, 4);


--
-- PostgreSQL database dump complete
--

