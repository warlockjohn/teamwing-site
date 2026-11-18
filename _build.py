#!/usr/bin/env python3
# Сборка сайта TeamWing: python3 _build.py
# Тексты — в T ниже (ru / en / kk). Файлы с «_» в начале GitHub Pages не публикует.
import html
import os

EMAIL = 'teamwing.app@gmail.com'
BETA = ''  # публичная ссылка TestFlight; пока пусто — кнопка не показывается
UPDATED = {'ru': '18 ноября 2026', 'en': 'November 18, 2026', 'kk': '2026 жылғы 18 қараша'}
LANGS = ['ru', 'en', 'kk']
LANG_LABEL = {'ru': 'Рус', 'en': 'Eng', 'kk': 'Қаз'}
BASE = '/teamwing-site/'  # сайт живёт в подпапке warlockjohn.github.io/teamwing-site

ICONS = {
    'users': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6.5 6.5 0 0 1 3.5 6"/></svg>',
    'cal': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M8 14h2M14 14h2M8 17h2"/></svg>',
    'check': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="m8 12 3 3 5-6"/></svg>',
    'coin': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="7" rx="7" ry="3"/><path d="M5 7v5c0 1.7 3.1 3 7 3s7-1.3 7-3V7M5 12v5c0 1.7 3.1 3 7 3s7-1.3 7-3v-5"/></svg>',
    'trophy': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 4h8v5a4 4 0 0 1-8 0zM8 6H4.5a3 3 0 0 0 3.5 4M16 6h3.5a3 3 0 0 1-3.5 4M12 13v4M8 21h8M9 17h6v4H9z"/></svg>',
    'cloud': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 18a4.5 4.5 0 0 1-.5-9A6 6 0 0 1 18 8.5a4.5 4.5 0 0 1-.5 9.5z"/><path d="M12 11v5M9.5 13.5 12 11l2.5 2.5"/></svg>',
    'lock': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
}

