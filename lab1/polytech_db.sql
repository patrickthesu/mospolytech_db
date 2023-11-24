--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 15.4

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

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS '';


--
-- Name: doc_type; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.doc_type AS ENUM (
    'Russian passport',
    'Foreign passpor',
    'Other'
);


ALTER TYPE public.doc_type OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: department; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.department (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    faculy_id integer NOT NULL,
    head_id integer NOT NULL
);


ALTER TABLE public.department OWNER TO postgres;

--
-- Name: department_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.department_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.department_id_seq OWNER TO postgres;

--
-- Name: department_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.department_id_seq OWNED BY public.department.id;


--
-- Name: document; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.document (
    id integer NOT NULL,
    document_type public.doc_type NOT NULL,
    series_number character varying(30) NOT NULL
);


ALTER TABLE public.document OWNER TO postgres;

--
-- Name: document_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.document_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.document_id_seq OWNER TO postgres;

--
-- Name: document_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.document_id_seq OWNED BY public.document.id;


--
-- Name: faculty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faculty (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    dean_id integer NOT NULL,
    description text
);


ALTER TABLE public.faculty OWNER TO postgres;

--
-- Name: faculty_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.faculty_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faculty_id_seq OWNER TO postgres;

--
-- Name: faculty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.faculty_id_seq OWNED BY public.faculty.id;


--
-- Name: student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student (
    id integer NOT NULL,
    full_name character varying(255) NOT NULL,
    student_group_id integer NOT NULL,
    is_leader boolean DEFAULT false NOT NULL,
    document_id integer NOT NULL
);


ALTER TABLE public.student OWNER TO postgres;

--
-- Name: student_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_group (
    id integer NOT NULL,
    name character varying(10) NOT NULL,
    department_id integer NOT NULL
);


ALTER TABLE public.student_group OWNER TO postgres;

--
-- Name: student_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_group_id_seq OWNER TO postgres;

--
-- Name: student_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_group_id_seq OWNED BY public.student_group.id;


--
-- Name: student_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_id_seq OWNER TO postgres;

--
-- Name: student_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_id_seq OWNED BY public.student.id;


--
-- Name: worker; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.worker (
    id integer NOT NULL,
    full_name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    password character varying(255) NOT NULL
);


ALTER TABLE public.worker OWNER TO postgres;

--
-- Name: worker_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.worker_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.worker_id_seq OWNER TO postgres;

--
-- Name: worker_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.worker_id_seq OWNED BY public.worker.id;


--
-- Name: department id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department ALTER COLUMN id SET DEFAULT nextval('public.department_id_seq'::regclass);


--
-- Name: document id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.document ALTER COLUMN id SET DEFAULT nextval('public.document_id_seq'::regclass);


--
-- Name: faculty id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty ALTER COLUMN id SET DEFAULT nextval('public.faculty_id_seq'::regclass);


--
-- Name: student id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student ALTER COLUMN id SET DEFAULT nextval('public.student_id_seq'::regclass);


--
-- Name: student_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group ALTER COLUMN id SET DEFAULT nextval('public.student_group_id_seq'::regclass);


--
-- Name: worker id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker ALTER COLUMN id SET DEFAULT nextval('public.worker_id_seq'::regclass);


--
-- Data for Name: department; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.department (id, name, faculy_id, head_id) FROM stdin;
1	Инфокогнитивные технологии	1	3
2	Прикладная информатика	1	4
3	СМАРТ-технологии	1	5
4	Информационная безопасность	1	6
5	Менеджмент	2	7
6	Реклама и связи с общественностью в медиаиндустрии	2	8
7	Управление персоналом	2	9
8	Экономика и организация	2	10
\.


