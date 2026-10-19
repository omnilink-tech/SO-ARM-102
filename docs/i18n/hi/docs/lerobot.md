<!-- translation-navigation -->
[English](../../en/docs/lerobot.md) · [Русский](../../ru/docs/lerobot.md) · [Español](../../es/docs/lerobot.md) · [Français](../../fr/docs/lerobot.md) · [Deutsch](../../de/docs/lerobot.md) · [Português (Brasil)](../../pt-BR/docs/lerobot.md) · [简体中文](../../zh-CN/docs/lerobot.md) · [日本語](../../ja/docs/lerobot.md) · [हिन्दी](../../hi/docs/lerobot.md) · [العربية](../../ar/docs/lerobot.md)

[English source](../../../../docs/lerobot.md)
<!-- /translation-navigation -->

<!-- translated-content -->
<a id="so-arm-102-with-lerobot"></a>
# LeRobot के साथ SO-ARM 102

Hugging Face LeRobot के साथ अलग से अनुरक्षित [SO-ARM 102 प्लगइन](https://github.com/roboninecom/SO-ARM-102-Lerobot) का उपयोग करें। यह फॉलोअर के STS3235, STS3250 और STS3215 मोटरों के मिश्रण का समर्थन करता है।

<a id="install"></a>
## इंस्टॉलेशन

Python 3.12 का उपयोग करें और प्लेटफ़ॉर्म की आवश्यकताओं के लिए [LeRobot इंस्टॉलेशन गाइड](https://huggingface.co/docs/lerobot/en/installation) का पालन करें। सक्रिय एनवायरनमेंट में:

```bash
python -m pip install 'lerobot[feetech,core_scripts]==0.6.1'
python -m pip install 'lerobot_robot_so_arm102[feetech]==0.1.0a1'
```

<a id="set-up-and-control"></a>
## सेटअप और नियंत्रण

फॉलोअर के लिए `so_arm102_follower` और SO-101 या SO-ARM 102 लीडर के लिए मानक `so101_leader` प्रकार का उपयोग करें।

[मोटर सेटअप](https://github.com/roboninecom/SO-ARM-102-Lerobot#connect-and-set-up), [कैलिब्रेशन](https://github.com/roboninecom/SO-ARM-102-Lerobot#calibrate) और [टेलीऑपरेशन](https://github.com/roboninecom/SO-ARM-102-Lerobot#teleoperate) के लिए प्लगइन के निर्देशों का पालन करें। पहले से कॉन्फ़िगर किए गए आर्म पर मोटर सेटअप छोड़ दें। उदाहरण के पोर्ट अपने पोर्ट से बदलें और कैलिब्रेशन के बाद वही आर्म ID रखें।

निर्दिष्ट पैकेज संस्करण अल्फ़ा रिलीज़ है। सोर्स कोड, टेस्ट, रिलीज़ और सॉफ़्टवेयर सहायता प्लगइन रिपॉज़िटरी में रहेंगे। मैकेनिकल फ़ाइलें और असेंबली निर्देश यहाँ रहेंगे।
<!-- /translated-content -->
