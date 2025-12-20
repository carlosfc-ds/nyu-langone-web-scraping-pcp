# MongoDB Projections Basics

MongoDB projections control which fields appear in query results, helping optimize performance by returning only needed data. Use the second argument in `find()` queries like `db.my_collection.find(query, projection)`.

## Basic Syntax

The projection is a document where fields are set to `1` (include) or `0` (exclude). By default, `_id` is included unless excluded.

```python
db.my_collection.find(
    {}, ## empty means all docs
    { name: 1, age: 1, _id: 0 } # projection
)
```

This returns only `name` and `age`, excluding `_id`.

## Include vs Exclude

- **Include specific fields** (most common): Set desired fields to `1`. Cannot mix includes/excludes except for `_id`.

```python
db.users.find(
    { age: { $gt: 25 } }, 
    { name: 1, email: 1 }
)
```

- **Exclude specific fields**: Set unwanted fields to `0`.

```python
db.users.find(
    {}, 
    { password: 0 }
)
```


Mixing `1` and `0` (except `_id: 0`) causes errors.

## Array Projections

Use operators for arrays:

- `$slice`: Limit array elements.

```python
db.posts.find({}, { comments: { $slice: 5 } }) # First 5 comments
db.posts.find({}, { comments: { $slice: -3 } }) # Last 3 comments
```

- `$elemMatch`: Match array elements.

```python
db.posts.find(
    { "comments.author": "alice" },
    { "comments.$": 1 } # First matching comment
)
```


These reduce data transfer for large arrays.

## Best Practices

- Always project in production to minimize bandwidth.
- Exclude `_id: 0` when unnecessary.
- Use aggregation `$project` for complex reshaping:

```python
db.my_collection.aggregate(
    [{ $project: { 
        title: 1, 
        modified: { $toDate: "$date" } 
    }}]
)
```

Test projections in mongosh for efficiency.