T = {
    'ru': {
        'title': 'TeamWing — кабинет тренера любительской команды',
        'desc': 'Приложение для тренера любительской команды на iPhone: состав, расписание, посещаемость, оплаты и статистика матчей. Данные хранятся только на телефоне.',
        'h1': 'Вся команда — в одном телефоне',
        'lead': 'Состав, тренировки, посещаемость, взносы и статистика матчей. Без таблиц, тетрадок и пересчётов в чате.',
        'badge': 'Стать тестером',
        'badge_small': 'Бета в TestFlight · для iPhone',
        'soon': 'Бета в TestFlight — по приглашению',
        'note': 'Для iPhone. Интерфейс — на русском и английском.',
        'feat_h': 'Что умеет TeamWing',
        'feat': [
            ('users', 'Игроки и составы', 'Карточки игроков с номерами и позициями, звенья и варианты состава — перетаскиванием.'),
            ('cal', 'Расписание', 'Тренировки по дням недели, переносы и отмены отдельных занятий.'),
            ('check', 'Посещаемость', 'Отметки за пару касаний — видно, кто ходит, а кто пропускает.'),
            ('coin', 'Взносы и долги', 'Услуги и абонементы, начисления за месяц, полные и частичные оплаты, фонд и казначей.'),
            ('trophy', 'Матчи и статистика', 'Результаты товарищеских игр, голы, передачи, штрафы и вратари.'),
            ('cloud', 'Резервные копии', 'Вся команда в одном файле — сохраните в iCloud Drive и восстановите на другом телефоне.'),
        ],
        'priv_h': 'Данные команды — только у вас',
        'priv': 'Без регистрации, без наших серверов, без рекламы и аналитики. База хранится на телефоне тренера, а копии вы сохраняете сами — туда, куда решите.',
        'why_h': 'Почему TeamWing',
        'why': 'Приложение сделал в Алматы разработчик, который почти 20 лет занимается финансовыми системами, — для знакомой любительской команды. Задача простая: чтобы тренер не держал команду в голове и в пяти разных чатах.',
        'nav_privacy': 'Конфиденциальность',
        'nav_support': 'Поддержка',
        'nav_home': 'Главная',
        'made': 'Сделано в Алматы',
        'privacy_title': 'Политика конфиденциальности',
        'updated': 'Обновлено',
        'privacy': [
            ('', '<p class="hi"><b>Коротко:</b> TeamWing не собирает ваши данные. Нет регистрации, нет наших серверов, нет рекламы и аналитики. Всё, что вы вносите, хранится только на вашем устройстве.</p>'),
            ('Какие данные хранит приложение', '<p>Сведения, которые вводит тренер: название команды и логотип; имена игроков, номера, позиции, телефоны, даты рождения и вступления; расписание и посещаемость; результаты и статистика матчей; услуги, начисления, оплаты и долги; настройки команды. Необязательные поля заполняются по желанию.</p><p>Всё это хранится в файле внутри приложения на вашем iPhone. Разработчик не имеет к нему доступа.</p>'),
            ('Интернет и сторонние сервисы', '<p>Приложению не нужен интернет для работы. В нём нет собственного сервера, рекламы, систем аналитики и сторонних SDK, которые собирали бы данные. TeamWing не обрабатывает банковские платежи: учёт оплат — это записи, которые делает тренер.</p>'),
            ('Разрешения', '<ul><li><b>Фото</b> — только чтобы вы сами выбрали изображение для логотипа команды. Остальная фототека приложению не передаётся.</li><li><b>Файлы</b> — только тот файл резервной копии, который вы сами выбрали для восстановления.</li></ul><p>Камера, микрофон и геолокация не используются.</p>'),
            ('Резервные копии', '<p>Копия создаётся только по вашей команде и сохраняется туда, куда вы выберете в меню «Поделиться», — например, в iCloud Drive. Копия — это JSON-файл <b>без пароля и шифрования</b>, в нём есть телефоны, даты рождения и финансовая история команды. Храните его у себя и не передавайте посторонним. Если вы сохраните копию в iCloud Drive или другой сервис, она хранится по правилам этого сервиса.</p><p>Перед восстановлением из копии приложение автоматически сохраняет текущие данные на телефоне, чтобы их можно было вернуть.</p>'),
            ('Данные игроков', '<p>TeamWing — инструмент тренера. Внося сведения об игроках, тренер отвечает за то, чтобы участники знали, какие данные он ведёт, а для несовершеннолетних — их родители или законные представители. Если игрок хочет исправить или удалить свои данные, ему нужно обратиться к своему тренеру. TeamWing не создаёт публичных профилей и ничего не публикует.</p>'),
            ('Тестирование через TestFlight', '<p>Если вы тестируете бету, Apple может передавать разработчику отчёты о сбоях и ваши отзывы с той информацией, которую вы сами в них укажете. Подробнее — в <a href="https://www.apple.com/legal/privacy/data/en/test-flight/">правилах TestFlight</a>. Не прикладывайте к отзывам скриншоты с реальными данными игроков без необходимости.</p>'),
            ('Удаление данных', '<p>Удалите приложение — и все его данные будут удалены с телефона. Копии, которые вы сохранили сами, остаются там, куда вы их сохранили, — удалите их вручную.</p>'),
            ('Изменения', '<p>Если политика изменится — например, когда в приложении появятся аккаунты игроков и синхронизация, — новая версия появится на этой странице с новой датой, а сама функция будет описана до её включения.</p>'),
            ('Связь', f'<p>Владелец приложения: Yevgeniy Avdonin.<br>Вопросы о конфиденциальности: <a href="mailto:{EMAIL}">{EMAIL}</a></p>'),
        ],
        'support_title': 'Поддержка',
        'support_lead': 'Ответы на частые вопросы. Не нашли свой — напишите, ответим.',
        'faq': [
            ('Как установить бету?', '<ol><li>Установите приложение <b>TestFlight</b> из App Store.</li><li>Откройте на iPhone приглашение — письмо или ссылку — и нажмите «Принять», затем «Установить».</li><li>Обновления приходят через TestFlight.</li></ol>'),
            ('Где хранятся данные команды?', '<p>Только на вашем iPhone, внутри приложения. Регистрации и облака разработчика нет — поэтому регулярно делайте резервные копии.</p>'),
            ('Как сохранить копию в iCloud?', '<ol><li>«Настройки» → «Резервная копия и восстановление» → сохранить данные.</li><li>В меню выберите «Сохранить в Файлы» → iCloud Drive → папку (например, TeamWing) → «Сохранить».</li><li>Откройте «Файлы» и убедитесь, что копия появилась и загрузилась.</li></ol>'),
            ('Как перенести команду на другой телефон?', '<ol><li>На старом телефоне сохраните копию в iCloud Drive или отправьте файл себе.</li><li>На новом установите TeamWing, откройте «Настройки» → «Резервная копия и восстановление» → «Выбрать файл копии».</li><li>Проверьте содержимое копии и подтвердите замену.</li></ol>'),
            ('Я перешёл с Expo Go — где мои данные?', '<p>Версия из TestFlight — отдельное приложение, данные из Expo Go в неё сами не переносятся. Сохраните копию в Expo Go и восстановите её в TeamWing, как описано выше. Не удаляйте Expo Go, пока не убедитесь, что всё перенеслось.</p>'),
            ('Можно посмотреть приложение без своих данных?', '<p>Да: при первом запуске нажмите «Пройти обучение на примере» — приложение покажет вымышленную хоккейную команду с подсказками по шагам. Ваши данные не затрагиваются. Пройти обучение заново: «Настройки» → «Пройти обучение заново».</p>'),
            ('Могут ли игроки видеть свои данные?', '<p>Пока нет — сейчас это кабинет тренера. Приложение для игроков в планах.</p>'),
        ],
        'contact_h': 'Написать нам',
        'contact': f'Почта: <a href="mailto:{EMAIL}">{EMAIL}</a>. Если вы тестируете бету, можно отправить отзыв прямо из TestFlight — сделайте скриншот в приложении и нажмите «Поделиться бета-отзывом».',
    },
    'en': {
        'title': 'TeamWing — a coach’s app for amateur teams',
        'desc': 'An iPhone app for amateur team coaches: roster, schedule, attendance, payments and match stats. Your data stays on your phone.',
        'h1': 'Your whole team in one phone',
        'lead': 'Roster, practices, attendance, fees and match stats. No spreadsheets, notebooks or recounting in group chats.',
        'badge': 'Join the beta',
        'badge_small': 'TestFlight · for iPhone',
        'soon': 'TestFlight beta — by invitation',
        'note': 'For iPhone. The interface is in English and Russian.',
        'feat_h': 'What TeamWing does',
        'feat': [
            ('users', 'Players and lineups', 'Player cards with numbers and positions, lines and lineup variants — drag and drop.'),
            ('cal', 'Schedule', 'Weekly practices, with single sessions rescheduled or cancelled.'),
            ('check', 'Attendance', 'Mark it in a couple of taps and see who shows up and who skips.'),
            ('coin', 'Fees and debts', 'Services and memberships, monthly charges, full and partial payments, team fund and treasurer.'),
            ('trophy', 'Games and stats', 'Friendly game results, goals, assists, penalties and goalies.'),
            ('cloud', 'Backups', 'The whole team in one file — save it to iCloud Drive and restore on another phone.'),
        ],
        'priv_h': 'Team data stays with you',
        'priv': 'No sign-up, no servers of ours, no ads or analytics. The database lives on the coach’s phone, and you save backups yourself, wherever you choose.',
        'why_h': 'Why TeamWing',
        'why': 'Made in Almaty by a developer with almost 20 years in financial systems, for an amateur team he knows. The goal is simple: a coach shouldn’t have to keep the team in their head and in five different chats.',
        'nav_privacy': 'Privacy',
        'nav_support': 'Support',
        'nav_home': 'Home',
        'made': 'Made in Almaty',
        'privacy_title': 'Privacy Policy',
        'updated': 'Updated',
        'privacy': [
            ('', '<p class="hi"><b>In short:</b> TeamWing does not collect your data. No sign-up, no servers of ours, no ads or analytics. Everything you enter is stored only on your device.</p>'),
            ('What data the app stores', '<p>Information the coach enters: team name and logo; player names, numbers, positions, phone numbers, dates of birth and joining; schedule and attendance; game results and stats; services, charges, payments and debts; team settings. Optional fields are filled in only if you choose to.</p><p>All of it is stored in a file inside the app on your iPhone. The developer has no access to it.</p>'),
            ('Internet and third parties', '<p>The app does not need the internet to work. It has no server of its own, no ads, no analytics and no third-party SDKs that collect data. TeamWing does not process bank payments: payment tracking is records the coach makes.</p>'),
            ('Permissions', '<ul><li><b>Photos</b> — only so you can pick an image for the team logo yourself. The rest of your library is not shared with the app.</li><li><b>Files</b> — only the backup file you choose to restore.</li></ul><p>The camera, microphone and location are not used.</p>'),
            ('Backups', '<p>A backup is created only when you ask and saved wherever you choose in the Share menu — for example, iCloud Drive. A backup is a JSON file <b>without a password or encryption</b>; it contains the team’s phone numbers, dates of birth and payment history. Keep it to yourself and do not share it. If you save a backup to iCloud Drive or another service, that service’s terms apply.</p><p>Before restoring from a backup, the app automatically saves the current data on the phone so it can be rolled back.</p>'),
            ('Player data', '<p>TeamWing is a coach’s tool. When entering information about players, the coach is responsible for letting them know what data is kept — and, for minors, their parents or legal guardians. A player who wants their data corrected or deleted should contact their coach. TeamWing creates no public profiles and publishes nothing.</p>'),
            ('Testing via TestFlight', '<p>If you test the beta, Apple may share crash reports and your feedback, including whatever you put in it, with the developer. See <a href="https://www.apple.com/legal/privacy/data/en/test-flight/">TestFlight &amp; Privacy</a>. Please avoid attaching screenshots with real player data unless needed.</p>'),
            ('Deleting data', '<p>Delete the app and all of its data is removed from the phone. Backups you saved yourself stay where you put them — delete them manually.</p>'),
            ('Changes', '<p>If this policy changes — for example, when player accounts and sync are added — the new version will appear on this page with a new date, and the feature will be described before it is turned on.</p>'),
            ('Contact', f'<p>App owner: Yevgeniy Avdonin.<br>Privacy questions: <a href="mailto:{EMAIL}">{EMAIL}</a></p>'),
        ],
        'support_title': 'Support',
        'support_lead': 'Answers to common questions. Didn’t find yours? Write to us.',
        'faq': [
            ('How do I install the beta?', '<ol><li>Install <b>TestFlight</b> from the App Store.</li><li>Open the invitation — email or link — on your iPhone, tap Accept, then Install.</li><li>Updates arrive through TestFlight.</li></ol>'),
            ('Where is the team data stored?', '<p>Only on your iPhone, inside the app. There is no account and no developer cloud — so make backups regularly.</p>'),
            ('How do I save a backup to iCloud?', '<ol><li>Settings («Настройки») → Backup and restore («Резервная копия и восстановление») → save data.</li><li>In the menu choose Save to Files → iCloud Drive → a folder (e.g. TeamWing) → Save.</li><li>Open Files and check that the backup is there and uploaded.</li></ol>'),
            ('How do I move the team to another phone?', '<ol><li>On the old phone, save a backup to iCloud Drive or send the file to yourself.</li><li>On the new phone, install TeamWing and open Settings → Backup and restore → Choose backup file («Выбрать файл копии»).</li><li>Review the backup contents and confirm the replacement.</li></ol>'),
            ('Can I try the app without my own data?', '<p>Yes: on first launch tap Take the tutorial — the app shows a fictional hockey team with step-by-step hints. Your data is not touched. To take it again: Settings → Take the tutorial again.</p>'),
            ('Can players see their own data?', '<p>Not yet — for now it is a coach’s app. A players’ app is planned.</p>'),
        ],
        'contact_h': 'Contact us',
        'contact': f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a>. If you are testing the beta, you can send feedback right from TestFlight — take a screenshot in the app and tap Share Beta Feedback.',
    },
    'kk': {
        'title': 'TeamWing — әуесқой команда жаттықтырушысының кабинеті',
        'desc': 'Әуесқой команда жаттықтырушысына арналған iPhone қосымшасы: құрам, кесте, қатысу, төлемдер және матч статистикасы. Деректер тек телефонда сақталады.',
        'h1': 'Бүкіл команда — бір телефонда',
        'lead': 'Құрам, жаттығулар, қатысу, жарналар және матч статистикасы. Кестелерсіз, дәптерсіз және чатта қайта санаусыз.',
        'badge': 'Тестер болу',
        'badge_small': 'TestFlight бетасы · iPhone үшін',
        'soon': 'TestFlight бетасы — шақыру бойынша',
        'note': 'iPhone үшін. Интерфейс — орыс және ағылшын тілдерінде.',
        'feat_h': 'TeamWing не істей алады',
        'feat': [
            ('users', 'Ойыншылар мен құрамдар', 'Нөмірі мен позициясы бар ойыншы карталары, буындар мен құрам нұсқалары — сүйреп апару арқылы.'),
            ('cal', 'Кесте', 'Апта күндері бойынша жаттығулар, жекелеген сабақтарды ауыстыру және болдырмау.'),
            ('check', 'Қатысу', 'Бірнеше түртумен белгілеу — кім келеді, кім қалдырады, бәрі көрінеді.'),
            ('coin', 'Жарналар мен қарыздар', 'Қызметтер мен абонементтер, айлық есептеулер, толық және ішінара төлемдер, қор және қазынашы.'),
            ('trophy', 'Матчтар мен статистика', 'Жолдастық ойындар нәтижелері, голдар, пастар, айыппұлдар және қақпашылар.'),
            ('cloud', 'Сақтық көшірмелер', 'Бүкіл команда бір файлда — iCloud Drive-қа сақтап, басқа телефонда қалпына келтіріңіз.'),
        ],
        'priv_h': 'Команда деректері — тек сізде',
        'priv': 'Тіркеусіз, біздің серверлерсіз, жарнамасыз және аналитикасыз. Деректер базасы жаттықтырушының телефонында, ал көшірмелерді өзіңіз қалаған жерге сақтайсыз.',
        'why_h': 'Неліктен TeamWing',
        'why': 'Қосымшаны Алматыда 20 жылға жуық қаржы жүйелерімен айналысатын әзірлеуші таныс әуесқой команда үшін жасады. Мақсат қарапайым: жаттықтырушы команданы басында және бес түрлі чатта ұстамауы керек.',
        'nav_privacy': 'Құпиялылық',
        'nav_support': 'Қолдау',
        'nav_home': 'Басты бет',
        'made': 'Алматыда жасалған',
        'privacy_title': 'Құпиялылық саясаты',
        'updated': 'Жаңартылды',
        'privacy': [
            ('', '<p class="hi"><b>Қысқаша:</b> TeamWing сіздің деректеріңізді жинамайды. Тіркеу жоқ, біздің серверлер жоқ, жарнама мен аналитика жоқ. Енгізген барлық деректер тек құрылғыңызда сақталады.</p>'),
            ('Қосымша қандай деректерді сақтайды', '<p>Жаттықтырушы енгізетін мәліметтер: команда атауы мен логотипі; ойыншылардың аты-жөні, нөмірлері, позициялары, телефондары, туған және қосылған күндері; кесте мен қатысу; матч нәтижелері мен статистикасы; қызметтер, есептеулер, төлемдер мен қарыздар; команда баптаулары. Міндетті емес өрістер қалауыңыз бойынша толтырылады.</p><p>Мұның бәрі iPhone-дағы қосымшаның ішіндегі файлда сақталады. Әзірлеушінің оған қолжетімділігі жоқ.</p>'),
            ('Интернет және үшінші тараптар', '<p>Қосымшаға жұмыс істеу үшін интернет қажет емес. Онда өз сервері, жарнама, аналитика жүйелері және деректер жинайтын үшінші тарап SDK-лары жоқ. TeamWing банк төлемдерін өңдемейді: төлемдер есебі — жаттықтырушы жасайтын жазбалар.</p>'),
            ('Рұқсаттар', '<ul><li><b>Фото</b> — тек команда логотипіне сурет таңдауыңыз үшін. Фототекаңыздың қалған бөлігі қосымшаға берілмейді.</li><li><b>Файлдар</b> — тек қалпына келтіру үшін өзіңіз таңдаған сақтық көшірме файлы.</li></ul><p>Камера, микрофон және геолокация пайдаланылмайды.</p>'),
            ('Сақтық көшірмелер', '<p>Көшірме тек сіздің командаңыз бойынша жасалады және «Бөлісу» мәзірінде таңдаған жерге сақталады — мысалы, iCloud Drive-қа. Көшірме — <b>құпиясөзсіз және шифрлаусыз</b> JSON файлы, онда команданың телефондары, туған күндері және қаржы тарихы бар. Оны өзіңізде сақтаңыз және бөгде адамдарға бермеңіз. Көшірмені iCloud Drive-қа немесе басқа сервиске сақтасаңыз, сол сервистің ережелері қолданылады.</p><p>Көшірмеден қалпына келтірер алдында қосымша ағымдағы деректерді қайтару мүмкін болуы үшін телефонда автоматты түрде сақтайды.</p>'),
            ('Ойыншылардың деректері', '<p>TeamWing — жаттықтырушының құралы. Ойыншылар туралы мәліметтерді енгізгенде жаттықтырушы олардың қандай деректер жүргізілетінін білуіне, ал кәмелетке толмағандар үшін — олардың ата-аналарының немесе заңды өкілдерінің білуіне жауапты. Ойыншы өз деректерін түзеткісі немесе жойғысы келсе, жаттықтырушысына жүгінуі керек. TeamWing жария профильдер жасамайды және ештеңе жарияламайды.</p>'),
            ('TestFlight арқылы тестілеу', '<p>Бетаны тестілесеңіз, Apple әзірлеушіге ақаулар туралы есептерді және сіз көрсеткен ақпараты бар пікірлеріңізді бере алады. Толығырақ — <a href="https://www.apple.com/legal/privacy/data/en/test-flight/">TestFlight ережелерінде</a>. Қажет болмаса, пікірлерге ойыншылардың нақты деректері бар скриншоттарды тіркемеңіз.</p>'),
            ('Деректерді жою', '<p>Қосымшаны жойыңыз — оның барлық деректері телефоннан жойылады. Өзіңіз сақтаған көшірмелер сақталған жерінде қалады — оларды қолмен жойыңыз.</p>'),
            ('Өзгерістер', '<p>Саясат өзгерсе — мысалы, қосымшада ойыншылар аккаунттары мен синхрондау пайда болғанда — жаңа нұсқа осы бетте жаңа күнмен жарияланады, ал функцияның өзі қосылғанға дейін сипатталады.</p>'),
            ('Байланыс', f'<p>Қосымша иесі: Yevgeniy Avdonin.<br>Құпиялылық сұрақтары: <a href="mailto:{EMAIL}">{EMAIL}</a></p>'),
        ],
        'support_title': 'Қолдау',
        'support_lead': 'Жиі қойылатын сұрақтарға жауаптар. Өз сұрағыңызды таппасаңыз — жазыңыз.',
        'faq': [
            ('Бетаны қалай орнатамын?', '<ol><li>App Store-дан <b>TestFlight</b> қосымшасын орнатыңыз.</li><li>iPhone-да шақыруды — хатты немесе сілтемені — ашып, «Қабылдау», сосын «Орнату» басыңыз.</li><li>Жаңартулар TestFlight арқылы келеді.</li></ol>'),
            ('Команда деректері қайда сақталады?', '<p>Тек iPhone-ыңызда, қосымшаның ішінде. Тіркеу де, әзірлеушінің бұлты да жоқ — сондықтан сақтық көшірмелерді жүйелі түрде жасаңыз.</p>'),
            ('Көшірмені iCloud-қа қалай сақтаймын?', '<ol><li>«Настройки» → «Резервная копия и восстановление» → деректерді сақтау.</li><li>Мәзірден «Файлдарға сақтау» → iCloud Drive → қалта (мысалы, TeamWing) → «Сақтау» таңдаңыз.</li><li>«Файлдар» қосымшасын ашып, көшірменің пайда болып, жүктелгенін тексеріңіз.</li></ol>'),
            ('Команданы басқа телефонға қалай көшіремін?', '<ol><li>Ескі телефонда көшірмені iCloud Drive-қа сақтаңыз немесе файлды өзіңізге жіберіңіз.</li><li>Жаңасында TeamWing орнатып, «Настройки» → «Резервная копия и восстановление» → «Выбрать файл копии» ашыңыз.</li><li>Көшірме мазмұнын тексеріп, ауыстыруды растаңыз.</li></ol>'),
            ('Қосымшаны өз деректерімсіз көруге бола ма?', '<p>Иә: алғаш іске қосқанда «Пройти обучение на примере» түймесін басыңыз — қосымша ойдан шығарылған хоккей командасын қадамдық кеңестермен көрсетеді. Деректеріңізге әсер етпейді. Қайта өту: «Настройки» → «Пройти обучение заново».</p>'),
            ('Ойыншылар өз деректерін көре ала ма?', '<p>Әзірге жоқ — қазір бұл жаттықтырушы кабинеті. Ойыншыларға арналған қосымша жоспарда бар.</p>'),
        ],
        'contact_h': 'Бізге жазу',
        'contact': f'Пошта: <a href="mailto:{EMAIL}">{EMAIL}</a>. Бетаны тестілеп жүрсеңіз, пікірді TestFlight-тан тікелей жібере аласыз — қосымшада скриншот жасап, «Бета пікірімен бөлісу» түймесін басыңыз.',
    },
}


