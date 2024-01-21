--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

-- Started on 2024-01-22 00:22:25

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16438)
-- Name: userscredits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.userscredits (
    user_id bigint NOT NULL,
    credits bigint DEFAULT 200 NOT NULL,
    user_name text,
    gender text
);


ALTER TABLE public.userscredits OWNER TO postgres;

--
-- TOC entry 4833 (class 0 OID 16438)
-- Dependencies: 215
-- Data for Name: userscredits; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.userscredits (user_id, credits, user_name, gender) FROM stdin;
6414782114	8	Gfdvn	male
902258385	1	Женя	\N
687228036	4	аллах	female
6826384548	3297	Annie	male
1483622044	24180	Артемий	male
5636576703	0	Артем	\N
6511162898	72	JC	male
6756248458	199	Pigu	\N
\.


--
-- TOC entry 4689 (class 2606 OID 16443)
-- Name: userscredits userscredits_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userscredits
    ADD CONSTRAINT userscredits_pkey PRIMARY KEY (user_id);


-- Completed on 2024-01-22 00:22:26

--
-- PostgreSQL database dump complete
--

