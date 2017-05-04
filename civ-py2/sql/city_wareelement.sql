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
-- Name: city_wareelement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('city_wareelement_id_seq', 45, true);


--
-- Data for Name: city_wareelement; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (24, '兵车', 'bing_che', 23, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (23, '雪橇', 'xue_qiao', 7, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (22, '马车', 'ma_che', 7, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (21, '牛车', 'niu_che', 7, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (25, '精铜', 'jing_tong', 22, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (26, '精铁', 'jing_tie', 22, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (31, '余皇', 'yu_huang', 4, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (30, '楼船战舰', 'lou_chuan_zhan_jian', 4, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (29, '粮船', 'liang_chuan', 4, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (28, '蒙冲斗舰', 'meng_chong_dou_jian', 4, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (27, '游击赤马舟', 'you_ji_chi_ma_zhou', 4, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (36, '火炮', 'huo_pao', 32, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (35, '塔楼', 'jian_lou', 23, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (34, '投石机', 'tou_shi_ji', 23, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (33, '破城锤', 'po_cheng_chui', 23, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (32, '云梯', 'yun_ti', 23, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (45, '火枪', 'huo_qiang', 32, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (44, '火铳', 'huo_chong', 32, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (43, '陌刀', 'mo_dao', 32, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (37, '朴刀', 'pu_dao', 32, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (38, '长枪', 'chang_qiang', 32, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (40, '盔甲', 'kui_jia', 32, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (39, '盾牌', 'dun_pai', 32, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (1, '青瓷', 'ci_qi_1', 26, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (2, '赤瓷', 'ci_qi_2', 26, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (3, '金瓷', 'ci_qi_3', 26, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (4, '雪瓷', 'ci_qi_4', 26, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (5, '幽瓷', 'ci_qi_5', 26, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (6, '竹叶青', 'jiu_shui_1', 25, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (7, '女儿红', 'jiu_shui_2', 25, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (8, '黄桂稠酒', 'jiu_shui_3', 25, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (9, '五粮液', 'jiu_shui_4', 25, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (10, '茅台', 'jiu_shui_5', 25, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (11, '青木家俱', 'mu_qi_1', 27, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (12, '红木家俱', 'mu_qi_2', 27, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (13, '金色木器', 'mu_qi_3', 27, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (14, '莹雪木器', 'mu_qi_4', 27, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (15, '黑晶家俱', 'mu_qi_5', 27, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (16, '青玉', 'yu_qi_1', 28, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (17, '红宝石', 'yu_qi_2', 28, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (18, '金玉', 'yu_qi_3', 28, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (19, '钻石', 'yu_qi_4', 28, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (20, '黛玉', 'yu_qi_5', 28, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (42, '连弩', 'lian_nu', 32, 1, 1, 1, 1, 11);
INSERT INTO city_wareelement (id, name, code, building_element_id, food, wood, ore, gold, "time") VALUES (41, '弓箭', 'gong_jian', 32, 1, 1, 1, 1, 11);


--
-- PostgreSQL database dump complete
--

