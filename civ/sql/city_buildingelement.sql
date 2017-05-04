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
-- Name: city_buildingelement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('city_buildingelement_id_seq', 39, true);


--
-- Data for Name: city_buildingelement; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (23, '器械厂', 'qi_xie_chang', 45, 0, 0, 45, 0, 0, 45, 0, 0, 50, 0, 0, 0, 1, 0, 360, 3);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (25, '酒坊', 'jiu_fang', 45, 0, 0, 40, 0, 0, 30, 0, 0, 45, 0, 0, 0, 1, 0, 360, 3);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (26, '窑厂', 'yao_chang', 35, 0, 0, 30, 0, 0, 25, 0, 0, 40, 0, 0, 0, 1, 0, 360, 3);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (27, '木坊', 'mu_fang', 35, 0, 0, 40, 0, 0, 30, 0, 0, 45, 0, 0, 0, 1, 0, 360, 3);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (28, '石坊', 'shi_fang', 35, 0, 0, 35, 0, 0, 30, 0, 0, 40, 0, 0, 0, 1, 0, 360, 3);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (39, '烽火台', 'feng_huo_tai', 30, 0, 0, 35, 0, 0, 25, 0, 0, 60, 0, 0, 0, 1, 0, 360, 0);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (38, '城门', 'cheng_men', 35, 0, 0, 35, 0, 0, 30, 0, 0, 50, 0, 0, 0, 1, 0, 360, 0);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (37, '城墙', 'cheng_qiang', 35, 0, 0, 30, 0, 0, 30, 0, 0, 60, 0, 0, 0, 1, 0, 360, 0);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (22, '精矿司', 'jing_kuang_si', 45, 0, 0, 55, 0, 0, 45, 0, 0, 55, 0, 0, 0, 1, 0, 360, 3);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (32, '兵器厂', 'bing_qi_chang', 35, 0, 0, 45, 5, 0, 35, 0, 112, 35, 0, 0, 0, 1, 0, 240, 3);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (21, '医馆', 'yi_guan', 50, 0, 0, 50, 0, 0, 35, 0, 0, 45, 0, 0, 0, 1, 0, 240, 7);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (8, '膳房', 'shan_fang', 60, 0, 0, 35, 0, 0, 30, 0, 0, 65, 0, 0, 0, 1, 0, 240, 4);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (9, '乐坊', 'yue_fang', 55, 0, 0, 50, 0, 0, 30, 0, 0, 55, 0, 0, 0, 1, 0, 240, 4);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (10, '酒肆', 'jiu_si', 65, 0, 0, 55, 0, 0, 30, 0, 0, 60, 0, 0, 0, 1, 0, 360, 4);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (11, '棋院', 'qi_yuan', 40, 0, 0, 40, 0, 0, 25, 0, 0, 60, 0, 0, 0, 1, 0, 360, 4);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (12, '画坊', 'hua_fang', 50, 0, 0, 55, 0, 0, 25, 0, 0, 55, 0, 0, 0, 1, 0, 360, 4);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (13, '景苑', 'jing_yuan', 50, 0, 0, 50, 0, 0, 30, 0, 0, 65, 0, 0, 0, 1, 0, 240, 4);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (16, '道观', 'dao_guan', 45, 0, 0, 40, 0, 0, 25, 0, 0, 50, 0, 0, 0, 1, 0, 240, 5);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (17, '寺院', 'si_yuan', 45, 0, 0, 50, 0, 0, 30, 0, 0, 65, 0, 0, 0, 1, 0, 360, 5);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (18, '基督教堂', 'ji_du_jiao_tang', 45, 0, 0, 40, 0, 0, 30, 0, 0, 50, 0, 0, 0, 1, 0, 360, 5);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (19, '清真寺', 'qing_zhen_si', 45, 0, 0, 40, 0, 0, 30, 0, 0, 50, 0, 0, 0, 1, 0, 360, 5);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (15, '魔法学校', 'mo_fa_xue_xiao', 45, 0, 0, 50, 0, 0, 30, 0, 0, 60, 0, 0, 0, 1, 0, 360, 6);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (14, '武馆', 'wu_guan', 50, 0, 0, 45, 0, 0, 40, 0, 0, 65, 0, 0, 0, 1, 0, 360, 6);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (4, '船坞', 'chuan_wu', 45, 0, 0, 50, 0, 0, 30, 0, 0, 65, 0, 0, 0, 1, 0, 360, 6);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (7, '市舶司', 'shi_bo_si', 40, 0, 0, 45, 0, 0, 30, 0, 0, 50, 0, 0, 0, 1, 0, 360, 7);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (6, '营建司', 'ying_jian_si', 50, 0, 0, 55, 0, 0, 30, 0, 0, 60, 0, 0, 0, 1, 0, 360, 7);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (20, '鸿胪寺', 'hong_lu_si', 45, 0, 0, 40, 0, 0, 30, 0, 0, 50, 0, 0, 0, 1, 0, 360, 7);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (5, '太学', 'tai_xue', 50, 0, 0, 50, 0, 0, 30, 0, 0, 45, 0, 0, 0, 1, 0, 240, 8);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (24, '驯兽场', 'xun_shou_chang', 30, 0, 0, 40, 0, 0, 15, 0, 0, 40, 0, 0, 0, 1, 0, 240, 3);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (3, '兵部', 'bing_bu', 45, 0, 0, 40, 0, 0, 45, 0, 0, 80, 0, 0, 0, 1, 0, 360, 6);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (31, '木棚', 'mu_peng', 35, 0, 0, 35, 0, 100, 35, 0, 0, 45, 0, 0, 0, 1, 0, 360, 2);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (29, '矿库', 'kuang_ku', 35, 0, 0, 40, 0, 0, 120, 0, 0, 45, 0, 0, 0, 1, 0, 240, 2);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (30, '粮仓', 'liang_cang', 30, 0, 100, 35, 0, 0, 35, 0, 0, 45, 0, 0, 0, 1, 0, 360, 2);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (36, '矿场', 'kuang_chang', 35, 0, 0, 35, 0, 0, 25, 5, 15, 10, 0, 0, 0, 1, 0, 240, 1);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (35, '木场', 'mu_chang', 50, 0, 0, 40, 5, 30, 35, 0, 0, 10, 0, 0, 0, 1, 0, 360, 1);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (34, '粮田', 'liang_tian', 40, 5, 20, 35, 0, 0, 25, 0, 0, 15, 0, 0, 0, 1, 0, 360, 1);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (33, '忠烈祠', 'zhong_lie_ci', 50, 0, 0, 40, 0, 0, 30, 0, 0, 40, 0, 1, 1, 1, 0, 360, 4);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (1, '皇宫', 'huang_gong', 90, 0, 0, 120, 0, 0, 100, 0, 0, 150, 300, 0, 0, 1, 100, 1200, 9);
INSERT INTO city_buildingelement (id, name, code, food, food_speed, food_storage, wood, wood_speed, wood_storage, ore, ore_speed, ore_storage, gold, gold_storage, horse, dog, people, people_storage, "time", civilization_value) VALUES (2, '府衙', 'fu_ya', 90, 0, 0, 120, 0, 0, 100, 0, 0, 150, 300, 0, 0, 1, 0, 480, 8);


--
-- PostgreSQL database dump complete
--

