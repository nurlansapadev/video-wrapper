# Стиль «Рашоян-Honest Lies» (rashoyan-honest-lies)

> Переносимый файл стиля обложки: копируется в `channels/<канал>/styles/` любого канала без правок. Внутри — только оформление, без привязки к эпизодам.
> Как подключить: добавить строку в реестр стилей `branding.md` канала. Сборка слоями — `core/thumbnails.md`.

## Происхождение
- **Производный от** «Рашоян стиль» (`styles/rashoyan-style.md`). Всё, что не указано ниже как отличие, — **как в родителе** (человек по пояс с эмоцией, ≤ 3 элементов, безопасная зона, красная «таблетка» на ключевом слове).
- Создан по решению Nurlan 16.10.2026 на EP-07: почти чёрный фон родителя заменён на холодный синий, чтобы тёплый цветной герой выделялся сильнее.
- **Эталон композиции (Nurlan, 16.10.2026):** EP-07 p2 — `production/honest-lies/ep-7/07_thumbnail/thumb-rashoyan-honest-lies-p2.jpg` (Кэмпер + гравюра Ганди, `HE SAVED HIM?`). Так компоновать сразу — сетка и промпт одним заходом ниже.

## Отличия от родителя
| Что | Родитель «Рашоян стиль» | Этот стиль |
|---|---|---|
| **Фон** | почти чёрный графит, тёплый ореол за головой | **бледно-синий туман** на тёмно-синем (решение Nurlan 16.10.2026; заменил «космическую пыль») |
| **Текст** | одна плоская строка сверху во всю ширину | **объёмные буквы** (экструзия, градиент, сильная тень); если голова героя занимает верх — блок из 2 строк в свободном верхнем углу |

## Суть
Человек крупно с читаемой эмоцией в холодном синем тумане + короткий объёмный удар. Тепло героя против холода фона.
**Сильнее всего:** истории с человеком в центре — его решение, двойная игра, разоблачение; где эмоция лица и есть крючок.

## Фон — бледно-синий туман
- База — тёмно-синий `#0E1A2E`–`#16263F`, к краям темнее (виньетка).
- Мягкий клубящийся туман, бледно-синий / сталь-синий `#2A3F5F`–`#476287`, низкий контраст; самый светлый туман — за героем, отделяет его по яркости.
- Допустима лёгкая мелкая пыль в тумане (как на эталоне), без звёзд-бликов.
- Без планет, галактик, световых лучей, сцены, предметов.
- Зона текста — ровнее и темнее; нижние 30% и правый нижний угол — тёмные, пустые.
- Второстепенный объект может растворяться в тумане снизу (эталон: гравюра Ганди).

## Объект
Как в родителе: человек по пояс / по грудь, лицо 40–50% высоты, читаемая эмоция, только по реальному фото. Цвет кожи естественный, **насыщенность чуть приглушена**, тонкий холодный контровой свет от тумана по волосам и плечам. Сторона — любая (эталон: герой слева, второстепенный справа).

## Текст
- Белый с лёгким градиентом `#FFFFFF` → `#D9DEE6` книзу, тонкий блик по верхней кромке, экструзия 6–8 px тёмно-синяя `#0B1628` вниз-вправо, сильная мягкая тень. Ключевое слово — на глянцевой красной «таблетке» `#E3141B` с тёмно-красной толщиной `#8E0B10`.
- Шрифт: широкий геометрический гротеск Black, заглавные (тип Montserrat Black). Не узкий. Заглавные ~11–13% высоты — крупно (на эталоне увеличили: в 120 px читается заметно лучше).
- Позиция: по сетке-эталону — блок из 2 строк справа от головы героя, выровнен влево по x ≈ 36%, над второстепенным объектом. Никогда не нижние 30% и не правый нижний угол.
- Текст проходит «Тест 0,5 с» (`core/titles.md`) — понятен без названия.

