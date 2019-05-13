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
-- Name: member_helpercatalog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('member_helpercatalog_id_seq', 10, true);


--
-- Data for Name: member_helpercatalog; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO member_helpercatalog (id, name, slug) VALUES (1, '感谢辞', 'tribute');
INSERT INTO member_helpercatalog (id, name, slug) VALUES (2, '专有名词', 'proper-noun');
INSERT INTO member_helpercatalog (id, name, slug) VALUES (3, '重要公示', 'bulletin');
INSERT INTO member_helpercatalog (id, name, slug) VALUES (4, '时区概念', 'time-zone');
INSERT INTO member_helpercatalog (id, name, slug) VALUES (5, '玩家帐号', 'member-account');
INSERT INTO member_helpercatalog (id, name, slug) VALUES (6, '城市建筑', 'city-building');
INSERT INTO member_helpercatalog (id, name, slug) VALUES (7, '科技概念', 'tech');
INSERT INTO member_helpercatalog (id, name, slug) VALUES (8, '军事战争', 'military-battle');
INSERT INTO member_helpercatalog (id, name, slug) VALUES (9, '地图坐标', 'map-coordinate');
INSERT INTO member_helpercatalog (id, name, slug) VALUES (10, '盟邦协作', 'ally-cooperate');


--
-- PostgreSQL database dump complete
--

