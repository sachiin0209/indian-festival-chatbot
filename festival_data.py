"""
Festival knowledge base for the Indian Festival Chatbot.
Contains information about major Indian festivals across different states and regions,
including traditional attire and how to wear them.
"""

# General knowledge about traditional Indian attire
TRADITIONAL_ATTIRE_DB = {
    "saree": {
        "name": "Saree (Sari)",
        "description": "A traditional Indian garment consisting of a long piece of cloth (usually 5-9 yards) "
                      "that is draped around the body in various styles. It is one of the oldest forms of "
                      "clothing in India, dating back to the Indus Valley Civilization.",
        "how_to_wear": "Basic steps to wear a saree:\n"
                      "1. Tuck the plain end of the saree into your petticoat at the navel\n"
                      "2. Make 5-7 pleats of equal width, holding them together\n"
                      "3. Tuck the pleats into the petticoat, slightly to the left of the navel\n"
                      "4. Take the remaining fabric around your waist once\n"
                      "5. Bring the pallu (decorated end) over your left shoulder\n"
                      "6. Secure the pallu with a pin if needed",
        "types": [
            "Banarasi Saree (Uttar Pradesh)",
            "Kanjeevaram Saree (Tamil Nadu)",
            "Paithani Saree (Maharashtra)",
            "Kasavu Saree (Kerala)",
            "Bandhani Saree (Gujarat)",
            "Baluchari Saree (West Bengal)",
            "Mysore Silk Saree (Karnataka)",
            "Nauvari Saree (Maharashtra)",
            "Bengali Saree (West Bengal)"
        ],
        "occasions": "Weddings, Festivals, Formal Events, Religious Ceremonies"
    },
    "lehenga": {
        "name": "Lehenga Choli",
        "description": "A three-piece outfit consisting of a long skirt (lehenga), a fitted blouse (choli), "
                      "and a dupatta (scarf). It is popular across North India and is often worn for "
                      "weddings and festivals.",
        "how_to_wear": "Steps to wear a lehenga choli:\n"
                      "1. Wear the lehenga (skirt) at the waist, securing it with the drawstring\n"
                      "2. Put on the choli (blouse), ensuring it fits well\n"
                      "3. Drape the dupatta over your shoulders or head\n"
                      "4. Accessorize with matching jewelry",
        "types": [
            "Bridal Lehenga",
            "Party Wear Lehenga",
            "Festival Lehenga",
            "Designer Lehenga",
            "Chaniya Choli (Gujarat)",
            "Ghagra Choli (Rajasthan)"
        ],
        "occasions": "Weddings, Festivals, Parties, Special Occasions"
    },
    "kurta": {
        "name": "Kurta",
        "description": "A loose-fitting shirt or tunic that falls to the knees or lower. It is worn by both "
                      "men and women across India, often paired with pajamas, churidar, or jeans. The kurta-pajama "
                      "and kurta-churidar combinations are among the most popular traditional outfits in India.",
        "how_to_wear": "For men:\n"
                      "1. Wear a kurta with straight-cut pajama or churidar\n"
                      "2. Can be paired with a Nehru jacket for formal occasions\n"
                      "3. For kurta-pajama: Match the kurta with appropriate pajama style\n"
                      "4. For kurta-churidar: Ensure the churidar fits well at the ankles\n"
                      "5. Tuck the kurta into the bottom wear for a formal look\n"
                      "For women:\n"
                      "1. Wear with leggings, churidar, or jeans\n"
                      "2. Can be paired with a dupatta for traditional look",
        "types": [
            "Pathani Kurta",
            "Anarkali Kurta",
            "Straight Cut Kurta",
            "Designer Kurta",
            "Kediyu (Gujarat)",
            "Sherwani (Formal)",
            "Nehru Jacket",
            "Kurta Pajama Set",
            "Kurta Churidar Set",
            "Anarkali Churidar Set"
        ],
        "occasions": "Daily Wear, Festivals, Religious Ceremonies, Casual Events, Weddings"
    },
    "dhoti": {
        "name": "Dhoti",
        "description": "A traditional men's garment consisting of a rectangular piece of cloth wrapped around "
                      "the waist and legs. It is known by different names in different regions: veshti in "
                      "Tamil Nadu, mundu in Kerala, and dhoti in North India.",
        "how_to_wear": "Basic steps to wear a dhoti:\n"
                      "1. Hold the dhoti at the center of the long edge\n"
                      "2. Wrap around the waist, bringing both ends to the front\n"
                      "3. Make pleats in the front\n"
                      "4. Tuck the pleated portion into the waist at the back\n"
                      "5. Bring the remaining cloth between the legs and tuck at the back",
        "types": [
            "Cotton Dhoti",
            "Silk Dhoti",
            "Wedding Dhoti",
            "Temple Dhoti",
            "Veshti (Tamil Nadu)",
            "Mundu (Kerala)",
            "Panche (Karnataka)",
            "Tehmat (Punjab)",
            "Pheta (Maharashtra)"
        ],
        "occasions": "Religious Ceremonies, Weddings, Festivals, Traditional Events"
    },
    "salwar_kameez": {
        "name": "Salwar Kameez",
        "description": "A traditional outfit consisting of a long tunic (kameez), loose pants (salwar), and "
                      "a scarf (dupatta). Popular across North India, especially in Punjab. The churidar suit "
                      "is a variation where the salwar is replaced with a churidar.",
        "how_to_wear": "Steps to wear salwar kameez:\n"
                      "1. Wear the salwar or churidar at the waist\n"
                      "2. Put on the kameez (tunic)\n"
                      "3. For churidar: Ensure proper gathering at ankles\n"
                      "4. Drape the dupatta over shoulders or head\n"
                      "5. Accessorize with matching jewelry",
        "types": [
            "Punjabi Suit",
            "Churidar Suit",
            "Palazzo Suit",
            "Anarkali Suit",
            "Phulkari Suit",
            "Designer Suit",
            "Wedding Suit",
            "Party Wear Suit"
        ],
        "occasions": "Daily Wear, Festivals, Weddings, Parties, Formal Events"
    },
    "mekhela_chador": {
        "name": "Mekhela Chador",
        "description": "Traditional Assamese attire consisting of a two-piece garment - the mekhela (skirt) "
                      "and chador (wrap). Known for its elegant drape and traditional motifs.",
        "how_to_wear": "Steps to wear mekhela chador:\n"
                      "1. Wear the mekhela (skirt) at the waist\n"
                      "2. Drape the chador over the blouse\n"
                      "3. Make pleats in the front\n"
                      "4. Bring one end over the shoulder",
        "types": [
            "Silk Mekhela Chador",
            "Cotton Mekhela Chador",
            "Muga Silk Mekhela",
            "Pat Silk Mekhela"
        ],
        "occasions": "Bihu Festival, Weddings, Cultural Events"
    },
    "abaya": {
        "name": "Abaya",
        "description": "A long, flowing outer garment worn by Muslim women. It is typically black and worn "
                      "over regular clothes, often paired with a hijab (headscarf).",
        "how_to_wear": "Steps to wear abaya:\n"
                      "1. Wear regular clothes underneath\n"
                      "2. Put on the abaya over your clothes\n"
                      "3. Wear hijab to cover head and neck\n"
                      "4. Can be accessorized with a belt",
        "types": [
            "Traditional Abaya",
            "Modern Abaya",
            "Embroidered Abaya",
            "Designer Abaya"
        ],
        "occasions": "Eid, Religious Ceremonies, Daily Wear"
    },
    "pavadai_sattai": {
        "name": "Pavadai Sattai",
        "description": "Traditional Tamil attire for young girls, consisting of a long skirt (pavadai) and "
                      "blouse (sattai). For older girls, it includes a half saree (davani).",
        "how_to_wear": "Steps to wear pavadai sattai:\n"
                      "1. Wear the pavadai (skirt) at the waist\n"
                      "2. Put on the sattai (blouse)\n"
                      "3. For half saree: Drape the davani over the shoulder",
        "types": [
            "Simple Pavadai Sattai",
            "Half Saree",
            "Festival Pavadai",
            "Wedding Pavadai"
        ],
        "occasions": "Pongal, Temple Visits, Cultural Events"
    },
    "pajama": {
        "name": "Pajama (Payjama)",
        "description": "Traditional Indian pants that are loose-fitting and comfortable. They come in various "
                      "styles and are typically worn with a kurta. Pajamas are an essential part of traditional "
                      "Indian menswear and are worn across different regions of India.",
        "how_to_wear": "Steps to wear pajama:\n"
                      "1. Wear the pajama at the waist, securing with drawstring\n"
                      "2. For formal occasions, ensure proper length (should touch the ground)\n"
                      "3. For casual wear, can be slightly shorter\n"
                      "4. Can be paired with kurta, sherwani, or other traditional tops\n"
                      "5. For churidar style, the pajama should be tight at the ankles",
        "types": [
            "Straight Cut Pajama",
            "Churidar Pajama",
            "Pathani Pajama",
            "Suit Pajama",
            "Wedding Pajama",
            "Cotton Pajama",
            "Silk Pajama",
            "Designer Pajama"
        ],
        "occasions": "Daily Wear, Festivals, Weddings, Religious Ceremonies, Formal Events"
    },
    "churidar": {
        "name": "Churidar (Chudidar)",
        "description": "A tightly fitted trouser that is longer than the leg and gathered at the ankle, "
                      "creating a wrinkled effect. It is typically worn with a kurta or kameez and is popular "
                      "among both men and women across India. The churidar is known for its elegant drape and "
                      "comfortable fit.",
        "how_to_wear": "Steps to wear churidar:\n"
                      "1. Wear the churidar at the waist, securing with drawstring\n"
                      "2. Ensure proper length (should be longer than leg length)\n"
                      "3. Gather the extra fabric at the ankles to create the characteristic wrinkles\n"
                      "4. For women: Can be worn with kurta, kameez, or anarkali\n"
                      "5. For men: Typically worn with kurta or sherwani\n"
                      "6. For formal occasions, ensure the wrinkles are evenly distributed",
        "types": [
            "Cotton Churidar",
            "Silk Churidar",
            "Wedding Churidar",
            "Designer Churidar",
            "Printed Churidar",
            "Embroidered Churidar",
            "Anarkali Churidar",
            "Party Wear Churidar"
        ],
        "occasions": "Weddings, Festivals, Parties, Formal Events, Daily Wear"
    },
    "chuba": {
        "name": "Chuba (Tibetan Dress)",
        "description": "Traditional Tibetan dress worn by both men and women. It is a long-sleeved "
                      "robe that is tied at the waist with a sash. Women's chuba is often worn with "
                      "a colorful apron called pangden. The chuba is an essential part of Tibetan "
                      "cultural identity and is worn during festivals and daily life.",
        "how_to_wear": "Steps to wear chuba:\n"
                      "1. Put on the chuba like a robe\n"
                      "2. Wrap the right side over the left\n"
                      "3. Tie the sash (kera) around the waist\n"
                      "4. For women: Wear the pangden (apron) over the chuba\n"
                      "5. For formal occasions: Wear with traditional jewelry and accessories\n"
                      "6. For men: Can be worn with traditional boots and hat",
        "types": [
            "Traditional Chuba",
            "Festival Chuba",
            "Wedding Chuba",
            "Daily Wear Chuba",
            "Monk's Chuba",
            "Designer Chuba",
            "Silk Chuba",
            "Woolen Chuba"
        ],
        "occasions": "Losar, Buddhist Festivals, Weddings, Daily Wear, Cultural Events"
    },
    "turban": {
        "name": "Turban (Pagri/Safa/Pag)",
        "description": "A traditional headwear worn by men across different regions of India. Known by various names "
                      "like pagri, safa, or pag, the turban is a symbol of honor, respect, and dignity. Different "
                      "styles and colors hold cultural significance depending on the region and occasion.",
        "how_to_wear": "Basic steps to tie a turban:\n"
                      "1. Start with a long cloth (usually 5-7 meters)\n"
                      "2. Place one end on the forehead\n"
                      "3. Wrap around the head, making pleats\n"
                      "4. Continue wrapping, maintaining tension\n"
                      "5. Tuck the end securely\n"
                      "Note: Different regions have specific styles:\n"
                      "- Rajasthani Safa: Colorful, with a fan-like pleat\n"
                      "- Sikh Dastar: Neat, symmetrical wraps\n"
                      "- Mysore Peta: Distinctive style with a peak\n"
                      "- Marathi Pheta: Traditional style for ceremonies",
        "types": [
            "Rajasthani Safa",
            "Sikh Dastar",
            "Mysore Peta",
            "Marathi Pheta",
            "Punjabi Pagri",
            "Gujarati Fenta",
            "Maharashtrian Pagdi",
            "Wedding Turban",
            "Festival Turban",
            "Royal Turban"
        ],
        "occasions": "Weddings, Festivals, Religious Ceremonies, Cultural Events, Formal Occasions",
        "regional_variations": {
            "Rajasthan": "Colorful safas with elaborate pleats, often in bright colors like orange, pink, and yellow",
            "Punjab": "Neatly tied pagris, often in white or pastel colors, with the Sikh dastar being a distinct style",
            "Maharashtra": "Traditional pheta, often in saffron or white, worn during ceremonies and festivals",
            "Karnataka": "Mysore peta, a distinctive style with a peak, often in gold or white",
            "Gujarat": "Fenta, a simpler style often worn with traditional kurta",
            "Tamil Nadu": "Traditional pagdi, often in white or off-white, worn during ceremonies"
        },
        "significance": "The turban holds deep cultural and religious significance across India. It represents honor, "
                       "respect, and dignity. In Sikhism, it's an important religious symbol. Different colors and "
                       "styles can indicate social status, region, or occasion. For example, white turbans are often "
                       "worn during religious ceremonies, while colorful ones are preferred for festivals and weddings."
    }
}

