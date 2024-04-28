# Array of Nepali letters
ucode=0
nepali_letters = [
    "अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ",
    "क", "का", "कि", "की", "कु", "कू", "के", "कै", "को", "कौ",
    "ख", "खा", "खि", "खी", "खु", "खू", "खे", "खै", "खो", "खौ",
    "ग", "गा", "गि", "गी", "गु", "गू", "गे", "गै", "गो", "गौ",
    "घ", "घा", "घि", "घी", "घु", "घू", "घे", "घै", "घो", "घौ",
    "ङ", "ङा", "ङि", "ङी", "ङु", "ङू", "ङे", "ङै", "ङो", "ङौ",
    "च", "चा", "चि", "ची", "चु", "चू", "चे", "चै", "चो", "चौ",
    "छ", "छा", "छि", "छी", "छु", "छू", "छे", "छै", "छो", "छौ",
    "ज", "जा", "जि", "जी", "जु", "जू", "जे", "जै", "जो", "जौ",
    "झ", "झा", "झि", "झी", "झु", "झू", "झे", "झै", "झो", "झौ",
    "ञ", "ञा", "ञि", "ञी", "ञु", "ञू", "ञे", "ञै", "ञो", "ञौ",
    "ट", "टा", "टि", "टी", "टु", "टू", "टे", "टै", "टो", "टौ",
    "ठ", "ठा", "ठि", "ठी", "ठु", "ठू", "ठे", "ठै", "ठो", "ठौ",
    "ड", "डा", "डि", "डी", "डु", "डू", "डे", "डै", "डो", "डौ",
    "ढ", "ढा", "ढि", "ढी", "ढु", "ढू", "ढे", "ढै", "ढो", "ढौ",
    "ण", "णा", "णि", "णी", "णु", "णू", "णे", "णै", "णो", "णौ",
    "त", "ता", "ति", "ती", "तु", "तू", "ते", "तै", "तो", "तौ",
    "थ", "था", "थि", "थी", "थु", "थू", "थे", "थै", "थो", "थौ",
    "द", "दा", "दि", "दी", "दु", "दू", "दे", "दै", "दो", "दौ",
    "ध", "धा", "धि", "धी", "धु", "धू", "धे", "धै", "धो", "धौ",
    "न", "ना", "नि", "नी", "नु", "नू", "ने", "नै", "नो", "नौ",
    "प", "पा", "पि", "पी", "पु", "पू", "पे", "पै", "पो", "पौ",
    "फ", "फा", "फि", "फी", "फु", "फू", "फे", "फै", "फो", "फौ",
    "ब", "बा", "बि", "बी", "बु", "बू", "बे", "बै", "बो", "बौ",
    "भ", "भा", "भि", "भी", "भु", "भू", "भे", "भै", "भो", "भौ",
    "म", "मा", "मि", "मी", "मु", "मू", "मे", "मै", "मो", "मौ",
    "य", "या", "यि", "यी", "यु", "यू", "ये", "यै", "यो", "यौ",
    "र", "रा", "रि", "री", "रु", "रू", "रे", "रै", "रो", "रौ",
    "ल", "ला", "लि", "ली", "लु", "लू", "ले", "लै", "लो", "लौ",
    "व", "वा", "वि", "वी", "वु", "वू", "वे", "वै", "वो", "वौ",
    "श", "शा", "शि", "शी", "शु", "शू", "शे", "शै", "शो", "शौ",
    "ष", "षा", "षि", "षी", "षु", "षू", "षे", "षै", "षो", "षौ",
    "स", "सा", "सि", "सी", "सु", "सू", "से", "सै", "सो", "सौ",
    "ह", "हा", "हि", "ही", "हु", "हू", "हे", "है", "हो", "हौ",
    "क्ष", "क्षा", "क्षि", "क्षी", "क्षु", "क्षू", "क्षे", "क्षै", "क्षो", "क्षौ",
    "त्र", "त्रा", "त्रि", "त्री", "त्रु", "त्रू", "त्रे", "त्रै", "त्रो", "त्रौ",
    "ज्ञ", "ज्ञा", "ज्ञि", "ज्ञी", "ज्ञु", "ज्ञू", "ज्ञे", "ज्ञै", "ज्ञो", "ज्ञौ",    
    "०", "१", "२", "३", "४", "५", "६", "७", "८", "९"
]

for n in nepali_letters:
    ucode=ucode+1
    print(n,ucode)