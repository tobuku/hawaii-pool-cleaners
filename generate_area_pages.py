#!/usr/bin/env python3
"""
generate_area_pages.py
Creates 53 area-specific vinyl pool service pages for hawaiipoolcleaners.com
Run: python generate_area_pages.py
Output: areas/[slug]/index.html  (files are NOT git-tracked until deploy_areas.py pushes them)
"""

import os

POOL_IMGS = [
    '1','3','4','10','11','21','22','30','37','38','39','40','41','42','43','44','45',
    '49','60','61','67','68','71','72','73','74','75','76','77','79','91','92','93',
    '95','96','97','99','100','101','102','103','104','105','106','107','108','109',
    '110','111','112','113','114'
]

def img(area_idx, slot):
    return '/img/pools/' + POOL_IMGS[(area_idx * 11 + slot) % len(POOL_IMGS)] + '.jpg'

AREAS = [
    {
        "slug": "aiea",
        "name": "Aiea",
        "title": "Vinyl Pool Installation & Cleaning in Aiea, Hawaii | Hawaii Pool Cleaners",
        "desc": "Expert vinyl liner installation, repair, and pool cleaning in Aiea, Hawaii. Hawaii Pool Cleaners serves central Oahu. Free quotes — call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Aiea",
        "hero_sub": "Aiea homeowners count on Hawaii Pool Cleaners for vinyl liner replacements, pool repairs, and weekly maintenance. We're familiar with every block between Halawa and Pearlridge.",
        "intro_h": "Central Oahu's Pool Specialists",
        "intro_p": "Aiea sits in the heart of central Oahu where tradewind pollen and the salt-laden air off Pearl Harbor hit pools hard. Whether your liner is bubbling away from the bead track or your pump is running rough, we diagnose and fix it fast.",
        "feat_p": "Older Aiea homes often have pools that haven't had liner work in a decade or more. Our team handles full replacements from drain to refill, including resetting bead channels that have degraded over time.",
        "feat_bullets": ["Full vinyl liner replacement — drain to refill","Weekly and bi-weekly maintenance plans","Filter and pump diagnostics","Chemical balancing tailored to central Oahu water","Free on-site quotes"],
        "cta_h2": "Ready to Book Service in Aiea?",
        "cta_p": "Call 808-864-3605 or request a free quote online. We serve Aiea and all of central Oahu.",
    },
    {
        "slug": "ewa-beach",
        "name": "Ewa Beach",
        "title": "Vinyl Pool Installation & Cleaning in Ewa Beach, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Ewa Beach, Hawaii. Hawaii Pool Cleaners — Oahu's pool specialists. Free quotes — call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Ewa Beach",
        "hero_sub": "Ewa Beach is one of Oahu's fastest-growing communities and we're here to keep its pools looking sharp. From new liner installs to weekly chemical service, Hawaii Pool Cleaners has Ewa covered.",
        "intro_h": "Pool Care for Ewa Beach's Growing Neighborhoods",
        "intro_p": "Ewa Beach developments continue expanding along the second city corridor, bringing hundreds of new residential pools online every year. New pools need proper startup chemistry and quality liners from the start — and that's exactly what we provide.",
        "feat_p": "The dry, sun-drenched climate on the Ewa plain accelerates UV damage to pool liners. We source UV-resistant materials rated for Hawaii's intense sun so your liner lasts years longer than a budget replacement.",
        "feat_bullets": ["New pool liner installation for recently built homes","UV-resistant liner materials for Ewa's intense sun","Weekly chemical and maintenance service","Filter, pump, and equipment repair","Free on-site assessments — no pressure"],
        "cta_h2": "Ewa Beach Pool Service — Book Today",
        "cta_p": "Call 808-864-3605 or submit a free quote request. We're in Ewa Beach regularly.",
    },
    {
        "slug": "ewa-gentry",
        "name": "Ewa Gentry",
        "title": "Vinyl Pool Installation & Cleaning in Ewa Gentry, Hawaii | Hawaii Pool Cleaners",
        "desc": "Professional vinyl pool liner installation, repair, and cleaning in Ewa Gentry, Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Ewa Gentry",
        "hero_sub": "Ewa Gentry's planned communities have some of Oahu's newest residential pools. Hawaii Pool Cleaners handles liner installs, chemical service, and full maintenance for Ewa Gentry homeowners.",
        "intro_h": "Serving Ewa Gentry's Master-Planned Communities",
        "intro_p": "Ewa Gentry developments like Hoakalei and Villages of Ewa feature modern pool designs with specific liner requirements. Our team installs and services pools in these communities regularly and understands the HOA standards each neighborhood maintains.",
        "feat_p": "Even newer liners in Ewa Gentry face stress from the area's dry heat and limited rainfall. We monitor water chemistry closely on every visit so small problems don't become expensive repairs.",
        "feat_bullets": ["Liner installs compatible with modern pool shell designs","HOA-compliant pool maintenance","Chemical balancing and weekly service","Equipment diagnostics and repair","Free on-site quotes"],
        "cta_h2": "Get Ewa Gentry Pool Service Scheduled",
        "cta_p": "Call 808-864-3605 or request a free quote. We're in Ewa Gentry every week.",
    },
    {
        "slug": "haleiwa",
        "name": "Haleiwa",
        "title": "Vinyl Pool Installation & Cleaning in Haleiwa, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Haleiwa, North Shore Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Haleiwa",
        "hero_sub": "On the North Shore, pools work hard year-round. Hawaii Pool Cleaners brings professional vinyl liner service and maintenance to Haleiwa and the surrounding North Shore communities.",
        "intro_h": "North Shore Pool Specialists",
        "intro_p": "Haleiwa sits where Oahu's surf culture meets a relaxed rural vibe — and the pools here reflect that, from private estate pools back in the valley to compact plunge pools on vacation rental properties. We service them all.",
        "feat_p": "North Shore pools collect a lot of debris — leaves from the kukui trees, dust from the unpaved roads, and salt spray from the nearby coast. Regular maintenance on a consistent schedule keeps chemistry balanced and equipment running clean.",
        "feat_bullets": ["Vinyl liner installation and full replacements","Vacation rental pool maintenance programs","Debris removal and regular cleaning","Chemical balancing for coastal conditions","Filter and pump service"],
        "cta_h2": "Haleiwa & North Shore Pool Service",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve the entire North Shore corridor.",
    },
    {
        "slug": "hauula",
        "name": "Hauula",
        "title": "Vinyl Pool Installation & Cleaning in Hauula, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Hauula on Oahu's windward coast. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Hauula",
        "hero_sub": "Hauula's lush windward setting is beautiful — but the elevated rainfall and humidity demand more from your pool. Hawaii Pool Cleaners provides expert liner work and maintenance for Hauula homeowners.",
        "intro_h": "Windward Pool Care in Hauula",
        "intro_p": "Hauula sits in one of Oahu's rainier stretches between Punaluu and Laie. The constant moisture, algae pressure, and organic debris load here require a more aggressive maintenance approach than drier parts of the island.",
        "feat_p": "Windward pools accumulate phosphates from runoff faster than anywhere on Oahu. We treat for algae prevention proactively and keep filters clean so your system handles the extra load without failing.",
        "feat_bullets": ["Algae prevention and phosphate treatment","Vinyl liner replacement and repair","Weekly maintenance for windward conditions","Filter cleaning and pump service","Free quotes — no obligation"],
        "cta_h2": "Hauula Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We regularly serve the windward coast.",
    },
    {
        "slug": "honolulu",
        "name": "Honolulu",
        "title": "Vinyl Pool Installation & Cleaning in Honolulu, Hawaii | Hawaii Pool Cleaners",
        "desc": "Expert vinyl pool liner installation, repair, and pool cleaning throughout Honolulu. Hawaii Pool Cleaners — Oahu's pool specialists. Free quotes — call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Honolulu",
        "hero_sub": "From Manoa to Moiliili, Hawaii Pool Cleaners provides vinyl liner installation, pool repair, and maintenance services throughout Honolulu. We're the local team Honolulu homeowners trust.",
        "intro_h": "Honolulu's Vinyl Pool Liner Experts",
        "intro_p": "Honolulu's diverse neighborhoods — valley homes, hillside estates, urban bungalows — each present unique pool conditions. Our team services pools of every size and age across the city, from aging pools in need of new liners to well-maintained systems that just need routine care.",
        "feat_p": "City pools in Honolulu deal with added challenges: shade from structures, higher foot traffic, and trade-wind-driven debris. We customize our maintenance plans to match your pool's actual conditions, not a one-size-fits-all schedule.",
        "feat_bullets": ["Full vinyl liner installation across all Honolulu neighborhoods","Pool repair and restoration","Weekly and bi-weekly maintenance","Chemical balancing and water testing","Filter and pump diagnostics"],
        "cta_h2": "Honolulu Pool Service — Schedule Today",
        "cta_p": "Call 808-864-3605 or submit a free quote request for any Honolulu address.",
    },
    {
        "slug": "kaaawa",
        "name": "Kaaawa",
        "title": "Vinyl Pool Installation & Cleaning in Kaaawa, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Kaaawa on Oahu's windward coast. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Kaaawa",
        "hero_sub": "Kaaawa is a quiet windward gem tucked between the Ko'olau cliffs and the coast. Hawaii Pool Cleaners brings professional pool service to Kaaawa homeowners who want their pools maintained to the same standard as the rest of the island.",
        "intro_h": "Remote Windward Service — No Extra Charge",
        "intro_p": "Kaaawa is off the beaten path, but we make the drive. Homes here have spectacular views and pools that deserve proper care. High rainfall, organic debris from the mountains, and salt from the nearby ocean all factor into our service approach here.",
        "feat_p": "Because windward pools like those in Kaaawa face intense biological load — algae, phosphates, and organic matter — we include preventive treatments in every maintenance visit, not just when you call with a problem.",
        "feat_bullets": ["Windward-specific algae prevention program","Vinyl liner installation and repair","Consistent weekly or bi-weekly service","Filter cleaning and pump repair","Free quotes — we come to you"],
        "cta_h2": "Kaaawa Pool Service — We Make the Drive",
        "cta_p": "Call 808-864-3605 or request a free quote. No service area surcharge for windward Oahu.",
    },
    {
        "slug": "kahala",
        "name": "Kahala",
        "title": "Vinyl Pool Installation & Cleaning in Kahala, Hawaii | Hawaii Pool Cleaners",
        "desc": "Premium vinyl pool liner installation, repair, and pool cleaning in Kahala, Honolulu. Hawaii Pool Cleaners — discreet, professional service. Free quotes — 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Kahala",
        "hero_sub": "Kahala is one of Oahu's most prestigious neighborhoods, and the pools here reflect that. Hawaii Pool Cleaners delivers white-glove vinyl liner service and maintenance that matches Kahala's high standards.",
        "intro_h": "Premium Pool Service for Kahala Estates",
        "intro_p": "Kahala's large estate lots often feature custom pool designs with high-end finishes. Our team works carefully around landscaping, hardscape, and existing equipment — leaving everything exactly as we found it except for the water, which we leave sparkling.",
        "feat_p": "Many Kahala pools have older liners installed before today's UV-resistant technology existed. Upgrading to a modern liner dramatically improves appearance, reduces water loss, and can cut chemical usage because the material is less porous.",
        "feat_bullets": ["Premium vinyl liner installation for estate pools","Discreet, professional service visits","Custom maintenance plans for large pools","Equipment upgrades and pump replacement","Free on-site consultations"],
        "cta_h2": "Kahala Pool Service — Schedule a Consultation",
        "cta_p": "Call 808-864-3605 or request a free quote. We respect your property and your privacy.",
    },
    {
        "slug": "kahuku",
        "name": "Kahuku",
        "title": "Vinyl Pool Installation & Cleaning in Kahuku, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Kahuku, North Shore Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Kahuku",
        "hero_sub": "At the top of Oahu's windward coast, Kahuku homeowners deserve the same quality pool service as any other part of the island. Hawaii Pool Cleaners makes regular runs to Kahuku and the surrounding North Shore.",
        "intro_h": "Full-Service Pool Care at the Top of Oahu",
        "intro_p": "Kahuku's coastal location means pools here battle salt air, strong winds, and the debris that comes with being next to agricultural land. Our Kahuku clients appreciate a reliable schedule they can count on — we show up, we do the work, and we report back on anything that needs attention.",
        "feat_p": "Kahuku vacation rental properties in particular benefit from our maintenance programs. A pool issue discovered by a guest is worse than one caught by your technician on a Tuesday. We keep your rental pool guest-ready at all times.",
        "feat_bullets": ["Vinyl liner replacement for rural and coastal pools","Vacation rental pool programs","Wind and debris management","Chemical service and water testing","Free on-site quotes"],
        "cta_h2": "Kahuku Pool Service — We Come to You",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Kahuku and all of the North Shore.",
    },
    {
        "slug": "kailua",
        "name": "Kailua",
        "title": "Vinyl Pool Installation & Cleaning in Kailua, Hawaii | Hawaii Pool Cleaners",
        "desc": "Expert vinyl pool liner installation, repair, and pool cleaning in Kailua, windward Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Kailua",
        "hero_sub": "Kailua is the windward side's crown jewel — beautiful homes, lush greenery, and pools that see year-round use. Hawaii Pool Cleaners keeps Kailua pools clean, balanced, and liner-perfect.",
        "intro_h": "Kailua's Trusted Pool Service Team",
        "intro_p": "Kailua's combination of warm temperatures, frequent rain, and lush vegetation creates a constant challenge for pool chemistry. Phosphates from organic runoff, algae growth, and debris from overhanging trees keep our Kailua clients' pools on a busy maintenance schedule.",
        "feat_p": "We see more algae calls in Kailua than almost anywhere else on Oahu. Our proactive approach — testing phosphates every visit, brushing regularly, and adjusting sanitizer based on actual conditions — prevents green water before it starts.",
        "feat_bullets": ["Proactive algae prevention for windward pools","Full vinyl liner replacement and repair","Weekly maintenance tailored to Kailua's conditions","Filter and pump service","Free on-site quotes"],
        "cta_h2": "Kailua Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We're in Kailua multiple times per week.",
    },
    {
        "slug": "kalama-valley",
        "name": "Kalama Valley",
        "title": "Vinyl Pool Installation & Cleaning in Kalama Valley, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Kalama Valley, East Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Kalama Valley",
        "hero_sub": "Tucked into the hills above Hawaii Kai, Kalama Valley offers quiet residential living with some of East Oahu's most spacious yards and pools. Hawaii Pool Cleaners provides full-service pool care for Kalama Valley homeowners.",
        "intro_h": "East Oahu Pool Specialists",
        "intro_p": "Kalama Valley's hillside location brings more wind and leaf debris than nearby coastal areas. Pools here often have tree cover that increases organic load in the water. Our maintenance program addresses this with regular brushing, phosphate treatment, and debris removal.",
        "feat_p": "Many Kalama Valley homes have had their pools for twenty-plus years. A liner in that age range is often ready for replacement — and a new UV-resistant liner instantly transforms the look and performance of the entire pool.",
        "feat_bullets": ["Vinyl liner replacement for mature East Oahu pools","Debris and organic load management","Weekly maintenance and chemical balancing","Filter and pump repair","Free on-site pool assessments"],
        "cta_h2": "Kalama Valley Pool Service — Get a Free Quote",
        "cta_p": "Call 808-864-3605 or request a free quote online. We serve Kalama Valley and all of East Oahu.",
    },
    {
        "slug": "kalihi",
        "name": "Kalihi",
        "title": "Vinyl Pool Installation & Cleaning in Kalihi, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Kalihi, Honolulu. Hawaii Pool Cleaners — affordable, professional pool service. Free quotes — 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Kalihi",
        "hero_sub": "Kalihi is one of Honolulu's most established residential corridors. Hawaii Pool Cleaners serves Kalihi homeowners with professional vinyl liner work, pool cleaning, and maintenance at fair prices.",
        "intro_h": "Dependable Pool Service for Kalihi Homeowners",
        "intro_p": "Kalihi's older residential neighborhoods have pools that have served families for decades. Aging liners, older equipment, and deferred maintenance are common — and all of it is fixable. We specialize in bringing neglected pools back to full operation without unnecessary upsells.",
        "feat_p": "A cracked or bubbling liner isn't just an eyesore — it's losing you water and money every day. We assess the condition honestly and give you a straight recommendation: patch repair when that's the right call, full replacement when it's time.",
        "feat_bullets": ["Honest liner assessments — patch vs. replace guidance","Full vinyl liner replacement","Pool restoration for neglected systems","Chemical service and water balancing","Free on-site quotes"],
        "cta_h2": "Kalihi Pool Service — Honest, Affordable Work",
        "cta_p": "Call 808-864-3605 or request a free quote. No upsells, no surprises.",
    },
    {
        "slug": "kaneohe",
        "name": "Kaneohe",
        "title": "Vinyl Pool Installation & Cleaning in Kaneohe, Hawaii | Hawaii Pool Cleaners",
        "desc": "Expert vinyl pool liner installation, repair, and pool cleaning in Kaneohe, windward Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Kaneohe",
        "hero_sub": "Kaneohe is the windward side's largest town, and its pools need specialists who understand the unique demands of high rainfall and lush vegetation. Hawaii Pool Cleaners is the windward team Kaneohe trusts.",
        "intro_h": "Kaneohe's Windward Pool Experts",
        "intro_p": "Kaneohe receives more rain than nearly anywhere else on Oahu, which dilutes pool chemistry, increases phosphate load, and creates persistent algae pressure. We've dialed in our approach for Kaneohe specifically — more frequent chemical checks, targeted phosphate removal, and consistent brushing keep pools clear year-round.",
        "feat_p": "We service dozens of Kaneohe pools on a regular schedule and understand the seasonal shifts in water chemistry that affect windward pools differently than leeward ones. That local knowledge means fewer problems and more time enjoying your pool.",
        "feat_bullets": ["Windward-optimized maintenance programs","Full vinyl liner replacement and repair","Algae prevention and phosphate management","Equipment diagnostics and repair","Free on-site quotes"],
        "cta_h2": "Kaneohe Pool Service — Schedule a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We're in Kaneohe every week.",
    },
    {
        "slug": "kapolei",
        "name": "Kapolei",
        "title": "Vinyl Pool Installation & Cleaning in Kapolei, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Kapolei, Oahu's second city. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Kapolei",
        "hero_sub": "Kapolei has grown into Oahu's second city, and with that growth comes thousands of residential pools. Hawaii Pool Cleaners is the local team keeping Kapolei pools clean, safe, and liner-perfect.",
        "intro_h": "Kapolei Pool Service — Built for the West Side",
        "intro_p": "Kapolei's hot, dry climate and high sun exposure are hard on pool liners. We see UV degradation and chemical imbalances here more acutely than on other parts of the island. Our service plans account for that — we test more frequently and use materials rated for extreme UV exposure.",
        "feat_p": "New construction in Kapolei means many pools are still in their first liner cycle, but the sun out here ages liners faster. We'll let you know honestly when it's time for a replacement and exactly what your options are.",
        "feat_bullets": ["UV-resistant liner installation for Kapolei's sun exposure","New construction pool startup and chemical service","Weekly maintenance and water testing","Filter and pump repair","Free on-site quotes"],
        "cta_h2": "Kapolei Pool Service — Get a Free Quote",
        "cta_p": "Call 808-864-3605 or submit a quote request online. We're in Kapolei regularly.",
    },
    {
        "slug": "laie",
        "name": "Laie",
        "title": "Vinyl Pool Installation & Cleaning in Laie, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Laie, North Shore Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Laie",
        "hero_sub": "Laie's tight-knit community on the North Shore windward coast deserves reliable pool service. Hawaii Pool Cleaners provides vinyl liner work and maintenance for Laie homeowners throughout the year.",
        "intro_h": "Reliable Pool Care for Laie",
        "intro_p": "Laie sits at the convergence of windward rainfall and North Shore coastal conditions, which creates challenging chemistry for pool owners. We factor in the elevated phosphate levels and salt air when calibrating our chemical service, keeping water clear even in the wettest months.",
        "feat_p": "Our team makes the full drive to Laie on scheduled routes, so there's no premium for the distance. We treat Laie clients with the same priority and consistency as any Honolulu address.",
        "feat_bullets": ["Windward-adjusted chemical service","Full vinyl liner replacement and repair","Consistent weekly maintenance visits","Filter cleaning and equipment repair","Free quotes — no distance surcharge"],
        "cta_h2": "Laie Pool Service — We Come to You",
        "cta_p": "Call 808-864-3605 or request a free quote. Laie is on our regular route.",
    },
    {
        "slug": "maili",
        "name": "Maili",
        "title": "Vinyl Pool Installation & Cleaning in Maili, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Maili on the Waianae Coast. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Maili",
        "hero_sub": "Maili is on the Waianae coast where the sun is relentless and pool liners age faster than anywhere on Oahu. Hawaii Pool Cleaners brings professional liner work and maintenance to Maili and the surrounding coast.",
        "intro_h": "Waianae Coast Pool Specialists",
        "intro_p": "The west side gets more sun per day than any other part of Oahu. For pool liners, that means accelerated UV degradation, higher evaporation, and chemical imbalance from heat. We understand the west side's specific conditions and build our service plans around them.",
        "feat_p": "We use only UV-rated liner materials on Waianae coast installations. A standard liner that would last eight years elsewhere may fail in four on the west side. Going with the right material upfront saves you money over the life of the pool.",
        "feat_bullets": ["UV-rated liner materials for west side conditions","Full liner installation and replacement","Chemical service calibrated for high-heat environments","Weekly maintenance and water testing","Free on-site quotes"],
        "cta_h2": "Maili Pool Service — Get a Free Quote",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve the entire Waianae coast.",
    },
    {
        "slug": "makaha",
        "name": "Makaha",
        "title": "Vinyl Pool Installation & Cleaning in Makaha, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Makaha, Waianae Coast Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Makaha",
        "hero_sub": "Makaha is where Oahu's wild west side meets the ocean — and pools here need a service team that knows the territory. Hawaii Pool Cleaners serves Makaha homeowners with full vinyl liner and maintenance services.",
        "intro_h": "West Side Pool Care Done Right",
        "intro_p": "Makaha's pools face the harshest UV conditions on Oahu, plus the red volcanic dust that blows off the inland cliffs and settles in pool water. Our service visits include thorough debris and sediment removal alongside standard chemical service.",
        "feat_p": "Getting a pool service company to come to Makaha regularly has historically been a challenge. We've built that route into our schedule because west side homeowners deserve consistent, reliable service — not excuses about distance.",
        "feat_bullets": ["Full vinyl liner installation and replacement","Sediment and dust removal from west-side pools","Regular chemical service and water balancing","Filter and pump repair","Free on-site quotes — no distance upcharge"],
        "cta_h2": "Makaha Pool Service — We're on the Route",
        "cta_p": "Call 808-864-3605 or request a free quote. Makaha is on our regular west side schedule.",
    },
    {
        "slug": "makakilo",
        "name": "Makakilo",
        "title": "Vinyl Pool Installation & Cleaning in Makakilo, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Makakilo, Kapolei area Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Makakilo",
        "hero_sub": "Perched on the hillside above Kapolei, Makakilo homes enjoy sweeping views and year-round swimming weather. Hawaii Pool Cleaners keeps Makakilo pools in top condition with liner work, cleaning, and maintenance.",
        "intro_h": "Hillside Pool Specialists — Makakilo",
        "intro_p": "Makakilo's elevation brings slightly more wind than the flats below, which means higher debris load and more evaporation in pool water. We account for this on every service visit, topping off chemical concentrations and clearing debris before it settles.",
        "feat_p": "Many Makakilo pools were built during the community's development boom and their liners are reaching end-of-life. We offer free assessments to tell you honestly where you stand — and a fair price when it's time for a new one.",
        "feat_bullets": ["Liner assessment and honest replacement recommendations","Full vinyl liner installation","Wind and debris management for hillside pools","Weekly maintenance and chemical balancing","Free on-site quotes"],
        "cta_h2": "Makakilo Pool Service — Request a Free Quote",
        "cta_p": "Call 808-864-3605 or submit a quote request. We serve Makakilo and all of the Kapolei area.",
    },
    {
        "slug": "manoa",
        "name": "Manoa",
        "title": "Vinyl Pool Installation & Cleaning in Manoa, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Manoa Valley, Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Manoa",
        "hero_sub": "Manoa Valley's lush canopy and frequent afternoon showers make pool maintenance a unique challenge. Hawaii Pool Cleaners delivers expert vinyl liner service and ongoing maintenance for Manoa homeowners.",
        "intro_h": "Pool Care in Manoa's Green Valley",
        "intro_p": "Manoa is one of Honolulu's rainiest neighborhoods, with afternoon showers almost daily in the wet season. That rainfall dilutes pool chemistry, adds organic matter, and feeds algae growth. Our Manoa maintenance plans are calibrated for this — more frequent water testing and proactive phosphate management.",
        "feat_p": "The tree canopy in Manoa is beautiful but hard on pools. Leaf litter, flower debris, and shading all affect water chemistry differently. We brush, skim, and vacuum thoroughly on every visit and adjust chemistry to match what the weather has done to your water.",
        "feat_bullets": ["Rain-adjusted chemical service for Manoa's wet climate","Organic debris management and pool brushing","Full vinyl liner replacement and repair","Filter maintenance and pump service","Free on-site quotes"],
        "cta_h2": "Manoa Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Manoa Valley and all of Honolulu.",
    },
    {
        "slug": "mililani",
        "name": "Mililani",
        "title": "Vinyl Pool Installation & Cleaning in Mililani, Hawaii | Hawaii Pool Cleaners",
        "desc": "Expert vinyl pool liner installation, repair, and pool cleaning in Mililani, central Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Mililani",
        "hero_sub": "Mililani is one of Oahu's most family-friendly planned communities, and its residential pools are in constant use. Hawaii Pool Cleaners keeps Mililani pools clean, safe, and properly maintained year-round.",
        "intro_h": "Mililani Pool Service — Central Oahu's Best",
        "intro_p": "Mililani's higher elevation brings cooler temperatures and more wind than coastal areas, which actually slows algae growth — but it also drives more debris into pools. Our maintenance visits always include thorough skimming and vacuuming alongside chemical service.",
        "feat_p": "Many Mililani pools are in that ten-to-fifteen-year range where the original liner is starting to show wear. A faded, stiff, or leaking liner is a sure sign it's time for a replacement. We offer free assessments and transparent pricing on all liner work.",
        "feat_bullets": ["Vinyl liner replacement for maturing Mililani pools","Family pool maintenance — safe water guaranteed","Weekly chemical and cleaning service","Filter and pump repair and maintenance","Free on-site assessments"],
        "cta_h2": "Mililani Pool Service — Get a Free Quote",
        "cta_p": "Call 808-864-3605 or request a free quote. We're in Mililani multiple times weekly.",
    },
    {
        "slug": "nanakuli",
        "name": "Nanakuli",
        "title": "Vinyl Pool Installation & Cleaning in Nanakuli, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Nanakuli, Waianae Coast Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Nanakuli",
        "hero_sub": "Nanakuli sits at the start of the Waianae coast where the sun is strong and pool liners take a beating. Hawaii Pool Cleaners brings professional vinyl liner service and maintenance to Nanakuli homeowners.",
        "intro_h": "West Side Vinyl Pool Service — Nanakuli",
        "intro_p": "Nanakuli's location at the gateway to the Waianae coast means intense UV exposure and dry, salt-laden air. Liners here fade and become brittle faster than the island average. We use UV-resistant materials on every west-side installation and factor the conditions into our chemical service plan.",
        "feat_p": "We're committed to serving the whole island — not just the easy routes. Nanakuli is on our west side schedule, and our clients here get the same quality and consistency as any Honolulu address.",
        "feat_bullets": ["UV-resistant liner installation for west side sun","Full liner replacement and repair","Chemical service for hot, dry conditions","Weekly maintenance and water testing","Free on-site quotes — no upcharge for west side"],
        "cta_h2": "Nanakuli Pool Service — We Serve the West Side",
        "cta_p": "Call 808-864-3605 or request a free quote. Nanakuli is on our regular route.",
    },
    {
        "slug": "pearl-city",
        "name": "Pearl City",
        "title": "Vinyl Pool Installation & Cleaning in Pearl City, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Pearl City, central Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Pearl City",
        "hero_sub": "Pearl City is central Oahu's hub — close to everything and home to thousands of residential pools. Hawaii Pool Cleaners has been servicing Pearl City pools for years and knows the area well.",
        "intro_h": "Pearl City Pool Specialists",
        "intro_p": "Pearl City's older and newer neighborhoods sit side by side, which means we service everything from classic fiberglass pools with vinyl overlays to brand-new shell construction. Our team adapts to what the pool needs, not a scripted service checklist.",
        "feat_p": "Pearl City sits right on the Pearl Harbor waterway, and the salt air from the harbor affects pools here differently than pools further inland. We test for mineral buildup and calcium hardness on every visit to keep your plumbing and liner in good shape.",
        "feat_bullets": ["Liner installation accounting for Pearl Harbor salt air","Calcium and mineral management","Weekly maintenance and chemical service","Filter and pump diagnostics","Free on-site quotes"],
        "cta_h2": "Pearl City Pool Service — Schedule Today",
        "cta_p": "Call 808-864-3605 or request a free quote. Pearl City is on our central Oahu route.",
    },
    {
        "slug": "pearl-harbor",
        "name": "Pearl Harbor",
        "title": "Vinyl Pool Installation & Cleaning near Pearl Harbor, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning for residential pools near Pearl Harbor, Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning near Pearl Harbor",
        "hero_sub": "The neighborhoods surrounding Pearl Harbor are home to thousands of residential and military housing pools. Hawaii Pool Cleaners serves all residential pool owners in the Pearl Harbor area.",
        "intro_h": "Pool Service for the Pearl Harbor Area",
        "intro_p": "Living near Pearl Harbor means your pool is exposed to the salt and mineral content of one of Oahu's largest estuaries. We test water chemistry with that in mind — calcium hardness, total dissolved solids, and alkalinity all require closer monitoring in this zone.",
        "feat_p": "We service residential properties throughout the Pearl Harbor corridor. If you're in military housing and manage your own pool maintenance, or in a neighboring civilian community, we can set up a regular service plan that works with your schedule.",
        "feat_bullets": ["Salt and mineral-aware chemical service","Full vinyl liner installation and repair","Weekly and bi-weekly maintenance plans","Equipment inspection and repair","Free on-site quotes"],
        "cta_h2": "Pearl Harbor Area Pool Service — Book Today",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve all residential properties in the Pearl Harbor area.",
    },
    {
        "slug": "waialua",
        "name": "Waialua",
        "title": "Vinyl Pool Installation & Cleaning in Waialua, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Waialua, North Shore Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Waialua",
        "hero_sub": "Waialua is North Shore Oahu at its most authentic — agricultural, coastal, and unhurried. Hawaii Pool Cleaners provides dependable vinyl liner service and pool maintenance for Waialua homeowners and property owners.",
        "intro_h": "North Shore Pool Care — Waialua",
        "intro_p": "Waialua's mix of old sugar plantation land, newer residential developments, and coastal properties means we service pools with very different histories. Whether it's a pool that's never had professional service or one that just needs a liner refresh, our team handles it.",
        "feat_p": "Waialua pools on agricultural plots often deal with high iron content in the water supply, which stains liners and equipment. We test for iron and manganese on first visits and recommend the right treatment to prevent permanent staining.",
        "feat_bullets": ["Iron and mineral treatment for agricultural-area pools","Full vinyl liner replacement and repair","Consistent weekly maintenance service","Chemical balancing for North Shore conditions","Free on-site quotes"],
        "cta_h2": "Waialua Pool Service — Request a Free Quote",
        "cta_p": "Call 808-864-3605 or submit a quote request. We serve Waialua and the entire North Shore.",
    },
    {
        "slug": "waianae",
        "name": "Waianae",
        "title": "Vinyl Pool Installation & Cleaning in Waianae, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Waianae, west Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Waianae",
        "hero_sub": "The Waianae coast has some of Oahu's most loyal communities — and homeowners here deserve pool service that actually shows up. Hawaii Pool Cleaners is committed to the west side with regular routes and no distance fees.",
        "intro_h": "West Side Pool Service — Waianae",
        "intro_p": "Waianae sits in the driest, sunniest microclimate on Oahu. Evaporation is high, UV is intense, and pool liners here age faster than anywhere else on the island. Our west-side service plans are specifically designed for these conditions — not copied from a Honolulu template.",
        "feat_p": "We've replaced dozens of liners on the Waianae coast and know what materials last in this climate. We'll never sell you a liner that can't handle the sun out here. Every Waianae installation gets UV-resistant material as standard.",
        "feat_bullets": ["UV-resistant liner materials — standard on west side","Full liner installation and replacement","Chemical service calibrated for Waianae heat","Weekly maintenance and water testing","Free on-site quotes — no west side surcharge"],
        "cta_h2": "Waianae Pool Service — We're on the West Side",
        "cta_p": "Call 808-864-3605 or request a free quote. Waianae is on our regular route.",
    },
    {
        "slug": "waikiki",
        "name": "Waikiki",
        "title": "Vinyl Pool Installation & Cleaning in Waikiki, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Waikiki, Honolulu. Hawaii Pool Cleaners — free quotes for condo and residential pools. Call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Waikiki",
        "hero_sub": "Waikiki's residential high-rises and private homes have pools that work overtime. Hawaii Pool Cleaners handles vinyl liner service and pool maintenance for Waikiki property owners and HOA managers.",
        "intro_h": "Pool Maintenance for Waikiki's Urban Properties",
        "intro_p": "Waikiki pools face unique demands: heavy use, saltwater proximity, urban pollution, and the expectations of residents and guests who take pool appearance seriously. Our maintenance visits are thorough, professional, and timed to minimize disruption.",
        "feat_p": "Saltwater from the nearby ocean and constant use accelerates liner wear in Waikiki. We inspect liners for early signs of delamination or seam failure on every maintenance visit, catching problems before they turn into emergencies.",
        "feat_bullets": ["Liner inspection on every maintenance visit","Saltwater-adjacent chemical management","High-traffic pool maintenance programs","Equipment inspection and repair","Free on-site quotes for HOA and residential pools"],
        "cta_h2": "Waikiki Pool Service — Schedule a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We handle residential and HOA pools in Waikiki.",
    },
    {
        "slug": "waimanalo",
        "name": "Waimanalo",
        "title": "Vinyl Pool Installation & Cleaning in Waimanalo, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Waimanalo, windward Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Waimanalo",
        "hero_sub": "Waimanalo's stunning beachside setting and lush windward valley make it one of Oahu's most special communities. Hawaii Pool Cleaners serves Waimanalo homeowners with full vinyl liner service and professional pool maintenance.",
        "intro_h": "Windward Pool Care in Waimanalo",
        "intro_p": "Waimanalo catches the full force of the tradewinds funneling through the Koolau gap, bringing debris, moisture, and organic material that challenges pool chemistry. We service Waimanalo pools with windward-tuned chemical protocols and thorough debris removal on every visit.",
        "feat_p": "Many Waimanalo properties are agricultural or estate-sized, with pools that can be harder to access. Our team comes equipped for any situation and knows how to work efficiently on large properties.",
        "feat_bullets": ["Windward-calibrated chemical service","Full vinyl liner replacement and repair","Debris and organic matter management","Equipment diagnostics and repair","Free on-site quotes"],
        "cta_h2": "Waimanalo Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. Waimanalo is on our regular windward route.",
    },
    {
        "slug": "waipahu",
        "name": "Waipahu",
        "title": "Vinyl Pool Installation & Cleaning in Waipahu, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Waipahu, central Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Waipahu",
        "hero_sub": "Waipahu is central Oahu's working-family community, and the pools here get serious use. Hawaii Pool Cleaners provides dependable vinyl liner service and pool maintenance for Waipahu homeowners.",
        "intro_h": "Waipahu Pool Specialists — Fair Prices, Quality Work",
        "intro_p": "Waipahu's central location and older housing stock mean many pools are mid-life or older. Liner replacements, equipment upgrades, and chemical rehabilitation are all common requests from our Waipahu clients. We handle all of it efficiently and at prices that make sense.",
        "feat_p": "Central Oahu's water supply has specific mineral characteristics that affect pool chemistry. We calibrate our chemical service for Waipahu's specific water profile, which means fewer chemical problems and longer liner life.",
        "feat_bullets": ["Liner replacement and restoration for aging pools","Water profile-adjusted chemical service","Weekly maintenance and cleaning","Filter and pump repair","Free on-site quotes"],
        "cta_h2": "Waipahu Pool Service — Get a Free Quote",
        "cta_p": "Call 808-864-3605 or request a free quote. Waipahu is on our central Oahu route.",
    },
    {
        "slug": "whitmore-village",
        "name": "Whitmore Village",
        "title": "Vinyl Pool Installation & Cleaning in Whitmore Village, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Whitmore Village, central Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Whitmore Village",
        "hero_sub": "Whitmore Village is one of central Oahu's most rural communities, tucked above Mililani in the pineapple fields. Hawaii Pool Cleaners provides full vinyl liner service and pool maintenance for Whitmore Village residents.",
        "intro_h": "Rural Central Oahu Pool Service",
        "intro_p": "Whitmore Village's elevation and agricultural surroundings bring unique challenges to pool maintenance — dust from nearby fields settles in pool water, and the higher altitude means stronger UV than sea-level communities. We factor all of this into our service approach.",
        "feat_p": "Getting reliable pool service to Whitmore Village has been a challenge for residents for years. We've built it into our route and show up consistently, on schedule, so you're not left chasing a service company.",
        "feat_bullets": ["UV-adjusted service for higher elevation","Dust and agricultural debris removal","Full vinyl liner installation and repair","Weekly maintenance and chemical balancing","Free on-site quotes"],
        "cta_h2": "Whitmore Village Pool Service — We Come to You",
        "cta_p": "Call 808-864-3605 or request a free quote. Whitmore Village is on our central Oahu schedule.",
    },
    {
        "slug": "ahuimanu",
        "name": "Ahuimanu",
        "title": "Vinyl Pool Installation & Cleaning in Ahuimanu, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Ahuimanu, windward Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Ahuimanu",
        "hero_sub": "Nestled in the Ko'olau foothills above Kaneohe, Ahuimanu is a quiet residential community where Hawaii Pool Cleaners provides reliable vinyl liner service and pool maintenance.",
        "intro_h": "Ko'olau Foothills Pool Specialists",
        "intro_p": "Ahuimanu's position in the Ko'olau foothills means pools here are shaded part of the day and exposed to the moisture coming off the mountains. Algae grows quickly in partially shaded pools with high humidity — we address this with a proactive chemical program tailored to windward conditions.",
        "feat_p": "Pools in the Ahuimanu area often collect heavy leaf debris from the surrounding trees. Our visits include thorough skimming and vacuuming alongside standard chemical service, keeping equipment from clogging.",
        "feat_bullets": ["Shaded pool algae prevention","Full vinyl liner replacement and repair","Debris management for wooded lots","Chemical balancing for windward conditions","Free on-site quotes"],
        "cta_h2": "Ahuimanu Pool Service — Schedule a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Ahuimanu and all of windward Oahu.",
    },
    {
        "slug": "aina-haina",
        "name": "Aina Haina",
        "title": "Vinyl Pool Installation & Cleaning in Aina Haina, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Aina Haina, East Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Aina Haina",
        "hero_sub": "Aina Haina is a beloved East Honolulu neighborhood with well-established homes and pools that have been part of the landscape for decades. Hawaii Pool Cleaners keeps Aina Haina pools clean, safe, and liner-fresh.",
        "intro_h": "East Honolulu Pool Service — Aina Haina",
        "intro_p": "Aina Haina sits in the transitional zone between city Honolulu and the greener eastern suburbs. Pools here often have mature landscaping nearby, which means more organic debris and more shading than pools in newer developments. We come prepared for that on every visit.",
        "feat_p": "Many Aina Haina pools are reaching the age where their original liners need replacement. The neighborhood's charming older homes often have pools that have served families for a generation — and a new liner can give them another.",
        "feat_bullets": ["Liner replacement for mature East Honolulu pools","Organic debris and shade management","Weekly maintenance and chemical service","Equipment inspection and repair","Free on-site quotes"],
        "cta_h2": "Aina Haina Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Aina Haina and all of East Honolulu.",
    },
    {
        "slug": "ala-moana",
        "name": "Ala Moana",
        "title": "Vinyl Pool Installation & Cleaning near Ala Moana, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning for residential and condo pools near Ala Moana, Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning near Ala Moana",
        "hero_sub": "The Ala Moana corridor is one of Honolulu's most densely developed areas, with high-rise residences and town homes that have private pool facilities. Hawaii Pool Cleaners services condo and residential pools throughout the Ala Moana area.",
        "intro_h": "Urban Pool Maintenance — Ala Moana",
        "intro_p": "Urban pool environments near Ala Moana deal with saltwater proximity from the canal and ocean, high foot traffic in condo pools, and the shade and humidity that come with dense high-rise development. Our service program is calibrated for exactly these conditions.",
        "feat_p": "HOA and condo property managers in the Ala Moana area rely on us for consistent, professional service that meets their property standards. We document every visit and make it easy to track pool condition over time.",
        "feat_bullets": ["HOA and condo pool maintenance programs","Salt-air chemical management for ocean proximity","High-traffic pool maintenance","Vinyl liner inspection and repair","Free quotes for property managers and homeowners"],
        "cta_h2": "Ala Moana Area Pool Service — Request a Quote",
        "cta_p": "Call 808-864-3605 or submit a quote request. We handle condo and residential pools near Ala Moana.",
    },
    {
        "slug": "aliamanu",
        "name": "Aliamanu",
        "title": "Vinyl Pool Installation & Cleaning in Aliamanu, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Aliamanu, Salt Lake area Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Aliamanu",
        "hero_sub": "Aliamanu's hillside community above Salt Lake offers some of the best views on Oahu — and homeowners here want their pools to match. Hawaii Pool Cleaners provides professional vinyl liner service and maintenance for Aliamanu.",
        "intro_h": "Hillside Pool Specialists — Aliamanu",
        "intro_p": "Aliamanu's mix of military housing and civilian residences means we service a wide range of pool configurations here. Military housing pools tend to be well-maintained but benefit from professional chemical service; civilian pools vary more widely in condition and age.",
        "feat_p": "The hillside location brings consistent tradewind exposure to Aliamanu pools — which is actually good for air circulation but means more airborne debris in the water. We skim and vacuum thoroughly on every visit.",
        "feat_bullets": ["Vinyl liner installation and replacement","Military and civilian residential pool service","Tradewind debris management","Chemical balancing and water testing","Free on-site quotes"],
        "cta_h2": "Aliamanu Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Aliamanu, Salt Lake, and the surrounding area.",
    },
    {
        "slug": "campbell-industrial-park",
        "name": "Campbell Industrial Park",
        "title": "Vinyl Pool Installation & Cleaning near Campbell Industrial Park, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning for residential pools near Campbell Industrial Park, Kapolei Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning near Campbell Industrial Park",
        "hero_sub": "Residential communities near Campbell Industrial Park and the Kapolei waterfront have growing pools that need professional care. Hawaii Pool Cleaners serves this area with full vinyl liner and maintenance services.",
        "intro_h": "Kapolei Waterfront Pool Service",
        "intro_p": "The residential areas near Campbell Industrial Park sit close to Oahu's leeward coast and the working waterfront. Salt air, industrial particulates, and the intense west-side sun create a demanding environment for pool liners and equipment. Our team knows this stretch of coast well.",
        "feat_p": "We use marine-grade liner materials on installs near the waterfront where salt air concentration is highest. The extra investment in material quality pays off in years of additional liner life.",
        "feat_bullets": ["Marine-grade liner materials for waterfront proximity","Salt and particulate chemical management","Full vinyl liner installation and repair","Weekly maintenance service","Free on-site quotes"],
        "cta_h2": "Campbell Industrial Park Area Pool Service",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve the Kapolei waterfront corridor.",
    },
    {
        "slug": "downtown-honolulu",
        "name": "Downtown Honolulu",
        "title": "Vinyl Pool Installation & Cleaning in Downtown Honolulu, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning for residential and condo pools in Downtown Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Downtown Honolulu",
        "hero_sub": "Downtown Honolulu's residential properties and upscale condominiums have private pools that demand professional attention. Hawaii Pool Cleaners provides white-glove vinyl liner service and pool maintenance in the heart of the city.",
        "intro_h": "Downtown Honolulu Pool Service",
        "intro_p": "Downtown Honolulu pools exist in a unique urban environment — surrounded by concrete and glass, exposed to salt air from the harbor, and maintained to the high standards of the city's most prominent properties. Our team operates professionally and discreetly in any setting.",
        "feat_p": "Harbor salt air and urban pollution accelerate liner degradation in downtown pools. We inspect liners thoroughly on every maintenance visit and address minor issues before they become major ones.",
        "feat_bullets": ["Urban pool maintenance with minimal disruption","Harbor salt-air chemical management","Vinyl liner inspection and repair","HOA and residential property service","Free on-site quotes"],
        "cta_h2": "Downtown Honolulu Pool Service — Schedule Today",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Downtown Honolulu and all of urban Honolulu.",
    },
    {
        "slug": "enchanted-lake",
        "name": "Enchanted Lake",
        "title": "Vinyl Pool Installation & Cleaning in Enchanted Lake, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Enchanted Lake, Kailua windward Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Enchanted Lake",
        "hero_sub": "Enchanted Lake is one of Kailua's most desirable neighborhoods, with beautiful homes along the lake that often feature private pools. Hawaii Pool Cleaners provides expert vinyl liner service and maintenance for Enchanted Lake homeowners.",
        "intro_h": "Lakeside Pool Specialists — Enchanted Lake",
        "intro_p": "Lakeside pools in Enchanted Lake deal with unique water chemistry influences — moisture from the lake, waterfowl activity, and the lush windward vegetation all contribute to elevated phosphates and organic load in pool water. We manage this proactively so your pool stays clear.",
        "feat_p": "The Enchanted Lake community has some of Kailua's most beautiful pools. We treat this neighborhood accordingly — careful, professional service that keeps everything looking as good as the surroundings.",
        "feat_bullets": ["Phosphate management for lakeside pool environments","Full vinyl liner replacement and repair","Proactive algae prevention","Weekly maintenance and chemical service","Free on-site quotes"],
        "cta_h2": "Enchanted Lake Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. Enchanted Lake is on our regular Kailua route.",
    },
    {
        "slug": "hawaii-kai",
        "name": "Hawaii Kai",
        "title": "Vinyl Pool Installation & Cleaning in Hawaii Kai, Hawaii | Hawaii Pool Cleaners",
        "desc": "Expert vinyl pool liner installation, repair, and pool cleaning in Hawaii Kai, East Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Hawaii Kai",
        "hero_sub": "Hawaii Kai's marina community and upscale estates feature some of Oahu's finest private pools. Hawaii Pool Cleaners delivers premium vinyl liner service and professional maintenance that matches Hawaii Kai's high standards.",
        "intro_h": "Hawaii Kai's Pool Service Specialists",
        "intro_p": "Hawaii Kai's waterfront properties and hillside estates have demanding pools — large surface areas, custom shapes, and the salt air that comes with marina living. Our team is experienced with Hawaii Kai's range of pool configurations and the water chemistry challenges specific to this area.",
        "feat_p": "Marina proximity means elevated salt and mineral content in the air, which accelerates liner wear and stains equipment. We test for this on every visit and apply the right preventive treatments to keep your pool looking pristine.",
        "feat_bullets": ["Marine-environment liner materials for marina proximity","Estate and custom pool maintenance","Mineral and stain prevention treatments","Full vinyl liner installation and repair","Free on-site consultations"],
        "cta_h2": "Hawaii Kai Pool Service — Request a Consultation",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Hawaii Kai and all of East Honolulu.",
    },
    {
        "slug": "hickam-housing",
        "name": "Hickam Housing",
        "title": "Vinyl Pool Installation & Cleaning in Hickam Housing, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning for residential pools in Hickam Housing, Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Hickam Housing",
        "hero_sub": "Hickam Housing offers military families some of Oahu's most well-kept residential communities. Hawaii Pool Cleaners provides professional vinyl liner service and pool maintenance for Hickam residential pool owners.",
        "intro_h": "Pool Service for Hickam Residential Communities",
        "intro_p": "Hickam's coastal location means pools here face salt air from Pearl Harbor and the nearby shoreline. The housing community's standards are high, and our service is designed to meet them — professional, thorough, and always on schedule.",
        "feat_p": "Military families rotating through Hickam often inherit pools that haven't been professionally serviced. We offer a comprehensive first-visit assessment that covers water chemistry, liner condition, and equipment status so you know exactly what you're working with.",
        "feat_bullets": ["Comprehensive pool assessment for new residents","Vinyl liner inspection, repair, and replacement","Salt-air chemical management","Consistent weekly maintenance","Free on-site quotes"],
        "cta_h2": "Hickam Housing Pool Service — Schedule a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Hickam Housing and surrounding military communities.",
    },
    {
        "slug": "iroquois-point",
        "name": "Iroquois Point",
        "title": "Vinyl Pool Installation & Cleaning in Iroquois Point, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning for residential pools in Iroquois Point, Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Iroquois Point",
        "hero_sub": "Iroquois Point is one of Oahu's most scenic military residential communities, jutting into Pearl Harbor. Hawaii Pool Cleaners provides expert vinyl liner service and pool maintenance for Iroquois Point homeowners.",
        "intro_h": "Pearl Harbor Peninsula Pool Service",
        "intro_p": "Sitting at the tip of a peninsula surrounded by Pearl Harbor, Iroquois Point pools deal with maximum salt and mineral exposure. The water chemistry here is among the most demanding on the island — and we've developed a specific protocol for it over years of servicing this community.",
        "feat_p": "Our Pearl Harbor peninsula protocol includes extra mineral sequestrant treatment, more frequent pH adjustments, and a closer eye on liner seams where salt intrusion is most likely to cause early failure.",
        "feat_bullets": ["Pearl Harbor peninsula chemical protocol","Salt and mineral sequestrant treatment","Vinyl liner inspection, repair, and replacement","Regular weekly maintenance service","Free on-site quotes"],
        "cta_h2": "Iroquois Point Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We regularly serve Iroquois Point.",
    },
    {
        "slug": "kaimuki",
        "name": "Kaimuki",
        "title": "Vinyl Pool Installation & Cleaning in Kaimuki, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Kaimuki, East Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Kaimuki",
        "hero_sub": "Kaimuki is one of Honolulu's most beloved urban neighborhoods, full of character homes and lush yards — many with private pools. Hawaii Pool Cleaners handles vinyl liner work and pool maintenance throughout Kaimuki.",
        "intro_h": "Kaimuki Pool Service — East Honolulu Character",
        "intro_p": "Kaimuki's elevated neighborhood has some of the most mature landscaping in Honolulu, which means pools here collect significant organic debris. Bougainvillea, plumeria, and mango trees all shed material that drives up phosphates and clogs filters. We come prepared for the extra work.",
        "feat_p": "Many Kaimuki pools were built in the mid-century era when the neighborhood was developing. Liners from that era have long since been replaced once or twice, but many are due again. We inspect and give you a straight assessment.",
        "feat_bullets": ["Organic debris and phosphate management","Full vinyl liner replacement and repair","Filter cleaning and pump service","Weekly maintenance for established neighborhoods","Free on-site pool assessments"],
        "cta_h2": "Kaimuki Pool Service — Schedule Today",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Kaimuki and all of East Honolulu.",
    },
    {
        "slug": "kakaako",
        "name": "Kakaako",
        "title": "Vinyl Pool Installation & Cleaning in Kakaako, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool maintenance for condo and residential pools in Kakaako, Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Kakaako",
        "hero_sub": "Kakaako's sleek new towers and creative district bring a modern urban energy to Honolulu's waterfront. Hawaii Pool Cleaners maintains condo and residential pools in Kakaako with the same professional polish the neighborhood demands.",
        "intro_h": "Kakaako Condo Pool Specialists",
        "intro_p": "Kakaako's new development boom has brought hundreds of condo pools online in recent years. These pools are often high-visibility — open to residents and guests — which means appearance and water quality are non-negotiable. We understand what property managers and HOAs expect and consistently deliver it.",
        "feat_p": "Urban pools in Kakaako deal with salt air from the nearby ocean, particulate dust from ongoing nearby construction, and high turnover from condo guests and residents. Our maintenance schedule keeps up with all of it.",
        "feat_bullets": ["HOA and condo pool maintenance programs","Construction dust and salt air management","Vinyl liner inspection and repair","High-traffic pool chemical balancing","Free quotes for property managers and owners"],
        "cta_h2": "Kakaako Pool Service — Request a Quote",
        "cta_p": "Call 808-864-3605 or submit a quote request. We service condo and residential pools in Kakaako.",
    },
    {
        "slug": "kaneohe-bay",
        "name": "Kaneohe Bay",
        "title": "Vinyl Pool Installation & Cleaning near Kaneohe Bay, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning for properties near Kaneohe Bay, windward Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning near Kaneohe Bay",
        "hero_sub": "Properties along Kaneohe Bay enjoy spectacular views and unique microclimatic conditions. Hawaii Pool Cleaners provides expert vinyl liner service and pool maintenance for homeowners along the bay.",
        "intro_h": "Bay-Adjacent Pool Specialists",
        "intro_p": "Homes bordering Kaneohe Bay deal with salt spray, high humidity, and the biological load that comes with living next to a productive reef ecosystem. Pool water near the bay tends to have elevated mineral content and benefits from more frequent testing and adjustment.",
        "feat_p": "Bay-adjacent liners are exposed to more salt intrusion and UV reflection off the water than inland pools. We specify liner materials with enhanced UV and salt resistance for all Kaneohe Bay area installations.",
        "feat_bullets": ["Salt-resistant liner materials for bay properties","Bay-specific water chemistry management","Full vinyl liner replacement and repair","Weekly maintenance service","Free on-site quotes"],
        "cta_h2": "Kaneohe Bay Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve all properties along Kaneohe Bay.",
    },
    {
        "slug": "kapahulu",
        "name": "Kapahulu",
        "title": "Vinyl Pool Installation & Cleaning in Kapahulu, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Kapahulu, Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Kapahulu",
        "hero_sub": "Kapahulu connects Waikiki to the rest of Honolulu — a neighborhood with real character, loyal residents, and pools that serve hardworking families year-round. Hawaii Pool Cleaners provides dependable vinyl liner and maintenance service in Kapahulu.",
        "intro_h": "Kapahulu Pool Service — Central Honolulu",
        "intro_p": "Kapahulu's compact lots and mature tree cover mean pools here deal with constant debris from overhanging vegetation. We skim, brush, and vacuum thoroughly on every visit and keep filters clean so your pump isn't fighting a losing battle.",
        "feat_p": "Kapahulu pools benefit from the same professional care as anywhere else on the island. We don't scale back on service quality for urban neighborhoods — every pool gets the same thorough attention.",
        "feat_bullets": ["Thorough debris management for treed lots","Full vinyl liner installation and repair","Weekly maintenance and chemical service","Filter and pump maintenance","Free on-site quotes"],
        "cta_h2": "Kapahulu Pool Service — Schedule Today",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Kapahulu and all of central Honolulu.",
    },
    {
        "slug": "lanikai",
        "name": "Lanikai",
        "title": "Vinyl Pool Installation & Cleaning in Lanikai, Hawaii | Hawaii Pool Cleaners",
        "desc": "Premium vinyl pool liner installation, repair, and pool cleaning in Lanikai, Kailua Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Lanikai",
        "hero_sub": "Lanikai is consistently ranked among the world's most beautiful places — and the homes and pools here reflect that. Hawaii Pool Cleaners delivers premium vinyl liner service and meticulous maintenance for Lanikai properties.",
        "intro_h": "World-Class Pool Care for Lanikai",
        "intro_p": "Lanikai's oceanfront and beachside properties sit directly in the path of the tradewinds and salt spray from the Pacific. Pool liners here face aggressive conditions that demand high-quality materials and more frequent monitoring than inland pools.",
        "feat_p": "We install only UV-resistant, salt-tolerant liner materials in Lanikai. The extra cost of premium material is minimal compared to the cost of an early failure at one of Oahu's most desirable addresses.",
        "feat_bullets": ["Premium UV and salt-resistant liner materials","Oceanfront pool maintenance protocols","Meticulous service for high-value properties","Full vinyl liner installation and repair","Free on-site consultations"],
        "cta_h2": "Lanikai Pool Service — Schedule a Consultation",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Lanikai and all of the Kailua coast.",
    },
    {
        "slug": "mccully",
        "name": "McCully",
        "title": "Vinyl Pool Installation & Cleaning in McCully, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in McCully, Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in McCully",
        "hero_sub": "McCully is one of Honolulu's most central urban neighborhoods, just mauka of the Ala Wai. Hawaii Pool Cleaners provides professional vinyl liner service and pool maintenance for McCully's residential and condo properties.",
        "intro_h": "Central Honolulu Pool Service — McCully",
        "intro_p": "McCully pools sit close to the Ala Wai Canal, which means salt air and humidity are ever-present. Urban pools in this area also deal with construction dust and heavy pedestrian use in condo settings. Our chemical program accounts for all of these inputs.",
        "feat_p": "We service both private residential pools and condo building pools in McCully. Our team is accustomed to working in tight urban spaces and fitting pool service into the rhythm of busy city buildings.",
        "feat_bullets": ["Urban pool maintenance with minimal footprint","Canal salt-air chemical management","Vinyl liner inspection and repair","Condo and HOA pool programs","Free on-site quotes"],
        "cta_h2": "McCully Pool Service — Request a Quote",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve McCully and all of central Honolulu.",
    },
    {
        "slug": "moanalua",
        "name": "Moanalua",
        "title": "Vinyl Pool Installation & Cleaning in Moanalua, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Moanalua, Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Moanalua",
        "hero_sub": "Moanalua Valley and its surrounding neighborhoods have some of Oahu's most spacious residential properties. Hawaii Pool Cleaners provides vinyl liner installation, pool repair, and maintenance throughout Moanalua.",
        "intro_h": "Moanalua Valley Pool Specialists",
        "intro_p": "Moanalua's valley setting means cooler temperatures and more shade than coastal Oahu, which affects pool chemistry. Shaded pools grow algae faster and need more consistent brushing and phosphate management. We build this into our Moanalua service approach.",
        "feat_p": "The valley setting also means more organic debris from the surrounding vegetation. Our service visits include thorough skimming and vacuuming alongside chemical service — not just a quick chemical dump.",
        "feat_bullets": ["Shaded pool algae prevention and phosphate management","Full vinyl liner replacement and repair","Debris management for valley properties","Weekly maintenance and chemical balancing","Free on-site quotes"],
        "cta_h2": "Moanalua Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Moanalua and all of greater Honolulu.",
    },
    {
        "slug": "niu-valley",
        "name": "Niu Valley",
        "title": "Vinyl Pool Installation & Cleaning in Niu Valley, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Niu Valley, East Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Niu Valley",
        "hero_sub": "Niu Valley is a quiet, established East Honolulu community where families have been swimming in backyard pools for decades. Hawaii Pool Cleaners keeps Niu Valley pools clean, safe, and properly maintained year-round.",
        "intro_h": "East Honolulu Pool Service — Niu Valley",
        "intro_p": "Niu Valley's hillside location and lush vegetation create some of East Oahu's most beautiful pool settings — and some of its most organic-heavy water. Mature trees shed leaves, flowers, and seed pods that keep pool filters working hard. We come to every visit ready to deal with that.",
        "feat_p": "Niu Valley pools often date from the community's original development, and many original liners have been replaced at least once. If yours is showing signs of wear — fading, bubbling, rough texture — it's time for an assessment.",
        "feat_bullets": ["Liner assessment for aging East Honolulu pools","Debris and organic matter management","Full vinyl liner replacement and repair","Weekly maintenance and chemical service","Free on-site quotes"],
        "cta_h2": "Niu Valley Pool Service — Schedule a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Niu Valley and all of East Honolulu.",
    },
    {
        "slug": "palolo",
        "name": "Palolo",
        "title": "Vinyl Pool Installation & Cleaning in Palolo, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Palolo Valley, Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Palolo",
        "hero_sub": "Palolo Valley is one of Honolulu's greenest communities, tucked between the Ko'olau foothills and the city. Hawaii Pool Cleaners provides vinyl liner service and pool maintenance for Palolo homeowners.",
        "intro_h": "Valley Pool Care in Palolo",
        "intro_p": "Palolo Valley gets some of the heaviest rainfall of any Honolulu neighborhood. Pools here can experience significant chemistry dilution after a hard rain — alkalinity drops, pH shifts, and algae can take hold quickly if chemistry isn't adjusted promptly. We check in after major rain events and adjust accordingly.",
        "feat_p": "The valley walls channel debris into Palolo pools during heavy rains. Our visits always include vacuuming of sediment that settles after rainfall, keeping your filter and liner in good condition.",
        "feat_bullets": ["Post-rain chemical adjustment service","Sediment and debris management","Full vinyl liner replacement and repair","Weekly maintenance and water testing","Free on-site quotes"],
        "cta_h2": "Palolo Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Palolo Valley and all of greater Honolulu.",
    },
    {
        "slug": "punchbowl",
        "name": "Punchbowl",
        "title": "Vinyl Pool Installation & Cleaning in Punchbowl, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in the Punchbowl area, Honolulu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Punchbowl",
        "hero_sub": "The Punchbowl neighborhood sits at the edge of the ancient volcanic crater above downtown Honolulu. Homes here have great views, established yards, and pools that Hawaii Pool Cleaners keeps in excellent condition.",
        "intro_h": "Punchbowl Area Pool Service",
        "intro_p": "Punchbowl's elevation and location on the rim of the crater bring consistent tradewind exposure and a mix of sun and shadow throughout the day. Pools here benefit from a service approach that accounts for the variable light conditions and the debris that blows in off the hillside.",
        "feat_p": "Many Punchbowl homes are older Honolulu properties with established pools. We offer honest liner assessments for older installations and fair pricing on replacements when the time comes.",
        "feat_bullets": ["Liner assessment and replacement for older Honolulu homes","Variable-exposure chemical management","Weekly maintenance and debris management","Filter and pump repair","Free on-site quotes"],
        "cta_h2": "Punchbowl Pool Service — Schedule a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve the Punchbowl area and all of Honolulu.",
    },
    {
        "slug": "salt-lake",
        "name": "Salt Lake",
        "title": "Vinyl Pool Installation & Cleaning in Salt Lake, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning in Salt Lake, Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning in Salt Lake",
        "hero_sub": "Salt Lake is one of Oahu's established mid-island communities with a mix of residential homes and condo developments. Hawaii Pool Cleaners provides professional vinyl liner service and pool maintenance throughout Salt Lake.",
        "intro_h": "Salt Lake Pool Specialists",
        "intro_p": "Salt Lake sits between Pearl Harbor and the Honolulu hillsides, exposed to the salt air that moves inland from the harbor. Pool liners in this area experience elevated salt stress — we account for that in our chemical service and in our liner material recommendations.",
        "feat_p": "Salt Lake's housing mix means we service everything from single-family backyard pools to condo building amenities. We adapt our service approach to the setting without compromising on quality or thoroughness.",
        "feat_bullets": ["Harbor salt-air chemical management","Vinyl liner installation rated for coastal proximity","HOA and residential pool programs","Weekly maintenance and chemical service","Free on-site quotes"],
        "cta_h2": "Salt Lake Pool Service — Request a Quote",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Salt Lake and all of mid-island Oahu.",
    },
    {
        "slug": "schofield-barracks",
        "name": "Schofield Barracks",
        "title": "Vinyl Pool Installation & Cleaning near Schofield Barracks, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning for residential pools near Schofield Barracks, central Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning near Schofield Barracks",
        "hero_sub": "The residential communities surrounding Schofield Barracks in central Oahu are home to thousands of military and civilian families with pools. Hawaii Pool Cleaners provides reliable vinyl liner service and maintenance for this community.",
        "intro_h": "Central Oahu Military Community Pool Service",
        "intro_p": "Schofield's central Oahu location at higher elevation brings cooler temperatures, more frequent rainfall than the coasts, and strong tradewinds that deposit debris in pools. Our central Oahu service route covers Schofield regularly with the same consistency our clients expect anywhere on the island.",
        "feat_p": "Military families rotating through Schofield benefit from our comprehensive pool assessments on arrival — we document current liner condition, equipment status, and water chemistry so you inherit a clear picture of your pool's health.",
        "feat_bullets": ["Arrival pool assessment for rotating military families","Full vinyl liner inspection and replacement","Central Oahu rain-adjusted chemical service","Weekly maintenance plans","Free on-site quotes"],
        "cta_h2": "Schofield Area Pool Service — Book a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve Schofield Barracks and central Oahu.",
    },
    {
        "slug": "tripler-army-medical-center",
        "name": "Tripler Army Medical Center",
        "title": "Vinyl Pool Installation & Cleaning near Tripler, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning for residential pools near Tripler Army Medical Center, Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning near Tripler Army Medical Center",
        "hero_sub": "The residential neighborhoods surrounding Tripler Army Medical Center have active military and civilian families who need reliable pool service. Hawaii Pool Cleaners serves this community with professional vinyl liner work and maintenance.",
        "intro_h": "Pool Service for the Tripler Area",
        "intro_p": "The Tripler area sits on the hillside above Pearl Harbor, with commanding views and pools that face salt air from below and tradewind debris from above. It's a dual challenge — mineral buildup from the salt and organic debris from the hillside vegetation — and we handle both on every service visit.",
        "feat_p": "We offer priority scheduling for medical staff and military personnel with demanding and irregular schedules. Tell us your constraints and we'll build a service plan that works around them.",
        "feat_bullets": ["Flexible scheduling for medical and military personnel","Salt and mineral management for hillside pools","Vinyl liner inspection and repair","Weekly maintenance and chemical service","Free on-site quotes"],
        "cta_h2": "Tripler Area Pool Service — Schedule a Visit",
        "cta_p": "Call 808-864-3605 or request a free quote. We serve the Tripler area and all of Oahu.",
    },
    {
        "slug": "wheeler-army-airfield",
        "name": "Wheeler Army Airfield",
        "title": "Vinyl Pool Installation & Cleaning near Wheeler Army Airfield, Hawaii | Hawaii Pool Cleaners",
        "desc": "Vinyl liner installation, repair, and pool cleaning for residential pools near Wheeler Army Airfield, central Oahu. Hawaii Pool Cleaners — free quotes, call 808-864-3605.",
        "h1": "Vinyl Pool Installation & Cleaning near Wheeler Army Airfield",
        "hero_sub": "Wheeler's central Oahu location puts residential pools in a unique microclimate — higher elevation, more rainfall, and tradewind exposure. Hawaii Pool Cleaners provides dependable vinyl liner service and pool maintenance for Wheeler-area homeowners.",
        "intro_h": "Wheeler Area Pool Service — Central Oahu",
        "intro_p": "The Wheeler area gets more rainfall than coastal Oahu and is exposed to strong tradewinds that cross the central plain. Pools here dilute quickly in the rainy season, and the open exposure means more airborne debris than sheltered coastal neighborhoods. We adjust our service to match.",
        "feat_p": "Wheeler-area families benefit from a reliable, on-schedule service team. We don't cancel or reschedule on short notice — when you book a maintenance day, we show up.",
        "feat_bullets": ["Rain-adjusted chemical service for central Oahu","Wind and debris management for open-exposure pools","Full vinyl liner installation and repair","Consistent weekly maintenance schedule","Free on-site quotes"],
        "cta_h2": "Wheeler Area Pool Service — Book Today",
        "cta_p": "Call 808-864-3605 or request a free quote. Wheeler is on our regular central Oahu route.",
    },
]