# Keywords for traditional attire
ATTIRE_KEYWORDS = {
    "saree": ["saree", "sari", "sarees", "sarong", "traditional dress", "indian dress", "how to wear saree", 
              "nauvari saree", "paithani", "kasavu saree", "bengali saree", "banarasi saree", "kanjeevaram saree"],
    "lehenga": ["lehenga", "lehenga choli", "lehengas", "choli", "indian skirt", "traditional skirt", 
                "chaniya choli", "ghagra choli"],
    "kurta": ["kurta", "kurti", "kurtas", "indian tunic", "traditional shirt", "pathani", "anarkali", 
              "kediyu", "nehru jacket", "sherwani", "kurta pajama", "kurta payjama", "kurta pyjama", 
              "kurta churidar", "kurta chudidar"],
    "dhoti": ["dhoti", "veshti", "mundu", "traditional lower garment", "indian lower garment", "panche", 
              "tehmat", "pheta"],
    "salwar_kameez": ["salwar kameez", "punjabi suit", "churidar", "salwar", "kameez", "dupatta", 
                      "chunni", "phulkari", "churidar suit", "chudidar suit"],
    "mekhela_chador": ["mekhela chador", "assamese dress", "mekhela", "chador"],
    "abaya": ["abaya", "hijab", "burqa", "islamic dress", "muslim dress"],
    "pavadai_sattai": ["pavadai sattai", "half saree", "pavadai", "davani", "tamil traditional dress"],
    "pajama": ["pajama", "payjama", "pyjama", "indian pants", "traditional pants", "churidar pajama", 
               "straight cut pajama", "pathani pajama", "suit pajama"],
    "churidar": ["churidar", "chudidar", "churidar suit", "chudidar suit", "tight pants", "indian leggings", 
                 "traditional leggings", "kurta churidar", "kurta chudidar"],
    "chuba": ["chuba", "tibetan dress", "himalayan dress", "tibetan robe", 
              "tibetan traditional dress", "pangden", "tibetan apron"],
    "turban": ["turban", "pagri", "safa", "pag", "dastar", "peta", "pheta", "pagdi", "fenta", 
               "traditional headwear", "indian headwear", "how to tie turban", "how to wear turban",
               "sikh turban", "rajasthani turban", "punjabi turban", "marathi turban"]
}

