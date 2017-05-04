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
-- Name: member_techelement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('member_techelement_id_seq', 1, false);


--
-- Data for Name: member_techelement; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (1, '政治学', 'zheng_zhi_xue', 150, 500, 1200, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (6, '艺术', 'yi_shu', 350, 850, 1500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (7, '烹饪', 'peng_ren', 350, 850, 1500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (2, '文字', 'wen_zi', 150, 600, 1200, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (3, '算数', 'shu_xue', 200, 600, 1200, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (5, '原始哲学', 'yuan_shi_zhe_xue', 150, 800, 1200, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (8, '围棋', 'wei_qi', 380, 1200, 1700, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (17, '科学方法', 'ke_ji_fang_fa', 800, 3500, 7000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (16, '教育学', 'jiao_yu_xue', 500, 3500, 5500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (15, '医学', 'yi_xue', 500, 2500, 5500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (14, '基督教', 'ji_du_jiao', 650, 2500, 3500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (13, '伊斯兰教', 'yi_si_lan_jiao', 650, 2500, 3500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (12, '道教', 'dao_jiao', 650, 2500, 3500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (11, '佛教', 'fo_jiao', 650, 2500, 3500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (10, '宗教', 'zong_jiao', 600, 2000, 3500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (9, '天文学', 'tian_wen_xue', 420, 1800, 2200, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (19, '耕种技术', 'gen_zhong_ji_shu', 1000, 5000, 8500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (20, '打井术', 'da_jin_shu', 1100, 6000, 9000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (21, '良田术', 'liang_tian_shu', 1200, 3500, 3000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (22, '探矿术', 'tan_kuang_shu', 1200, 5000, 3500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (23, '补种术', 'bu_zhong_shu', 1200, 3500, 2400, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (24, '石料深加工技术', 'shi_liao_shen_jia_gong_ji_shu', 1300, 4500, 7000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (25, '工具改良术', 'gong_ju_gai_liang_shu', 1500, 7000, 10000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (26, '建筑学', 'jian_zhu_xue', 1500, 9000, 11000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (27, '工程学', 'gong_cheng_xue', 1500, 7500, 11000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (18, '科举制度', 'ke_ju_zhi_du', 1000, 5000, 8000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (28, '加工工艺学', 'jia_gong_gong_yi_xue', 1600, 5000, 4000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (29, '高级加工工艺学', 'gao_ji_jia_gong_gong_yi_xue', 2000, 12000, 14000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (30, '贸易法', 'mao_yi_fa', 800, 2500, 2000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (31, '驯养术', 'xun_yang_shu', 1200, 3500, 5000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (32, '马匹改良术', 'ma_pi_gai_liang_shu', 2500, 6000, 12000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (33, '管理学', 'guan_li_xue', 1500, 9000, 12000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (34, '灾害预防', 'zai_hai_yu_fang', 2500, 6000, 7000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (35, '冶锻技术', 'ye_lian_ji_shu', 2500, 9000, 12000, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (36, '纺织编织技术', 'fang_zhi_bian_zhi_ji_shu', 1800, 3500, 4500, 1);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (37, '阵法研究', 'zhe_fa_yan_jiu', 2800, 12000, 12000, 7);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (38, '兵法传承', 'bing_fa_chuan_cheng', 3000, 15000, 15000, 2);
INSERT INTO member_techelement (id, name, code, civilization_value, gold, "time", prestige) VALUES (4, '几何', 'ji_he', 100, 600, 1200, 1);


--
-- PostgreSQL database dump complete
--

