# -*- coding: utf-8 -*-
"""Legal page copy (privacy, terms, cookies, refund) in English and Spanish."""

UPDATED = {"en": "Last updated: October 2, 2026", "es": "Última actualización: 2 de octubre de 2026"}
EMAIL = "anamariapalacios1608@gmail.com"
PHONE = "+1 (954) 534-1345"
TEL = "+19545341345"

MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
CONTACT = {
    "en": [("ul", ["AMP Insurance Assistance, Ana María Palacios",
                   f"Email: {MAIL}",
                   f'WhatsApp or phone: <a href="tel:{TEL}">{PHONE}</a>',
                   'Instagram: <a href="https://instagram.com/amptravelinsurance" rel="noopener">@amptravelinsurance</a>'])],
    "es": [("ul", ["AMP Insurance Assistance, Ana María Palacios",
                   f"Correo: {MAIL}",
                   f'WhatsApp o teléfono: <a href="tel:{TEL}">{PHONE}</a>',
                   'Instagram: <a href="https://instagram.com/amptravelinsurance" rel="noopener">@amptravelinsurance</a>'])],
}
GH = "https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement"
WAP = "https://www.whatsapp.com/legal/privacy-policy"
WAT = "https://www.whatsapp.com/legal/terms-of-service"

LEGAL = {}

