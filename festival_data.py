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
            "Mysore Silk Saree (Karnataka)"
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
            "Designer Lehenga"
        ],
        "occasions": "Weddings, Festivals, Parties, Special Occasions"
    },
    "kurta": {
        "name": "Kurta",
        "description": "A loose-fitting shirt or tunic that falls to the knees or lower. It is worn by both "
                      "men and women across India, often paired with pajamas, churidar, or jeans.",
        "how_to_wear": "For men:\n"
                      "1. Wear a kurta with straight-cut pajama or churidar\n"
                      "2. Can be paired with a Nehru jacket for formal occasions\n"
                      "For women:\n"
                      "1. Wear with leggings, churidar, or jeans\n"
                      "2. Can be paired with a dupatta for traditional look",
        "types": [
            "Pathani Kurta",
            "Anarkali Kurta",
            "Straight Cut Kurta",
            "Designer Kurta"
        ],
        "occasions": "Daily Wear, Festivals, Religious Ceremonies, Casual Events"
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
            "Temple Dhoti"
        ],
        "occasions": "Religious Ceremonies, Weddings, Festivals, Traditional Events"
    }
}

# Keywords for traditional attire
ATTIRE_KEYWORDS = {
    "saree": ["saree", "sari", "sarees", "sarong", "traditional dress", "indian dress", "how to wear saree"],
    "lehenga": ["lehenga", "lehenga choli", "lehengas", "choli", "indian skirt", "traditional skirt"],
    "kurta": ["kurta", "kurti", "kurtas", "indian tunic", "traditional shirt", "pathani", "anarkali"],
    "dhoti": ["dhoti", "veshti", "mundu", "traditional lower garment", "indian lower garment"]
}

FESTIVAL_DATABASE = {
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
    "bihu": {
        "name": "Bihu",
        "states": ["Assam"],
        "month": "April",
        "description": "Assam's harvest festival celebrated three times a year. "
                      "Features traditional Bihu dance, music, and feasting."
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
    "lohri": {
        "name": "Lohri",
        "states": ["Punjab", "Haryana", "Himachal Pradesh"],
        "month": "January",
        "description": "Celebrates the winter solstice and harvest. "
                      "Features bonfires, traditional songs, and distribution of sweets."
    },
    "baisakhi": {
        "name": "Baisakhi",
        "states": ["Punjab", "Haryana"],
        "month": "April",
        "description": "Celebrates the harvest of rabi crops and the Sikh New Year. "
                      "Features bhangra dance, fairs, and community feasts."
    },
    "rakhi": {
        "name": "Raksha Bandhan",
        "states": ["All India"],
        "month": "August",
        "description": "Celebrates the bond between brothers and sisters. "
                      "Features tying of rakhi threads and exchange of gifts."
    },
    "janmashtami": {
        "name": "Janmashtami",
        "states": ["All India", "Uttar Pradesh", "Maharashtra", "Gujarat"],
        "month": "August-September",
        "description": "Celebrates the birth of Lord Krishna. "
                      "Features fasting, prayers, and dahi handi celebrations."
    },
    "karwa_chauth": {
        "name": "Karwa Chauth",
        "states": ["North India", "Punjab", "Haryana", "Uttar Pradesh", "Rajasthan"],
        "month": "October-November",
        "description": "A festival where married women fast for their husbands' longevity. "
                      "Features fasting, prayers, and moon sighting ceremonies."
    },
    "navratri": {
        "name": "Navratri",
        "states": ["All India", "Gujarat", "West Bengal", "Maharashtra"],
        "month": "September-October",
        "description": "Nine nights of worship dedicated to Goddess Durga. "
                      "Features garba dance, fasting, and cultural programs."
    },
    "makar_sankranti": {
        "name": "Makar Sankranti",
        "states": ["All India"],
        "month": "January",
        "description": "Celebrates the sun's entry into Capricorn. "
                      "Features kite flying, sesame sweets, and holy dips in rivers."
    },
    "gudi_padwa": {
        "name": "Gudi Padwa",
        "states": ["Maharashtra", "Karnataka", "Andhra Pradesh"],
        "month": "March-April",
        "description": "Celebrates the Marathi New Year. "
                      "Features raising of Gudi flags and traditional feasts."
    },
    "buddha_purnima": {
        "name": "Buddha Purnima",
        "states": ["All India", "Bihar", "Uttar Pradesh"],
        "month": "April-May",
        "description": "Celebrates the birth, enlightenment, and death of Gautama Buddha. "
                      "Features prayers, meditation, and acts of charity."
    },
    "gurpurab": {
        "name": "Gurpurab",
        "states": ["Punjab", "Haryana", "Delhi"],
        "month": "Varies (Based on Sikh Calendar)",
        "description": "Celebrates the birth anniversaries of Sikh Gurus. "
                      "Features prayers, langar (community kitchen), and processions."
    }
}

# Keywords for better matching
FESTIVAL_KEYWORDS = {
    "diwali": ["diwali", "deepavali", "festival of lights", "laxmi puja", "diwali dress", "diwali clothes"],
    "holi": ["holi", "festival of colors", "color festival", "holi dress", "holi clothes"],
    "pongal": ["pongal", "tamil harvest", "tamil festival", "pongal dress", "pavadai sattai"],
    "bihu": ["bihu", "assam festival", "assamese festival"],
    "onam": ["onam", "kerala festival", "kerala harvest", "onam dress", "kasavu saree"],
    "durga_puja": ["durga puja", "durgotsav", "durga festival", "sharadotsav", "durga puja dress"],
    "ganesh_chaturthi": ["ganesh chaturthi", "ganpati", "vinayaka chaturthi", "ganpati dress", "nauvari saree"],
    "eid_ul_fitr": ["eid", "eid ul fitr", "ramzan eid", "ramadan eid", "eid dress", "eid clothes"],
    "eid_ul_adha": ["eid ul adha", "bakrid", "bakr eid", "sacrifice festival", "eid dress", "eid clothes"],
    "christmas": ["christmas", "xmas", "jesus birth", "christmas dress", "christmas clothes"],
    "lohri": ["lohri", "punjabi winter festival"],
    "baisakhi": ["baisakhi", "vaisakhi", "sikh new year"],
    "rakhi": ["rakhi", "raksha bandhan", "rakhi festival"],
    "janmashtami": ["janmashtami", "krishna janmashtami", "gokulashtami"],
    "karwa_chauth": ["karwa chauth", "karva chauth", "fasting festival"],
    "navratri": ["navratri", "navaratri", "nine nights"],
    "makar_sankranti": ["makar sankranti", "sankranti", "pongal", "lohri"],
    "gudi_padwa": ["gudi padwa", "marathi new year", "ugadi"],
    "buddha_purnima": ["buddha purnima", "buddha jayanti", "vesak"],
    "gurpurab": ["gurpurab", "guru nanak jayanti", "sikh festival"]
} 