FESTIVAL_DATABASE = {
    # Hindu Festivals
    "diwali": {
        "name": "Diwali",
        "states": ["All India", "Gujarat", "Maharashtra", "Karnataka", "Tamil Nadu", "West Bengal"],
        "month": "October-November",
        "description": "The Festival of Lights, celebrating the victory of light over darkness. "
                      "People light diyas, decorate homes, exchange sweets, and celebrate with fireworks.",
        "traditional_dress": {
            "women": {
                "name": "Saree or Lehenga Choli",
                "description": "Women typically wear elegant sarees or lehenga cholis. "
                             "For saree: Drape the pallu over the left shoulder, pleat the saree neatly. "
                             "For lehenga: Wear with a matching choli and dupatta draped over the shoulder.",
                "colors": "Rich colors like red, gold, maroon, and green are popular"
            },
            "men": {
                "name": "Kurta Pajama or Sherwani",
                "description": "Men wear traditional kurta pajama or formal sherwani. "
                             "For kurta: Wear with straight-cut pajama and a Nehru jacket if desired. "
                             "For sherwani: Wear with churidar and a stole (dupatta) around the neck.",
                "colors": "Cream, gold, maroon, and black are common choices"
            }
        }
    },
    "holi": {
        "name": "Holi",
        "states": ["All India", "Uttar Pradesh", "Rajasthan", "Gujarat", "Bihar"],
        "month": "March",
        "description": "The Festival of Colors, celebrating spring and love. "
                      "People play with colors, dance, and enjoy traditional sweets like gujiya.",
        "traditional_dress": {
            "women": {
                "name": "White Kurta with Churidar or Salwar",
                "description": "Women wear white kurta with churidar or salwar. "
                             "The white color makes the colors more vibrant. "
                             "Wear old clothes as they will get stained with colors.",
                "colors": "White base with colorful dupatta"
            },
            "men": {
                "name": "White Kurta Pajama",
                "description": "Men wear white kurta pajama. "
                             "The white fabric shows the colors beautifully. "
                             "Wear old clothes as they will get stained.",
                "colors": "White base with colorful stole"
            }
        }
    },
    "navratri": {
        "name": "Navratri",
        "states": ["All India", "Gujarat", "West Bengal", "Maharashtra"],
        "month": "September-October",
        "description": "Nine nights of worship dedicated to Goddess Durga. "
                      "Features garba dance, fasting, and cultural programs.",
        "traditional_dress": {
            "women": {
                "name": "Chaniya Choli (Gujarat) or Traditional Saree (East India)",
                "description": "In Gujarat: Three-piece outfit with colorful skirt (chaniya), blouse (choli) and dupatta. "
                               "In Bengal: White saree with red border for first day, colorful sarees subsequent days.",
                "colors": "Bright colors with mirror work (Gujarat), Red/White (Bengal)"
            },
            "men": {
                "name": "Kediyu with Dhoti (Gujarat) or Kurta Pajama (North India)",
                "description": "In Gujarat: Short kurta called kediyu with dhoti and colorful turban. "
                              "Elsewhere: Simple kurta pajama for garba/dandiya.",
                "colors": "White with red/gold accents (Gujarat)"
            }
        }
    },
    "durga_puja": {
        "name": "Durga Puja",
        "states": ["West Bengal", "Odisha", "Assam", "Bihar"],
        "month": "September-October",
        "description": "Celebrates the victory of Goddess Durga over the demon Mahishasura. "
                      "Features elaborate pandals, cultural programs, and immersion ceremonies.",
        "traditional_dress": {
            "women": {
                "name": "Bengali Saree",
                "description": "Women wear traditional Bengali saree (usually cotton or silk). "
                             "Drape in the Bengali style: make broad pleats in front, "
                             "bring the pallu over the left shoulder, and let it fall freely.",
                "colors": "White with red border (traditional) or colorful designs"
            },
            "men": {
                "name": "Dhoti Kurta",
                "description": "Men wear dhoti with kurta. "
                             "For dhoti: Wrap around waist, make pleats in front, "
                             "and tuck the end into the waist at the back. "
                             "Wear a kurta on top.",
                "colors": "White dhoti with white or colored kurta"
            }
        }
    },
    "ganesh_chaturthi": {
        "name": "Ganesh Chaturthi",
        "states": ["Maharashtra", "Karnataka", "Goa", "Telangana"],
        "month": "August-September",
        "description": "Celebrates the birth of Lord Ganesha. "
                      "Features installation of Ganesha idols, cultural programs, and immersion processions.",
        "traditional_dress": {
            "women": {
                "name": "Nauvari Saree or Paithani",
                "description": "Women wear Nauvari saree (nine-yard saree) or Paithani. "
                             "For Nauvari: Drape like a dhoti, bring the pallu over the left shoulder. "
                             "For Paithani: Drape in the traditional Maharashtrian style.",
                "colors": "Bright colors with traditional motifs"
            },
            "men": {
                "name": "Dhoti Kurta with Pheta",
                "description": "Men wear dhoti with kurta and pheta (turban). "
                             "For dhoti: Wrap around waist, make pleats in front. "
                             "For pheta: Wrap the turban around the head in traditional style.",
                "colors": "White dhoti with colored kurta and matching pheta"
            }
        }
    },
    "janmashtami": {
        "name": "Janmashtami",
        "states": ["All India", "Uttar Pradesh", "Maharashtra", "Gujarat"],
        "month": "August-September",
        "description": "Celebrates the birth of Lord Krishna. "
                      "Features fasting, prayers, and dahi handi celebrations.",
        "traditional_dress": {
            "women": {
                "name": "Traditional Saree or Lehenga",
                "description": "Women dress as Gopis (Krishna's devotees) in colorful traditional attire. "
                               "In Maharashtra: Wear nauvari saree for dahi handi events.",
                "colors": "Bright colors like peacock blue, yellow, green"
            },
            "men": {
                "name": "Dhoti with Peacock Feather Crown",
                "description": "Many dress as little Krishna in yellow dhoti, peacock feather crown "
                              "and flute. Others wear simple dhoti-kurta.",
                "colors": "Yellow (for Krishna) or white"
            }
        }
    },
    "onam": {
        "name": "Onam",
        "states": ["Kerala"],
        "month": "August-September",
        "description": "Kerala's harvest festival celebrating King Mahabali's return. "
                      "Features grand feasts (Onasadya), boat races, and floral decorations.",
        "traditional_dress": {
            "women": {
                "name": "Kasavu Saree",
                "description": "Women wear traditional Kasavu saree with gold border. "
                             "Drape in the Kerala style: pleat the saree at the back, "
                             "bring the pallu over the left shoulder, and tuck the end into the waist.",
                "colors": "Cream/white with gold border"
            },
            "men": {
                "name": "Mundu with Shirt",
                "description": "Men wear mundu (dhoti) with a formal shirt. "
                             "For mundu: Wrap around waist, make pleats in front, "
                             "and tuck the end into the waist at the back. "
                             "Wear a shirt on top.",
                "colors": "White mundu with white or colored shirt"
            }
        }
    },
    "pongal": {
        "name": "Pongal",
        "states": ["Tamil Nadu", "Andhra Pradesh", "Karnataka"],
        "month": "January",
        "description": "A harvest festival celebrating the sun god and agricultural prosperity. "
                      "Features the preparation of sweet Pongal rice and traditional cattle worship.",
        "traditional_dress": {
            "women": {
                "name": "Pavadai Sattai or Half Saree",
                "description": "Young girls wear Pavadai Sattai (long skirt with blouse). "
                             "Married women wear half saree or full saree. "
                             "For half saree: Wear the pavadai (skirt) at waist, blouse on top, "
                             "and the davani (half saree) draped over the shoulder.",
                "colors": "Bright colors like yellow, orange, and green"
            },
            "men": {
                "name": "Veshti (Dhoti) with Shirt",
                "description": "Men wear veshti (dhoti) with a formal shirt. "
                             "For veshti: Wrap around waist, make pleats in front, "
                             "and tuck the end into the waist at the back.",
                "colors": "White veshti with colored shirt"
            }
        }
    },
    "makar_sankranti": {
        "name": "Makar Sankranti",
        "states": ["All India"],
        "month": "January",
        "description": "Celebrates the sun's entry into Capricorn. Known by different names across India: "
                      "Pongal in Tamil Nadu, Lohri in Punjab, Bihu in Assam, Uttarayan in Gujarat. "
                      "Features kite flying, sesame sweets, and holy dips in rivers.",
        "traditional_dress": {
            "women": {
                "name": "Regional Attire",
                "description": "Varies by region - Punjabi suit in North, Saree in East, "
                             "Ghagra Choli in Gujarat, Pavadai in South.",
                "colors": "Festive colors - yellow, orange, red"
            },
            "men": {
                "name": "Regional Attire",
                "description": "Kurta pajama in North, Dhoti in East, Kediyu in Gujarat, "
                             "Veshti in South.",
                "colors": "White with colorful accents"
            }
        }
    },
    "bihu": {
        "name": "Bihu",
        "states": ["Assam"],
        "month": "April",
        "description": "Assam's harvest festival celebrated three times a year. "
                      "Features traditional Bihu dance, music, and feasting.",
        "traditional_dress": {
            "women": {
                "name": "Mekhela Chador",
                "description": "Two-piece silk attire consisting of mekhela (skirt) and chador (wrap). "
                             "Drape the chador over the blouse with elegant pleats in front.",
                "colors": "Red and white traditional, but modern versions in all colors"
            },
            "men": {
                "name": "Dhoti with Gamosa",
                "description": "White dhoti with red-bordered gamosa (towel) around neck. "
                             "Sometimes wear a kurta or shirt on top.",
                "colors": "White with red accents"
            }
        }
    },
    "gudi_padwa": {
        "name": "Gudi Padwa",
        "states": ["Maharashtra", "Karnataka", "Andhra Pradesh"],
        "month": "March-April",
        "description": "Celebrates the Marathi New Year. "
                      "Features raising of Gudi flags and traditional feasts.",
        "traditional_dress": {
            "women": {
                "name": "Nauvari Saree or Paithani",
                "description": "Traditional nine-yard saree draped like a dhoti or "
                             "elegant Paithani saree with peacock designs.",
                "colors": "Green and saffron popular, or Paithani's distinctive borders"
            },
            "men": {
                "name": "Kurta with Dhoti and Pheta",
                "description": "Kurta with dhoti and traditional Marathi turban (pheta) "
                             "in saffron or white.",
                "colors": "White or saffron"
            }
        }
    },
    "ugadi": {
        "name": "Ugadi",
        "states": ["Andhra Pradesh", "Telangana", "Karnataka"],
        "month": "March-April",
        "description": "New Year celebration for Telugu and Kannada communities. "
                      "Features special dishes like Ugadi Pachadi and home decorations.",
        "traditional_dress": {
            "women": {
                "name": "Saree with Traditional Jewelry",
                "description": "Silk sarees like Kanjeevaram or Gadwal with traditional gold jewelry. "
                             "Young girls may wear lehenga-style pavada.",
                "colors": "Bright colors with gold borders"
            },
            "men": {
                "name": "Panche with Shirt",
                "description": "Traditional dhoti called panche with formal shirt. "
                             "Elders may wear angavastram over shoulder.",
                "colors": "White or cream with gold borders"
            }
        }
    },
    "vishu": {
        "name": "Vishu",
        "states": ["Kerala"],
        "month": "April",
        "description": "Malayali New Year celebrated with Vishu Kani (auspicious sight) "
                      "and Vishu Sadya (feast).",
        "traditional_dress": {
            "women": {
                "name": "Kasavu Saree",
                "description": "Traditional off-white saree with golden border, "
                             "draped in Kerala style with pleats at back.",
                "colors": "Cream/white with gold"
            },
            "men": {
                "name": "Mundu with Shirt",
                "description": "White mundu (dhoti) with golden border and shirt. "
                             "Elders may wear angavastram.",
                "colors": "White with gold border"
            }
        }
    },
    "karwa_chauth": {
        "name": "Karwa Chauth",
        "states": ["North India", "Punjab", "Haryana", "Uttar Pradesh", "Rajasthan"],
        "month": "October-November",
        "description": "A festival where married women fast for their husbands' longevity. "
                      "Features fasting, prayers, and moon sighting ceremonies.",
        "traditional_dress": {
            "women": {
                "name": "Red Saree or Lehenga",
                "description": "Bridal-style red attire with heavy embroidery. "
                             "Wear traditional jewelry like mangalsutra, bangles and maang tikka.",
                "colors": "Red, maroon, pink with gold embroidery"
            },
            "men": {
                "name": "Kurta with Jacket",
                "description": "Formal kurta with Nehru jacket or sherwani. "
                             "Often in coordinating colors with wife's outfit.",
                "colors": "Cream, gold, or colors matching spouse's outfit"
            }
        }
    },
    "rakhi": {
        "name": "Raksha Bandhan",
        "states": ["All India"],
        "month": "August",
        "description": "Celebrates the bond between brothers and sisters. "
                      "Features tying of rakhi threads and exchange of gifts.",
        "traditional_dress": {
            "women": {
                "name": "Colorful Saree or Salwar Kameez",
                "description": "Festive attire in bright colors, often coordinating with brother's outfit. "
                             "Traditional jewelry preferred.",
                "colors": "Bright pinks, yellows, greens"
            },
            "men": {
                "name": "Kurta Pajama",
                "description": "Traditional kurta pajama to receive rakhi. "
                             "Often in colors matching sister's outfit.",
                "colors": "White, cream, or colors matching sister's outfit"
            }
        }
    },
    "mahashivratri": {
        "name": "Mahashivratri",
        "states": ["All India", "Uttar Pradesh", "Tamil Nadu", "Andhra Pradesh"],
        "month": "February-March",
        "description": "The Great Night of Shiva, celebrated with fasting, prayers and night-long vigils.",
        "traditional_dress": {
            "women": {
                "name": "Green Saree",
                "description": "Green is associated with Lord Shiva. Women wear green sarees "
                             "with minimal jewelry as it's a day of austerity.",
                "colors": "Green in various shades"
            },
            "men": {
                "name": "Dhoti with Rudraksha",
                "description": "Simple white dhoti with rudraksha beads. Some apply vibhuti "
                             "(sacred ash) on forehead and body.",
                "colors": "White"
            }
        }
    },

    # Muslim Festivals
    "eid_ul_fitr": {
        "name": "Eid-ul-Fitr",
        "states": ["All India"],
        "month": "Varies (Islamic Calendar)",
        "description": "Marks the end of Ramadan, the Islamic holy month of fasting. "
                      "Features prayers, feasting, and charity.",
        "traditional_dress": {
            "women": {
                "name": "Abaya or Hijab with Traditional Dress",
                "description": "Women wear abaya (long cloak) or hijab with traditional dress. "
                             "For abaya: Wear over regular clothes, can be plain or embroidered. "
                             "For hijab: Wrap around head and shoulders, secure with pins.",
                "colors": "Black, navy, or pastel colors"
            },
            "men": {
                "name": "Kurta Pajama with Topi",
                "description": "Men wear kurta pajama with a topi (cap). "
                             "For kurta: Wear with straight-cut pajama. "
                             "For topi: Wear on head, can be plain or embroidered.",
                "colors": "White or pastel colors"
            }
        }
    },
    "eid_ul_adha": {
        "name": "Eid-ul-Adha",
        "states": ["All India"],
        "month": "Varies (Islamic Calendar)",
        "description": "The Festival of Sacrifice, commemorating Prophet Ibrahim's devotion. "
                      "Features prayers, animal sacrifice, and charity.",
        "traditional_dress": {
            "women": {
                "name": "Abaya or Hijab with Traditional Dress",
                "description": "Similar to Eid-ul-Fitr, women wear abaya or hijab. "
                             "For abaya: Wear over regular clothes, can be plain or embroidered. "
                             "For hijab: Wrap around head and shoulders, secure with pins.",
                "colors": "Black, navy, or pastel colors"
            },
            "men": {
                "name": "Kurta Pajama with Topi",
                "description": "Similar to Eid-ul-Fitr, men wear kurta pajama with topi. "
                             "For kurta: Wear with straight-cut pajama. "
                             "For topi: Wear on head, can be plain or embroidered.",
                "colors": "White or pastel colors"
            }
        }
    },
    "muharram": {
        "name": "Muharram",
        "states": ["All India", "Uttar Pradesh", "Karnataka", "Telangana"],
        "month": "Varies (Islamic Calendar)",
        "description": "Islamic New Year and mourning of Imam Hussain's martyrdom. "
                      "Features processions and religious gatherings.",
        "traditional_dress": {
            "women": {
                "name": "Black Abaya or Simple Dress",
                "description": "Black is worn as color of mourning. Simple attire without "
                             "ornamentation to reflect solemnity of occasion.",
                "colors": "Black or dark colors"
            },
            "men": {
                "name": "Black Kurta with White Topi",
                "description": "Black kurta symbolizing mourning with white cap. "
                             "Some communities wear green shawls.",
                "colors": "Black with white"
            }
        }
    },
    "milad_un_nabi": {
        "name": "Milad-un-Nabi",
        "states": ["All India"],
        "month": "Varies (Islamic Calendar)",
        "description": "Celebrates the birth of Prophet Muhammad. Features prayers, "
                      "processions and charity events.",
        "traditional_dress": {
            "women": {
                "name": "Green Hijab with Traditional Dress",
                "description": "Green is associated with Prophet Muhammad. Women wear green "
                             "hijab with traditional dress in white or green.",
                "colors": "Green and white"
            },
            "men": {
                "name": "White Kurta with Green Shawl",
                "description": "White kurta pajama with green shawl or scarf. "
                             "Green topi often worn.",
                "colors": "White with green accents"
            }
        }
    },

    # Christian Festivals
    "christmas": {
        "name": "Christmas",
        "states": ["All India", "Goa", "Kerala", "Mizoram", "Nagaland"],
        "month": "December",
        "description": "Celebrates the birth of Jesus Christ. "
                      "Features midnight mass, carol singing, and festive decorations.",
        "traditional_dress": {
            "women": {
                "name": "Western Formal Wear or Traditional Dress",
                "description": "Women wear western formal wear or traditional dress. "
                             "For western: Dress or skirt with blouse. "
                             "For traditional: Saree or salwar kameez.",
                "colors": "Red, green, gold, and white"
            },
            "men": {
                "name": "Western Formal Wear or Traditional Dress",
                "description": "Men wear western formal wear or traditional dress. "
                             "For western: Suit or formal shirt with trousers. "
                             "For traditional: Kurta pajama or sherwani.",
                "colors": "Black, navy, or festive colors"
            }
        }
    },
    "easter": {
        "name": "Easter",
        "states": ["All India", "Goa", "Kerala", "North East States"],
        "month": "March-April",
        "description": "Celebrates the resurrection of Jesus Christ. Features special church "
                      "services and family meals.",
        "traditional_dress": {
            "women": {
                "name": "White Dress or Saree",
                "description": "White symbolizes purity and resurrection. Women wear white "
                             "western dresses or white sarees/salwar kameez.",
                "colors": "White with pastel accents"
            },
            "men": {
                "name": "White Shirt with Trousers",
                "description": "White shirt with dark trousers or full white suit. "
                             "In Kerala: White mundu with shirt.",
                "colors": "White"
            }
        }
    },
    "good_friday": {
        "name": "Good Friday",
        "states": ["All India"],
        "month": "March-April",
        "description": "Commemorates the crucifixion of Jesus Christ. Day of prayer and fasting.",
        "traditional_dress": {
            "women": {
                "name": "Somber Attire",
                "description": "Simple, modest clothing in dark colors reflecting solemnity "
                             "of the occasion. No jewelry.",
                "colors": "Black, navy, dark colors"
            },
            "men": {
                "name": "Dark Formal Wear",
                "description": "Dark colored shirts with trousers. No bright colors or patterns.",
                "colors": "Black, dark grey, navy"
            }
        }
    },

    # Sikh Festivals
    "gurpurab": {
        "name": "Gurpurab",
        "states": ["Punjab", "Haryana", "Delhi"],
        "month": "Varies (Based on Sikh Calendar)",
        "description": "Celebrates the birth anniversaries of Sikh Gurus. "
                      "Features prayers, langar (community kitchen), and processions.",
        "traditional_dress": {
            "women": {
                "name": "Salwar Kameez with Dupatta",
                "description": "Traditional Punjabi suit with dupatta. Often in bright colors "
                             "with phulkari embroidery.",
                "colors": "Bright colors with phulkari work"
            },
            "men": {
                "name": "Kurta with Tehmat",
                "description": "Traditional Sikh attire consisting of kurta with tehmat "
                             "(Punjabi version of dhoti) and turban.",
                "colors": "White or blue with orange accents"
            }
        }
    },
    "baisakhi": {
        "name": "Baisakhi",
        "states": ["Punjab", "Haryana"],
        "month": "April",
        "description": "Celebrates the harvest of rabi crops and the Sikh New Year. "
                      "Features bhangra dance, fairs, and community feasts.",
        "traditional_dress": {
            "women": {
                "name": "Punjabi Suit with Phulkari Dupatta",
                "description": "Bright colored salwar kameez with phulkari embroidery dupatta. "
                             "Heavy traditional jewelry like jhumkas and paranda.",
                "colors": "Yellow, orange, bright green"
            },
            "men": {
                "name": "Kurta with Tehmat and Turban",
                "description": "Bright colored kurta with white tehmat and matching turban. "
                             "Traditional Sikh footwear (juttis) completes the look.",
                "colors": "Blue, yellow, orange"
            }
        }
    },
    "holla_mohalla": {
        "name": "Holla Mohalla",
        "states": ["Punjab"],
        "month": "March",
        "description": "Sikh festival showcasing martial arts, poetry and music. "
                      "Held at Anandpur Sahib with mock battles and displays of valor.",
        "traditional_dress": {
            "women": {
                "name": "Punjabi Suit with Chunni",
                "description": "Traditional Punjabi dress with colorful chunni. "
                             "Practical clothing for outdoor celebrations.",
                "colors": "Bright festive colors"
            },
            "men": {
                "name": "Bana (Traditional Sikh Warrior Attire)",
                "description": "Blue robes with dumala (turban) and martial accessories. "
                             "Some wear chainmail and carry traditional weapons for displays.",
                "colors": "Blue with saffron accents"
            }
        }
    },

    # Jain Festivals
    "paryushana": {
        "name": "Paryushana",
        "states": ["Gujarat", "Rajasthan", "Maharashtra", "Karnataka"],
        "month": "August-September",
        "description": "Most important Jain festival of forgiveness and introspection. "
                      "Features fasting, prayers and recitation of sacred texts.",
        "traditional_dress": {
            "women": {
                "name": "Simple Saree or Salwar Kameez",
                "description": "Plain white or off-white attire without ornamentation "
                             "to reflect simplicity and purity during the festival.",
                "colors": "White or very light colors"
            },
            "men": {
                "name": "White Dhoti with Shawl",
                "description": "Simple white dhoti with white cloth covering upper body. "
                             "Some wear mouth cloth (muhpatti) during prayers.",
                "colors": "White"
            }
        }
    },
    "mahavir_jayanti": {
        "name": "Mahavir Jayanti",
        "states": ["All India"],
        "month": "March-April",
        "description": "Celebrates the birth of Lord Mahavira, the 24th Tirthankara. "
                      "Features temple visits, processions and charitable acts.",
        "traditional_dress": {
            "women": {
                "name": "White Saree or Salwar Kameez",
                "description": "White attire symbolizing purity and non-violence. "
                             "Minimal jewelry if any.",
                "colors": "White"
            },
            "men": {
                "name": "White Dhoti with Angavastram",
                "description": "White dhoti with white cloth covering upper body. "
                             "Some carry small brooms as part of monastic tradition.",
                "colors": "White"
            }
        }
    },

    # Buddhist Festivals
    "buddha_purnima": {
        "name": "Buddha Purnima",
        "states": ["All India", "Bihar", "Uttar Pradesh", "Sikkim", "Arunachal Pradesh", "Ladakh"],
        "month": "April-May",
        "description": "Celebrates the birth, enlightenment, and death of Gautama Buddha. "
                      "Features prayers, meditation, and acts of charity. Also known as Vesak or Buddha Jayanti.",
        "traditional_dress": {
            "women": {
                "name": "White or Saffron Saree",
                "description": "White or saffron colored simple saree symbolizing purity "
                             "and renunciation. No elaborate jewelry. Some wear traditional "
                             "Tibetan chuba in Himalayan regions.",
                "colors": "White or saffron"
            },
            "men": {
                "name": "White Dhoti with Saffron Shawl",
                "description": "White dhoti with saffron shawl, colors of Buddhist monks. "
                             "Some wear simple white kurta. In Himalayan regions, men may "
                             "wear traditional Tibetan chuba.",
                "colors": "White with saffron"
            }
        }
    },
    "losar": {
        "name": "Losar",
        "states": ["Sikkim", "Arunachal Pradesh", "Ladakh", "Himachal Pradesh"],
        "month": "February-March",
        "description": "Tibetan New Year celebration. Features traditional dances, prayers, "
                      "and community feasts. Celebrated with great enthusiasm in Buddhist "
                      "communities, especially in Himalayan regions.",
        "traditional_dress": {
            "women": {
                "name": "Tibetan Chuba",
                "description": "Traditional Tibetan dress (chuba) with colorful apron (pangden). "
                             "Worn with traditional jewelry and headdress. The chuba is a long "
                             "sleeved dress tied at the waist with a sash.",
                "colors": "Bright colors with traditional patterns"
            },
            "men": {
                "name": "Tibetan Chuba with Boots",
                "description": "Traditional Tibetan men's chuba with boots and hat. "
                             "The chuba is a long robe tied at the waist with a sash. "
                             "Often worn with traditional Tibetan boots.",
                "colors": "Deep colors like maroon, navy, or black"
            }
        }
    },
    "saga_dawa": {
        "name": "Saga Dawa",
        "states": ["Sikkim", "Arunachal Pradesh", "Ladakh"],
        "month": "May-June",
        "description": "Celebrates Buddha's enlightenment and parinirvana. Features prayer "
                      "meetings, processions, and acts of merit. Considered the holiest "
                      "month in the Tibetan Buddhist calendar.",
        "traditional_dress": {
            "women": {
                "name": "Simple Chuba or White Saree",
                "description": "Traditional Tibetan chuba or simple white saree. "
                             "Modest dressing is preferred as it's a solemn occasion. "
                             "Minimal jewelry is worn.",
                "colors": "White or traditional Tibetan colors"
            },
            "men": {
                "name": "Traditional Chuba",
                "description": "Traditional Tibetan chuba with simple accessories. "
                             "Modest dressing is preferred. Some may wear white "
                             "clothes to symbolize purity.",
                "colors": "White or traditional Tibetan colors"
            }
        }
    },
    "lhabab_duchen": {
        "name": "Lhabab Duchen",
        "states": ["Sikkim", "Arunachal Pradesh", "Ladakh"],
        "month": "October-November",
        "description": "Celebrates Buddha's descent from Trayastrimsha heaven. "
                      "Features prayers, meditation, and acts of merit. Considered "
                      "one of the four great holy days in Tibetan Buddhism.",
        "traditional_dress": {
            "women": {
                "name": "Traditional Chuba",
                "description": "Traditional Tibetan chuba with modest accessories. "
                             "Simple and respectful attire is preferred for temple visits. "
                             "Can be paired with traditional apron (pangden).",
                "colors": "Traditional Tibetan colors"
            },
            "men": {
                "name": "Traditional Chuba",
                "description": "Traditional Tibetan chuba with simple accessories. "
                             "Modest dressing is preferred for temple visits. "
                             "Often worn with traditional hat.",
                "colors": "Traditional Tibetan colors"
            }
        }
    },
    "monlam": {
        "name": "Monlam",
        "states": ["Sikkim", "Arunachal Pradesh", "Ladakh"],
        "month": "January-February",
        "description": "Great Prayer Festival. Features extensive prayers, teachings, "
                      "and religious ceremonies. Celebrated with great devotion in "
                      "Tibetan Buddhist communities.",
        "traditional_dress": {
            "women": {
                "name": "Traditional Chuba",
                "description": "Traditional Tibetan chuba with modest accessories. "
                             "Simple and respectful attire is preferred for prayers. "
                             "Traditional jewelry may be worn.",
                "colors": "Traditional Tibetan colors"
            },
            "men": {
                "name": "Traditional Chuba",
                "description": "Traditional Tibetan chuba with simple accessories. "
                             "Modest dressing is preferred for prayers. "
                             "Often worn with traditional hat.",
                "colors": "Traditional Tibetan colors"
            }
        }
    }
}