LEGAL["privacy"] = {
 "file": "privacy.html",
 "title": {"en": "Privacy Policy", "es": "Política de privacidad"},
 "desc": {"en": "How AMP Insurance Assistance handles the information you share through this website and WhatsApp.",
          "es": "Cómo AMP Insurance Assistance maneja la información que compartes en este sitio y por WhatsApp."},
 "intro": {
  "en": "This policy explains what information this website handles and how Ana María Palacios (\"I\" or \"me\"), who runs AMP Insurance Assistance, uses it. If you have a question, contact me using the details at the end.",
  "es": "Esta política explica qué información maneja este sitio web y cómo la usa Ana María Palacios (\"yo\"), quien dirige AMP Insurance Assistance. Si tienes alguna pregunta, contáctame con los datos al final."},
 "sections": {
  "en": [
   ("What this site collects", [
     "This site has no database and no user accounts. It does not store what you type in the quote form. When you press \"Send on WhatsApp\", your browser builds a message from your answers and opens WhatsApp. Nothing reaches me unless you press send inside WhatsApp.",
     "The quote form asks only for what a first quote needs, depending on the type of insurance:",
     ("ul", ["<b>Auto:</b> the ZIP code where the car is kept, each driver's name and date of birth, each vehicle's year, make, and model, and optionally the coverage you want and your current insurer",
             "<b>Home and property:</b> property type and ZIP code, the owner's name and date of birth, and optionally the year built, your current insurer, and extra coverage you want quoted",
             "<b>Renters:</b> the ZIP code of your rental, your name and date of birth, and optionally your move-in date and the rough value of your belongings",
             "<b>Travel:</b> each traveler's name and date of birth, where the trip starts and goes, your country of residence, and optionally travel dates, trip purpose, and coverage preferences",
             "<b>Business:</b> business name, what it does, its ZIP code, your name, and optionally years in business, number of employees, and the coverage you need",
             "<b>For every type:</b> optionally a WhatsApp number and an email address"]),
     "When you message me on WhatsApp, I also see your WhatsApp phone number and profile name, as with any WhatsApp message.",
     "Only include people who agreed to share their details with me. Please do not send driver's license numbers, VINs, Social Security numbers, health information, passport numbers, or payment details through the form. If a quote needs more information, I will tell you what is needed and why."]),
   ("How I use your information", [
     ("ul", ["To prepare and send you quotes",
             "To answer your questions",
             "To help you buy and use a policy you choose",
             "To keep records that the law requires"]),
     "I do not sell or rent your information. I do not use it for advertising, and I do not add you to marketing lists without your permission."]),
   ("Who else receives it", [
     ("ul", [f"<b>WhatsApp (Meta)</b> carries our messages. <a href=\"{WAP}\" rel=\"noopener\">WhatsApp's privacy policy</a> applies to its service.",
             "<b>AGB Insurance</b>, the insurance agency I work through for auto, home, renters, and business insurance, and its licensed agents receive the details needed to prepare a quote or issue a policy when you ask me to do that.",
             "<b>Best Travel Assistance</b> receives the details needed to quote or issue a travel plan when you ask me for travel insurance.",
             "<b>Insurance companies</b> receive the details needed to price or issue the policy you ask about. They handle it under their own privacy notices.",
             f"<b>GitHub</b> hosts this website and may log technical data, such as your IP address, to deliver and protect the site. See the <a href=\"{GH}\" rel=\"noopener\">GitHub privacy statement</a>.",
             "<b>Email</b>: if you write to me by email, your message is handled by my email provider.",
             "<b>Authorities</b>, when the law requires me to share information."]),
     "If you buy a policy, the company that issues it will give you its own privacy notice explaining how it handles your information."]),
   ("Cookies and tracking", [
     "This site does not use cookies, analytics, or advertising trackers. It saves your language choice (English or Spanish) in your own browser. The <a href=\"cookies.html\">Cookie Policy</a> has the details."]),
   ("How long I keep it", [
     "I keep our conversations only as long as I need them for the purposes above, plus any period that insurance record-keeping rules require. You can ask me to delete your details sooner, unless the law requires me to keep them."]),
   ("Your choices and rights", [
     ("ul", ["Ask me what information I have about you",
             "Ask me to correct or delete it",
             "Tell me to stop contacting you at any time"]),
     "Depending on where you live, such as California, the European Union, or Colombia, you may have more rights under local law. To use any of these rights, contact me. I will answer as soon as I can and within any deadline the law sets."]),
   ("Children", [
     "This site is not directed to children under 13, and I do not knowingly collect information from them. A parent or guardian may include a child's name and date of birth in a quote request, for example as a traveler or a driver on a family policy."]),
   ("Security", [
     "WhatsApp encrypts messages end to end. I take reasonable steps to protect the information you send me, but no method of sending or storing information is completely secure."]),
   ("Do Not Track", [
     "This site does not track you across other websites, so it works the same way whether or not your browser sends a Do Not Track or Global Privacy Control signal."]),
   ("Visitors outside the United States", [
     "I work from the United States. If you contact me from another country, your information will be handled in the United States."]),
   ("Changes to this policy", [
     "If I change this policy, I will update the date at the top of this page."]),
   ("Contact", CONTACT["en"]),
  ],
  "es": [
   ("Qué recoge este sitio", [
     "Este sitio no tiene base de datos ni cuentas de usuario. No guarda lo que escribes en el formulario de cotización. Cuando presionas \"Enviar por WhatsApp\", tu navegador arma un mensaje con tus respuestas y abre WhatsApp. No me llega nada a menos que toques enviar dentro de WhatsApp.",
     "El formulario pide solo lo que necesita una primera cotización, según el tipo de seguro:",
     ("ul", ["<b>Auto:</b> el código postal donde se guarda el auto, el nombre y la fecha de nacimiento de cada conductor, el año, la marca y el modelo de cada vehículo, y de forma opcional la cobertura que quieres y tu aseguradora actual",
             "<b>Hogar y propiedad:</b> tipo de propiedad y código postal, el nombre y la fecha de nacimiento del dueño, y de forma opcional el año de construcción, tu aseguradora actual y coberturas extra que quieras cotizar",
             "<b>Inquilinos:</b> el código postal de tu alquiler, tu nombre y fecha de nacimiento, y de forma opcional tu fecha de mudanza y el valor aproximado de tus pertenencias",
             "<b>Viaje:</b> el nombre y la fecha de nacimiento de cada viajero, dónde empieza y a dónde va el viaje, tu país de residencia, y de forma opcional las fechas, el motivo del viaje y tus preferencias de cobertura",
             "<b>Negocio:</b> nombre del negocio, a qué se dedica, su código postal, tu nombre, y de forma opcional los años en operación, el número de empleados y la cobertura que necesitas",
             "<b>Para todos:</b> de forma opcional un número de WhatsApp y un correo electrónico"]),
     "Cuando me escribes por WhatsApp, también veo tu número de WhatsApp y tu nombre de perfil, como en cualquier mensaje de WhatsApp.",
     "Incluye solo a personas que aceptaron compartir sus datos conmigo. Por favor no envíes por el formulario números de licencia de conducir, VIN, Seguro Social, información de salud, números de pasaporte ni datos de pago. Si una cotización necesita más información, te diré qué hace falta y por qué."]),
   ("Cómo uso tu información", [
     ("ul", ["Para preparar y enviarte cotizaciones",
             "Para responder tus preguntas",
             "Para ayudarte a comprar y usar la póliza que elijas",
             "Para guardar los registros que exige la ley"]),
     "No vendo ni alquilo tu información. No la uso para publicidad y no te agrego a listas de mercadeo sin tu permiso."]),
   ("Quién más la recibe", [
     ("ul", [f"<b>WhatsApp (Meta)</b> transmite nuestros mensajes. La <a href=\"{WAP}\" rel=\"noopener\">política de privacidad de WhatsApp</a> aplica a su servicio.",
             "<b>AGB Insurance</b>, la agencia de seguros con la que trabajo para seguros de auto, hogar, inquilinos y negocios, y sus agentes con licencia reciben los datos necesarios para preparar una cotización o emitir una póliza cuando me pides hacerlo.",
             "<b>Best Travel Assistance</b> recibe los datos necesarios para cotizar o emitir un plan de viaje cuando me pides un seguro de viaje.",
             "<b>Compañías de seguros</b> reciben los datos necesarios para cotizar o emitir la póliza que consultas. Ellas los manejan según sus propios avisos de privacidad.",
             f"<b>GitHub</b> aloja este sitio y puede registrar datos técnicos, como tu dirección IP, para entregar y proteger el sitio. Consulta la <a href=\"{GH}\" rel=\"noopener\">declaración de privacidad de GitHub</a>.",
             "<b>Correo electrónico</b>: si me escribes por correo, tu mensaje lo maneja mi proveedor de correo.",
             "<b>Autoridades</b>, cuando la ley me obligue a compartir información."]),
     "Si compras una póliza, la compañía que la emite te dará su propio aviso de privacidad sobre cómo maneja tu información."]),
   ("Cookies y rastreo", [
     "Este sitio no usa cookies, analítica ni rastreadores de publicidad. Guarda tu elección de idioma (inglés o español) en tu propio navegador. La <a href=\"cookies.html\">Política de cookies</a> tiene los detalles."]),
   ("Cuánto tiempo la guardo", [
     "Guardo nuestras conversaciones solo mientras las necesite para los fines anteriores, más el tiempo que exijan las normas de registros de seguros. Puedes pedirme que borre tus datos antes, salvo que la ley me obligue a conservarlos."]),
   ("Tus opciones y derechos", [
     ("ul", ["Preguntarme qué información tengo sobre ti",
             "Pedirme que la corrija o la borre",
             "Pedirme que deje de contactarte en cualquier momento"]),
     "Según dónde vivas, por ejemplo California, la Unión Europea o Colombia, puedes tener más derechos bajo la ley local. Para ejercer cualquiera de ellos, contáctame. Te responderé lo antes posible y dentro de cualquier plazo que fije la ley."]),
   ("Menores de edad", [
     "Este sitio no está dirigido a menores de 13 años y no recojo a sabiendas información de ellos. Un padre, madre o tutor puede incluir el nombre y la fecha de nacimiento de un menor en una solicitud de cotización, por ejemplo como viajero o como conductor en una póliza familiar."]),
   ("Seguridad", [
     "WhatsApp cifra los mensajes de extremo a extremo. Tomo medidas razonables para proteger la información que me envías, pero ningún método de envío o almacenamiento es completamente seguro."]),
   ("No rastrear (Do Not Track)", [
     "Este sitio no te rastrea en otros sitios web, así que funciona igual si tu navegador envía o no una señal de Do Not Track o Global Privacy Control."]),
   ("Visitantes fuera de Estados Unidos", [
     "Trabajo desde Estados Unidos. Si me contactas desde otro país, tu información se manejará en Estados Unidos."]),
   ("Cambios a esta política", [
     "Si cambio esta política, actualizaré la fecha al inicio de esta página."]),
   ("Contacto", CONTACT["es"]),
  ]}
}

