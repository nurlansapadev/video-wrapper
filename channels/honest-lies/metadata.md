# metadata.md — Метаданные: Honest Lies

> Дополняет `core/metadata.md`.

## Базовые теги (на каждое видео)
```
espionage history, intelligence history, declassified files, covert operations,
deception history, propaganda history, industrial espionage, information warfare,
disinformation, psychological warfare, dark history, spy documentary,
espionage, declassified, intelligence, spy history, true spy story,
secret history, espionage documentary, covert operations history
```
Плюс пак по шаблону эпизода и 8–12 точечных тегов (имена, место, явление). **Точечные — короткие, 2–3 слова** (EP-06, EP-07: длинные «имя + событие + год» удаляются — «reagan rajiv gandhi 1985», «thomas norris medal of honor»; остаются «mercenary school», «air india 182»). Полные паки — репо honest-lies, `channel/keywords.md`.

| Шаблон | Пак |
|---|---|
| Кража / технологии | industrial espionage, corporate espionage, stolen technology, economic espionage, trade secrets, technology theft |
| Ложь / пропаганда | propaganda, disinformation, active measures, influence operation, media manipulation, psyop |
| Операция | covert operation, secret operation, CIA operation, intelligence operation, tradecraft |
| Мелкая сошка | ordinary people history, butterfly effect history, small player big impact, forgotten history |

## Хэштеги (решение Nurlan, 07.10.2026)
**Используем** — **последней строкой описания**, после `video_credits_text.txt`. YouTube показывает первые три над названием.
**Состав — география эпизода + `#HonestLies` (Nurlan, 16.10.2026; заменяет «2 по теме + канальный»):**
- перечислить **страны** эпизода и его **основной город**;
- по США — **город и/или штат**, без `#USA` (США и так понятно);
- последним — `#HonestLies`.
- Пример EP-07: `#India #Alabama #Vietnam #HonestLies`.
Переопределяет `core/metadata.md` («до 3 штук»): география может дать 4–6 тегов; лимит YouTube — 15. Порядок — по весу в сюжете: первые три видны над названием.

## Публикация
- Дату и время решает Nurlan — упаковщик не предлагает
- Аудитория: **не для детей**
- Категория: **Education** (Nurlan, 07.10.2026)
- Плейлист: пока не используем
- Язык: English
- Конечная заставка: следующий/прошлый эпизод + подписка — после финальной фразы и монтажной тишины, не поверх
- Карточка — на прошлый эпизод, если он упомянут
- **Субтитры (Video elements → Subtitles) — не добавляем** (Nurlan, 10.10.2026). Quiz — не используем
- **Закреплённый комментарий — обязателен** в каждом эпизоде (Nurlan, 07.10.2026): вопрос зрителю по теме, без ответа и без «подпишитесь». Финал — `output/pinned_comment.txt`.
- **Своё видео не смотреть** (Nurlan, 07.10.2026): чтобы не добавлять просмотры из Кыргызстана в географию аудитории. Комментарий — через **YouTube Studio → Content → видео → Comments**; закрепить — на странице видео / в приложении, сразу поставив плеер на паузу (не досматривать).