## Сетка-эталон (замер EP-07 p2, доли кадра 16:9; ±3%)
| Элемент | Где | Размер / детали |
|---|---|---|
| **Герой** (цвет) | слева: x 0–50%, от верхнего края до низа | голова у верхнего края (макушка y ≈ 5%), лицо ≈ 40% высоты, глаза y ≈ 33%; поясной план, руки скрещены, корпус слегка к центру, взгляд в камеру, эмоция |
| **Текст** | справа от головы героя, сверху: блок **выровнен влево по x ≈ 36%**, до x ≈ 95% | 2 строки: строка 1 y 10–25%, строка 2 y 30–45%; заглавные ≈ 15% высоты; «таблетка» — на ключевом слове строки 1 |
| **Второстепенный** (гравюра) | справа под текстом: x 60–90%, y 35–75% | по плечи, лицо ≈ 22%; смотрит в сторону героя; низ растворяется в тумане; не перекрыт текстом |
| **Фон** | весь кадр | тёмно-синий туман, светлее за героем и в центре; виньетка |
| **Пусто** | правый нижний угол x 82–100%, y 80–100% | тёмный туман |

Иерархия на 120 px: лицо героя → текст → второстепенный. Элементов — три.

## Как генерировать одним заходом — инструкция упаковщику (решение Nurlan, 16.10.2026)

> **В этом стиле обложка делается одним промптом**, а не слоями 1–3 (`core/workflow.md`, 4.3–4.5 заменяются этим разделом). Слои — только запасной путь, если одним заходом не вышло после 2–3 точечных правок.

### Вход (до промпта)
1. **Текст пары утверждён** (шаг 3) и прошёл «Тест 0,5 с» — без названия, вместе с лицом, понятен и рождает вопрос.
2. **Объекты утверждены** (4.1): **герой** — человек, чья эмоция и есть крючок (в цвете, слева); **второстепенный** — цель / жертва / символ (гравюра или фото, справа под текстом).
3. **Рефы — точечным вопросом**, по одному: «Есть фото <кто>? Нужно для <герой / второстепенный>» → `07_thumbnail/work/` (сначала — `02_characters/`, `face_policy` в `cast.json`). Реальные люди — только с фото (своё фото Nurlan, в т. ч. другое, с эмоцией, — допустимо). По описанию лицо не генерировать.

### Подготовка (сам, до выдачи)
4. **Посмотреть фото героя:** что убрать (оружие, других людей, фон), какая одежда нужна по сюжету, какая эмоция уже есть — промпт её **усиливает**, а не создаёт с нуля.
5. **Посмотреть второстепенного:** куда смотрит. Зеркалить **не по умолчанию** — только если смотрит из кадра наружу и Nurlan хочет связь взглядом («глаза в глаза» не обязательно, Nurlan 16.10.2026).
6. **Разбить текст на 2 строки:** строка 1 — 1–2 слова + **ключевое слово на красной таблетке** (ирония, цифра, вердикт); строка 2 — короткое слово / вопрос. Длинная строка — первая (под неё — ширина до x 95%).
7. **Буквы:** только латиница; «$» — только в цифре. После p1 с «$» в p2 генератор оставляет хвост на «S» (урок EP-07: «Ş») — в промпте всегда строка «Every letter is a plain Latin capital — no accents, no cedillas, no stray strokes».

### Выдача Nurlan
8. Заполнить шаблон ниже: `{изменения героя}`, `{эмоция}`, `{mirrored / not mirrored}`, слова строк. **Цифры сетки не менять** — они замер эталона.
9. Сказать: **ChatGPT**, вложения строго по порядку — **image 1 = герой, image 2 = второстепенный**. Один промпт, без вариантов.

### Оценка результата (каждый раз, таблицей)
10. Сохранить → `07_thumbnail/work/gen-oneshot-pN.webp`; замер `tools/thumb_metrics.py` + превью 120 px (рядом с эталоном).
11. Проверить по пунктам:
| Пункт | Норма |
|---|---|
| Герой | слева x 0–50%, лицо ≈ 40%, глаза y ≈ 33%, эмоция читается в 120 px, лицо = фото |
| Второстепенный | x 60–90%, y 35–75%, лицо ≈ 22%, не перекрыт текстом, лицо = приложенный реф (не похож — **спросить, какое фото дал**, а не обвинять генератор: EP-07, Nurlan дал другое фото) |
| Текст | блок от x ≈ 36%, 2 строки, заглавные ≈ 15%, объём, таблетка на ключевом, **каждая буква чистая** |
| Пусто | правый нижний угол тёмный (замер ≤ 30) |
| Элементов | ровно три, ничего лишнего |
| Тест 0,5 с | без названия — вопрос рождается |