NAV_HTML = '''<nav class="nav">
  <a href="/" class="nav-logo">
    <img src="/img/beaudoins-hawaii-pool-cleaners-logo.png" alt="Hawaii Pool Cleaners">
    <div class="nav-logo-text">Hawaii Pool Cleaners<span>Island Pool Experts</span></div>
  </a>
  <ul class="nav-links">
    <li><a href="/">Home</a></li>
    <li><a href="/about/">About</a></li>
    <li><a href="/offerings/">Offerings</a></li>
    <li><a href="/blog/">Blog</a></li>
    <li><a href="/contact/" class="nav-cta">Free Liner Quote</a></li>
  </ul>
  <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="nav-mobile" id="navMobile" aria-hidden="true">
  <ul class="nav-mobile-links">
    <li><a href="/">Home</a></li>
    <li><a href="/about/">About</a></li>
    <li><a href="/offerings/">Offerings</a></li>
    <li><a href="/blog/">Blog</a></li>
  </ul>
  <a href="/contact/" class="mobile-cta-btn">Free Liner Quote</a>
</div>'''

FOOTER_HTML = '''<footer>
  <div class="footer-inner">
    <div class="footer-brand">
      <img src="/img/beaudoins-hawaii-pool-cleaners-logo.png" alt="Hawaii Pool Cleaners">
      <div class="footer-brand-name">Hawaii Pool Cleaners</div>
      <p class="footer-brand-desc">Hawaii's vinyl pool liner specialists. Expert installation, repair, and pool maintenance across Oahu.</p>
    </div>
    <div>
      <div class="footer-col-title">Navigation</div>
      <ul class="footer-links">
        <li><a href="/">Home</a></li>
        <li><a href="/about/">About</a></li>
        <li><a href="/offerings/">Offerings</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-col-title">Services</div>
      <ul class="footer-links">
        <li><a href="/offerings/">Vinyl Liner Installation</a></li>
        <li><a href="/offerings/">Vinyl Liner Repair</a></li>
        <li><a href="/offerings/">Pool Repair &amp; Restoration</a></li>
        <li><a href="/offerings/">Pool Cleaning &amp; Maintenance</a></li>
        <li><a href="/faqs/">FAQs</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p class="footer-copy">&copy; 2026 Hawaii Pool Cleaners. All rights reserved.</p>
    <div class="footer-line"></div>
  </div>
</footer>'''

