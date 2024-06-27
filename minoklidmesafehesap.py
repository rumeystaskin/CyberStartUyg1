import math

# noktaları tanımlama
points = [(1, 2), (3, 4), (6, 8), (2, 1), (7, 5)]


# öklid mesafesi için fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# mesafeleri hesaplama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


# minimum mesafeyi bulma
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