### Правки — по одному пункту
12. Формула: `Edit the attached image: change ONLY <что>. Do not change anything else — same size, no crop, no zoom, no re-render; everything else stays pixel-identical.` + конкретика (%, координаты, «Spell exactly»).
13. Типовые: уменьшить/сдвинуть второстепенного на N% · исправить букву · вернуть лицо с рефа (приложить реф как image 2) · текст крупнее · убрать лишний объект. Nurlan может сам масштабировать/зеркалить — это решение, не ошибка.

### Вторая пара (A/B)
14. **Не новым заходом**, а правкой утверждённой p1: «replace ONLY the words of the text», тот же стиль, высота, выравнивание. Тогда A/B сравнивает только текст. (Если Nurlan сознательно делает p2 отдельным заходом — сравнивается вся обложка, записать это в `status.md`.)

### Финал
15. «Утверждаю» → экспорт сам: 1280×720 JPG, quality 92 → `07_thumbnail/thumb-rashoyan-honest-lies-pN.jpg`; блок версии в `status.md` (рефы, промпт, правки, файл). Удачное отличие от эталона — в «Опыт».

## Промпт одним заходом (герой + второстепенный + текст) — шаблон
Прикладываются: **image 1** — фото героя, **image 2** — гравюра второстепенного. Генератор — ChatGPT (держит лицо и раскладку). Если что-то съехало — точечная правка одним пунктом, не перегенерация.
```
Create a YouTube thumbnail, 16:9, 1280x720, using two attached images: image 1 = the main man (photo), image 2 = an engraved portrait (secondary person).

BACKGROUND: a dark navy base (#0E1A2E to #16263F) with soft drifting pale steel-blue fog (#2A3F5F to #476287), a few fine faint dust specks, low contrast, darker toward all edges (vignette). Lightest fog behind the main man and in the center. No scenery, no objects, no light beams.

MAIN MAN (image 1) — LEFT side, the hero, in color:
- Keep his face and identity exactly as in image 1 — same features, hair, skin. Do not make him look like someone else.
- {изменения: одежда / убрать оружие и людей}
- Waist-up, arms crossed on his chest, body turned slightly toward the center, looking straight into the camera.
- Expression: {эмоция, читаемая, без гримасы}.
- He fills x 0–50% of the frame; top of his head near the top edge (about y 5%); his face (forehead to chin) about 40% of the frame height; eyes at about y 33%; his body continues to the bottom edge.
- Slightly muted natural colors, warm skin; soft key light from the front-right; thin cool blue rim light from the fog on his hair and shoulders.

SECONDARY (image 2) — RIGHT side, smaller, below the text:
- Keep the engraving exactly as it is — same face, identity, line-engraving style and blue-white tones. Do not redraw, do not add color.
- Remove its flat background; head and shoulders only; the lower edge dissolves softly into the fog (no hard cut, no frame).
- Place it at x 60–90%, y 35–75%; face about 22% of the frame height. Not mirrored{или: mirrored} — he looks toward the main man.

TEXT — upper right, a two-line block LEFT-aligned at x 36% of the width, extending to about x 95%:
- Line 1 (y 10–25%): "{СЛОВО}" in white 3D letters, then "{КЛЮЧЕВОЕ}" in white letters on a glossy rounded red pill.
- Line 2 (y 30–45%): "{СЛОВО}" in white 3D letters.
- Capitals about 15% of the frame height. Font: wide geometric sans-serif, Black weight, ALL CAPS (like Montserrat Black). NOT condensed, NOT Anton, NOT Impact.
- 3D letters: white face with a subtle vertical gradient #FFFFFF to #D9DEE6, thin bright highlight along the top edge, solid dark navy #0B1628 extrusion 6–8 px toward the bottom-right, strong soft drop shadow (offset ~8 px down, blur ~18 px, black 70%).
- Red pill #E3141B, corner radius ~25% of its height, darker red #8E0B10 extrusion at the bottom edge, soft highlight on its top half.
- The text does not touch the main man's head and does not cover the secondary person's face. No outline, no glow, no other boxes.
- Spell exactly: "{СТРОКА 1}" / "{СТРОКА 2}". Every letter is a plain Latin capital — no accents, no cedillas, no stray strokes.

Keep the bottom-right corner (x 82–100%, y 80–100%) dark and empty. Exactly three elements: the main man, the secondary portrait, the text. No other text, logos or objects.
```