def url(lang, page):
    prefix = BASE if lang == 'ru' else f'{BASE}{lang}/'
    return prefix + ('' if page == 'index' else f'{page}.html')


def page(lang, name, title, desc, body):
    t = T[lang]
    langs = ''.join(
        f'<a href="{url(l, name)}" class="{"on" if l == lang else ""}" hreflang="{l}">{LANG_LABEL[l]}</a>' for l in LANGS
    )
    alternates = ''.join(f'<link rel="alternate" hreflang="{l}" href="https://warlockjohn.github.io{url(l, name)}">' for l in LANGS)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://warlockjohn.github.io{BASE}assets/icon.png">
<meta name="theme-color" content="#F2F4FA" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0F1222" media="(prefers-color-scheme: dark)">
{alternates}
<link rel="icon" href="{BASE}assets/favicon.png">
<link rel="apple-touch-icon" href="{BASE}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{BASE}style.css">
</head>
<body>
<div class="wrap">
<header class="top">
  <a class="brand" href="{url(lang, 'index')}"><img src="{BASE}assets/icon.png" alt="">TeamWing</a>
  <nav class="langs">{langs}</nav>
</header>
{body}
<footer>
  <span>© 2026 TeamWing · {t['made']}</span>
  <a href="{url(lang, 'index')}">{t['nav_home']}</a>
  <a href="{url(lang, 'privacy')}">{t['nav_privacy']}</a>
  <a href="{url(lang, 'support')}">{t['nav_support']}</a>
  <a href="mailto:{EMAIL}">{EMAIL}</a>