LEGAL["cookies"] = {
 "file": "cookies.html",
 "title": {"en": "Cookie Policy", "es": "Política de cookies"},
 "desc": {"en": "This site uses no cookies, analytics, or ad trackers. It only remembers your language choice in your browser.",
          "es": "Este sitio no usa cookies, analítica ni rastreadores de publicidad. Solo recuerda tu idioma en tu navegador."},
 "intro": {"en": "Short version: this site does not use cookies, analytics, advertising pixels, or embedded third-party content.",
           "es": "En resumen: este sitio no usa cookies, analítica, píxeles de publicidad ni contenido incrustado de terceros."},
 "sections": {
  "en": [
   ("What the site stores", [
     "One item in your browser's local storage:",
     ("ul", ["<b>Name:</b> amp_lang",
             "<b>Value:</b> \"en\" or \"es\"",
             "<b>Purpose:</b> remembers the language you picked so the site shows it next time",
             "<b>Where it lives:</b> only on your device. The site never sends it to me or anyone else.",
             "<b>How long:</b> until you clear your browser's site data"])]),
   ("Fonts and icons", [
     "The fonts and icons are hosted on this site, so opening a page does not contact Google Fonts or any other font service."]),
   ("Hosting", [
     f"GitHub Pages delivers this site. GitHub may process technical data, such as your IP address, to deliver and protect it. See the <a href=\"{GH}\" rel=\"noopener\">GitHub privacy statement</a>."]),
   ("Links to other services", [
     "The WhatsApp and Instagram links take you to those services. They use their own cookies under their own policies once you get there."]),
   ("Why there is no cookie banner", [
     "Cookie consent laws require permission before a site stores information that is not needed for something you asked for. This site sets no cookies, and the only thing it stores is the language you chose. If I ever add analytics or other tracking, I will update this policy and ask for your consent where the law requires it."]),
   ("Contact", CONTACT["en"]),
  ],
  "es": [
   ("Qué guarda el sitio", [
     "Un elemento en el almacenamiento local de tu navegador:",
     ("ul", ["<b>Nombre:</b> amp_lang",
             "<b>Valor:</b> \"en\" o \"es\"",
             "<b>Propósito:</b> recuerda el idioma que elegiste para mostrarlo la próxima vez",
             "<b>Dónde está:</b> solo en tu dispositivo. El sitio nunca me lo envía a mí ni a nadie.",
             "<b>Cuánto dura:</b> hasta que borres los datos del sitio en tu navegador"])]),
   ("Fuentes e íconos", [
     "Las fuentes y los íconos están alojados en este sitio, así que abrir una página no contacta a Google Fonts ni a ningún otro servicio de fuentes."]),
   ("Alojamiento", [
     f"GitHub Pages entrega este sitio. GitHub puede procesar datos técnicos, como tu dirección IP, para entregarlo y protegerlo. Consulta la <a href=\"{GH}\" rel=\"noopener\">declaración de privacidad de GitHub</a>."]),
   ("Enlaces a otros servicios", [
     "Los enlaces de WhatsApp e Instagram te llevan a esos servicios. Ellos usan sus propias cookies según sus propias políticas cuando llegas allí."]),
   ("Por qué no hay aviso de cookies", [
     "Las leyes de consentimiento de cookies exigen permiso antes de que un sitio guarde información que no es necesaria para algo que pediste. Este sitio no usa cookies, y lo único que guarda es el idioma que elegiste. Si algún día agrego analítica u otro rastreo, actualizaré esta política y pediré tu consentimiento cuando la ley lo exija."]),
   ("Contacto", CONTACT["es"]),
  ]}
}