--
-- Data for Name: document; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.document (id, document_type, series_number) FROM stdin;
1	Russian passport	1108 571722
2	Russian passport	5469 259809
3	Russian passport	3147 179139
4	Russian passport	6316 590950
5	Russian passport	8748 971882
6	Russian passport	4937 330704
7	Russian passport	7117 911234
8	Russian passport	6034 638431
9	Russian passport	1571 193896
10	Russian passport	7007 282869
11	Russian passport	3629 746449
12	Russian passport	6840 960959
13	Russian passport	5784 130420
14	Russian passport	6606 458299
15	Russian passport	7312 410194
16	Russian passport	4896 685041
17	Russian passport	5132 963380
18	Russian passport	1866 540730
19	Russian passport	5556 230443
20	Russian passport	6761 523176
21	Russian passport	9079 195996
22	Russian passport	8426 888076
23	Russian passport	9010 163573
24	Russian passport	2983 422569
25	Russian passport	2637 630598
26	Russian passport	9770 378287
27	Russian passport	7926 689354
28	Russian passport	1484 944678
29	Russian passport	7140 911720
30	Russian passport	6062 432741
31	Russian passport	9948 553592
32	Russian passport	6337 316160
33	Russian passport	4230 691539
34	Russian passport	7999 754563
35	Russian passport	3231 522581
36	Russian passport	9661 638002
37	Russian passport	1620 748014
38	Russian passport	2771 562624
39	Russian passport	6610 911195
40	Russian passport	3120 891971
41	Russian passport	3455 769455
42	Russian passport	1572 236474
43	Russian passport	3641 167120
44	Russian passport	3929 234463
45	Russian passport	3813 565713
46	Russian passport	9361 717632
47	Russian passport	1586 985730
48	Russian passport	3655 988932
49	Russian passport	2952 317854
50	Russian passport	8372 905213
51	Russian passport	6779 784476
52	Russian passport	5276 547287
53	Russian passport	6082 213308
54	Russian passport	7305 537047
55	Russian passport	8069 840878
56	Russian passport	6211 580716
57	Russian passport	4035 385155
58	Russian passport	9435 787561
59	Russian passport	7218 459518
60	Russian passport	1751 246995
61	Russian passport	6257 207117
62	Russian passport	4604 694238
63	Russian passport	3402 852181
64	Russian passport	7913 817865
65	Russian passport	4576 579912
66	Russian passport	6498 119876
67	Russian passport	1339 530916
68	Russian passport	6741 770302
69	Russian passport	2522 854423
70	Russian passport	4117 743314
71	Russian passport	9852 256352
72	Russian passport	6474 671342
73	Russian passport	8999 347709
74	Russian passport	4603 461411
75	Russian passport	9663 448630
76	Russian passport	7393 747443
77	Russian passport	5987 504962
78	Russian passport	5508 776549
79	Russian passport	1464 635867
80	Russian passport	3625 634351
81	Russian passport	6588 100469
82	Russian passport	9819 785381
83	Russian passport	9581 470582
84	Russian passport	3713 127987
85	Russian passport	5997 431313
86	Russian passport	2177 475171
87	Russian passport	8059 305840
88	Russian passport	1495 521410
89	Russian passport	9266 597434
90	Russian passport	1139 287096
91	Russian passport	1314 738924
92	Russian passport	9825 868509
93	Russian passport	7136 634459
94	Russian passport	3472 555878
95	Russian passport	4179 994682
96	Russian passport	1483 159561
97	Russian passport	3156 916794
98	Russian passport	9863 663038
99	Russian passport	9414 764374
100	Russian passport	7850 929981
101	Russian passport	5447 269703
102	Russian passport	2369 894921
103	Russian passport	7755 555738
104	Russian passport	2808 709439
105	Russian passport	8893 425485
106	Russian passport	1684 692262
107	Russian passport	1420 490389
108	Russian passport	9108 859864
109	Russian passport	7613 532760
110	Russian passport	4044 595209
111	Russian passport	7970 509204
112	Russian passport	2496 109688
113	Russian passport	1533 813980
114	Russian passport	7132 626345
115	Russian passport	1941 525154
116	Russian passport	5740 984343
117	Russian passport	4206 105729
118	Russian passport	9982 132664
119	Russian passport	2800 518427
120	Russian passport	2052 191124
121	Russian passport	5703 522436
122	Russian passport	9351 866245
123	Russian passport	5831 754971
124	Russian passport	6507 612604
125	Russian passport	1543 558894
126	Russian passport	4219 870545
127	Russian passport	5260 798910
128	Russian passport	7587 828167
129	Russian passport	9661 290212
130	Russian passport	3259 689846
131	Russian passport	6012 810385
132	Russian passport	4824 427067
133	Russian passport	6579 891866
134	Russian passport	4018 800323
135	Russian passport	6467 492964
136	Russian passport	6268 587980
137	Russian passport	5204 483424
138	Russian passport	4844 248595
139	Russian passport	4767 544459
140	Russian passport	1789 406525
141	Russian passport	6467 357445
142	Russian passport	8005 579172
143	Russian passport	6239 118914
144	Russian passport	5670 770106
145	Russian passport	1578 597131
146	Russian passport	3090 770425
147	Russian passport	9350 843741
148	Russian passport	5023 780509
149	Russian passport	5071 376122
150	Russian passport	7264 373545
151	Russian passport	2522 679694
152	Russian passport	7784 999415
153	Russian passport	9788 196759
154	Russian passport	8369 845632
155	Russian passport	2180 923300
156	Russian passport	7952 911364
157	Russian passport	2581 972947
158	Russian passport	8860 739531
159	Russian passport	1345 504135
160	Russian passport	9796 774324
161	Russian passport	3641 823187
162	Russian passport	2962 209579
163	Russian passport	1679 656698
164	Russian passport	7886 339154
165	Russian passport	1847 825291
166	Russian passport	3048 913892
167	Russian passport	2626 358402
168	Russian passport	5388 350201
169	Russian passport	5023 948550
170	Russian passport	1983 213201
171	Russian passport	3465 250742
172	Russian passport	3623 997519
173	Russian passport	4790 860794
174	Russian passport	2163 135293
175	Russian passport	1569 443486
176	Russian passport	2944 570194
177	Russian passport	6062 755970
178	Russian passport	2743 890992
179	Russian passport	2688 530096
180	Russian passport	1013 945419
181	Russian passport	5787 130587
182	Russian passport	2878 192389
183	Russian passport	4001 346837
184	Russian passport	8179 270297
185	Russian passport	2574 894175
186	Russian passport	6921 510851
187	Russian passport	8243 893927
188	Russian passport	7185 867483
189	Russian passport	9023 525343
190	Russian passport	1547 605196
191	Russian passport	5529 456310
192	Russian passport	8676 864742
193	Russian passport	4161 955474
194	Russian passport	7475 254895
195	Russian passport	5023 183790
196	Russian passport	2495 661959
197	Russian passport	5589 951312
198	Russian passport	9738 635205
199	Russian passport	4796 893184
200	Russian passport	3692 390743
201	Russian passport	1114 367951
202	Russian passport	4820 681238
203	Russian passport	8823 171528
204	Russian passport	4448 545172
205	Russian passport	1664 924304
206	Russian passport	9150 106483
207	Russian passport	1267 764988
208	Russian passport	7989 635937
209	Russian passport	2947 815255
210	Russian passport	6788 700590
211	Russian passport	7806 192624
212	Russian passport	4646 469378
213	Russian passport	9647 486168
214	Russian passport	5285 865205
215	Russian passport	9871 170533
216	Russian passport	5506 882100
217	Russian passport	1469 584708
218	Russian passport	8986 539131
219	Russian passport	1512 744045
220	Russian passport	9886 542730
221	Russian passport	9804 630882
222	Russian passport	6994 801015
223	Russian passport	5264 898858
224	Russian passport	7043 385276
225	Russian passport	8959 172839
226	Russian passport	2364 589776
227	Russian passport	9071 909639
228	Russian passport	3772 237512
229	Russian passport	9764 378773
230	Russian passport	4963 429511
231	Russian passport	8075 434993
232	Russian passport	3397 417333
233	Russian passport	5184 933867
234	Russian passport	9218 593107
235	Russian passport	3247 591327
236	Russian passport	3676 488419
237	Russian passport	5223 642794
238	Russian passport	9838 480020
239	Russian passport	8500 955746
240	Russian passport	2629 116121
241	Russian passport	4726 909015
242	Russian passport	6634 459093
243	Russian passport	3262 600514
244	Russian passport	2776 904258
245	Russian passport	1985 656557
246	Russian passport	3656 744697
247	Russian passport	1172 518964
248	Russian passport	5732 352686
249	Russian passport	9814 705459
250	Russian passport	1137 708263
251	Russian passport	5900 748798
252	Russian passport	4559 929727
253	Russian passport	8468 911214
254	Russian passport	2901 564139
255	Russian passport	1076 311486
256	Russian passport	4512 854870
257	Russian passport	5058 715857
258	Russian passport	8160 654341
259	Russian passport	5700 454467
260	Russian passport	2045 217491
261	Russian passport	7274 510686
262	Russian passport	3199 168902
263	Russian passport	8076 810300
264	Russian passport	6352 106013
265	Russian passport	8614 546674
266	Russian passport	4236 793148
267	Russian passport	6188 412994
268	Russian passport	2812 771659
269	Russian passport	9733 445593
270	Russian passport	7678 413834
271	Russian passport	4969 875532
272	Russian passport	2577 187794
273	Russian passport	2205 949624
274	Russian passport	9665 640515
275	Russian passport	4870 490817
276	Russian passport	4780 330382
277	Russian passport	5488 342461
278	Russian passport	1370 609718
279	Russian passport	1560 464180
280	Russian passport	6055 823202
281	Russian passport	4659 193046
282	Russian passport	7099 764025
283	Russian passport	2213 329129
284	Russian passport	4036 716662
285	Russian passport	8284 744768
286	Russian passport	1281 398880
287	Russian passport	6557 747858
288	Russian passport	7525 926464
289	Russian passport	7333 263206
290	Russian passport	6749 581988
291	Russian passport	7121 295629
292	Russian passport	5984 422722
293	Russian passport	2788 972505
294	Russian passport	8600 986122
295	Russian passport	7462 578771
296	Russian passport	7128 809804
297	Russian passport	6450 969752
298	Russian passport	3186 416174
299	Russian passport	2438 575213
300	Russian passport	5598 328986
301	Russian passport	7574 540948
302	Russian passport	7825 447295
303	Russian passport	7966 796995
304	Russian passport	5803 454883
305	Russian passport	1953 627503
306	Russian passport	9966 912100
307	Russian passport	6812 139579
308	Russian passport	2661 630487
309	Russian passport	5639 523782
310	Russian passport	6628 355853
311	Russian passport	3023 497969
312	Russian passport	2067 286616
313	Russian passport	5647 204472
314	Russian passport	8561 795550
315	Russian passport	9887 787978
316	Russian passport	2292 561337
317	Russian passport	8279 778943
318	Russian passport	7270 438133
319	Russian passport	1461 906263
320	Russian passport	2801 150766
321	Russian passport	1874 523966
322	Russian passport	6912 285762
323	Russian passport	3685 236394
324	Russian passport	6746 151823
325	Russian passport	6621 785924
326	Russian passport	6864 288162
327	Russian passport	3477 319405
328	Russian passport	2928 196921
329	Russian passport	5215 917939
330	Russian passport	1268 786269
331	Russian passport	1967 378790
332	Russian passport	7025 825880
333	Russian passport	5101 293011
334	Russian passport	4177 861354
335	Russian passport	7286 466485
336	Russian passport	1924 564901
337	Russian passport	1766 131888
338	Russian passport	1825 831045
339	Russian passport	7025 996663
340	Russian passport	1877 816849
341	Russian passport	2523 696123
342	Russian passport	9170 382247
343	Russian passport	1709 807634
344	Russian passport	8535 256015
345	Russian passport	3724 143523
346	Russian passport	3446 755646
347	Russian passport	2947 614689
348	Russian passport	7096 204081
349	Russian passport	3683 607905
350	Russian passport	5658 473390
351	Russian passport	5823 106926
352	Russian passport	7192 364008
353	Russian passport	2479 762438
354	Russian passport	5961 303384
355	Russian passport	5902 102611
356	Russian passport	6710 302149
357	Russian passport	1346 854917
358	Russian passport	7829 266355
359	Russian passport	1465 521675
360	Russian passport	7883 584403
361	Russian passport	2948 605005
362	Russian passport	3739 530283
363	Russian passport	8884 706375
364	Russian passport	7460 596314
365	Russian passport	5784 537067
366	Russian passport	4780 416430
367	Russian passport	6714 866486
368	Russian passport	5751 302240
369	Russian passport	7803 803019
370	Russian passport	4336 700237
371	Russian passport	3830 173216
372	Russian passport	3889 585868
373	Russian passport	9479 500309
374	Russian passport	2173 829167
375	Russian passport	7085 984355
376	Russian passport	1425 114238
377	Russian passport	4230 633272
378	Russian passport	5949 568981
379	Russian passport	8402 225197
380	Russian passport	7463 699357
381	Russian passport	9655 925555
382	Russian passport	5682 317583
383	Russian passport	3815 948772
384	Russian passport	3521 129328
385	Russian passport	9562 949368
386	Russian passport	5824 371836
387	Russian passport	6098 641799
388	Russian passport	1237 448564
389	Russian passport	2269 172018
390	Russian passport	3027 626366
391	Russian passport	9444 722050
392	Russian passport	6609 218691
393	Russian passport	3612 210215
394	Russian passport	3048 773691
395	Russian passport	8407 612129
396	Russian passport	2848 316436
397	Russian passport	3060 643278
398	Russian passport	1962 158452
399	Russian passport	3221 484165
400	Russian passport	6567 185429
401	Russian passport	4328 910083
402	Russian passport	4101 786936
403	Russian passport	7226 884848
404	Russian passport	9846 897962
405	Russian passport	5580 745498
406	Russian passport	5792 524384
407	Russian passport	8666 695925
408	Russian passport	2781 480160
409	Russian passport	8795 921893
410	Russian passport	5027 517760
411	Russian passport	4030 339090
412	Russian passport	8923 958013
413	Russian passport	1449 877137
414	Russian passport	3086 228183
415	Russian passport	1578 141408
416	Russian passport	6015 331147
417	Russian passport	1770 562728
418	Russian passport	8278 729485
419	Russian passport	3523 454912
420	Russian passport	2381 502061
421	Russian passport	2756 471253
422	Russian passport	8820 790645
423	Russian passport	3671 130582
424	Russian passport	4014 495155
\.


