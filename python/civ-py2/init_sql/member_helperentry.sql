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
-- Name: member_helperentry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('member_helperentry_id_seq', 6, true);


--
-- Data for Name: member_helperentry; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO member_helperentry (id, name, slug, helper_catalog_id, language, is_public, content, last_date) VALUES (4, '遇九回一', 'nine-one-zh-cn', 2, 'zh-cn', true, '遇九回一，是指按顺序执行编号为1-9的序号时，有时是从中间某数开始执行，此时执行到9后，如果还可以执行，则回复至1序。如456789123，789123456等。', '2009-06-22 23:01:29+08');
INSERT INTO member_helperentry (id, name, slug, helper_catalog_id, language, is_public, content, last_date) VALUES (2, 'Thank Every Player', 'thank-every-player-en', 1, 'en', true, 'Thank Every Player.', '2009-06-21 22:48:12+08');
INSERT INTO member_helperentry (id, name, slug, helper_catalog_id, language, is_public, content, last_date) VALUES (3, '测试', 'zh-cn', 1, 'zh-cn', true, '测试', '2009-06-21 22:48:50+08');
INSERT INTO member_helperentry (id, name, slug, helper_catalog_id, language, is_public, content, last_date) VALUES (1, '感谢玩友', 'thank-every-player-zh-cn', 1, 'zh-cn', true, '感谢各位玩家。', '2009-06-21 22:45:43+08');
INSERT INTO member_helperentry (id, name, slug, helper_catalog_id, language, is_public, content, last_date) VALUES (5, '关于游戏中的级别进阶', 'about-level-zh-cn', 2, 'zh-cn', false, '游戏大量体现九和十二的数字概念，因九为中国传统文化最大阳数，十二为中国传统文化最大阴数。皇帝也称为九五之尊重，这些数字概念仅是为宣场中华文化，有些地方可以商量更改，不用这些数字概念。', '2009-06-22 23:02:49+08');
INSERT INTO member_helperentry (id, name, slug, helper_catalog_id, language, is_public, content, last_date) VALUES (6, '游戏将于七月初正式启动', 'start-up-in-july', 3, 'zh-cn', false, '游戏将于七月初正式启动。', '2009-06-22 23:11:11+08');


--
-- PostgreSQL database dump complete
--