LEGAL["terms"] = {
 "file": "terms.html",
 "title": {"en": "Terms and Conditions", "es": "Términos y condiciones"},
 "desc": {"en": "The terms for using this website and requesting an insurance quote from AMP Insurance Assistance.",
          "es": "Los términos para usar este sitio y pedir una cotización de seguro a AMP Insurance Assistance."},
 "intro": {"en": "By using this website you agree to these terms. If you do not agree, please do not use the site.",
           "es": "Al usar este sitio aceptas estos términos. Si no estás de acuerdo, por favor no uses el sitio."},
 "sections": {
  "en": [
   ("About this site", [
     "Ana María Palacios runs this website under the name AMP Insurance Assistance. It shares general information about auto, home, renters, travel, and business insurance and lets you request a quote through WhatsApp.",
     "Ana is a licensed travel insurance agent, and travel plans are offered through Best Travel Assistance. For auto, home, renters, and business insurance, she acts as your advisor, and a licensed agent at AGB Insurance, an independent insurance agency, prepares your quote and issues your policy."]),
   ("General information only", [
     "The content on this site is general information. It is not legal, financial, or tax advice, and it does not describe the terms of any specific policy. Laws and requirements mentioned on this site can change."]),
   ("Quotes", [
     ("ul", ["Quotes are free and you have no obligation to buy.",
             "A quote is an estimate based on the information you give. The final price, eligibility, and coverage are set by the company that issues the policy when you apply.",
             "Prices and policies can change until a policy is issued.",
             "Please give accurate information. Wrong or missing information can change your price or affect a claim."])]),
   ("Policies", [
     "If you buy a policy, your contract is with the company that issues it, not with this website. The policy documents decide what is covered, including benefits, limits, deductibles, exclusions, and how claims work. Please read them before you buy, and ask me about anything that is unclear."]),
   ("Payments and refunds", [
     "This website does not take payments. See the <a href=\"refund.html\">Refund Policy</a> for how cancellations and refunds work."]),
   ("WhatsApp", [
     f"The quote form opens WhatsApp with a message you can review before you send it. Your use of WhatsApp is subject to <a href=\"{WAT}\" rel=\"noopener\">WhatsApp's terms</a>."]),
   ("Using the site", [
     "Please do not misuse the site, try to break or overload it, or send other people's information without their permission."]),
   ("Ownership", [
     "The text, design, and AMP logo belong to Ana María Palacios or the people who licensed them to her. The AGB Insurance and Best Travel Assistance names and logos belong to their owners and are used with permission. Photos are used under their licenses. Please do not copy content from this site for commercial use without permission."]),
   ("Links", [
     "Links to other websites are for convenience. I do not control those sites and I am not responsible for their content or practices."]),
   ("No guarantees", [
     "I work to keep this site accurate, but it may contain errors or become out of date. The site is provided \"as is\"."]),
   ("Limits on liability", [
     "To the extent the law allows, I am not responsible for indirect losses caused by using this website. Nothing in these terms limits rights you have under consumer protection or insurance laws that cannot be limited."]),
   ("Accessibility", [
     "I want everyone to be able to use this site, and I work toward the WCAG 2.1 AA guidelines. If any part of the site is hard to use, contact me and I will help you another way."]),
   ("Changes to these terms", [
     "If I change these terms, I will update the date at the top of this page."]),
   ("Contact", CONTACT["en"]),
  ],
  "es": [
   ("Sobre este sitio", [
     "Ana María Palacios administra este sitio bajo el nombre AMP Insurance Assistance. El sitio comparte información general sobre seguros de auto, hogar, inquilinos, viaje y negocios, y te permite pedir una cotización por WhatsApp.",
     "Ana es agente con licencia de seguros de viaje, y los planes de viaje se ofrecen a través de Best Travel Assistance. Para seguros de auto, hogar, inquilinos y negocios, ella es tu asesora, y un agente con licencia de AGB Insurance, una agencia de seguros independiente, prepara tu cotización y emite tu póliza."]),
   ("Solo información general", [
     "El contenido de este sitio es información general. No es asesoría legal, financiera ni tributaria, y no describe los términos de ninguna póliza específica. Las leyes y requisitos mencionados en este sitio pueden cambiar."]),
   ("Cotizaciones", [
     ("ul", ["Las cotizaciones son gratis y no tienes obligación de comprar.",
             "Una cotización es un estimado basado en la información que das. El precio final, la elegibilidad y la cobertura los define la compañía que emite la póliza cuando la solicitas.",
             "Los precios y las pólizas pueden cambiar hasta que se emite una póliza.",
             "Por favor da información correcta. Información errónea o incompleta puede cambiar tu precio o afectar un reclamo."])]),
   ("Pólizas", [
     "Si compras una póliza, tu contrato es con la compañía que la emite, no con este sitio. Los documentos de la póliza definen qué cubre, incluidos beneficios, límites, deducibles, exclusiones y cómo funcionan los reclamos. Léelos antes de comprar y pregúntame lo que no esté claro."]),
   ("Pagos y reembolsos", [
     "Este sitio no recibe pagos. Consulta la <a href=\"refund.html\">Política de reembolsos</a> para saber cómo funcionan las cancelaciones y los reembolsos."]),
   ("WhatsApp", [
     f"El formulario abre WhatsApp con un mensaje que puedes revisar antes de enviarlo. Tu uso de WhatsApp está sujeto a los <a href=\"{WAT}\" rel=\"noopener\">términos de WhatsApp</a>."]),
   ("Uso del sitio", [
     "Por favor no hagas mal uso del sitio, no intentes dañarlo o sobrecargarlo, y no envíes información de otras personas sin su permiso."]),
   ("Propiedad", [
     "Los textos, el diseño y el logo AMP pertenecen a Ana María Palacios o a quienes le dieron licencia. Los nombres y logos de AGB Insurance y Best Travel Assistance pertenecen a sus dueños y se usan con permiso. Las fotos se usan bajo sus licencias. Por favor no copies contenido de este sitio para uso comercial sin permiso."]),
   ("Enlaces", [
     "Los enlaces a otros sitios son para tu conveniencia. No controlo esos sitios y no soy responsable de su contenido ni de sus prácticas."]),
   ("Sin garantías", [
     "Trabajo para que este sitio sea preciso, pero puede tener errores o quedar desactualizado. El sitio se ofrece \"tal cual\"."]),
   ("Límites de responsabilidad", [
     "En la medida que la ley lo permita, no soy responsable por pérdidas indirectas causadas por el uso de este sitio. Nada en estos términos limita derechos que tengas bajo leyes de protección al consumidor o de seguros que no se puedan limitar."]),
   ("Accesibilidad", [
     "Quiero que todos puedan usar este sitio y trabajo para cumplir las pautas WCAG 2.1 AA. Si alguna parte del sitio es difícil de usar, contáctame y te ayudo por otro medio."]),
   ("Cambios a estos términos", [
     "Si cambio estos términos, actualizaré la fecha al inicio de esta página."]),
   ("Contacto", CONTACT["es"]),
  ]}
}