## Константы для промпта слоя 1 (обязательны, остальное — под сценарий)
```
Background only. No people, no text, no objects.
Pale-blue fog: a dark navy base (#0E1A2E to #16263F) with soft, slow drifting pale steel-blue mist (#2A3F5F to #476287), low contrast; darker toward all edges (vignette). A few fine faint dust specks in the mist are OK; no sharp stars, no lens flares.
The lightest mist is where the main person will be, so he separates from the background by brightness.
No planets, no galaxies, no light beams, no scenery.
Text area: darker and calmer, even tone.
Bottom 30%: plain dark navy; bottom-right corner plain, dark and empty.
16:9, 1280x720.
```

## Константы для промпта слоя 2
- Человек: как в родителе (`styles/rashoyan-style.md`) + `Slightly muted natural colors, warm skin; thin cool blue rim light from the fog on his hair and shoulders, so he sits naturally in the blue scene.`
- Всегда: `No more than three elements. Keep the text area and the bottom-right corner empty. Do not change the background, do not add text.`

## Константы для промпта слоя 3
```
Font: wide geometric sans-serif, Black weight, ALL CAPS (like Montserrat Black). NOT condensed, NOT Anton, NOT Impact. Capitals about 12% of the frame height.
3D letters: white face with a subtle vertical gradient #FFFFFF to #D9DEE6, thin bright highlight along the top edge, solid dark navy #0B1628 extrusion 6–8 px toward the bottom-right, strong soft drop shadow (offset ~8 px down, blur ~18 px, black 70%).
Key word on a glossy rounded red pill #E3141B (corner radius ~25% of its height) with a darker red #8E0B10 extrusion at the bottom edge and a soft highlight on its top half.
No outline, no glow, no other boxes. Spell exactly: ... No other text anywhere. Nothing in the bottom 30% or the bottom-right corner.
```

## Опыт
- 16.10.2026 — стиль создан на EP-07 (Кэмпер + Ганди). Второстепенный объект — портрет-гравюра (сине-белая), герой — в цвете; проверяется, станет ли это константой стиля.
- 16.10.2026 — EP-07, тест фона: «космическая пыль» vs «синий туман» — Nurlan выбрал туман; константа фона заменена на бледно-синий туман.
- 16.10.2026 — EP-07, слой 3: плоский текст («наклейка») → объём (экструзия + градиент + тень) → увеличен. Утверждено как константа текста.
- 16.10.2026 — EP-07: голова героя у верхнего края → текст блоком из 2 строк справа-сверху над второстепенным объектом.
- 16.10.2026 — Nurlan: эталон композиции — EP-07 p2 (герой слева, текст-блок справа сверху, гравюра под текстом). Записаны сетка-эталон и «промпт одним заходом»; на EP-07 собиралось 4 слоями + ручное зеркало Nurlan. Проверить одним заходом на следующем эпизоде.
- 16.10.2026 — EP-07, первый тест «одним заходом» (ChatGPT, `ep-7/07_thumbnail/work/gen-oneshot-p2.webp`): сетка, герой, текст, буквы — ✅ с первого раза (Nurlan: «отличный результат»). Второстепенный — другое фото Ганди (улыбка, шапка), приложенное Nurlan, — по референсу, ✅. Сетка-эталон + промпт одним заходом работают.
