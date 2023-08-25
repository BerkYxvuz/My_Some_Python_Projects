class Question:
    def __init__(self, soru, secenekler, cevap):
        self.soru = soru
        self.secenekler = secenekler
        self.cevap = cevap
    def CevapKontrol(self, cevapla):
        return self.cevap == cevapla

class Quiz:
    def __init__(self,sorular):
        self.score = 0
        self.sorular = sorular
        self.soruno = 0
        self.tahmin = None
    def SoruGetir(self):
        return self.sorular[self.soruno]
    def SoruGoster(self):
        soru = self.SoruGetir()
        print(f'Soru {self.soruno + 1}: {soru.soru}')

        for i in soru.secenekler:
            print(f'*{i}')
        cevapla = input('Cevap: ')
        print(Question.CevapKontrol(cevapla))

q1 = Question("KREB'in tersi nedir?", ["Berk", "Krep", "Rekb", "Brek"], "Berk")
sorular = [q1]

quiz = Quiz(sorular)
quiz.SoruGoster()