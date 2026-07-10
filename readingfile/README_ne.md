# फाइलबाट डाटा प्राप्त गर्ने तरिका

## उद्देश्य

यस सामग्रीमा, Python प्रयोग गरेर फाइलबाट डाटा पढ्ने र प्रत्येक लाइन छुट्टाछुट्टै प्रक्रिया गर्ने तरिका सिकिन्छ।

यस कार्यक्रममा, RPN (Reverse Polish Notation) को अभिव्यक्तिहरू फाइलबाट पढिन्छन् र गणनाको परिणाम देखाइन्छ।

---

## इनपुट, प्रोसेसिङ र आउटपुट

कार्यक्रम सामान्यतया तलको प्रवाहमा चल्छ।

```text
Input -> Processing -> Output
```

यस पटकको मुख्य बुँदा इनपुट दिने तरिका परिवर्तन गर्नु हो।

- पहिले अभिव्यक्ति सिधै प्रोग्राममा लेखिन्थ्यो वा `input()` बाट लिइन्थ्यो।
- अहिले अभिव्यक्तिहरू फाइलमा लेखेर Python बाट त्यो फाइल पढिन्छ।

## प्रयोग हुने फाइलहरू

उदाहरणका लागि, तलको संरचना प्रयोग गरिन्छ।

```text
rpn_file_io/
├── run_rpn_file.py
├── rpn_calculator.py
├── expressions.txt
└── results.txt
```

प्रत्येक फाइलको भूमिका यस्तो छ।

- `run_rpn_file.py`: फाइल पढेर RPN गणना चलाउने फाइल
- `rpn_calculator.py`: RPN गणनाका लागि फङ्सनहरू लेख्ने फाइल
- `expressions.txt`: इनपुट फाइल, जहाँ RPN अभिव्यक्ति लेखिन्छ
- `results.txt`: आउटपुट फाइल, जहाँ परिणाम लेखिन्छ

### `expressions.txt` को उदाहरण

```text
3 4 +
10 2 /
10 0 /
5 a +
3 4 5 +
```

हरेक लाइनमा एउटा RPN अभिव्यक्ति लेखिन्छ।

`3 4 +` को सामान्य (infix) अर्थ `3 + 4` हो।

## फाइल खोल्ने आधारभूत ढाँचा

Python मा फाइल पढ्दा `open()` प्रयोग गरिन्छ।

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    print(line)
```

यो कोडले `expressions.txt` खोल्छ र लाइन-लाइनमा देखाउँछ।

### `open()` को अर्थ

`open("expressions.txt", "r", encoding="utf-8")`

- `"expressions.txt"`: खोल्न चाहिएको फाइल नाम
- `"r"`: read मोड (पढ्ने मोड)
- `encoding="utf-8"`: क्यारेक्टर इन्कोडिङ सेटिङ

### `with` किन प्रयोग गर्ने

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  ...
```

`with` प्रयोग गर्दा काम सकिएपछि फाइल स्वतः बन्द हुन्छ।

त्यसैले सामान्यतया `with open(...)` प्रयोग गर्नु राम्रो हुन्छ।

## लाइन अनुसार पढ्ने

```python
with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    print(line)
```

`for line in file:` ले फाइलको सामग्री लाइन-लाइनमा निकाल्छ।

उदाहरणका लागि `expressions.txt` मा यो छ भने:

```text
3 4 +
10 2 /
```

`line` मा क्रमशः यी मान आउँछन्:

- पहिलो पटक: `"3 4 +\n"`
- दोस्रो पटक: `"10 2 /\n"`

## `strip()` ले नयाँ लाइन हटाउने

फाइलबाट पढिएको प्रत्येक लाइनको अन्त्यमा प्रायः newline हुन्छ।

त्यसैले `strip()` प्रयोग गरिन्छ।

```python
expression = line.strip()
```

उदाहरण:

```python
line = "3 4 +\n"
expression = line.strip()

print(expression)
```

नतिजा:

```text
3 4 +
```

`strip()` ले अगाडि र पछाडिका अनावश्यक खाली स्थान र newline हटाउँछ।

