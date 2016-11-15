class GradebookEntry:
    def __init__(self):
        self._scores = {}

    def add_midterm_exam_score(self, score):
        if 'midterm' not in self._scores:
            self._scores['midterm'] = []
        self._scores['midterm'].append(score)

    def add_project_score(self, score):
        if 'project' not in self._scores:
            self._scores['project'] = []
        self._scores['project'].append(score)

    def add_final_exam_score(self, score):
        self._scores['final'] = score

    def get_midterm_exam_scores(self):
        return self._scores['midterm']

    def get_project_scores(self):
        return self._scores['project']

    def get_final_exam_score(self):
        return self._scores['final']

class GradebookEntryDropLowestProject(GradebookEntry):
    def get_project_scores(self):
        scores = sorted(self._scores["project"])
        return scores[1:]

class GradebookEntryDropLowestMidterm(GradebookEntry):
    def get_midterm_exam_scores(self):
        scores = sorted(self._scores["midterm"])
        return scores[1:]



