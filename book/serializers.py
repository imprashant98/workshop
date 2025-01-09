from rest_framework import serializers  # Import serializers module from Django REST Framework
from .models import Book  # Import the Book model from the current app's models

# Define a serializer for the Book model
class BookSerializer(serializers.ModelSerializer):  
    # Meta class specifies additional options for the serializer
    class Meta:
        model = Book  # Link this serializer to the Book model
        fields = '__all__'  # Include all fields from the Book model in the serializer








# from rest_framework import serializers
# from .models import Book

# # Serializer for listing books
# class BookListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book  # Link to the Book model
#         fields = ['id', 'title', 'author']  # Include only fields needed for listing

# # Serializer for retrieving detailed information about a single book
# class BookRetrieveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book  # Link to the Book model
#         fields = '__all__'  # Include all fields for detailed retrieval

# # Serializer for creating/updating a book
# class BookWriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book  # Link to the Book model
#         fields = ['title', 'author', 'description', 'published_date']  # Specify writable fields

#     # Add custom validation if needed
#     def validate_title(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError("Title must be at least 3 characters long.")
#         return value