--
-- Data for Name: faculty; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.faculty (id, name, dean_id, description) FROM stdin;
1	Факультет информационных технологий	1	Мы знаем как сделать учебу увлекательной\n\nОбразовательные программы созданы совместно с профессионалами из Ассоциации Интернет Разработчиков, 1С, Autodesk, Mail.ru, Лаборатории Касперского, Яндекса и других ведущих ИТ-компаний, поэтому студенты получают самые актуальные знания и легко находят работу уже во время учебы на старших курсах.\n\nМы оперативно реагируем на изменения ИТ-рынка и каждый год вносим изменения в учебные планы, а 30% наших преподавателей – руководители и сотрудники ведущих IT-компаний.\n\nОсобое внимание уделяется развитию прикладных навыков – работа над реальными проектами является обязательной частью учебного процесса, начиная с первого семестра. Каждый семестр представители деловой среды формируют пакет заданий, поэтому у каждого выпускника за плечами как минимум 8 готовых ИТ-проектов и опыт работы с индустриальным заказчиком. Или студент может развивать свой стартап, как это сделали студенты из проекта GreenPL\n\nВместе с тем мы понимаем, что для успешной карьеры только профессиональных навыков уже недостаточно, поэтому активно развиваем коммуникативные и предпринимательские навыки (soft skills). Кроме того, начиная с первого семестра, вы можете проходить бесплатное обучение на сертифицированных курсах и программах 1С, Cisco, Microsoft, Digital Design и других. Выпускникам курсов выдаются международные сертификаты.\n\nУчиться у нас интересно: экзамены по прикладным дисциплинам проходят не по теоретическим билетам, а в форме решения реальных кейсов от ИТ-компаний. Например, нужно за один или несколько дней разработать сложный веб-сайт, мобильное приложение, или собрать и запрограммировать робота.
2	Факультет экономики и управления	2	Что мы делаем?\n\nМы даём только нужные знания и ничего лишнего. Точечная подготовка кадров под конкретные управленческие позиции по заказу отраслевых предприятий обеспечивает востребованность всех наших выпускников.\n\nОбучаясь у нас, вы не только получите теоретические знания, прикладные навыки, приобретёте управленческие компетенции, но и станете обладателями незаурядных знаний, научитесь командной работе, приобретете лидерские и организаторские качества. Часть занятий построена в формате игр и реальных кейсов. На чемпионатах по Управленческим боям студенты развивают soft skills, учатся аргументировать и отстаивать свою позицию, решать ситуационные задачи, в «Парламентском клубе» тренируют навыки публичных выступлений, а на Digital PRактике проводят маркетинговые исследования и создают рекламные проекты. В процессе обучения со студентами проводятся практикоориентированные занятия в управе и префектуре района, Московской Городской Думе, Государственной Думе РФ, Совете Федерации. Проводить мастер-классы приглашают представителей коммуникационных агентств. Стажировку и практику наши студенты проходят в таких компаниях как Samsung, BMW, Газпром, Ростелеком, Сбербанк, Промсвязьбанк, МГТС, Мосгортранс, Мосавтосантранс, Минэкономразвития, Минпром, Минтранс, Министерстве науки и высшего образования РФ, аппарате Госдумы, Федеральном казначействе РФ, администрациях и управах районов Москвы.\n
\.


