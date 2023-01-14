from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import os
from os import path
import pyttsx3
from gtts import gTTS
from playsound2 import playsound

wel = pyttsx3.init()
voices = wel.getProperty('voices')
wel.setProperty('voices', voices[0].id)
FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),"enviroment.ui"))
class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.mandel_buttons()
        self.mandel_editeline()

    def mandel_buttons(self):
        self.pushButton_2.clicked.connect(self.edit_mywighttab)
        self.pushButton_3.clicked.connect(self.edit_mywighttab1)
        self.pushButton_4.clicked.connect(self.edit_mywighttab2)
        self.pushButton_5.clicked.connect(self.edit_mywighttab3)
        self.pushButton_6.clicked.connect(self.edit_mywighttab4)
        self.pushButton_7.clicked.connect(self.edit_mywighttab5)
        self.pushButton_11.clicked.connect(self.edit_mywighttab8)
        self.pushButton_8.clicked.connect(self.read)
        self.pushButton_14.clicked.connect(self.read1)
        self.pushButton_29.clicked.connect(self.read2)
        self.pushButton_31.clicked.connect(self.read4)
        self.pushButton_44.clicked.connect(self.read5)
        self.pushButton_47.clicked.connect(self.read6)
        self.pushButton_12.clicked.connect(self.text2voice)
        self.pushButton_13.clicked.connect(self.text2voice1)
        self.pushButton_28.clicked.connect(self.text2voice2)
        self.pushButton_30.clicked.connect(self.text2voice4)
        self.pushButton_43.clicked.connect(self.text2voice5)
        self.pushButton_48.clicked.connect(self.text2voice6)
        self.pushButton_17.clicked.connect(self.playvideo1)
        self.pushButton_18.clicked.connect(self.playvideo2)
        self.pushButton_27.clicked.connect(self.playvideo3)
        self.pushButton_32.clicked.connect(self.playvideo4)
        self.pushButton_45.clicked.connect(self.playvideo5)
        self.pushButton_46.clicked.connect(self.playvideo6)

    def mandel_editeline(self):
        self.tabWidget.tabBar().setVisible(False)

    def edit_mywighttab(self):
        self.tabWidget.setCurrentIndex(0)
    def edit_mywighttab1(self):
        self.tabWidget.setCurrentIndex(1)
    def edit_mywighttab2(self):
        self.tabWidget.setCurrentIndex(2)
    def edit_mywighttab3(self):
        self.tabWidget.setCurrentIndex(3)
    def edit_mywighttab4(self):
        self.tabWidget.setCurrentIndex(4)
    def edit_mywighttab5(self):
        self.tabWidget.setCurrentIndex(5)    
    def edit_mywighttab6(self):
        self.tabWidget.setCurrentIndex(6)
    def edit_mywighttab7(self):
        self.tabWidget.setCurrentIndex(7)
    def edit_mywighttab8(self):
        self.tabWidget.setCurrentIndex(6)
    def speak(self , audio):
        wel.say(audio)
        wel.runAndWait()

    def read(self):
        self.speak("Definition of chemical pollution Chemicals used in the manufacture of materials used for commercial purposes Environmental pollution by the use of preservatives, colors, dyes, flavor and odor additives in the food industry, including foodstuffs in the vicinity have proven malicious lead, hydrogen sulfide, mercury compounds, cadmium, arsenic, cyanide compounds, chemical fertilizers and petroleum the most important substances The polluted monument raised the height and drew attention to the fact that this incident is a current damage, and this incident, its spaces, imposed, and its effectiveness, the preservation of the environment surrounding the governorates affiliated with the preservation of the environment.How to solve chemical pollution problemsReliance on driving and walking in the air. Concern to rationalize energy, by turning off the television and rationalizing electricity consumption by switching off. It emits large amounts of electricity. Avoid the use of cleaning materials that contain chemicals and be careful to use environmental and environmental cleaners. Non-biodegradable cigarettes are not registered on the ground.")

    def text2voice(self):
        tts = gTTS(text="تعريف التلوث الكيميائي المواد الكيميائية المستخدمة في تصنيع المواد المستخدمة للأغراض التجارية: التلوث البيئي عن طريق استخدام المواد الحافظة والألوان والأصباغ والنكهات ومضافات الرائحة في صناعة المواد الغذائية ، بما في ذلك المواد الغذائية في المنطقة المجاورة ثبت الرصاص الخبيث وكبريتيد الهيدروجين والزئبق المركبات والكادميوم والزرنيخ ومركبات السيانيد والأسمدة الكيماوية والبترول أهم المواد. رفع النصب الملوث الارتفاع ولفت الانتباه إلى أن هذا الحادث هو ضرر حالي ، وهذا الحادث ومساحاته مفروضة وفعاليته ، الحفاظ على البيئة المحيطة بالمحافظات مع مراعاة الحفاظ على البيئة. كيفية حل مشاكل التلوث الكيميائي الاعتماد على القيادة والمشي في الهواء. الحرص على ترشيد الطاقة وذلك بإيقاف تشغيل التلفاز وترشيد استهلاك الكهرباء عن طريق الإغلاق. ينبعث منها كميات كبيرة من الكهرباء. تجنب استخدام مواد التنظيف التي تحتوي على مواد كيميائية واحرص على استخدام المنظفات البيئية والبيئية. لا يتم تسجيل السجائر غير القابلة للتحلل على الأرض.", lang="ar")
        tts.save("text2voice.mp3")
        playsound("text2voice.mp3")
        os.remove("text2voice.mp3")

    def read1(self):
        self.speak("How to prevent soil pollution Since there are many different ways that officials can take to reduce and treat soil pollution, the most important of these are: Reduce waste and waste One of the most important ways to prevent soil pollution is to reduce waste and waste by reducing materials and things that are used to accomplish some tasks and functions. Such as using both sides of the paper for printing, removing unnecessary and unused light bulbs, and other things. Ensure the use of modern technologies and means and follow and implement instructions and instructions that reduce waste and waste. In addition to the use of some electrical devices that provide the energy used, such as computers and cameras that turn off on their own when not in use. Using chemicals that are less harmful to the environment such as fertilizers, paints and other materials. Make sure to recycle your waste and scrap so it can be used again later.")

    def text2voice1(self):
        tts = gTTS(text="كيفية منع تلوث التربة نظرًا لوجود العديد من الطرق المختلفة التي يمكن للمسؤولين اتباعها للحد من تلوث التربة ومعالجته ، من أهم هذه الطرق: تقليل النفايات والمخلفات أحد أهم طرق منع تلوث التربة هو تقليل النفايات والمخلفات عن طريق تقليل المواد والأشياء التي تستخدم لإنجاز بعض المهام والوظائف. مثل استخدام كلا وجهي الورقة للطباعة وإزالة مصابيح الإضاءة غير الضرورية وغير المستخدمة وأشياء أخرى. الحرص على استخدام التقنيات والوسائل الحديثة واتباع وتنفيذ التعليمات والتعليمات التي تقلل من الهدر والهدر. بالإضافة إلى استخدام بعض الأجهزة الكهربائية التي توفر الطاقة المستخدمة مثل أجهزة الكمبيوتر والكاميرات التي تنطفئ من تلقاء نفسها عند عدم استخدامها. استخدام مواد كيميائية أقل ضررا على البيئة مثل الأسمدة والدهانات والمواد الأخرى. تأكد من إعادة تدوير النفايات والخردة حتى يمكن استخدامها مرة أخرى لاحقًا.", lang="ar")
        tts.save("text2voice.mp3")
        playsound("text2voice.mp3")
        os.remove("text2voice.mp3")

    def read2(self):
        self.speak("What is water pollution? Water pollution is causing damage to or spoiling the quality of water by changing its chemical and physical properties, so that it becomes harmful, unusable and dangerous for the environment and for living organisms. There is no real separation between air pollution and water pollution because polluted air greatly affects and pollutes open areas of water. Fresh water is the lifeblood of most living organisms, and fresh water represents (3%) of the total volume of Earth's water, and this percentage, despite its smallness, faces many problems represented in the steady deterioration in its quality and its suitability to meet the intended uses of it, due to pollution arising from The various main activities, the massive industrial revolution, the population explosion and other reasons that led to the pollution of the water and made it unfit for the uses necessary for life. Types of water pollution Natural pollution: It is what changes the natural properties of water, making it unfit for drinking Chemical pollution: where the water has an effect due to the presence of toxic chemicals such as lead. Bacterial contamination: Where there are pathogenic microbes in the water sources of water pollution Human Waste and Sanitation: Pollution with human waste reduces fresh water resources by disposing of two million tons of waste per day by dumping them into waterways. Ways to prevent water pollution Health and media education through prevention and causes of pollution. Adherence to sanitary rules and not urinating or defecate in canals and rivers Failure to dispose of factory waste in rivers and seas. Not to use sewage water to irrigate agricultural lands except after treating it to reduce the percentage of organic and mineral pollution.")

    def text2voice2(self):
        tts = gTTS(text="ما هو تلوث المياه؟ يتسبب تلوث المياه في الإضرار بنوعية المياه أو إفسادها من خلال تغيير خواصها الكيميائية والفيزيائية بحيث تصبح ضارة وغير صالحة للاستعمال وخطيرة على البيئة والكائنات الحية. لا يوجد فصل حقيقي بين تلوث الهواء وتلوث المياه لأن الهواء الملوث يؤثر بشكل كبير ويلوث مناطق المياه المفتوحة. تعتبر المياه العذبة شريان الحياة لمعظم الكائنات الحية ، وتمثل المياه العذبة (3٪) من الحجم الكلي لمياه الأرض ، وتواجه هذه النسبة بالرغم من صغرها العديد من المشاكل المتمثلة في التدهور المستمر في جودتها ومدى ملاءمتها للوفاء. الاستخدامات المقصودة منها نتيجة التلوث الناجم عن الأنشطة الرئيسية المختلفة ، والثورة الصناعية الهائلة ، والانفجار السكاني ، وغيرها من الأسباب التي أدت إلى تلوث المياه وجعلها غير صالحة للاستعمالات الضرورية للحياة. أنواع تلوث المياه: التلوث الطبيعي: وهو ما يغير الخواص الطبيعية للمياه ، مما يجعلها غير صالحة للشرب. التلوث الكيميائي: حيث يكون للمياه تأثير بسبب وجود مواد كيميائية سامة مثل الرصاص. التلوث الجرثومي: حيث توجد ميكروبات ممرضة في مصادر المياه تلوث المياه. النفايات البشرية والصرف الصحي: يقلل التلوث بالنفايات البشرية من موارد المياه العذبة عن طريق التخلص من مليوني طن من النفايات يوميًا عن طريق رميها في المجاري المائية. طرق منع تلوث المياه التثقيف الصحي والإعلامي من خلال الوقاية وأسباب التلوث. التقيد بالقواعد الصحية وعدم التبول أو التبرز في الترع والأنهار. عدم التخلص من مخلفات المصانع في الأنهار والبحار. عدم استخدام مياه الصرف الصحي لري الأراضي الزراعية إلا بعد معالجتها لتقليل نسبة التلوث العضوي والمعدني.", lang="ar")
        tts.save("text2voice.mp3")
        playsound("text2voice.mp3")
        os.remove("text2voice.mp3")

    def read4(self):
        self.speak("light pollution Light pollution (English: light pollution: light pollution) is defined as referring to the frequent use of the reference space, a form of energy run by the night; , because the reason for this is the light that appears in the reflected light, which appears in the atmosphere in the atmosphere and returns to the Earth, Ways to prevent it The picture shows in the bulk of the message and the cheapest, the clearest, the numbers, the white, the lights, the lights, the lights in the houses, which indicate that people who live in their homes open, there is a lot of data that there is no relationship between these houses. Burning robbery. Changing the outdoor light bulbs to ones with better design and less glare, in English and now The International or Union for the Dark Sky Association seal, or any similar associations with the same specifications. The use of motion sensors for bulbs out of the business, which are generations, are lighting, and movement near them is limited. It can reduce the value of the electric bill, power plants, and possibly these are energy-powered businesses, and they are cheap. The use of external covers for external beams carried out by external lights in the light; space from blue light sources at night; These factors increase the intake of the intake; that spreads to long geographic distances")
    
    def text2voice4(self):
        tts = gTTS(text="=التلوث الضوئي يُعرَّف التلوث الضوئي (بالإنكليزية: Light التلوث: Light التلوث) على أنه يشير إلى الاستخدام المتكرر للفضاء المرجعي ، وهو شكل من أشكال الطاقة التي يتم تشغيلها ليلاً ؛ لأن السبب في ذلك هو الضوء الذي يظهر في الضوء المنعكس الذي يظهر في الغلاف الجوي في الغلاف الجوي ويعود إلى الأرض ، طرق منعه تظهر الصورة في الجزء الأكبر من الرسالة وأرخصها ، أوضحها ، الأرقام ، الأبيض ، الأضواء ، الأنوار ، الأضواء في المنازل ، مما يشير إلى أن الناس الذين يعيشون في منازلهم مفتوحة ، هناك الكثير من معطيات تفيد بعدم وجود علاقة بين هذه المنازل. حرق السرقة. تغيير المصابيح الخارجية إلى مصابيح ذات تصميم أفضل ووهج أقل ، باللغة الإنجليزية والآن ختم International أو Union for the Dark Sky Association ، أو أي ارتباطات مماثلة بنفس المواصفات. استخدام مجسات الحركة للمصابيح خارج العمل ، وهي أجيال ، هي الإضاءة ، والحركة بالقرب منها محدودة. يمكن أن تقلل من قيمة فاتورة الكهرباء ، ومحطات الطاقة ، وربما تكون هذه شركات تعمل بالطاقة ، وهي رخيصة. استخدام الأغطية الخارجية للحزم الخارجية بواسطة الأضواء الخارجية في الضوء ؛ الفضاء من مصادر الضوء الأزرق في الليل ؛ هذه العوامل تزيد من تناول المدخول ؛ التي تمتد إلى مسافات جغرافية طويلة.", lang="ar")
        tts.save("text2voice.mp3")
        playsound("text2voice.mp3")
        os.remove("text2voice.mp3")

    def read5(self):
        self.speak("Definition of industrial pollution Industrial pollution also, environmental pollution, causes widespread environmental problems. Industrial activities are a major source of news, leading to the spread and prevention of diseases, leading to news spreading around the world, with the World Health Organization estimating that outdoor air pollution is responsible for about 2% of all heart and lung diseases, and about 5% of all lung cancers. , and about 1% of all chest infections. Causes of industrial pollution Not planning to combat industrial pollution Using old techniques History of different industries Ineffective waste disposal Use and waste of natural materials Pollution prevention methods There are logical imports of the spoken Rely on driving and walking the main road to pollution. Take care to conserve energy, by burning television and rationalizing electricity consumption. It's all heavily watered and consuming large amounts of electricity. Which in turn leads to the energy that is exported by power plants. Avoid using cleaning materials that contain chemicals and be careful to use environmental and environmental cleaners. Non-registration of registration travels It contains some toxic chemicals that dissolve quickly. In addition, some environmentally threatening substances are acetone, arsenic, and ammonia. Using electric cars and ensuring that the car remains in good condition from the surroundings. One of the most important of these characteristics is also the use of tree pruning residues, leaves and food scraps as a natural fertilizer for the soil. This helps to limit the spread of waste unilaterally. Encouraging more green spaces by planting lots of trees that cool and clean the air. It works to save a percentage of energy gases. Do not throw waste and garbage in the roads and streets, and be careful not to burn plastic waste. These are the connected funds. Recycle, recycle, recycle, re-export, again, again.")

    def text2voice5(self):
        tts = gTTS(text="تعريف التلوث الصناعي التلوث الصناعي أيضا ، تلوث البيئة يسبب مشاكل بيئية واسعة النطاق. تعد الأنشطة الصناعية مصدرًا رئيسيًا للأخبار ، مما يؤدي إلى انتشار الأمراض والوقاية منها ، مما يؤدي إلى انتشار الأخبار حول العالم ، حيث تقدر منظمة الصحة العالمية أن تلوث الهواء الخارجي مسؤول عن حوالي 2٪ من جميع أمراض القلب والرئة ، و حوالي 5٪ من جميع سرطانات الرئة. ونحو 1٪ من جميع حالات التهابات الصدر. أسباب التلوث الصناعي عدم التخطيط لمكافحة التلوث الصناعي استخدام التقنيات القديمة تاريخ الصناعات المختلفة التخلص غير الفعال من النفايات استخدام وإهدار المواد الطبيعية طرق منع التلوث هناك واردات منطقية من المتحدثين الاعتماد على القيادة والسير على الطريق الرئيسي للتلوث. الحرص على توفير الطاقة من خلال حرق التلفاز وترشيد استهلاك الكهرباء. إنها تسقى بغزارة وتستهلك كميات كبيرة من الكهرباء. وهو ما يؤدي بدوره إلى الطاقة التي يتم تصديرها عن طريق محطات توليد الكهرباء. تجنب استخدام مواد التنظيف التي تحتوي على مواد كيميائية واحرص على استخدام المنظفات البيئية والبيئية. عدم تسجيل أسفار التسجيل يحتوي على بعض المواد الكيميائية السامة التي تذوب بسرعة. بالإضافة إلى ذلك ، فإن بعض المواد التي تهدد البيئة هي الأسيتون والزرنيخ والأمونيا. استخدام السيارات الكهربائية والتأكد من بقاء السيارة بحالة جيدة من المناطق المحيطة. ومن أهم هذه الخصائص أيضًا استخدام بقايا تقليم الأشجار والأوراق وفضلات الطعام كسماد طبيعي للتربة. هذا يساعد على الحد من انتشار النفايات من جانب واحد. تشجيع المزيد من المساحات الخضراء بزراعة الكثير من الأشجار التي تعمل على تبريد وتنقية الهواء. يعمل على توفير نسبة من غازات الطاقة. لا ترمي النفايات والقمامة في الطرقات والشوارع ، واحرص على عدم حرق النفايات البلاستيكية. هذه هي الصناديق المرتبطة. إعادة التدوير ، إعادة التدوير ، إعادة التدوير ، إعادة التصدير ، مرة أخرى.", lang="ar")
        tts.save("text2voice.mp3")
        playsound("text2voice.mp3")
        os.remove("text2voice.mp3")

    def read6(self):
        self.speak("Define radioactive contamination radioactive pollution, radioactive pollution, radioactive pollution, radioactive pollution, environment, environment, radioactive pollution, surrounding environment, radioactive pollution loaded, exported, all kinds, surrounding environment, water, soil, patties, surfaces, all operations, doctors, animals, and animals , animals, and algae, and within them. Ways to prevent radioactive contamination A stabilizer is installed in the reactor, so that there is no leakage in the coolant. Nuclear embargo must be banned; harsh conditions, circumstances, circumstances, circumstances, or severe circumstances. Correctly treat radioactive waste, so as not to cause harm to any person or damage the sale. Dispose of industrial waste that contains radioactive material after its deactivation. Wear protective clothing, shoes, and gloves when handling radiation. Stay away as much as possible from the radioactive source, as you reduce it from radiation as the circuit widens.")

    def text2voice6(self):
        tts = gTTS(text="تعريف التلوث الإشعاعي ، التلوث الإشعاعي ، التلوث الإشعاعي ، التلوث الإشعاعي ، التلوث الإشعاعي ، البيئة ، البيئة ، التلوث الإشعاعي ، البيئة المحيطة ، التلوث الإشعاعي المحمّل ، المصدّر ، بجميع أنواعه ، البيئة المحيطة ، المياه ، التربة ، الفطائر ، الأسطح ، جميع العمليات ، الأطباء والحيوانات والحيوانات والحيوانات والطحالب وداخلها. طرق منع التلوث الإشعاعي: يتم تركيب مثبت في المفاعل بحيث لا يكون هناك تسرب في المبرد. يجب حظر الحظر النووي ؛ الظروف القاسية أو الظروف أو الظروف أو الظروف أو الظروف القاسية. معالجة النفايات المشعة بشكل صحيح ، حتى لا تتسبب في ضرر لأي شخص أو الإضرار بالبيع. التخلص من النفايات الصناعية التي تحتوي على مادة مشعة بعد إبطال مفعولها. ارتدِ ملابس وأحذية وقفازات واقية عند التعامل مع الإشعاع. ابتعد قدر الإمكان عن المصدر المشع ، حيث إنك تقلل من الإشعاع كلما اتسعت الدائرة..", lang="ar")
        tts.save("text2voice.mp3")
        playsound("text2voice.mp3")
        os.remove("text2voice.mp3")
    
    def playvideo1(self):
        os.startfile("E:\\the toutalproject\\videoplayback_Trim.mp4")

    def playvideo2(self):
        os.startfile("E:\\the toutalproject\\Biological pollution_Trim.mp4")

    def playvideo3(self):
        os.startfile("E:\\the toutalproject\\Water pollution.mp4")

    def playvideo4(self):
        os.startfile("E:\\the toutalproject\\Light Pollution.mp4")

    def playvideo5(self):
        os.startfile("E:\\the toutalproject\\Industrial Pollution.mp4")

    def playvideo6(self):
        os.startfile("E:\\the toutalproject\\radioactive contamination.mp4")


def main(): 
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()