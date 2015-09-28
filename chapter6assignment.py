text = "X-DSPAM-Confidence:    0.8475";
x = text.find('0.8475')
y = len(text)
print float(text[x:y])
