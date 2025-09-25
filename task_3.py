class PointsForPlace:
    def __init__(self):
        self.points = 0
    def get_points_for_place(self, place):
        self.place = place
        if place > 100:
            return 'Баллы начисляются только первым 100 участникам'
        elif place < 1:
             return 'Спортсмен не может занять нулевое или отрицательное место'
        else:
            self.points = 101 - place
            return self.points


class PointsForMeters:
    def __init__(self):
        self.points = 0
    def get_points_for_meters(self, meters):
        self.meters = meters
        if meters < 0:
            return 'Количество метров не может быть отрицательным'
        else:
            self.points = meters * 0.5
            return self.points
    

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        self.total = 0
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)

    @staticmethod    
    def get_total_points(place, meters):
       total = PointsForPlace().get_points_for_place(place) + PointsForMeters().get_points_for_meters(meters)
       return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 