--
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student (id, full_name, student_group_id, is_leader, document_id) FROM stdin;
1	Алиомаров Тимур Алиомарович	1	f	1
2	Буракова Полина Юрьевна	1	f	2
3	Вашкевич Алексей Константинович	1	f	3
4	Глушков Андрей Андреевич	1	f	4
5	Давыдов Артём Сергеевич	1	f	5
6	Данилкина Дарья Александровна	1	f	6
7	Закарян Михаил Арманович	1	f	7
8	Каспрук Дмитрий Леонидович	1	f	8
9	Комендант Максим Игоревич	1	f	9
10	Корнеева Елизавета Сергеевна	1	f	10
11	Кучерова Мария Андреевна	1	f	11
12	Макарова Дарья Антоновна	1	f	12
13	Мурадян Лусинэ Гамлетовна	1	f	13
14	Попов Никита Сергеевич	1	f	14
15	Самойлова Валерия Александровна	1	f	15
16	Седых Евгений Максимович	1	f	16
17	Толмацкая Ирина Алексеевна	1	f	17
18	Шаповалов Александр Витальевич	1	f	18
19	Шишигина Кристина Николаевна	1	f	19
20	Шрейдер Кристина Ивановна	1	f	20
21	Яровой Денис Романович	1	f	21
22	Беликова Милана Витальевна	2	f	22
23	Ворошнина София Павловна	2	f	23
24	Гридчина Ангелина Андреевна	2	f	24
25	Долгов Дмитрий Александрович	2	f	25
26	Ершов Иван Олегович	2	f	26
27	Зайцев Константин Александрович	2	f	27
28	Ишкильдин Рамазан Фанилевич	2	f	28
29	Ишмухаметов Даниль Ринатович	2	f	29
30	Квашнина Ирина Александровна	2	f	30
31	Кириллов Вячеслав Александрович	2	f	31
32	Короткий Иван Михайлович	2	f	32
33	КУДРЯВЦЕВА ВАЛЕРИЯ АЛЕКСАНДРОВНА	2	f	33
34	КУШНАРЕВА МАРИЯ МИХАЙЛОВНА	2	f	34
35	МАКСИМОВ МАКСИМ АЛЕКСАНДРОВИЧ	2	f	35
36	Миндов Артём Владимирович	2	f	36
37	Мочалова Анастасия Вячеславовна	2	f	37
38	Набатчиков Никита Игоревич	2	f	38
39	Никифоров Александр Юрьевич	2	f	39
40	Ольховский Артём Сергеевич	2	f	40
41	Пахомова Анна Викторовна	2	f	41
42	Прокофьев Фёдор Олегович	2	f	42
43	Пуговкин Виктор Владимирович	2	f	43
44	Рыскин Сергей Денисович	2	f	44
45	Сапфиров Илья Александрович	2	f	45
46	Соболев Даниил Игоревич	2	f	46
47	СОКОЛОВ МАТВЕЙ ОЛЕГОВИЧ	2	f	47
48	Степанов Егор Фёдорович	2	f	48
49	Титенко Мария Петровна	2	f	49
50	Тохтабаев Шерзод Азат угли	2	f	50
51	Федюшкин Никита Андреевич	2	f	51
52	Хандаев Жаргал Арсаланович	2	f	52
53	Чурсина Анастасия Сергеевна	2	f	53
54	Шпарик Всеволод Сергеевич	2	f	54
55	Янышев Кирилл Александрович	2	f	55
56	Валеев Артур Ильсурович	3	f	56
57	Васильев Кирилл Александрович	3	f	57
58	Голубцов Родион Михайлович	3	f	58
59	Дроздов Савелий Александрович	3	f	59
60	Дукага Кобонго Грег Давид	3	f	60
61	Евсеев Федор Владимирович	3	f	61
62	Завьялова Дарья Константиновна	3	f	62
63	Игнатова Алина Алексеевна	3	f	63
64	Игнатова Валерия Алексеевна	3	f	64
65	Казарян Ашот Сергеевич	3	f	65
66	Карякин Иван Олегович	3	f	66
67	Касимцев Дамир Ринатович	3	f	67
68	Котенко Денис Вадимович	3	f	68
69	Лещинский Артём Игоревич	3	f	69
70	Лосев Артём Сергеевич	3	f	70
71	Пекунова Ольга Александровна	3	f	71
72	Прекин Артур Алексеевич	3	f	72
73	Прокуров Артемий Дмитриевич	3	f	73
74	Птушкин Петр Александрович	3	f	74
75	Репина Александра Денисовна	3	f	75
76	Свистушкин Егор Евгеньевич	3	f	76
77	Сёмкин Егор Николаевич	3	f	77
78	Скорцинский Данил Сергеевич	3	f	78
79	Степаненко Алексей Игоревич	3	f	79
80	Страшнова Ксения Валерьевна	3	f	80
81	Субботкина Екатерина Георгиевна	3	f	81
82	Сутурин Алексей Сергеевич	3	f	82
83	Тарасенко Наталия Дмитриевна	3	f	83
84	Тимонькина Виктория Викторовна	3	f	84
85	Тимошкова Юлия Александровна	3	f	85
86	Урамов Тимофей Леонидович	3	f	86
87	Федотова Юлия Сергеевна	3	f	87
88	Филатова Александра Игоревна	3	f	88
89	Хлюстова Екатерина Алексеевна	3	f	89
90	Хохлова Полина Андреевна	3	f	90
91	Чиркова Елизавета Олеговна	3	f	91
92	Чистяков Артем Дмитриевич	3	f	92
93	Шарипова Элиза Касымжановна	3	f	93
94	Аминова Амира Айнуровна	4	f	94
95	Базгудинов Тимур Айдарович	4	f	95
96	Барашков Илья Павлович	4	f	96
97	Гатиатуллина Лейсан Рафкатовна	4	f	97
98	Гаянов Айбулат Ильфакович	4	f	98
99	Гнездилова Дарья Владимировна	4	f	99
100	Гончаров Никита Валерьевич	4	f	100
101	ГРИГОРАЩЕНКО АНДРЕЙ АЛЕКСЕЕВИЧ	4	f	101
102	Денищенко Ксения Кирилловна	4	f	102
103	Дубинина Анна Сергеевна	4	f	103
104	Езгиндарова Варвара Сергеевна	4	f	104
105	Ерхов Вадим Игоревич	4	f	105
106	Зотова Дарья Владимировна	4	f	106
107	Илясов Дмитрий Витальевич	4	f	107
108	Казанцев Михаил Кириллович	4	f	108
109	Корбут Ренс Александрович	4	f	109
110	Кочетов Владимир Александрович	4	f	110
111	Крутов Петр Александрович	4	f	111
112	Култашева Алиса Сергеевна	4	f	112
113	Курмашев Дияр	4	f	113
114	Левицкий Артём Алексеевич	4	f	114
115	Мангушев Александр Витальевич	4	f	115
116	Мейриев Магомед-Амирхан Мусаевич	4	f	116
117	Мердеева Алина Рамилевна	4	f	117
118	Мирзоев Амирджон Гулшанович	4	f	118
119	Морозов Даниил Сергеевич	4	f	119
120	Надточей София Сергеевна	4	f	120
121	Намдыкова Ирина Александровна	4	f	121
122	Нургалиева Карина Маратовна	4	f	122
123	Нюдльчиев Владилен Геннадьевич	4	f	123
124	Остапчук Иван Андреевич	4	f	124
125	Перевозчиков Егор Леонидович	4	f	125
126	Сатюкова Татьяна Валерьевна	4	f	126
127	Стрелец Владислав	4	f	127
128	Тихомиров Роман Вячеславович	4	f	128
129	Трепов Максим Вячеславович	4	f	129
130	Фазлутдинова Карина Ринатовна	4	f	130
131	Федулов Иван Вячеславович	4	f	131
132	Холодова Елизавета Александровна	4	f	132
133	Черноусов Дмитрий Сергеевич	4	f	133
134	Чибарчиков Артем Ильнурович	4	f	134
135	Абдуллаева Алина Ринатовна	5	f	135
136	Алимпиев Глеб Павлович	5	f	136
137	Аминев Рамиль Рустемович	5	f	137
138	Баженов Александр Сергеевич	5	f	138
139	Волошин Максим Вадимович	5	f	139
140	Воронин Сергей Александрович	5	f	140
141	Головина Яна Михайловна	5	f	141
142	Гончаров Александр Дмитриевич	5	f	142
143	Евдокимова Марина Алексеевна	5	f	143
144	Жлобинский Владислав Алексеевич	5	f	144
145	Караманиц Георгий Сергеевич	5	f	145
146	Кибакин Виктор Михайлович	5	f	146
147	Кожалиев Сыймык Алтынбекович	5	f	147
148	Кошкин Степан Сергеевич	5	f	148
149	Крохалев Вячеслав Александрович	5	f	149
150	Линчак Дмитрий Юрьевич	5	f	150
151	Мальцев Артём Игоревич	5	f	151
152	Малюченко Светлана Александровна	5	f	152
153	Марченко Руслан Александрович	5	f	153
154	Носков Андрей Максимович	5	f	154
155	Роднов Кирилл Артемович	5	f	155
156	Фокин Илья Алексеевич	5	f	156
157	Хвостиков Семён Вадимович	5	f	157
158	Шаповалов Григорий Григорьевич	5	f	158
159	Шатаров Даниил Александрович	5	f	159
160	Юрков Матвей Алексеевич	5	f	160
161	Антипов Максим Анатольевич	6	f	161
162	Артамонов Денис Артурович	6	f	162
163	Борисов Андрей Александрович	6	f	163
164	Гетманская Софья Денисовна	6	f	164
165	Горшкова Дарья Олеговна	6	f	165
166	Емельянов Данил Николаевич	6	f	166
167	Ереминский Максим Валентинович	6	f	167
168	Зубарева Дарья Павловна	6	f	168
169	Калинин Антон Александрович	6	f	169
170	Китиашвили Вадим Гурамович	6	f	170
171	Клименко Никита Валентинович	6	f	171
172	Краснянская Алиса Александровна	6	f	172
173	Кузьмин Кирилл Сергеевич	6	f	173
174	Курбонов Аброр Музаффарович	6	f	174
175	Кухаренко Александр Дмитриевич	6	f	175
176	Лапина Вероника Александровна	6	f	176
177	Ляхов Александр Алексеевич	6	f	177
178	Метлякова Алина Андреевна	6	f	178
179	Соловьев Артем Викторович	6	f	179
180	Шалберкина Светлана Игоревна	6	f	180
181	Автухов Денис Александрович	7	f	181
182	Валов Алексей Васильевич	7	f	182
183	Волков Артём Александрович	7	f	183
184	Дыбова Ярослава Игоревна	7	f	184
185	Калачёва Анастасия Романовна	7	f	185
186	Королев Максим Дмитриевич	7	f	186
187	Лепешинский Егор Дмитриевич	7	f	187
188	Лисафьева Тамара Андреевна	7	f	188
189	Меньшенин Алексей Евгеньевич	7	f	189
190	Набоков Павел Николаевич	7	f	190
191	Намусси Тауфик	7	f	191
192	Непомнящих Игорь Алексеевич	7	f	192
193	Обухов Дмитрий Александрович	7	f	193
194	Петухов Данила Сергеевич	7	f	194
195	Платов Иван Витальевич	7	f	195
196	Резников Матвей Александрович	7	f	196
197	Рохас Миранда Марко Антонио	7	f	197
198	Савельев Михаил Артемович	7	f	198
199	Савчук Михаил Михайлович	7	f	199
200	Стрельников Сергей Андреевич	7	f	200
201	Тушенцов Александр Александрович	7	f	201
202	Флягин Евгений Константинович	7	f	202
203	Шабалин Александр Денисович	7	f	203
204	Штуров Роман Сергеевич	7	f	204
205	Абдуллаев Олим Улугбекович	8	f	205
206	Апокина Дарья Александровна	8	f	206
207	Барателия Тимур Адгурович	8	f	207
208	Батиевский Степан Ильич	8	f	208
209	Бибоев Хетаг Сосланович	8	f	209
210	Ванин Артём Викторович	8	f	210
211	Васин Глеб Алексеевич	8	f	211
212	Герасенков Илья Игоревич	8	f	212
213	Головкин Андрей Витальевич	8	f	213
214	Дейникин Максим Юрьевич	8	f	214
215	Зеленский Иван Алексеевич	8	f	215
216	Иванов Владислав Валерьевич	8	f	216
217	Касымов Эмин	8	f	217
218	Ким Ирина Алексеевна	8	f	218
219	Кудайбергенов Алишер Жолдошбекович	8	f	219
220	Кутузова Валерия Андреевна	8	f	220
221	Линьков Макс Александрович	8	f	221
222	Литвинов Иван Александрович	8	f	222
223	Мазин Илья Андреевич	8	f	223
224	Манукян Ваграм Георгович	8	f	224
225	Межитов Исмаил Равильевич	8	f	225
226	Миронов Мирон Андреевич	8	f	226
227	Михайлов Константин Максимович	8	f	227
228	Мишкин Михаил Андреевич	8	f	228
229	Николаев Михаил Артемович	8	f	229
230	Нуров Амир Тахирович	8	f	230
231	Осин Кирилл Андреевич	8	f	231
232	Пантелеев Дамил Денисович	8	f	232
233	Паринова Диана Александровна	8	f	233
234	Петроченко Кирилл	8	f	234
235	Петушкова Кира Андреевна	8	f	235
236	Поликарпов Никита Николаевич	8	f	236
237	Попрядухин Дмитрий Алексеевич	8	f	237
238	Савинкин Илья Дмитриевич	8	f	238
239	Чернушкин Георгий Александрович	8	f	239
240	Алимова Анна Александровна	9	f	240
241	Асанов Тимур Денисович	9	f	241
242	Бомуротов Шерхон Шодимурот угли	9	f	242
243	Буравцов Георгий Сергеевич	9	f	243
244	Бырда Мария Артуровна	9	f	244
245	Волков Кирилл Александрович	9	f	245
246	Вострецова Елизавета Евгеньевна	9	f	246
247	Гайбуллаева Гульшода Сохиб кизи	9	f	247
248	Грегориу Виейра Да Силва Ромуалду	9	f	248
249	Долгова Екатерина	9	f	249
250	Казангапова Карина Бауржановна	9	f	250
251	Магомедов Ислам Русланович	9	f	251
252	Мурадова Адиба Абдувалиевна	9	f	252
253	Норкулов Асадбек Норкул угли	9	f	253
254	Нурман кызы Мээрим	9	f	254
255	Отгонцэцэг Сайханцэцэг	9	f	255
256	Пичугин Дмитрий Евгеньевич	9	f	256
257	Ситникова Камилла Витальевна	9	f	257
258	Соколов Иван Евгеньевич	9	f	258
259	Сотиволдиев Абдурахим Равшанжон угли	9	f	259
260	Федотова Анна Вадимовна	9	f	260
261	Черникова Арина Витальевна	9	f	261
262	Анищенко Валерия Максимовна	10	f	262
263	Антонова Елена Дмитриевна	10	f	263
264	Афанасьева Дарья Владимировна	10	f	264
265	Афанасьева Ирина Евгеньевна	10	f	265
266	Беспалова Марина Владимировна	10	f	266
267	Бобков Игорь Михайлович	10	f	267
268	Болотникова Екатерина Андреевна	10	f	268
269	Буреева Виктория Александровна	10	f	269
270	Воронина София Дмитриевна	10	f	270
271	Галиханов Руслан Вазирович	10	f	271
272	Голубев Илья Михайлович	10	f	272
273	Гребенюк Даниил Дмитриевич	10	f	273
274	Гурикова Юлия Сергеевна	10	f	274
275	Ерома Игорь Владимирович	10	f	275
276	Живлюк Василиса Юрьевна	10	f	276
277	Иванова Полина Сергеевна	10	f	277
278	Игамбердиева Субхидамхон Мукимжановна	10	f	278
279	Какасьева Елизавета Александровна	10	f	279
280	Карышев Степан Николаевич	10	f	280
281	Когут Елена Александровна	10	f	281
282	Королевский Артём Павлович	10	f	282
283	Косарева Таисия Константиновна	10	f	283
284	Краснощекова Ирина Сергеевна	10	f	284
285	Лацис Маргарита Михайловна	10	f	285
286	Лебедева Арина Юрьевна	10	f	286
287	Манжосова Анна Андреевна	10	f	287
288	Мичко Сергей Николаевич	10	f	288
289	Москалев Илья Сергеевич	10	f	289
290	Муржак Михаил Андреевич	10	f	290
291	Мустафоев Мухсин Идибоевич	10	f	291
292	Набиев Максим Абдулович	10	f	292
293	Путинцева Валерия Сергеевна	10	f	293
294	Пыльнев Андрей Ильич	10	f	294
295	Сапунова Василиса Викторовна	10	f	295
296	Соболева Анастасия Романовна	10	f	296
297	Старухин Антон Павлович	10	f	297
298	Ториков Ярослав Денисович	10	f	298
299	Федотова Елена Васильевна	10	f	299
300	Хемракулыев Азиз	10	f	300
301	Хомишин Павел Геннадьевич	10	f	301
302	Ахмед Мохамед Мохамуд	11	f	302
303	Ахмедова Фатима Кудратовна	11	f	303
304	Бацина Дарья Александровна	11	f	304
305	Вакулюк Ульяна Артуровна	11	f	305
306	Володина Виктория Алексеевна	11	f	306
307	Гончарова Майя Евгеньевна	11	f	307
308	Дунаевская Кристина Михайловна	11	f	308
309	Кравчук Данила Игоревич	11	f	309
310	Кудряшов Иван Юрьевич	11	f	310
311	Мирошкина Дарья Евгеньевна	11	f	311
312	Морозова Варвара Григорьевна	11	f	312
313	Нечипорук Алексей Леонидович	11	f	313
314	Нижник Виолетта Сергеевна	11	f	314
315	Павленко Софья Станиславовна	11	f	315
316	Пермин Дмитрий Вячеславович	11	f	316
317	Петраков Андрей Евгеньевич	11	f	317
318	Петрова Алиса Вадимовна	11	f	318
319	Половников Иван Сергеевич	11	f	319
320	Рочева Виктория Витальевна	11	f	320
321	Сычева Маргарита Владимировна	11	f	321
322	Сычева Татьяна Александровна	11	f	322
323	Темчишена Ксения Константиновна	11	f	323
324	Чернышева Алиса Владимировна	11	f	324
325	Юнусова Маргарита Михайловна	11	f	325
326	Юхно Ксения Владимировна	11	f	326
327	Алёшин Александр Денисович	12	f	327
328	Аляутдинова Рената Рашидовна	12	f	328
329	Антуфьев Семён Александрович	12	f	329
330	Артюхин Константин Юрьевич	12	f	330
331	Баулин Макар Александрович	12	f	331
332	Витоженц Василиса Александровна	12	f	332
333	Вовчок Михаил Геннадьевич	12	f	333
334	Гаращук Анастасия Евгеньевна	12	f	334
335	Горюнов Кирилл Олегович	12	f	335
336	Гранкина Ева Марковна	12	f	336
337	Зайцева Софья Игоревна	12	f	337
338	Золотов Сергей Анатольевич	12	f	338
339	Иванов Евгений Кириллович	12	f	339
340	Исьянова Сабина Динаровна	12	f	340
341	Капустина Ангелина Евгеньевна	12	f	341
342	Ковалева Анна Дмитриевна	12	f	342
343	Кононова Юлия Игоревна	12	f	343
344	Кособоков Илья Александрович	12	f	344
345	Крылов Никита Максимович	12	f	345
346	Кудрявцев Владислав Александрович	12	f	346
347	Курепин Владислав Дмитриевич	12	f	347
348	Несудимов Кирилл Александрович	12	f	348
349	Салимбаева Мария	12	f	349
350	Азизова Нигорахон Азиз кизи	13	f	350
351	Алижонова Нозима Акмалжон кизи	13	f	351
352	Ализаде Фаган Шахин оглы	13	f	352
353	Буриев Абдулфайз Холмумин угли	13	f	353
354	Гадаев Хасан Дилшод угли	13	f	354
355	Гасанбекова Яна Сейдуллаевна	13	f	355
356	Голованов Дамир Артемович	13	f	356
357	Каландаров Хусан Азамат угли	13	f	357
358	Камилов Равшан Икрам угли	13	f	358
359	Кирьякова Наталия Александровна	13	f	359
360	Конякина Юлия Сергеевна	13	f	360
361	Куракин Руслан Вячеславович	13	f	361
362	Миронова Екатерина Антоновна	13	f	362
363	Муродов Шохжахон Хайрулло угли	13	f	363
364	Нурматов Уралбек Нарзуллаевич	13	f	364
365	Омонов Отамурод Отабек угли	13	f	365
366	Отахонов Диёрбек Уктам угли	13	f	366
367	Погорелова Алина Вячеславовна	13	f	367
368	Ражапбаев Сухроббек Музаффар угли	13	f	368
369	Ражапбаева Лобар Кахрамон кизи	13	f	369
370	Самохвалова Серафима Сергеевна	13	f	370
371	Синицын Никита Анатольевич	13	f	371
372	Султанов Канатбек Икрамович	13	f	372
373	Тошболтаев Низомиддин Келдиёр угли	13	f	373
374	Туланов Абдубанно Азамжон угли	13	f	374
375	Турдалиев Улугбек Умиджон угли	13	f	375
376	Турдиалиев Васлиддин Зойиржон угли	13	f	376
377	Турсунбоев Шохрух Рустамбой угли	13	f	377
378	Тусметов Бехруз Шухратович	13	f	378
379	Хакимбаев Мирали Закирович	13	f	379
380	Азаренкова Екатерина Сергеевна	14	f	380
381	Аминбаев Аброзхон Одилбек угли	14	f	381
382	Кочетыгов Илья Николаевич	14	f	382
383	Лошкарёва Эльвира Рустемовна	14	f	383
384	Машраббоев Комилжон Акмалжон угли	14	f	384
385	Пардаев Рустам Зафар угли	14	f	385
386	Свитайло Евгения Михайловна	14	f	386
387	Турдиев Бекзод Саттор угли	14	f	387
388	Хавка Святослав Николаевич	14	f	388
389	Шичкин Кирилл Владимирович	14	f	389
390	Боева Ксения Денисовна	15	f	390
391	Бурьянова Наталия Павловна	15	f	391
392	Джунусбаева Бегимай Аскарбековна	15	f	392
393	Исламов Радмил Маратович	15	f	393
394	Киселева Алина Александровна	15	f	394
395	Кравченко Дарья Александровна	15	f	395
396	Ли Юйтун	15	f	396
397	Линь Чжихэн	15	f	397
398	Санчы Долгар Болатовна	15	f	398
399	Собакина Таисья Дмитриевна	15	f	399
400	Фармонов Илхомжон Шариф угли	15	f	400
401	Якубов Исломджон Исроилович	15	f	401
402	Яценко Богдан Алексеевич	15	f	402
403	Арбузова Анна Андреевна	16	f	403
404	Афанасьева Дарья Владимировна	16	f	404
405	Балабанников Степан Владимирович	16	f	405
406	Васин Андрей Алексеевич	16	f	406
407	Гирина Елизавета Антоновна	16	f	407
408	Горох Алина Алексеевна	16	f	408
409	Жосан Никита Алексеевич	16	f	409
410	Жулина Александра Олеговна	16	f	410
411	Захаров Максим Валерьевич	16	f	411
412	Исроилов Хусейнбой Гуфронович	16	f	412
413	Кафаров Абдул-Хамид Хашим	16	f	413
414	Колесникова Мария Сергеевна	16	f	414
415	Мкртчян Армен Каренович	16	f	415
416	Петращук Егор Владимирович	16	f	416
417	Полупанова Арина Юрьевна	16	f	417
418	Просов Максим Игоревич	16	f	418
419	Редникова Варвара Ивановна	16	f	419
420	Руденко Анастасия Сергеевна	16	f	420
421	Сандуляк Татьяна Дмитриевна	16	f	421
422	Талызин Егор Сергеевич	16	f	422
423	Тетеркин Данила Сергеевич	16	f	423
424	Толубаев Антон Александрович	16	f	424
\.