CSS = ''':root{--teal:#00D082;--navy:#0a1628;--mid:#1a3a5c;--lteal:#7adcb4;--white:#ffffff;--lgray:#f8fafc;--muted:#4a6080;--shadow:0 8px 40px rgba(0,0,0,.12)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;font-size:16px}
body{font-family:'Libre Franklin',sans-serif;font-weight:400;line-height:1.65;color:var(--navy);background:var(--white);overflow-x:hidden;cursor:default}
a,button{cursor:pointer}
.nav{position:fixed;top:0;left:0;right:0;z-index:1000;padding:20px 48px;display:flex;align-items:center;justify-content:space-between;transition:all .4s ease;background:rgba(10,22,40,.92);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border-bottom:1px solid rgba(0,208,130,.12)}
.nav-logo{display:flex;align-items:center;gap:12px;text-decoration:none}
.nav-logo img{height:52px;width:52px;object-fit:contain;border-radius:4px}
.nav-logo-text{font-size:1rem;font-weight:700;color:#fff;line-height:1.2;letter-spacing:-.02em}
.nav-logo-text span{display:block;font-size:.62rem;font-weight:400;color:var(--lteal);letter-spacing:.14em;text-transform:uppercase}
.nav-links{display:flex;align-items:center;gap:32px;list-style:none}
.nav-links a{color:rgba(255,255,255,.82);text-decoration:none;font-size:.82rem;font-weight:500;letter-spacing:.06em;text-transform:uppercase;position:relative;transition:color .3s}
.nav-links a::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:var(--teal);transition:width .3s}
.nav-links a:hover{color:var(--teal)}
.nav-links a:hover::after{width:100%}
.nav-cta{background:var(--teal)!important;color:var(--navy)!important;padding:10px 26px!important;border-radius:50px!important;font-weight:700!important;transition:background .3s,transform .3s,box-shadow .3s!important}
.nav-cta::after{display:none!important}
.nav-cta:hover{background:var(--lteal)!important;transform:translateY(-2px)!important;box-shadow:0 8px 24px rgba(0,208,130,.4)!important}
.page-hero{padding:140px 40px 90px;background:linear-gradient(135deg,var(--navy) 0%,#0d2245 60%,#0e2a1e 100%);text-align:center;position:relative;overflow:hidden}
.page-hero::before{content:'';position:absolute;top:-80px;right:-80px;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(0,208,130,.07),transparent 70%);pointer-events:none}
.eyebrow{font-size:.7rem;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--teal);margin-bottom:14px;display:block}
.page-hero h1{font-size:clamp(2rem,4vw,3.2rem);font-weight:800;color:#fff;letter-spacing:-.035em;line-height:1.1;margin-bottom:18px}
.page-hero p{font-size:1.05rem;color:rgba(255,255,255,.62);max-width:560px;margin:0 auto;line-height:1.8}
.featured-section{padding:100px 40px;background:#fff}
.featured-inner{max-width:1200px;margin:0 auto}
.featured-hd{margin-bottom:56px}
.featured-hd h2{font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;color:var(--navy);line-height:1.12;letter-spacing:-.03em;margin-bottom:14px}
.featured-hd p{font-size:1rem;color:var(--muted);max-width:600px;line-height:1.76}
.featured-card{display:grid;grid-template-columns:1fr 1fr;border-radius:24px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.14)}
.featured-img{width:100%;height:100%;min-height:420px;object-fit:cover;display:block;transition:transform .6s ease}
.featured-card:hover .featured-img{transform:scale(1.04)}
.featured-img-wrap{overflow:hidden}
.featured-body{background:var(--navy);padding:56px 52px;display:flex;flex-direction:column;justify-content:center}
.featured-tag{font-size:.65rem;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--teal);margin-bottom:12px;display:block}
.featured-body h3{font-size:clamp(1.4rem,2.5vw,2rem);font-weight:800;color:#fff;line-height:1.15;letter-spacing:-.03em;margin-bottom:20px}
.featured-body p{font-size:.95rem;color:rgba(255,255,255,.6);line-height:1.78;margin-bottom:32px}
.featured-benefits{list-style:none;display:flex;flex-direction:column;gap:12px;margin-bottom:36px}
.featured-benefits li{display:flex;align-items:center;gap:12px;font-size:.88rem;color:rgba(255,255,255,.72)}
.featured-benefits li::before{content:'';width:8px;height:8px;border-radius:50%;background:var(--teal);flex-shrink:0}
.btn-teal{display:inline-block;background:var(--teal);color:var(--navy);text-decoration:none;font-weight:800;font-size:.82rem;letter-spacing:.1em;text-transform:uppercase;padding:15px 40px;border-radius:50px;transition:background .3s,box-shadow .3s,transform .3s}
.btn-teal:hover{background:var(--lteal);box-shadow:0 12px 36px rgba(0,208,130,.4);transform:translateY(-2px)}
.services-section{padding:100px 40px;background:var(--lgray)}
.services-hd{text-align:center;margin-bottom:64px}
.services-hd h2{font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;color:var(--navy);line-height:1.12;letter-spacing:-.03em;margin-bottom:14px}
.services-hd p{font-size:1rem;color:var(--muted);max-width:540px;margin:0 auto;line-height:1.76}
.services-grid{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.svc-card{background:#fff;border-radius:20px;overflow:hidden;box-shadow:var(--shadow);transition:box-shadow .4s,transform .4s}
.svc-card:hover{box-shadow:0 28px 70px rgba(0,0,0,.16);transform:translateY(-6px)}
.svc-img-wrap{overflow:hidden}
.svc-img{width:100%;height:210px;object-fit:cover;display:block;transition:transform .6s ease}
.svc-card:hover .svc-img{transform:scale(1.07)}
.svc-body{padding:30px 28px 34px}
.svc-num{font-size:2.8rem;font-weight:800;color:rgba(0,208,130,.16);line-height:1;letter-spacing:-.05em;margin-bottom:8px}
.svc-bar{width:36px;height:3px;background:var(--teal);border-radius:2px;margin-bottom:14px;transition:width .4s}
.svc-card:hover .svc-bar{width:60px}
.svc-title{font-size:1.1rem;font-weight:700;color:var(--navy);margin-bottom:10px;letter-spacing:-.02em}
.svc-desc{font-size:.88rem;color:var(--muted);line-height:1.72}
.process-section{padding:100px 40px;background:linear-gradient(135deg,var(--navy) 0%,var(--mid) 100%);position:relative;overflow:hidden}
.process-section::before{content:'';position:absolute;bottom:-100px;left:-100px;width:500px;height:500px;border-radius:50%;background:radial-gradient(circle,rgba(0,208,130,.07),transparent 70%);pointer-events:none}
.process-hd{text-align:center;margin-bottom:64px}
.process-hd h2{font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;color:#fff;line-height:1.12;letter-spacing:-.03em;margin-bottom:14px}
.process-hd p{font-size:1rem;color:rgba(255,255,255,.5);max-width:500px;margin:0 auto;line-height:1.76}
.process-grid{max-width:1000px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:36px}
.proc-item{text-align:center;padding:40px 28px;border:1px solid rgba(255,255,255,.07);border-radius:20px;background:rgba(255,255,255,.04);transition:border-color .4s,background .4s,transform .4s}
.proc-item:hover{border-color:rgba(0,208,130,.35);background:rgba(0,208,130,.06);transform:translateY(-6px)}
.proc-num{font-size:4rem;font-weight:800;color:rgba(0,208,130,.22);line-height:1;letter-spacing:-.05em;margin-bottom:16px}
.proc-title{font-size:1.1rem;font-weight:700;color:#fff;margin-bottom:12px;letter-spacing:-.02em}
.proc-desc{font-size:.88rem;color:rgba(255,255,255,.48);line-height:1.76}
.photo-strip{padding:80px 40px;background:var(--lgray)}
.photo-strip-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.strip-item{border-radius:16px;overflow:hidden}
.strip-img{width:100%;height:200px;object-fit:cover;display:block;transition:transform .5s ease}
.strip-item:hover .strip-img{transform:scale(1.05)}
.cta-section{padding:100px 40px;background:var(--white);text-align:center}
.cta-section h2{font-size:clamp(1.8rem,3vw,2.6rem);font-weight:800;color:var(--navy);letter-spacing:-.03em;margin-bottom:16px}
.cta-section p{font-size:1rem;color:var(--muted);max-width:480px;margin:0 auto 36px;line-height:1.76}
.btn-solid{display:inline-block;background:var(--teal);color:var(--navy);text-decoration:none;font-weight:800;font-size:.88rem;letter-spacing:.1em;text-transform:uppercase;padding:18px 52px;border-radius:50px;transition:background .3s,box-shadow .3s,transform .3s}
.btn-solid:hover{background:var(--lteal);box-shadow:0 16px 48px rgba(0,208,130,.4);transform:translateY(-2px)}
footer{background:#050e1a;padding:64px 40px 36px;border-top:1px solid rgba(255,255,255,.06)}
.footer-inner{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:60px;margin-bottom:56px}
.footer-brand img{height:60px;width:60px;object-fit:contain;border-radius:4px;margin-bottom:16px;display:block}
.footer-brand-name{font-size:1.05rem;font-weight:700;color:#fff;margin-bottom:12px}
.footer-brand-desc{font-size:.85rem;color:rgba(255,255,255,.4);line-height:1.76;max-width:300px}
.footer-col-title{font-size:.68rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--teal);margin-bottom:20px}
.footer-links{list-style:none;display:flex;flex-direction:column;gap:11px}
.footer-links a{font-size:.85rem;color:rgba(255,255,255,.45);text-decoration:none;transition:color .3s}
.footer-links a:hover{color:var(--teal)}
.footer-bottom{max-width:1200px;margin:0 auto;padding-top:26px;border-top:1px solid rgba(255,255,255,.06);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}
.footer-copy{font-size:.8rem;color:rgba(255,255,255,.28)}
.footer-line{width:56px;height:2px;background:linear-gradient(90deg,var(--teal),transparent);border-radius:2px}
.go-top{position:fixed;bottom:34px;right:34px;width:48px;height:48px;background:var(--teal);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;opacity:0;transform:translateY(18px);transition:opacity .3s,transform .3s,background .3s;z-index:999;border:none;box-shadow:0 8px 24px rgba(0,208,130,.38)}
.go-top.show{opacity:1;transform:translateY(0)}
.go-top:hover{background:var(--lteal)}
.go-top svg{width:22px;height:22px;color:var(--navy)}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.001ms!important;transition-duration:.001ms!important}}
.nav-toggle{display:none;flex-direction:column;justify-content:center;gap:5px;background:none;border:none;padding:6px;cursor:pointer;z-index:1002;flex-shrink:0}
.nav-toggle span{display:block;width:24px;height:2px;background:#fff;border-radius:2px;transition:transform .3s,opacity .3s}
.nav-toggle.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.nav-toggle.open span:nth-child(2){opacity:0}
.nav-toggle.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.nav-mobile{position:fixed;inset:0;background:rgba(10,22,40,.97);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);z-index:1001;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:translateX(100%);transition:transform .4s cubic-bezier(.77,0,.18,1);pointer-events:none}
.nav-mobile.open{transform:translateX(0);pointer-events:all}
.nav-mobile-links{list-style:none;display:flex;flex-direction:column;align-items:center;gap:0;width:100%;padding:0 24px;margin-bottom:36px}
.nav-mobile-links li{width:100%;text-align:center;border-bottom:1px solid rgba(255,255,255,.07)}
.nav-mobile-links li:first-child{border-top:1px solid rgba(255,255,255,.07)}
.nav-mobile-links a{display:block;padding:22px 16px;color:rgba(255,255,255,.85);text-decoration:none;font-size:1rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;transition:color .2s}
.nav-mobile-links a:hover{color:var(--teal)}
.mobile-cta-btn{display:inline-block;background:var(--teal);color:var(--navy)!important;text-decoration:none;font-weight:800;font-size:.88rem;letter-spacing:.1em;text-transform:uppercase;padding:16px 44px;border-radius:50px;transition:background .3s}
.mobile-cta-btn:hover{background:var(--lteal)}
@media(max-width:1024px){.featured-card{grid-template-columns:1fr}.services-grid{grid-template-columns:1fr 1fr}.process-grid{grid-template-columns:1fr}.photo-strip-inner{grid-template-columns:repeat(2,1fr)}}
@media(max-width:768px){.nav{padding:14px 20px}.nav-toggle{display:flex}.nav-links{display:none!important}.page-hero{padding:120px 20px 70px}.featured-section,.services-section,.process-section,.cta-section,.photo-strip{padding:70px 20px}.services-grid{grid-template-columns:1fr}.featured-body{padding:36px 28px}.footer-inner{grid-template-columns:1fr;gap:32px}.photo-strip-inner{grid-template-columns:1fr}}'''

