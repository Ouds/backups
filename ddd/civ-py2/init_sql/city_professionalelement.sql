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
-- Name: city_professionalelement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('city_professionalelement_id_seq', 33, true);


--
-- Data for Name: city_professionalelement; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (1, '文官', 'wen_guan', 1, 1, 1, 1, 1, 1, 1, 1, 11);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (3, '武将', 'wu_jiang', 3, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (2, '学士', 'xue_shi', 5, 1, 1, 1, 1, 1, 1, 1, 11);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (4, '女将', 'nv_jiang', 3, 2, 2, 2, 2, 2, 2, 1, 2);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (5, '儒将', 'ru_jiang', 3, 3, 3, 3, 3, 3, 3, 1, 3);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (6, '水门提督', 'shui_men_ti_du', 4, 4, 4, 4, 4, 4, 4, 1, 4);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (7, '运粮官', 'yun_liang_guan', 4, 4, 4, 4, 4, 4, 4, 1, 4);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (8, '大营建', 'da_ying_zao', 6, 4, 4, 4, 4, 4, 4, 1, 4);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (9, '市舶尹', 'shi_bo_yi', 7, 2, 2, 2, 2, 2, 2, 1, 2);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (10, '驯兽师', 'xun_shou_shi', 24, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (11, '酿酒师', 'niang_jiu_shi', 12, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (12, '陶瓷匠', 'tao_ci_jiang', 26, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (13, '木匠', 'mu_jiang', 27, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (14, '石匠', 'shi_jiang', 28, 4, 4, 4, 4, 4, 4, 1, 4);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (15, '厨师', 'chu_shi', 8, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (16, '乐师', 'yue_shi', 9, 3, 3, 3, 3, 3, 3, 1, 3);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (17, '棋士', 'qi_shi', 11, 4, 4, 4, 4, 4, 4, 1, 4);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (18, '调酒师', 'tiao_jiu_shi', 10, 3, 3, 3, 3, 3, 3, 1, 3);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (19, '画师', 'hua_shi', 12, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (20, '景苑师', 'jing_yuan_shi', 13, 4, 4, 4, 4, 4, 4, 1, 4);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (21, '游侠', 'you_xia', 14, 4, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (22, '巫师', 'wu_shi', 15, 3, 3, 3, 3, 3, 3, 1, 3);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (23, '精灵', 'jing_ling', 15, 3, 3, 3, 3, 3, 3, 1, 3);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (24, '道士', 'dao_shi', 16, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (25, '僧侣', 'seng_lv', 17, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (26, '牧师', 'mu_shi', 18, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (27, '阿訇', 'a_hong', 19, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (28, '鸿胪寺卿', 'hong_lu_si_qing', 20, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (29, '大夫', 'da_fu', 21, 5, 5, 5, 5, 5, 5, 1, 5);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (30, '精矿师', 'jing_kuang_shi', 22, 4, 4, 4, 4, 4, 4, 1, 4);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (31, '器械师', 'qi_xi_shi', 23, 4, 4, 4, 4, 44, 4, 1, 4);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (32, '兵器匠', 'bing_qi_jiang', 32, 4, 4, 4, 4, 4, 4, 1, 4);
INSERT INTO city_professionalelement (id, name, code, building_element_id, jiu_shui, mu_qi, yu_qi, ci_qi, horse, dog, gold, "time") VALUES (33, '司仪', 'si_yi', 33, 5, 5, 5, 5, 5, 5, 1, 5);


--
-- PostgreSQL database dump complete
--