</footer>
</div>
</body>
</html>
'''


def home(lang):
    t = T[lang]
    feat = ''.join(
        f'<div class="card"><div class="ico">{ICONS[i]}</div><h3>{h}</h3><p>{p}</p></div>' for i, h, p in t['feat']
    )
    cta = (f'<a class="badge" href="{BETA}"><span><small>{t["badge_small"]}</small>{t["badge"]}</span></a>'
           if BETA else f'<span class="soon">{t["soon"]}</span>')
    body = f'''<section class="hero">
  <div>
    <h1>{t['h1']}</h1>
    <p class="lead">{t['lead']}</p>
    {cta}
    <p class="note">{t['note']}</p>
  </div>
  <img class="appicon" src="{BASE}assets/icon.png" alt="TeamWing" width="260">
</section>
<h2>{t['feat_h']}</h2>
<section class="features">{feat}</section>
<section class="why priv"><div class="ico">{ICONS['lock']}</div><div><h2>{t['priv_h']}</h2><p>{t['priv']}</p></div></section>
<section class="why"><h2>{t['why_h']}</h2><p>{t['why']}</p></section>'''
    return page(lang, 'index', t['title'], t['desc'], body)


def privacy(lang):
    t = T[lang]
    parts = ''.join((f'<h2>{h}</h2>' if h else '') + b for h, b in t['privacy'])
    body = f'''<article class="doc">
  <h1>{t['privacy_title']}</h1>
  <p class="date">{t['updated']}: {UPDATED[lang]}</p>
  {parts}
</article>'''
    return page(lang, 'privacy', f"{t['privacy_title']} — TeamWing", t['desc'], body)


def support(lang):
    t = T[lang]
    faq = ''.join(f'<details><summary>{q}</summary>{a}</details>' for q, a in t['faq'])
    body = f'''<article class="doc">
  <h1>{t['support_title']}</h1>
  <p class="date">{t['support_lead']}</p>
  {faq}
</article>
<section class="why contact">
  <img src="{BASE}assets/icon.png" alt="" width="96" style="border-radius:22%">
  <div><h2>{t['contact_h']}</h2><p>{t['contact']}</p></div>
</section>'''
    return page(lang, 'support', f"{t['support_title']} — TeamWing", t['desc'], body)


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    for lang in LANGS:
        d = here if lang == 'ru' else os.path.join(here, lang)
        os.makedirs(d, exist_ok=True)
        for name, fn in [('index', home), ('privacy', privacy), ('support', support)]:
            with open(os.path.join(d, f'{name}.html'), 'w', encoding='utf-8') as f:
                f.write(fn(lang))
    print('ok')