SERVICES = [
    ("Pool Vacuuming", "Our professional vacuuming removes dirt, debris, and algae from pool floors and walls. We leave the water clear and the surface spotless after every visit."),
    ("Chlorine Treatments", "We apply precise chlorine levels to keep your water sanitized and safe. Chemical levels are monitored carefully to maintain a healthy swimming environment year-round."),
    ("Filter &amp; Pump Repairs", "Our technicians diagnose and repair filter and pump issues efficiently. We keep your circulation system running properly so water stays clean and clear."),
    ("Vinyl Liner Repair", "From minor patches to full bead-channel resets, we handle all liner repair work on-site. We assess honestly and only recommend replacement when it's truly needed."),
    ("Weekly Maintenance", "Consistent weekly service keeps your pool in peak condition year-round. We handle everything — chemicals, vacuuming, skimming, and equipment checks — on every visit."),
    ("pH &amp; Acid Balancing", "Balanced water protects your liner, equipment, and swimmers. We test and adjust total alkalinity, pH, calcium hardness, and stabilizer on every service visit."),
]

JS = '''(function(){
  'use strict';
  try { gsap.registerPlugin(ScrollTrigger); } catch(e){}
  var rm = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  var navToggle = document.getElementById('navToggle');
  var navMobile = document.getElementById('navMobile');
  if (navToggle && navMobile) {
    navToggle.addEventListener('click', function(){
      var isOpen = navMobile.classList.toggle('open');
      navToggle.classList.toggle('open', isOpen);
      navToggle.setAttribute('aria-expanded', String(isOpen));
      navMobile.setAttribute('aria-hidden', String(!isOpen));
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });
    navMobile.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        navMobile.classList.remove('open');
        navToggle.classList.remove('open');
        navToggle.setAttribute('aria-expanded','false');
        navMobile.setAttribute('aria-hidden','true');
        document.body.style.overflow = '';
      });
    });
  }
  var goTop = document.getElementById('goTop');
  if (goTop) {
    window.addEventListener('scroll',function(){goTop.classList.toggle('show',window.scrollY>400);},{passive:true});
    goTop.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
  }
  if (!rm) {
    try {
      gsap.from('.page-hero .eyebrow',{opacity:0,y:-14,duration:.7,delay:.2,ease:'power3.out'});
      gsap.from('.page-hero h1',{opacity:0,y:24,duration:.7,delay:.35,ease:'power3.out'});
      gsap.from('.page-hero p',{opacity:0,y:18,duration:.7,delay:.5,ease:'power3.out'});
      gsap.from('#featHd',{opacity:0,y:30,duration:.8,ease:'power3.out',scrollTrigger:{trigger:'#featHd',start:'top 85%'}});
      gsap.from('#featCard .featured-img-wrap',{opacity:0,x:-60,duration:1,ease:'power3.out',scrollTrigger:{trigger:'#featCard',start:'top 80%'}});
      gsap.from('#featCard .featured-body',{opacity:0,x:60,duration:1,ease:'power3.out',scrollTrigger:{trigger:'#featCard',start:'top 80%'}});
      gsap.from('#svcHd',{opacity:0,y:30,duration:.8,ease:'power3.out',scrollTrigger:{trigger:'#svcHd',start:'top 85%'}});
      gsap.from('.svc-card',{opacity:0,y:50,stagger:.15,duration:.8,ease:'power3.out',scrollTrigger:{trigger:'#svcGrid',start:'top 80%'}});
      gsap.from('#procHd',{opacity:0,y:30,duration:.8,ease:'power3.out',scrollTrigger:{trigger:'#procHd',start:'top 85%'}});
      gsap.from('.proc-item',{opacity:0,y:40,stagger:.2,duration:.8,ease:'power3.out',scrollTrigger:{trigger:'#procGrid',start:'top 80%'}});
      gsap.from('#photoStrip .strip-item',{opacity:0,y:36,scale:.96,stagger:.12,duration:.8,ease:'power3.out',scrollTrigger:{trigger:'#photoStrip',start:'top 82%'}});
      gsap.from('.cta-section h2,.cta-section p,.cta-section .btn-solid',{opacity:0,y:28,stagger:.15,duration:.7,ease:'power3.out',scrollTrigger:{trigger:'.cta-section',start:'top 85%'}});
    } catch(e){}
  }
})();'''


