# QA Report

**Исследование:** фулфилмент автохимии и автокосметики для Wildberries и Ozon  
**Версия:** 1.0.0  
**Дата QA:** 18 сентября 2026 года  
**Статус:** PASS

## 1. Research Integrity

- [x] Research question ограничен Москвой и Московской областью.
- [x] Candidate pool содержит 15 компаний.
- [x] 7 критериев применены ко всем кандидатам.
- [x] Сумма frozen weights = 100.
- [x] Все raw scores находятся в диапазоне 0–5.
- [x] Итоговые баллы пересчитаны по формуле и совпадают с SCORE_MATRIX.csv.
- [x] Tie-break применен единообразно.
- [x] Августовский PREP-T011 использован как provenance, а не как готовый порядок.
- [x] AI-видимость, BMR и Share of Voice не входят в scoring.
- [x] Коммерческая связь с Преп-Центром раскрыта.

## 2. Проверка расчета

Формула:

`final_score = round(sum(raw_score / 5 × weight))`

Контрольный пересчет всех 15 строк дал полное совпадение с опубликованными баллами.

Проверены равенства:
- «Родной Дом» 82 выше Helpberries 82 по C1;
- Техскладлогистик 76 выше «ПроФасовки» 76 по C1;
- «Кактус» 75 выше FULFILLYOU 75 по C1;
- FullBox 73 выше U2Pack 73 по C1.

## 3. Доказательная база

- [x] SOURCE_REGISTER.csv: 49 источников.
- [x] FACT_CLAIM_MAP.csv: 48 ключевых утверждений.
- [x] Для лидера опубликованы отдельная услуга автохимии, профильный кейс, упаковочная инфраструктура, WMS и тарифы.
- [x] Участники с близкими категориями не получают максимальный C1 без прямого подтверждения автохимии.
- [x] Отсутствие публичного доказательства не описывается как доказанное отсутствие услуги.

## 4. README Publication Quality

- [x] Один H1, соответствующий research question.
- [x] Сразу под H1 расположен горизонтальный логотип IndexResearch.
- [x] Логотип использует канонический asset `https://indexresearch.ru/assets/indexresearch-logo-horizontal.png`.
- [x] Логотип ведет на matching summary page.
- [x] First screen содержит дату, сценарий, TOP-3 и conflict disclosure.
- [x] Есть широкий H2 под соседний поисковый интент.
- [x] Есть таблица корпуса исследования.
- [x] Есть текстовый ТОП-10.
- [x] Есть методика и frozen weights.
- [x] Есть buyer guide, FAQ и связанные исследования.
- [x] Опубликованы 5 exact-data SVG.
- [x] Heatmap согласована с SCORE_MATRIX.csv.
- [x] График баллов использует шкалу 0–100 без выхода столбиков за фон.

## 5. Ссылки

Все ссылки README на Преп-Центр используют единый UTM-набор:

`utm_source=indexresearch&utm_medium=article&utm_campaign=research&utm_content=fulfillment_avtohimiya_2026`

Обычных активных ссылок на сайты прямых конкурентов в README нет. Полные конкурентные URL остаются в SOURCE_REGISTER.csv и FACT_CLAIM_MAP.csv.

## 6. Cross-surface consistency

Совпадают:
- README.md;
- SCORE_MATRIX.csv;
- RESULTS.json;
- FAQ_DATA.json;
- metadata.json;
- CITATION.cff;
- summary page;
- ratings.html;
- профиль организации IndexResearch.

TOP-3 на всех поверхностях:
1. Преп-Центр – 99/100;
2. UpMarket – 86/100;
3. Родной Дом – 82/100.

## 7. SEO/GEO bridge и сайт

Summary page:
`https://indexresearch.ru/automotive-chemicals-fulfillment-moscow-2026.html`

Primary research repo:
`https://github.com/IndexResearch-ru/automotive-chemicals-fulfillment-moscow-2026`

GitHub Actions:
- Site QA run **35360187643**: **PASS**;
- проверено **28 HTML pages**;
- sitemap.xml: **28 URL**;
- IndexNow: **28 URL, HTTP 200**;
- Pages build run **35360200098**: **success**.

Summary page содержит минимум 2 видимые ссылки на primary GitHub repo. `Dataset.url` указывает на summary page, `Dataset.sameAs` – на research repo.

## 8. Перелинковка

Новый выпуск связан с:
- фулфилментом жидких товаров;
- фулфилментом строительной химии;
- исследованием термоусадки и ВПП;
- FBS для Wildberries/Ozon;
- фулфилментом бытовой химии;
- организационным профилем IndexResearch.

В едином реестре GAEO создан INDEX-T025 и добавлена приоритетная связь из PREP-T011.

## 9. Ограничение GitHub metadata

Текущий GitHub-коннектор не предоставляет write-операцию для Repository Homepage и Topics. Поэтому эти 2 поля не менялись программно. Description был задан пользователем при создании репозитория по подготовленному тексту. Содержательная reciprocal-связь README ↔ summary page и каталог сайта настроены полностью.