--
-- Data for Name: student_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_group (id, name, department_id) FROM stdin;
1	221-362	1
2	231-362	1
3	221-365	2
4	231-365	2
5	211-327	3
6	221-327	3
7	211-352	4
8	221-352	4
9	211-611	5
10	221-611	5
11	221-631	6
12	211-631	6
13	222-641	7
14	228-641	7
15	201-621	8
16	221-621	8
\.


--
-- Data for Name: worker; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.worker (id, full_name, email, password) FROM stdin;
1	Демидов Дмитрий Григорьевич	fit-dean@mospolytech.ru	change_me
2	Назаренко Антон Владимирович	ad-dean@mospolytech.ru	change_me
3	Евгения Будылина	infokognetiv@mospolytech.ru	change_me
4	Алексей Осипов	priklad-it@mospolytech.ru	change_me
5	Алексей Золотарёв	smart@mospolytech.ru	change_me
6	Александр Красников	info-bez@mospolytech.ru	change_me
7	Елена Эдуардовна Аленина	managment@mospolytech.ru	change_me
8	Юлия Олеговна Алтунина	market@mospolytech.ru	change_me
9	Марина Михайловна Крекова	personal@mospolytech.ru	change_me
10	Александр Владимирович Тенищев 	econom@mospolytech.ru	change_me
\.