def build_page(area, idx):
    slug = area["slug"]
    name = area["name"]
    url = f"https://hawaiipoolcleaners.com/areas/{slug}/"
    bullets_html = "\n          ".join(f"<li>{b}</li>" for b in area["feat_bullets"])
    svc_cards = ""
    for i, (svc_title, svc_desc) in enumerate(SERVICES):
        svc_cards += f'''    <div class="svc-card">
      <div class="svc-img-wrap">
        <img src="{img(idx, i+2)}" alt="{svc_title} {name} Hawaii" class="svc-img" loading="lazy">
      </div>
      <div class="svc-body">
        <div class="svc-num">0{i+1}</div>
        <div class="svc-bar"></div>
        <h3 class="svc-title">{svc_title}</h3>
        <p class="svc-desc">{svc_desc}</p>
      </div>
    </div>\n'''

    schema = f'''{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Vinyl Pool Installation and Cleaning",
  "provider": {{
    "@type": "LocalBusiness",
    "name": "Hawaii Pool Cleaners",
    "url": "https://hawaiipoolcleaners.com",
    "telephone": "808-864-3605"
  }},
  "areaServed": {{
    "@type": "Place",
    "name": "{name}, Oahu, Hawaii"
  }},
  "description": "{area['desc']}"
}}'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{area["title"]}</title>
<meta name="description" content="{area["desc"]}">
<meta property="og:title" content="{area["title"]}">
<meta property="og:description" content="{area["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://hawaiipoolcleaners.com/wp-content/uploads/2024/06/Hawaii-Pool-Cleaners-Logo.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{area["title"]}">
<meta name="twitter:description" content="{area["desc"]}">
<meta name="twitter:image" content="https://hawaiipoolcleaners.com/wp-content/uploads/2024/06/Hawaii-Pool-Cleaners-Logo.jpg">
<link rel="canonical" href="{url}">
<script type="application/ld+json">
{schema}
</script>
<link rel="icon" href="/wp-content/uploads/2024/06/cropped-Hawaii-Pool-Cleaners-Logo-192x192.jpg" sizes="192x192">
<link rel="apple-touch-icon" href="/wp-content/uploads/2024/06/cropped-Hawaii-Pool-Cleaners-Logo-192x192.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>

{NAV_HTML}

<div class="page-hero">
  <span class="eyebrow">Serving {name}, Oahu</span>
  <h1>{area["h1"]}</h1>
  <p>{area["hero_sub"]}</p>
</div>

<section class="featured-section">
  <div class="featured-inner">
    <div class="featured-hd" id="featHd">
      <span class="eyebrow">Our Specialty</span>
      <h2>{area["intro_h"]}</h2>
      <p>{area["intro_p"]}</p>
    </div>
    <div class="featured-card" id="featCard">
      <div class="featured-img-wrap">
        <img src="{img(idx, 0)}" alt="Vinyl liner pool installation {name} Hawaii" class="featured-img" loading="lazy">
      </div>
      <div class="featured-body">
        <span class="featured-tag">Primary Service</span>
        <h3>Vinyl Liner Installation &amp; Repair in {name}</h3>
        <p>{area["feat_p"]}</p>
        <ul class="featured-benefits">
          {bullets_html}
        </ul>
        <a href="/contact/" class="btn-teal">Get a Free Liner Quote</a>
      </div>
    </div>
  </div>
</section>

<section class="services-section">
  <div class="services-hd" id="svcHd">
    <span class="eyebrow">All Services</span>
    <h2>Everything Your {name} Pool Needs</h2>
    <p>One call covers it all. We handle maintenance, chemistry, equipment, and repairs so you can just swim.</p>
  </div>
  <div class="services-grid" id="svcGrid">
{svc_cards}  </div>
</section>

<section class="process-section">
  <div class="process-hd" id="procHd">
    <span class="eyebrow">How It Works</span>
    <h2>Getting Started Is Simple</h2>
    <p>From first call to finished job, we make the process easy for {name} homeowners.</p>
  </div>
  <div class="process-grid" id="procGrid">
    <div class="proc-item">
      <div class="proc-num">01</div>
      <h3 class="proc-title">Call or Request Online</h3>
      <p class="proc-desc">Call 808-864-3605 or submit a quote request online. We respond quickly and work around your schedule.</p>
    </div>
    <div class="proc-item">
      <div class="proc-num">02</div>
      <h3 class="proc-title">On-Site Assessment</h3>
      <p class="proc-desc">We come to your {name} property, evaluate your pool, and walk you through exactly what needs to be done and why.</p>
    </div>
    <div class="proc-item">
      <div class="proc-num">03</div>
      <h3 class="proc-title">We Get It Done</h3>
      <p class="proc-desc">Our crew completes the work professionally and on schedule. We leave your pool clean, balanced, and ready to swim.</p>
    </div>
  </div>
</section>

<section class="photo-strip">
  <div class="photo-strip-inner" id="photoStrip">
    <div class="strip-item"><img src="{img(idx, 8)}" alt="{name} pool service Hawaii" class="strip-img" loading="lazy"></div>
    <div class="strip-item"><img src="{img(idx, 9)}" alt="Vinyl liner pool {name} Oahu" class="strip-img" loading="lazy"></div>
    <div class="strip-item"><img src="{img(idx, 10)}" alt="Pool cleaning {name} Hawaii" class="strip-img" loading="lazy"></div>
    <div class="strip-item"><img src="{img(idx, 1)}" alt="Pool maintenance {name} Oahu" class="strip-img" loading="lazy"></div>
  </div>
</section>

<section class="cta-section">
  <h2>{area["cta_h2"]}</h2>
  <p>{area["cta_p"]}</p>
  <a href="/contact/" class="btn-solid">Request a Free Quote</a>
</section>

{FOOTER_HTML}

<button class="go-top" id="goTop" aria-label="Back to top">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>
</button>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
{JS}
</script>
</body>
</html>'''


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    areas_dir = os.path.join(base, "areas")
    created = 0
    for idx, area in enumerate(AREAS):
        slug_dir = os.path.join(areas_dir, area["slug"])
        os.makedirs(slug_dir, exist_ok=True)
        out_path = os.path.join(slug_dir, "index.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(build_page(area, idx))
        created += 1
        print(f"  [{idx+1:02d}/{len(AREAS)}] areas/{area['slug']}/index.html")
    print(f"\nDone. {created} pages created in areas/")
    print("Files are NOT git-tracked yet. Run deploy_areas.py daily to push batches of 5-7.")


if __name__ == "__main__":
    main()
