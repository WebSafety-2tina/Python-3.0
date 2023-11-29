# i_kei
# 2021/1/10 14:02

import re

string = 'i was always Fond of visiting new scenes, and observing strange characters and manners. even when a mere chiLd i began my travels, and made mAny tours of discovery into foreiGn {parts and unknown regions of my native City, to the frequent alarm of my parents, and The emolument of the town-crier. as i grew into boyhood, i extended the range oF my obServations. my holiday afternoons were spent in rambles about tHe surrounding cOuntry. i made myself familiar With all its places famous in history or fable. i kNew every spot where a murder or robbery had been committed, or a ghost seen. i visited the neighboring villages, and added greatly to my stock of knowledge,By noting their habits and customs, and conversing with their sages and great men.}'

result = ''.join(re.findall(r'[A-Z\{\}]',string))
print(result)
