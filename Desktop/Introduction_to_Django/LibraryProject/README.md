# Create Operation

Command:

```python
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
```

# Retrieve Operation

Command:

```python
all_books = Book.objects.all()
for b in all_books:
    print(b.title, b.author, b.publication_year)
```

# Update Operation

Command:

```python
book.title = "Nineteen Eighty-Four"
book.save()
```

# Delete Operation

Command:

```python
book.delete()

# Confirm deletion
all_books = Book.objects.all()
print(all_books)
```
