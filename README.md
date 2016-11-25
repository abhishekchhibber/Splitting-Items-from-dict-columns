# Splitting Items from dict columns

[This python file](https://github.com/abhishekchhibber/Splitting-Items-from-dict-columns/blob/master/fintech%20trends%20break.py) converts dictonary rows such as this:
```
Title,Date,Trend,Segment,Country
"Indian bank launches WhatsApp, Facebook, Twitter mobile payments",2015-05-14,"New Products,Expansion","Mobile Fintech,Payment Processing",India


```
to these:

```
Title,Date,Segment,Country,Trend


"Indian bank launches WhatsApp, Facebook, Twitter mobile payments",2015-05-14,Mobile Fintech,India,New Products
"Indian bank launches WhatsApp, Facebook, Twitter mobile payments",2015-05-14,Payment Processing,India,New Products
"Indian bank launches WhatsApp, Facebook, Twitter mobile payments",2015-05-14,Mobile Fintech,India,Expansion
"Indian bank launches WhatsApp, Facebook, Twitter mobile payments",2015-05-14,Payment Processing,India,Expansion

```

PS: for saving time and code, it's better to do this through pandas, using the following:

```
s = data['Trend'].str.split(',').apply(Series, 1).stack()
s.index = s.index.droplevel(-1)
s.name = 'Trend'
del data['Trend']
df = data.join(s)

```