## प्रत्येक लाइन गणना गर्ने

यदि `calculate_rpn()` नामको फङ्सन छ भने, पढिएको अभिव्यक्तिलाई सीधै पठाउन सकिन्छ।

```python
from rpn_calculator import calculate_rpn

with open("expressions.txt", "r", encoding="utf-8") as file:
  for line in file:
    expression = line.strip()

    if expression == "":
      continue

    result = calculate_rpn(expression)

    print(expression, "=>", result)
```

### खाली लाइन बेवास्ता गर्ने

फाइलमा खाली लाइन भएमा, कार्यक्रमले खाली अभिव्यक्ति गणना गर्न खोज्न सक्छ।

त्यसैले यो सर्त थपिन्छ।

```python
if expression == "":
  continue
```

अर्थात्: लाइन खाली छ भने त्यो लाइन छोडेर अर्को लाइनमा जानु।

## परिणाम फाइलमा लेख्ने

स्क्रिनमा देखाउनुका साथै परिणाम फाइलमा पनि बचत गर्न सकिन्छ।

```python
from rpn_calculator import calculate_rpn

with open("expressions.txt", "r", encoding="utf-8") as input_file:
  with open("results.txt", "w", encoding="utf-8") as output_file:
    for line in input_file:
      expression = line.strip()

      if expression == "":
        continue

      result = calculate_rpn(expression)

      print(expression, "=>", result)
      output_file.write(f"{expression} => {result}\n")
```

### `print()` र `write()` बीच फरक

```python
print(expression, "=>", result)
output_file.write(f"{expression} => {result}\n")
```

- `print()`: टर्मिनलमा देखाउँछ
- `write()`: फाइलमा लेख्छ

### `\n` को अर्थ

`output_file.write(f"{expression} => {result}\n")`

अन्त्यको `\n` ले नयाँ लाइन जनाउँछ।

यो नभएमा सबै नतिजा एउटै लाइनमा जोडिन्छ।

## लेख्ने मोड

फाइलमा लेख्दा `"w"` प्रयोग गरिन्छ।

```python
open("results.txt", "w", encoding="utf-8")
```

`"w"` को अर्थ write मोड हो।

ध्यान दिनुहोस्: `"w"` ले प्रत्येक रनमा पुरानो सामग्री ओभरराइट गर्छ।

### थप्दै जान चाहिँदा

पहिलेकै नतिजा राखेर अन्त्यमा थप्न `"a"` प्रयोग गर्नुपर्छ।

```python
open("results.txt", "a", encoding="utf-8")
```

`"a"` को अर्थ append मोड हो।

तर यस पाठमा प्रत्येक पटक नयाँ परिणाम बनाउन `"w"` नै प्रयोग गरिन्छ।

## सारांश

यस पाठका मुख्य बुँदाहरू:

- `open()` बाट फाइल खोल्ने
- पढ्न `"r"` मोड प्रयोग गर्ने
- लेख्न `"w"` मोड प्रयोग गर्ने
- `for line in file:` ले लाइन-लाइनमा पढ्ने
- `strip()` ले newline हटाउने
- `write()` ले फाइलमा लेख्ने
- `\n` ले नयाँ लाइन दिने

## पूर्ण उदाहरण

```python
from rpn_calculator import calculate_rpn

input_filename = "expressions.txt"
output_filename = "results.txt"

with open(input_filename, "r", encoding="utf-8") as input_file:
  with open(output_filename, "w", encoding="utf-8") as output_file:
    for line in input_file:
      expression = line.strip()

      if expression == "":
        continue

      result = calculate_rpn(expression)

      print(expression, "=>", result)
      output_file.write(f"{expression} => {result}\n")
```

## GitHub मा अभिलेख राख्ने

फाइलबाट पढ्ने परिवर्तन पूरा भएपछि GitHub मा रेकर्ड गर्न सकिन्छ।

```bash
git status
git add .
git commit -m "Read RPN expressions from file"
git push
```

जापानी कमिट सन्देश चाहियो भने यो पनि प्रयोग गर्न सकिन्छ।

```bash
git commit -m "RPN式をファイルから読み込む"
```
