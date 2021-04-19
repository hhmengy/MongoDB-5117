# MongoDB-5117

## Query Examples

View Database
```
db
```

db.createCollection('students')

Show collections
```
show collections
```

Show all entries
```
db.students.find()
```

Insert one entry
```
db.students.insert({
	first: 'Dennis',
	last: 'Keller',
	major: 'computer science',
	enrollment: {
		semester: 'spring2021',
		classes: ['csci5117','csci1133']
	},
	date: Date()
})
```

Insert multiple entries
```
db.students.insertMany([
	{
		first: 'Heidi',
		last: 'Keller',
		major: 'computer science',
		enrollment: {
			semester: 'spring2021',
			classes: ['csci5117','csci1933']
		},
		date: Date()
	},
	{
		first: 'Derek',
		last: 'Wade',
		major: 'biology',
		enrollment: {
			semester: 'spring2021',
			classes: ['biol1011','chem1061']
		},
		date: Date()
	},
	{
		first: 'William',
		last: 'Wilson',
		major: 'economics',
		enrollment: {
			semester: 'spring2021',
			classes: ['econ1001','stat1013']
		},
		date: Date()
	},
	{
		first: 'Jan',
		last: 'Keller',
		major: 'chemistry',
		enrollment: {
			semester: 'spring2021',
			classes: ['chem1061','chem2022']
		},
		date: Date()
	}
])
```

Nicely show all entries
```
db.students.find().pretty()
```

Search for specific entries
```
db.students.find({ major: 'computer science' }).pretty()
```

Search for first instance of specific entries
```
db.students.findOne({ major: 'computer science' })
```

Sort entries in ascending order
```
db.students.find().sort({ first: 1 }).pretty()
```

Sort entries in descending order
```
db.students.find().sort({ first: -1 }).pretty()
```

Count number of entries
```
db.students.find().count()
```

Limit number of found entries
```
db.students.find().limit(3).pretty()
```

Update entire entry
```
db.students.update({ first: 'Jan' },
{
	first: 'Jan',
	last: 'Keller',
	major: 'data science',
	enrollment: {
		semester: 'spring2021',
		classes: ['csci4041','stat1001']
	},
	date: Date()
})
```

Update specific entry field
```
db.students.update({ first: 'Jan' },
{
  $set: {
    major: 'computer science'
  }
})
```

Chain query functions together
```
db.students.find({last:'Keller'}).limit(2).sort({first: 1}).pretty()
```

Iterate over entries
```
db.students.find().forEach(function(doc) {
	print(doc.first + " " + doc.last)
})
```

Delete entry
```
db.students.remove({ last: "Keller" })
```

Delete database
```
db.dropDatabase()
```