LEGAL["refund"] = {
 "file": "refund.html",
 "title": {"en": "Refund Policy", "es": "Política de reembolsos"},
 "desc": {"en": "Quotes are free. Refunds on a policy you buy follow that policy's terms. Here is how to ask for one.",
          "es": "Las cotizaciones son gratis. Los reembolsos de una póliza siguen sus términos. Así puedes pedir uno."},
 "intro": {"en": "This website does not sell anything or take payments, and quotes are free. There is nothing to refund for using the site or getting a quote.",
           "es": "Este sitio no vende nada ni recibe pagos, y las cotizaciones son gratis. No hay nada que reembolsar por usar el sitio o pedir una cotización."},
 "sections": {
  "en": [
   ("If you buy a policy", [
     "Cancellations and refunds are set by your policy's terms and the law that applies to it.",
     ("ul", ["<b>Auto, home, renters, and business policies:</b> you can usually cancel at any time. Any refund of unused premium is calculated under the policy's terms, and some policies charge a cancellation fee.",
             "<b>Travel plans:</b> many plans allow a full refund if you cancel within a review period after you buy, as long as the trip has not started and no claim has been made. The length of that period and its conditions vary by plan."]),
     "Check your policy documents for the exact rules."]),
   ("How to ask for a refund", [
     ("ul", ["Message me on WhatsApp or by email with your name and policy number.",
             "I will explain what your policy allows and help you send the request to the company that issued it.",
             "That company decides the request and pays any refund, usually to your original payment method."])]),
   ("Contact", CONTACT["en"]),
  ],
  "es": [
   ("Si compras una póliza", [
     "Las cancelaciones y los reembolsos los definen los términos de tu póliza y la ley que le aplica.",
     ("ul", ["<b>Pólizas de auto, hogar, inquilinos y negocio:</b> normalmente puedes cancelar en cualquier momento. Cualquier reembolso de prima no usada se calcula según los términos de la póliza, y algunas pólizas cobran un cargo por cancelación.",
             "<b>Planes de viaje:</b> muchos planes permiten un reembolso completo si cancelas dentro de un período de revisión después de comprar, siempre que el viaje no haya empezado y no se haya hecho ningún reclamo. La duración de ese período y sus condiciones cambian según el plan."]),
     "Revisa los documentos de tu póliza para conocer las reglas exactas."]),
   ("Cómo pedir un reembolso", [
     ("ul", ["Escríbeme por WhatsApp o por correo con tu nombre y número de póliza.",
             "Te explico lo que permite tu póliza y te ayudo a enviar la solicitud a la compañía que la emitió.",
             "Esa compañía decide la solicitud y paga cualquier reembolso, normalmente al método de pago original."])]),
   ("Contacto", CONTACT["es"]),
  ]}
}

LEGAL_ORDER = ["privacy", "terms", "cookies", "refund"]
