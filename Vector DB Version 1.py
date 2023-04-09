import pickle

class Vector:
    def __init__(self, components):
        self.components = components

    def add(self, other_vector):
        if len(self.components) != len(other_vector.components):
            raise ValueError("Vectors must have the same dimension to be added")
        result_components = [a + b for a, b in zip(self.components, other_vector.components)]
        return Vector(result_components)

    def subtract(self, other_vector):
        if len(self.components) != len(other_vector.components):
            raise ValueError("Vectors must have the same dimension to be subtracted")
        result_components = [a - b for a, b in zip(self.components, other_vector.components)]
        return Vector(result_components)

    def dot(self, other_vector):
        if len(self.components) != len(other_vector.components):
            raise ValueError("Vectors must have the same dimension to calculate the dot product")
        result_components = [a * b for a, b in zip(self.components, other_vector.components)]
        return sum(result_components)

    def magnitude(self):
        return (sum(c**2 for c in self.components))**0.5

    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(','.join(str(c) for c in self.components))

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            components = [float(c) for c in file.read().split(',')]
        return cls(components)


class VectorDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.vectors = {}

        try:
            with open(filename, 'rb') as file:
                self.vectors = pickle.load(file)
        except FileNotFoundError:
            pass

    def add_vector(self, vector_name, vector):
        self.vectors[vector_name] = vector

        with open(self.filename, 'wb') as file:
            pickle.dump(self.vectors, file)

    def delete_vector(self, vector_name):
        del self.vectors[vector_name]

        with open(self.filename, 'wb') as file:
            pickle.dump(self.vectors, file)

    def get_vector(self, vector_name):
        return self.vectors[vector_name]

    def get_all_vectors(self):
        return list(self.vectors.values())


# Create a vector database
db = VectorDatabase('vectors.pickle')

# Add vectors to the database
vector1 = Vector([1, 2, 3])
db.add_vector('vector1', vector1)

vector2 = Vector([4, 5, 6])
db.add_vector('vector2', vector2)

# Get a vector from the database
vector1_copy = db.get_vector('vector1')

# Print the vector's components
print(f"The components of vector1 are: {vector1_copy.components}")  

# Delete a vector from the database
db.delete_vector('vector2')

# Get all vectors from the database
all_vectors = db.get_all_vectors()

# Print the components of each vector
for vector in all_vectors:
    print(f"The components of {vector} are: {vector.components}")

# Create a new vector
vector3 = Vector([7, 8, 9])

# Add the new vector to the database
db.add_vector('vector3', vector3)

# Save the first vector to a file
vector1.save('vector1.txt')

# Load the vector from the file
loaded_vector = Vector.load('vector1.txt')

# Print the loaded vector's components
print(f"The components of loaded_vector are: {loaded_vector.components}")