--
-- Name: department_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.department_id_seq', 8, true);


--
-- Name: document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.document_id_seq', 424, true);


--
-- Name: faculty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.faculty_id_seq', 2, true);


--
-- Name: student_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_group_id_seq', 16, true);


--
-- Name: student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_id_seq', 424, true);


--
-- Name: worker_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.worker_id_seq', 10, true);


--
-- Name: department department_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_name_key UNIQUE (name);


--
-- Name: department department_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (id);


--
-- Name: document document_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.document
    ADD CONSTRAINT document_pkey PRIMARY KEY (id);


--
-- Name: faculty faculty_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_name_key UNIQUE (name);


--
-- Name: faculty faculty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (id);


--
-- Name: student_group student_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group
    ADD CONSTRAINT student_group_name_key UNIQUE (name);


--
-- Name: student_group student_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group
    ADD CONSTRAINT student_group_pkey PRIMARY KEY (id);


--
-- Name: student student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (id);


--
-- Name: worker worker_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker
    ADD CONSTRAINT worker_email_key UNIQUE (email);


--
-- Name: worker worker_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker
    ADD CONSTRAINT worker_pkey PRIMARY KEY (id);


--
-- Name: department department_faculy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_faculy_id_fkey FOREIGN KEY (faculy_id) REFERENCES public.faculty(id);


--
-- Name: department department_head_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_head_id_fkey FOREIGN KEY (head_id) REFERENCES public.worker(id);


--
-- Name: faculty faculty_dean_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_dean_id_fkey FOREIGN KEY (dean_id) REFERENCES public.worker(id);


--
-- Name: student student_document_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_document_id_fkey FOREIGN KEY (document_id) REFERENCES public.document(id);


--
-- Name: student_group student_group_department_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_group
    ADD CONSTRAINT student_group_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.department(id);


--
-- Name: student student_student_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_student_group_id_fkey FOREIGN KEY (student_group_id) REFERENCES public.student_group(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


--
-- PostgreSQL database dump complete
--

