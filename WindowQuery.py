from pyqtree import Index
from Graphstuff import *
from math import sin, cos, pi


# Checks if b1 is outside b2
def bboxoutside(b1, b2):
    return (b1[0] < b2[0] or b1[1] < b2[1] or b1[2] > b2[2] or b1[3] > b2[3])


class TreeStruct:
    bbox = (-10000, -10000, 10000, 10000)

    ##
    # Maintain link from points to rectangle objects?
    def __init__(self):
        self.index = Index(bbox=self.bbox, max_items=40, max_depth=15)

    def addRect(self, rect):
        if (bboxoutside(rect.bbox, self.bbox)):
            print('outside')
            pass  # TODO

        self.index.insert(rect, rect.bbox)

    def removeRect(self, rect):
        self.index.remove(rect, rect.bbox)

    def query(self, rect):
        candidates = self.index.intersect(rect.bbox)
        # return candidates
        # TBD if we want to make the check both ways or are okay with overlaps only being detected on one end
        return [candidate for candidate in candidates if rect.overlaps(candidate) or candidate.overlaps(rect)]