# Keywords for better matching
FESTIVAL_KEYWORDS = {
    # Hindu Festivals
    "diwali": ["diwali", "deepavali", "festival of lights", "laxmi puja", "diwali dress", "diwali clothes"],
    "holi": ["holi", "festival of colors", "color festival", "holi dress", "holi clothes"],
    "navratri": ["navratri", "navaratri", "nine nights", "garba", "dandiya", "durga puja"],
    "durga_puja": ["durga puja", "durgotsav", "durga festival", "sharadotsav", "durga puja dress", "bengali festival"],
    "ganesh_chaturthi": ["ganesh chaturthi", "ganpati", "vinayaka chaturthi", "ganpati dress", "nauvari saree", "maharashtra festival"],
    "janmashtami": ["janmashtami", "krishna janmashtami", "gokulashtami", "dahi handi", "krishna festival"],
    "onam": ["onam", "kerala festival", "kerala harvest", "onam dress", "kasavu saree", "onasadya"],
    "pongal": ["pongal", "tamil harvest", "tamil festival", "pongal dress", "pavadai sattai", "tamil new year"],
    "makar_sankranti": ["makar sankranti", "sankranti", "pongal", "lohri", "uttarayan", "bihu", "harvest festival"],
    "bihu": ["bihu", "assam festival", "assamese festival", "mekhela chador", "bihu dance"],
    "gudi_padwa": ["gudi padwa", "marathi new year", "ugadi", "maharashtra new year"],
    "ugadi": ["ugadi", "telugu new year", "kannada new year", "panchanga sravanam"],
    "vishu": ["vishu", "malayali new year", "vishu kani", "kerala new year"],
    "karwa_chauth": ["karwa chauth", "karva chauth", "fasting festival", "north indian festival"],
    "rakhi": ["rakhi", "raksha bandhan", "rakhi festival", "brother sister festival"],
    "mahashivratri": ["mahashivratri", "shivratri", "shiva festival", "night of shiva"],

    # Muslim Festivals
    "eid_ul_fitr": ["eid", "eid ul fitr", "ramzan eid", "ramadan eid", "eid dress", "eid clothes", "ramadan festival"],
    "eid_ul_adha": ["eid ul adha", "bakrid", "bakr eid", "sacrifice festival", "eid dress", "eid clothes", "qurbani"],
    "muharram": ["muharram", "islamic new year", "ashura", "mourning festival"],
    "milad_un_nabi": ["milad un nabi", "eid milad", "prophet birthday", "barah wafat"],

    # Christian Festivals
    "christmas": ["christmas", "xmas", "jesus birth", "christmas dress", "christmas clothes", "nativity"],
    "easter": ["easter", "resurrection", "easter sunday", "holy week", "good friday"],
    "good_friday": ["good friday", "crucifixion", "holy friday", "passion friday"],

    # Sikh Festivals
    "gurpurab": ["gurpurab", "guru nanak jayanti", "sikh festival", "guru birthday"],
    "baisakhi": ["baisakhi", "vaisakhi", "sikh new year", "harvest festival", "punjabi festival"],
    "holla_mohalla": ["holla mohalla", "holla", "sikh martial festival", "anandpur sahib"],

    # Jain Festivals
    "paryushana": ["paryushana", "parushan", "jain festival", "forgiveness festival"],
    "mahavir_jayanti": ["mahavir jayanti", "mahavir birthday", "jain festival"],

    # Buddhist Festivals
    "buddha_purnima": ["buddha purnima", "buddha jayanti", "vesak", "buddha birthday", 
                       "enlightenment day", "buddha festival"],
    "losar": ["losar", "tibetan new year", "buddhist new year", "himalayan new year", 
              "tibetan festival", "chuba festival"],
    "saga_dawa": ["saga dawa", "buddha enlightenment", "tibetan holy month", 
                  "buddhist holy month", "merit month"],
    "lhabab_duchen": ["lhabab duchen", "buddha descent", "tibetan festival", 
                      "buddhist holy day", "heaven descent"],
    "monlam": ["monlam", "great prayer festival", "tibetan prayer festival", 
               "buddhist prayer festival", "prayer month"]
} 